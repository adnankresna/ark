#!/usr/bin/env python3
"""
run_scenario.py — execute a single PM Brain test scenario.

USAGE
    python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn
    python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn --runs 5
    python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn --runs 5 --max-cost 25
    python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn --keep-workdir
    python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn --stop-after-turn 1

WHAT IT DOES
    For each run:
      1. Creates a fresh work dir (TemporaryDirectory, or tests/workdir/<ts>-... with --keep-workdir).
      2. Bootstraps the PM Brain scaffold into the work dir (cp -R of the canonical skill scaffold).
      3. Iterates through scenario inputs/ in filename order. For each turn:
         - Snapshots files-before.
         - Invokes `claude -p` in the work dir with the turn's artifact embedded in the prompt.
         - Snapshots files-after.
         - Runs the turn's structural assertions (with before/after snapshots).
         - Runs the turn's content (LLM-judge) assertions.
      4. At scenario end, runs final_state assertions.
      5. Writes results to tests/results/<date>-<scenario>-<run>.json.

    Across N runs, computes pass rates per assertion and compares to pass_threshold.

COST GUARD
    --max-cost is enforced via the per-call total_cost_usd field from `claude -p --output-format json`.
    Cumulative cost across all turns and judge calls in a single run is tracked. If the cumulative
    cost exceeds --max-cost, the run aborts (the remaining turns are skipped and the partial result
    is written). Other runs in the same invocation continue from $0.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("ERROR: PyYAML required. pip install pyyaml\n")
    sys.exit(1)

# Local imports (relative to this file's parent)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from checks import structural as structural_checks  # noqa: E402
from checks import content as content_checks  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SKILL_PATH = REPO_ROOT / ".claude" / "skills" / "pm-brain"
RESULTS_DIR = REPO_ROOT / "tests" / "results"
WORKDIR_ROOT = REPO_ROOT / "tests" / "workdir"
JUDGES_DIR = Path(__file__).resolve().parent / "judges"

CLAUDE_BIN = os.environ.get("PM_BRAIN_CLAUDE_BIN", "claude")
TURN_TIMEOUT_S = int(os.environ.get("PM_BRAIN_TURN_TIMEOUT", "600"))
JUDGE_TIMEOUT_S = int(os.environ.get("PM_BRAIN_JUDGE_TIMEOUT", "180"))

# Default models. The scenario-turn agent runs as Sonnet (realistic + ~3-5x cheaper than Opus).
# Most judges run as Sonnet (tight rubrics). High-judgment judges can opt into Opus via a
# `model: opus` field in expected.yaml.
DEFAULT_TURN_MODEL = os.environ.get("PM_BRAIN_TURN_MODEL", "sonnet")
DEFAULT_JUDGE_MODEL = os.environ.get("PM_BRAIN_JUDGE_MODEL", "sonnet")


# ============================================================
# Errors
# ============================================================

class CostBudgetExceeded(RuntimeError):
    pass


# ============================================================
# Cost tracking
# ============================================================

class CostTracker:
    """
    Tracks cumulative LLM cost (USD) for a single scenario run.

    max_cost=None disables the guard. Otherwise add() raises CostBudgetExceeded once
    cumulative cost crosses the budget. The caller catches it and finalizes a partial run.
    """

    def __init__(self, max_cost: float | None):
        self.max_cost = max_cost
        self.entries: list[dict] = []

    @property
    def total(self) -> float:
        return sum(e["cost"] for e in self.entries)

    def add(self, kind: str, label: str, cost: float) -> None:
        self.entries.append({"kind": kind, "label": label, "cost": cost})
        if self.max_cost is not None and self.total > self.max_cost:
            raise CostBudgetExceeded(
                f"cumulative cost ${self.total:.4f} exceeded --max-cost ${self.max_cost:.2f} "
                f"after {kind}:{label}"
            )

    def summary(self) -> dict:
        return {
            "total_usd": round(self.total, 4),
            "max_usd": self.max_cost,
            "by_kind": self._group_by_kind(),
            "entries": self.entries,
        }

    def _group_by_kind(self) -> dict:
        out: dict = {}
        for e in self.entries:
            out.setdefault(e["kind"], 0.0)
            out[e["kind"]] += e["cost"]
        return {k: round(v, 4) for k, v in out.items()}


# ============================================================
# Scenario loading
# ============================================================

def load_scenario(scenario_dir: Path) -> dict:
    """Load expected.yaml + sorted list of input files."""
    expected = yaml.safe_load((scenario_dir / "expected.yaml").read_text(encoding="utf-8"))
    inputs = sorted((scenario_dir / "inputs").glob("turn-*.md"))
    return {"expected": expected, "inputs": inputs}


# ============================================================
# Workdir
# ============================================================

def make_workdir(scenario_dir: Path, run_index: int, keep: bool) -> tuple[Path, callable]:
    """
    Returns (work_dir, cleanup_fn). cleanup_fn is callable with no args; it's a no-op
    when keep=True so the dir survives for inspection.
    """
    if keep:
        WORKDIR_ROOT.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        wd = WORKDIR_ROOT / f"{ts}-{scenario_dir.name}-run{run_index}"
        wd.mkdir(parents=True, exist_ok=False)
        return wd, lambda: None
    tmp = tempfile.mkdtemp(prefix="pm-brain-test-")
    return Path(tmp), lambda: shutil.rmtree(tmp, ignore_errors=True)


# ============================================================
# Brain bootstrap
# ============================================================

def bootstrap_brain(work_dir: Path) -> None:
    """
    Bootstrap a fresh PM Brain in work_dir by copying the canonical skill scaffold.

    Scenario tests check post-init behavior. Init has its own scenario slot (TBD:
    04-greenfield-init), which is the right place to exercise the interview workflow.
    """
    scaffold_src = SKILL_PATH / "scaffold"
    if not scaffold_src.exists():
        raise RuntimeError(f"Skill scaffold not found at {scaffold_src}")
    for item in scaffold_src.iterdir():
        dest = work_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


# ============================================================
# claude -p invocation
# ============================================================

TURN_PROMPT_TEMPLATE = """\
You are operating the PM Brain that lives in your current working directory.

