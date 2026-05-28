#!/usr/bin/env python3
"""
rejudge.py — re-run one or more LLM-judge assertions against a kept workdir, reusing
the agent_response captured in a prior result JSON.

USAGE
    python tests/harness/rejudge.py <result.json> --turn 7
    python tests/harness/rejudge.py <result.json> --turn 7 --judge full_trail_synthesized
    python tests/harness/rejudge.py <result.json> --final

WHY
    A full scenario re-run costs ~$5 in agent turns. When the only thing that changed
    is a judge rubric, the prompt template, or a scoring tweak, you just need to ask
    the judge again — not replay 10 turns. This script does that.

    It loads the kept workdir (from --keep-workdir runs), reads the agent_response that
    was stored in the result JSON, rebuilds the judge prompt, and calls `claude -p`.
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("ERROR: PyYAML required. pip install pyyaml\n")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checks import content as content_checks  # noqa: E402
from run_scenario import (  # noqa: E402
    CostTracker,
    JUDGES_DIR,
    JUDGE_TIMEOUT_S,
    DEFAULT_JUDGE_MODEL,
    REPO_ROOT,
    invoke_claude,
)


def find_turn_assertions(scenario_dir: Path, turn_index: int) -> tuple[str, list]:
    expected = yaml.safe_load((scenario_dir / "expected.yaml").read_text(encoding="utf-8"))
    for t in expected.get("turns", []):
        if t.get("turn") == turn_index:
            return t.get("input", "?"), t.get("content", []) or []
    return "?", []


def find_final_assertions(scenario_dir: Path) -> list:
    expected = yaml.safe_load((scenario_dir / "expected.yaml").read_text(encoding="utf-8"))
    return (expected.get("final_state", {}) or {}).get("content", []) or []


def filter_judges(assertions: list, judge_name: str | None) -> list:
    if not judge_name:
        return assertions
    return [a for a in assertions if isinstance(a, dict) and a.get("judge") == judge_name]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("result", type=Path, help="Path to a prior result JSON (from --keep-workdir run)")
    ap.add_argument("--turn", type=int, default=None, help="Re-judge content assertions for this turn (1-indexed)")
    ap.add_argument("--final", action="store_true", help="Re-judge final_state content assertions")
    ap.add_argument("--judge", type=str, default=None, help="Filter to one judge by name (e.g. full_trail_synthesized)")
    args = ap.parse_args()

    if not args.result.is_file():
        sys.exit(f"Result JSON not found: {args.result}")
    if (args.turn is None) == (not args.final):
        sys.exit("Specify exactly one of --turn N or --final")

    log = json.loads(args.result.read_text(encoding="utf-8"))
    work_dir = Path(log["work_dir"])
    if not work_dir.is_dir():
        sys.exit(f"Workdir from result is gone: {work_dir}")

    scenario_dir = REPO_ROOT / "tests" / "scenarios" / log["scenario"]
    if not scenario_dir.is_dir():
        sys.exit(f"Scenario dir not found: {scenario_dir}")

    cost = CostTracker(max_cost=None)

    if args.turn is not None:
        turn_record = next((t for t in log.get("turns", []) if t.get("turn") == args.turn), None)
        if turn_record is None:
            sys.exit(f"No turn {args.turn} in result JSON")
        input_name, assertions = find_turn_assertions(scenario_dir, args.turn)
        assertions = filter_judges(assertions, args.judge)
        if not assertions:
            sys.exit(f"No matching content assertions for turn {args.turn} (judge filter={args.judge!r})")
        agent_response = turn_record.get("agent_response", "")
        ctx = {
            "scenario": log["scenario"],
            "turn": args.turn,
            "input": input_name,
            "agent_response": agent_response,
        }
    else:
        assertions = filter_judges(find_final_assertions(scenario_dir), args.judge)
        if not assertions:
            sys.exit(f"No matching final_state content assertions (judge filter={args.judge!r})")
        ctx = {
            "scenario": log["scenario"],
            "turn": "final",
            "input": None,
            "agent_response": "",
        }

    results = []
    for a in assertions:
        r = content_checks.run_judge(
            work_dir=work_dir,
            assertion=a,
            judges_dir=JUDGES_DIR,
            scenario_context=ctx,
            invoke_claude=invoke_claude,
            cost_tracker=cost,
            judge_timeout_s=JUDGE_TIMEOUT_S,
            default_model=DEFAULT_JUDGE_MODEL,
        )
        results.append(r)
        print(json.dumps(r, indent=2))

    print(f"\ntotal_cost_usd: {cost.total:.4f}", file=sys.stderr)
    sys.exit(0 if all(r.get("passed") for r in results) else 1)


if __name__ == "__main__":
    main()
