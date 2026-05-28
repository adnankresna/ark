"""
Unit tests for the PostToolUse validator hook
(`.claude/skills/pm-brain/scaffold/.claude/hooks/validate_brain_file.py`).

Run from tests/harness/:
    python -m checks.test_hook_validator

No LLM calls. Each case spins up a fresh temp brain fixture, invokes the hook
script as a subprocess (the same way Claude Code invokes it), and asserts on:
  - exit code (0 = pass-or-warn, 2 = block)
  - whether the stderr message contains the expected diagnostic

The hook's two-tier severity is the load-bearing contract:
  BLOCK (exit 2) — evidence row with NO provenance attempt at all
                   (no enum tag and no [ingestion/...] / [source/...] link).
                   The agent can always fix this in-turn without depending on
                   any other file existing.
  WARN  (exit 0 + stderr) — broken internal links and unresolved path-typed
                            provenance links. Likely ordering issues (forward
                            reference, mutual reference). The structural sweep
                            at scenario end catches anything left over.

These tests assert that bedrock contract: don't block on ordering, do block
on truly-orphaned claims, never block on legitimate placeholders.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


HOOK = (
    Path(__file__).resolve().parents[3]
    / ".claude" / "skills" / "pm-brain" / "scaffold" / ".claude" / "hooks"
    / "validate_brain_file.py"
)


# ---- fixture builder ---------------------------------------------------------

def _make_brain(tmp: Path) -> Path:
    """Minimal brain layout the hook's _find_work_dir will recognize."""
    (tmp / "hypotheses").mkdir(parents=True, exist_ok=True)
    (tmp / "decisions").mkdir(parents=True, exist_ok=True)
    (tmp / "source" / "interviews").mkdir(parents=True, exist_ok=True)
    (tmp / "ingestion" / "interviews").mkdir(parents=True, exist_ok=True)
    (tmp / "knowledge").mkdir(parents=True, exist_ok=True)
    (tmp / "INDEX.md").write_text("# Index\n", encoding="utf-8")
    (tmp / "CLAUDE.md").write_text("# Brain\n", encoding="utf-8")
    return tmp


def _write(tmp: Path, rel: str, body: str) -> Path:
    p = tmp / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    return p