Read CLAUDE.md and INDEX.md, then ingest the artifact below following the PM Brain operating
manual. Apply changes directly — Autonomy mode is "act and tell" for this session.
Do not ask for confirmation. Do not stop to clarify; make the reasonable PM call.

This is turn {turn_index} of an automated scenario test. Do not assume any prior turns happened
unless evidence of them is present in the working directory.

=== ARTIFACT: {input_name} ===

{artifact}
"""


def invoke_claude(
    prompt: str,
    cwd: Path,
    timeout_s: int,
    model: str | None = None,
    extra_args: list[str] | None = None,
) -> dict:
    """
    Invoke `claude -p <prompt> --output-format json` and return the parsed envelope.

    `model` is passed via --model when non-empty. Set to a model alias ('sonnet', 'opus',
    'haiku') or a full model id. Defaults to no --model flag (caller's claude default).

    Returns dict with at least: returncode, stdout, stderr, parsed (the JSON envelope or
    {} on parse failure), cost_usd, result_text, model.
    """
    cmd = [
        CLAUDE_BIN,
        "-p", prompt,
        "--permission-mode", "bypassPermissions",
        "--no-session-persistence",
        "--output-format", "json",
        "--add-dir", str(cwd),
    ]
    if model:
        cmd += ["--model", model]
    if extra_args:
        cmd += extra_args

    try:
        res = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout_s,
            encoding="utf-8",
            errors="replace",
            # On Windows, claude is typically claude.cmd; subprocess needs shell=False but
            # finds the .cmd via PATHEXT when shell=False is fine on Python 3.8+.
            shell=False,
        )
    except subprocess.TimeoutExpired as e:
        return {
            "returncode": -1,
            "stdout": (e.stdout or "")[-4000:] if isinstance(e.stdout, str) else "",
            "stderr": f"TIMEOUT after {timeout_s}s",
            "parsed": {},
            "cost_usd": 0.0,
            "result_text": "",
            "error": "timeout",
        }
    except FileNotFoundError:
        return {
            "returncode": -1,
            "stdout": "",
            "stderr": f"`{CLAUDE_BIN}` not found on PATH",
            "parsed": {},
            "cost_usd": 0.0,
            "result_text": "",
            "error": "claude_not_found",
        }

    parsed = _parse_claude_json(res.stdout)
    return {
        "returncode": res.returncode,
        "stdout": res.stdout,
        "stderr": res.stderr,
        "parsed": parsed,
        "cost_usd": float(parsed.get("total_cost_usd", 0.0) or 0.0),
        "result_text": parsed.get("result", "") or "",
        "model": model or "default",
    }


def _parse_claude_json(stdout: str) -> dict:
    """
    The `--output-format json` envelope is a single JSON object on stdout. In rare cases
    a leading banner sneaks in; fall back to scanning lines from the bottom for parseable JSON.
    """
    if not stdout:
        return {}
    stripped = stdout.strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass
    for line in reversed(stripped.splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    return {}


# ============================================================
# Turn execution
# ============================================================

def snapshot_files(work_dir: Path) -> dict:
    """Return {relpath: mtime} for everything under work_dir, ignoring .git."""
    snap = {}
    for path in work_dir.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            rel = str(path.relative_to(work_dir)).replace("\\", "/")
            try:
                snap[rel] = path.stat().st_mtime
            except OSError:
                continue
    return snap


def run_turn(
    work_dir: Path,
    input_file: Path,
    turn_index: int,
    cost_tracker: CostTracker,
    model: str = DEFAULT_TURN_MODEL,
    timeout_s: int | None = None,
    prompt_mode: str = "wrapped",
) -> dict:
    """Execute one scenario turn and return a result dict with before/after snapshots.

    Per-turn `model` and `timeout_s` overrides come from expected.yaml entries
    (e.g. `model: opus`, `timeout_s: 900`). When omitted, the harness-level
    defaults apply (DEFAULT_TURN_MODEL and TURN_TIMEOUT_S).

    `prompt_mode` controls how the artifact is sent to the agent:
      - "wrapped" (default): wrap in TURN_PROMPT_TEMPLATE — assumes a populated brain
        exists in cwd (CLAUDE.md + INDEX.md readable).
      - "passthrough": send the artifact body verbatim as the prompt. Use for install
        scenarios where the brain doesn't exist yet.
    """
    files_before = snapshot_files(work_dir)
    artifact = input_file.read_text(encoding="utf-8")
    if prompt_mode == "passthrough":
        prompt = artifact
    else:
        prompt = TURN_PROMPT_TEMPLATE.format(
            turn_index=turn_index,
            input_name=input_file.name,
            artifact=artifact,
        )
    effective_timeout = timeout_s if timeout_s is not None else TURN_TIMEOUT_S
    t0 = time.time()
    invocation = invoke_claude(prompt, cwd=work_dir, timeout_s=effective_timeout, model=model)
    duration = time.time() - t0
    files_after = snapshot_files(work_dir)

    cost_tracker.add("turn", f"turn-{turn_index}", invocation["cost_usd"])

    return {
        "turn": turn_index,
        "input": input_file.name,
        "model": model,
        "timeout_s": effective_timeout,
        "duration_s": round(duration, 2),
        "returncode": invocation["returncode"],
        "cost_usd": invocation["cost_usd"],
        "agent_response": invocation["result_text"],
        "stderr_tail": (invocation["stderr"] or "")[-2000:],
        "error": invocation.get("error"),
        "files_before": files_before,
        "files_after": files_after,
    }


# ============================================================
# Structural assertion dispatch
# ============================================================

def run_structural_assertions(
    work_dir: Path,
    assertions: list,
    snapshots: dict | None = None,
) -> list:
    """
    Dispatch to checks.structural for each entry in `assertions`.

    snapshots = {"before": {...}, "after": {...}} when running per-turn assertions;
    None for final-state assertions (where the diff types are not used).
    """
    results = []
    for a in assertions or []:
        try:
            results.append(structural_checks.run_assertion(work_dir, a, snapshots=snapshots))
        except Exception as e:  # noqa: BLE001 — defensive; one bad assertion shouldn't kill the run
            results.append({
                "name": str(a),
                "passed": False,
                "detail": f"assertion crashed: {type(e).__name__}: {e}",
            })
    return results


# ============================================================
# Content (LLM-judge) assertion dispatch
# ============================================================

def run_content_assertions(
    work_dir: Path,
    assertions: list,
    scenario_context: dict,
    cost_tracker: CostTracker,
    default_judge_model: str = DEFAULT_JUDGE_MODEL,
) -> list:
    """
    Run LLM-judge assertions. Each rubric is a markdown prompt; the judge call returns a
    verdict line which is parsed to PASS/FAIL/UNCERTAIN. UNCERTAIN counts as FAIL for this run.

    Each assertion may carry an optional `model:` key to override the default judge model
    (e.g. `model: opus` for high-judgment rubrics like decision_quality, audit_trail).
    """
    results = []
    for a in assertions or []:
        try:
            results.append(content_checks.run_judge(
                work_dir=work_dir,
                assertion=a,
                judges_dir=JUDGES_DIR,
                scenario_context=scenario_context,
                invoke_claude=invoke_claude,
                cost_tracker=cost_tracker,
                judge_timeout_s=JUDGE_TIMEOUT_S,
                default_model=default_judge_model,
            ))
        except CostBudgetExceeded:
            raise
        except Exception as e:  # noqa: BLE001
            results.append({
                "name": str(a),
                "passed": False,
                "detail": f"judge crashed: {type(e).__name__}: {e}",
            })
    return results


# ============================================================
# Main runner
# ============================================================

def run_once(
    scenario_dir: Path,
    run_index: int,
    max_cost: float | None,
    keep_workdir: bool,
    stop_after_turn: int | None,
    skip_content: bool,
) -> dict:
    scenario = load_scenario(scenario_dir)
    expected = scenario["expected"]
    inputs = scenario["inputs"]

    cost_tracker = CostTracker(max_cost)
    work_dir, cleanup = make_workdir(scenario_dir, run_index, keep_workdir)
    print(f"  work_dir: {work_dir}", file=sys.stderr)

    run_log = {
        "scenario": scenario_dir.name,
        "run": run_index,
        "work_dir": str(work_dir),
        "kept_workdir": keep_workdir,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "turns": [],
        "final_state": {},
        "aborted": False,
        "abort_reason": None,
    }

    try:
        if expected.get("bootstrap", "scaffold") != "skip":
            bootstrap_brain(work_dir)
        else:
            # Install-style scenario: don't copy the scaffold (the agent's job).
            # Do pre-stage the SKILL itself at .claude/skills/pm-brain/ so /pm-brain
            # is discoverable and the agent can read scaffold/ from inside the skill —
            # this mirrors how a real install resolves the skill on disk.
            skill_dest = work_dir / ".claude" / "skills" / "pm-brain"
            skill_dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(SKILL_PATH, skill_dest)
            print(
                f"  bootstrap: skipped scaffold copy; staged skill at .claude/skills/pm-brain/",
                file=sys.stderr,
            )
        scenario_prompt_mode = expected.get("prompt_mode", "wrapped")
        turn_configs = {t["input"]: t for t in expected.get("turns", [])}

        for i, input_file in enumerate(inputs, start=1):
            if stop_after_turn is not None and i > stop_after_turn:
                break
            tcfg = turn_configs.get(input_file.name, {})
            turn_model = tcfg.get("model", DEFAULT_TURN_MODEL)
            turn_timeout = tcfg.get("timeout_s")  # None falls back to TURN_TIMEOUT_S
            turn_prompt_mode = tcfg.get("prompt_mode", scenario_prompt_mode)
            print(f"  turn {i}/{len(inputs)}: {input_file.name}", file=sys.stderr)
            turn_result = run_turn(
                work_dir, input_file, i, cost_tracker,
                model=turn_model, timeout_s=turn_timeout,
                prompt_mode=turn_prompt_mode,
            )
            snapshots = {
                "before": turn_result["files_before"],
                "after": turn_result["files_after"],
            }
            turn_result["structural"] = run_structural_assertions(
                work_dir, tcfg.get("structural", []), snapshots=snapshots,
            )
            if skip_content:
                turn_result["content"] = []
                turn_result["content_skipped"] = True
            else:
                turn_result["content"] = run_content_assertions(
                    work_dir,
                    tcfg.get("content", []),
                    scenario_context={
                        "scenario": scenario_dir.name,
                        "scenario_dir": str(scenario_dir),
                        "turn": i,
                        "input": input_file.name,
                        "agent_response": turn_result.get("agent_response", ""),
                    },
                    cost_tracker=cost_tracker,
                )
            # Trim snapshots from on-disk log — they're large and the assertion results carry
            # the relevant signal.
            turn_result.pop("files_before", None)
            turn_result.pop("files_after", None)
            run_log["turns"].append(turn_result)

        # Final-state assertions only run if we didn't stop early.
        if stop_after_turn is None:
            final_cfg = expected.get("final_state", {})
            run_log["final_state"] = {
                "structural": run_structural_assertions(
                    work_dir, final_cfg.get("structural", []), snapshots=None,
                ),
                "content": [] if skip_content else run_content_assertions(
                    work_dir,
                    final_cfg.get("content", []),
                    scenario_context={
                        "scenario": scenario_dir.name,
                        "scenario_dir": str(scenario_dir),
                        "turn": "final",
                        "input": None,
                    },
                    cost_tracker=cost_tracker,
                ),
                "content_skipped": skip_content,
            }
    except CostBudgetExceeded as e:
        run_log["aborted"] = True
        run_log["abort_reason"] = str(e)
        print(f"  ABORTED: {e}", file=sys.stderr)
    finally:
        run_log["finished_at"] = datetime.now(timezone.utc).isoformat()
        run_log["cost"] = cost_tracker.summary()
        if not keep_workdir:
            cleanup()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = RESULTS_DIR / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{scenario_dir.name}-run{run_index}.json"
    out.write_text(json.dumps(run_log, indent=2), encoding="utf-8")
    print(f"  result: {out}  cost=${cost_tracker.total:.4f}", file=sys.stderr)
    return run_log


# ============================================================
# Aggregation across runs
# ============================================================

def aggregate(run_logs: list, threshold: dict) -> dict:
    """
    Per-assertion pass-rate rollup across N runs, with structural/content threshold check.
    """
    structural_results: dict[str, list[bool]] = {}
    content_results: dict[str, list[bool]] = {}

    def collect(bucket, items):
        for item in items or []:
            bucket.setdefault(item["name"], []).append(bool(item.get("passed")))

    for log in run_logs:
        for turn in log.get("turns", []):
            collect(structural_results, turn.get("structural"))
            collect(content_results, turn.get("content"))
        fs = log.get("final_state") or {}
        collect(structural_results, fs.get("structural"))
        collect(content_results, fs.get("content"))

    def rate(d):
        return {name: round(sum(v) / len(v), 3) for name, v in d.items() if v}

    structural_rates = rate(structural_results)
    content_rates = rate(content_results)

    structural_min = min(structural_rates.values()) if structural_rates else 1.0
    content_min = min(content_rates.values()) if content_rates else 1.0

    struct_thresh = float(threshold.get("structural", 1.0))
    content_thresh = float(threshold.get("content", 0.8))

    passed = structural_min >= struct_thresh and content_min >= content_thresh

    return {
        "runs": len(run_logs),
        "threshold": {"structural": struct_thresh, "content": content_thresh},
        "min_pass_rate": {"structural": structural_min, "content": content_min},
        "per_assertion": {
            "structural": structural_rates,
            "content": content_rates,
        },
        "passed": passed,
        "aborted_runs": sum(1 for log in run_logs if log.get("aborted")),
        "total_cost_usd": round(sum(log.get("cost", {}).get("total_usd", 0.0) for log in run_logs), 4),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario", type=Path, help="Path to scenario dir, e.g. tests/scenarios/01-b2b-churn")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--max-cost", type=float, default=None,
                    help="Abort run when cumulative cost exceeds this (USD). Per-run, not cross-run.")
    ap.add_argument("--keep-workdir", action="store_true",
                    help="Persist work dir under tests/workdir/<ts>-... instead of a TemporaryDirectory.")
    ap.add_argument("--stop-after-turn", type=int, default=None,
                    help="Stop after turn N (1-indexed). Skips final_state assertions.")
    ap.add_argument("--skip-content", action="store_true",
                    help="Skip LLM-judge (content) assertions. Structural only. Free/cheap mode.")
    args = ap.parse_args()

    scenario_dir = args.scenario.resolve()
    if not scenario_dir.is_dir():
        sys.exit(f"Scenario dir not found: {scenario_dir}")
    if not (scenario_dir / "expected.yaml").exists():
        sys.exit(f"expected.yaml not found in {scenario_dir}")

    expected = yaml.safe_load((scenario_dir / "expected.yaml").read_text(encoding="utf-8"))
    threshold = expected.get("pass_threshold", {"structural": 1.0, "content": 0.8})

    logs = []
    for i in range(1, args.runs + 1):
        print(f"--- run {i}/{args.runs} ---", file=sys.stderr)
        log = run_once(
            scenario_dir,
            i,
            max_cost=args.max_cost,
            keep_workdir=args.keep_workdir,
            stop_after_turn=args.stop_after_turn,
            skip_content=args.skip_content,
        )
        logs.append(log)

    summary = aggregate(logs, threshold)
    print(json.dumps(summary, indent=2))
    sys.exit(0 if summary["passed"] else 1)


if __name__ == "__main__":
    main()