def _invoke_hook(file_path: Path) -> tuple[int, str, str]:
    """Run the hook as Claude Code would: feed JSON to stdin, capture exit + stderr."""
    payload = json.dumps({"tool_input": {"file_path": str(file_path)}})
    proc = subprocess.run(
        [sys.executable, str(HOOK)],
        input=payload,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return proc.returncode, proc.stdout, proc.stderr


# ---- fixture bodies ----------------------------------------------------------

PASS_BODY = """# Hypothesis: pass

Status: active

## Evidence for:

- Customer Tom said he'd switch without shared-budgets [source/interviews/2026-01-01-tom.md](../source/interviews/2026-01-01-tom.md)
- PM hunch: this is couples-budgeting pattern (intuition, PM, 2026-05-17)
- Common industry fact (industry-knowledge)
- Talked to Marcus offline (stakeholder-verbal, marcus, 2026-05-10)
- Heard in a chat conversation (chat, no artifact)

## Evidence against:

- (none yet)
"""

ORPHAN_BODY = """# Hypothesis: orphan

Status: active

## Evidence for:

- Tom said he wants shared budgets — strong signal.
- CS has fielded multiple requests this quarter.

## Evidence against:

- (none yet)
"""

WARN_PATH_BODY = """# Hypothesis: warn-path

Status: active

## Evidence for:

- Tom confirms shared-budgets demand [source/interviews/2026-05-17-tom.md](../source/interviews/2026-05-17-tom.md)

## Evidence against:

- (none yet)
"""

WARN_LINK_BODY = """# Hypothesis: warn-link

A reference [to another file](./other.md) that doesn't exist yet.

## Evidence for:

- A real claim with a tag (intuition, PM, 2026-05-17)

## Evidence against:

- (none yet)
"""

PLACEHOLDER_BODY = """# Hypothesis: placeholder

Status: active

## Evidence for:

- (none yet)
- TBD
- N/A
- *(none from current sources)*
- (None yet — billing model is explicitly unresolved.)
- —

## Evidence against:

- (none yet)
"""

BOLD_EVIDENCE_BODY = """# Hypothesis: bold-evidence

## Value risk
### H-V1: users want X
- **Evidence for:**
  - PM intuition says yes (intuition, PM, 2026-05-17)
  - An untagged claim that should orphan.

## Evidence against:

- (none yet)
"""

DECISION_PASS_BODY = """# Decision: 2026-05-17-foo

Status: pending
Reversal condition: if hypothesis H1 demoted by Q4.

## Evidence:

- Signal from Tom (stakeholder-verbal, tom, 2026-04-01)
- Source artifact [source/interviews/2026-01-01-tom.md](../source/interviews/2026-01-01-tom.md)
"""

DECISION_ORPHAN_BODY = """# Decision: 2026-05-17-bar

Status: pending
Reversal condition: if usage falls below 100 DAU.

## Evidence:

- Customer A wants this.
- Customer B also wants this.
"""

KNOWLEDGE_FILE_BODY = """# Knowledge — strategy

We will focus on couples-budgeting Q3. (no evidence rows here — not a brain audit file)

- A bullet without a tag
- Another bullet
"""


# ---- the cases --------------------------------------------------------------

# Each case: (name, [(rel_path, body), ...], file_under_test_rel, expected_exit, stderr_substr_or_None)
CASES: list[tuple] = [
    (
        "pass — all five enum forms + path-typed link",
        [("source/interviews/2026-01-01-tom.md", "raw\n"),
         ("hypotheses/pass.md", PASS_BODY)],
        "hypotheses/pass.md", 0, None,
    ),
    (
        "block — evidence rows with no provenance attempt",
        [("hypotheses/orphan.md", ORPHAN_BODY)],
        "hypotheses/orphan.md", 2, "BLOCKING",
    ),
    (
        "warn-only — path-typed link to source file that doesn't exist yet",
        [("hypotheses/warn-path.md", WARN_PATH_BODY)],
        "hypotheses/warn-path.md", 0, "warnings",
    ),
    (
        "warn-only — broken non-evidence internal link",
        [("hypotheses/warn-link.md", WARN_LINK_BODY)],
        "hypotheses/warn-link.md", 0, "warnings",
    ),
    (
        "pass — all known placeholder shapes are exempt",
        [("hypotheses/placeholder.md", PLACEHOLDER_BODY)],
        "hypotheses/placeholder.md", 0, None,
    ),
    (
        "block — bold-label evidence rows are scanned for orphans too",
        [("hypotheses/bold.md", BOLD_EVIDENCE_BODY)],
        "hypotheses/bold.md", 2, "BLOCKING",
    ),
    (
        "pass — decision file with valid provenance",
        [("source/interviews/2026-01-01-tom.md", "raw\n"),
         ("decisions/2026-05-17-foo.md", DECISION_PASS_BODY)],
        "decisions/2026-05-17-foo.md", 0, None,
    ),
    (
        "block — decision file with orphan evidence rows",
        [("decisions/2026-05-17-bar.md", DECISION_ORPHAN_BODY)],
        "decisions/2026-05-17-bar.md", 2, "BLOCKING",
    ),
    (
        "ignore — non-brain file (knowledge/) is not audited for orphans",
        [("knowledge/strategy.md", KNOWLEDGE_FILE_BODY)],
        "knowledge/strategy.md", 0, None,
    ),
    (
        "ignore — _SCHEMA.md is exempt",
        [("hypotheses/_SCHEMA.md", ORPHAN_BODY)],
        "hypotheses/_SCHEMA.md", 0, None,
    ),
    (
        "ignore — INDEX.md is exempt",
        [("hypotheses/INDEX.md", ORPHAN_BODY)],
        "hypotheses/INDEX.md", 0, None,
    ),
    (
        "ignore — file outside any brain root (no markers)",
        [],  # special: file written outside the fixture
        "__outside__/foo.md", 0, None,
    ),
    (
        "ignore — empty/malformed stdin payload",
        [],  # special: empty payload, no file_path
        "__empty__", 0, None,
    ),
]


# ---- runner -----------------------------------------------------------------

def _run() -> int:
    print(f"Hook script: {HOOK}")
    if not HOOK.is_file():
        print(f"FATAL: hook not found at {HOOK}")
        return 1

    failures = 0
    for name, fixture_files, file_under_test, expected_exit, expected_stderr_substr in CASES:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            _make_brain(tmp)
            for rel, body in fixture_files:
                _write(tmp, rel, body)

            # Special cases.
            if file_under_test == "__outside__/foo.md":
                # File in a temp dir with no brain markers → hook should ignore.
                with tempfile.TemporaryDirectory() as td2:
                    outside = Path(td2) / "foo.md"
                    outside.write_text(ORPHAN_BODY, encoding="utf-8")
                    code, _, err = _invoke_hook(outside)
            elif file_under_test == "__empty__":
                proc = subprocess.run(
                    [sys.executable, str(HOOK)],
                    input="",
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                code, err = proc.returncode, proc.stderr
            else:
                fp = tmp / file_under_test
                code, _, err = _invoke_hook(fp)

            exit_ok = (code == expected_exit)
            stderr_ok = (
                expected_stderr_substr is None
                or expected_stderr_substr.lower() in err.lower()
            )
            ok = exit_ok and stderr_ok
            mark = "PASS" if ok else "FAIL"
            print(f"  [{mark}] {name}  (exit={code}, expected={expected_exit})")
            if not ok:
                failures += 1
                if not exit_ok:
                    print(f"         exit mismatch: got {code} expected {expected_exit}")
                if not stderr_ok:
                    print(f"         expected stderr substr: {expected_stderr_substr!r}")
                    print(f"         actual stderr (first 400 chars): {err[:400]!r}")

    total = len(CASES)
    print(f"\n{total - failures}/{total} cases passed.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(_run())
