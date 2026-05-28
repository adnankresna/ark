"""
content.py — LLM-judge runner. Loads a rubric, builds the judge prompt with the
target file content + scenario context, calls `claude -p`, parses the VERDICT line.

UNCERTAIN counts as FAIL for the run. Aggregate pass-rate across N runs handles the noise.

Subprocess flakes (claude_not_found, timeout, empty result) are NOT brain-quality
signals — they're harness-environmental. We retry such invocations up to JUDGE_RETRY_MAX
times with backoff before recording the fail. Real model output (PASS/FAIL/UNCERTAIN,
or a non-empty response with no VERDICT line) is never retried — that would mask
genuine quality regressions behind noise.
"""

from __future__ import annotations

import re
import time
from pathlib import Path

# Retry tuning for subprocess-level flakes only (see _is_flake_invocation).
# 3 attempts caps wasted spend: if a launch race or transient throttle doesn't recover
# by attempt 3, attempt 4+ would just pay for more empty calls.
JUDGE_RETRY_MAX = 3
JUDGE_RETRY_BACKOFF_S = (1.0, 3.0, 8.0)  # sleep BEFORE attempt index N+1 (post-attempt-1, post-attempt-2)
# Invocation error codes that mean "subprocess never produced a real response" — not the model's fault.
_FLAKE_ERROR_CODES = frozenset({"claude_not_found", "timeout"})


JUDGE_PROMPT_TEMPLATE = """\
You are an evaluation judge for the PM Brain test suite.

Read the rubric below carefully. Then read the target file(s), the agent's response
text from this turn, and the scenario context. Then output exactly ONE line in the
required format. Do not output anything else.

The agent's response text is the chat-style summary the agent emitted at the end
of the turn. For synthesis-style turns (where the agent is asked to think rather
than write a new artifact), this is the primary signal — judge it as you would
judge the text directly.

=== RUBRIC ===

{rubric}

=== SCENARIO CONTEXT ===

- Scenario: {scenario}
- Turn: {turn}
- Last ingested input: {input}
- Expected meaning (from the test definition): {expected_meaning}
- Must NOT (from the test definition): {must_not}

=== AGENT RESPONSE (turn output, verbatim) ===

{agent_response}

=== TARGET FILE(S) ===

{targets}

=== END OF INPUT ===

Output exactly one line:
    VERDICT: PASS
    VERDICT: FAIL — <one-line reason>
    VERDICT: UNCERTAIN — <one-line reason>

Do not output anything else. No preamble. No explanation outside the verdict line.
"""

MAX_TARGET_CHARS = 30_000           # cap target-files blob per judge call
MAX_AGENT_RESPONSE_CHARS = 20_000   # cap inlined agent response (synthesis turns can be long)


def run_judge(
    work_dir: Path,
    assertion: dict,
    judges_dir: Path,
    scenario_context: dict,
    invoke_claude,           # callable: (prompt, cwd, timeout_s, model=...) -> dict
    cost_tracker,            # CostTracker instance
    judge_timeout_s: int = 180,
    default_model: str = "sonnet",
) -> dict:
    """
    Run one judge call against one assertion. Returns {name, passed, detail}.

    assertion is the dict form from expected.yaml, e.g.:
        {
          "judge": "hypothesis_proposed_not_promoted",
          "rubric": "judges/hypothesis_proposed.md",
          "target_glob": "hypotheses/*.md",
          "expected_meaning": "...",
          "must_not": "...",
          "model": "opus",   # optional: override default judge model
        }
    """
    if not isinstance(assertion, dict):
        return _result("malformed-content-assertion", False, f"expected dict, got {type(assertion).__name__}")

    judge_name = assertion.get("judge", "unnamed")
    # Prefer a scenario-local rubric override (tests/scenarios/<NN>/judges/foo.md) if present;
    # fall back to the shared rubric in tests/harness/judges/. This lets short focused scenarios
    # ship their own scenario-specific rubric text without polluting the shared ones.
    scenario_dir = scenario_context.get("scenario_dir")
    rubric_path = None
    if scenario_dir:
        rubric_path = _resolve_rubric_path(Path(scenario_dir) / "judges", assertion.get("rubric"))
    if rubric_path is None or not rubric_path.is_file():
        rubric_path = _resolve_rubric_path(judges_dir, assertion.get("rubric"))
    if rubric_path is None or not rubric_path.is_file():
        return _result(
            f"judge:{judge_name}",
            False,
            f"rubric not found: {assertion.get('rubric')}",
        )

    targets_blob, target_summary = _gather_targets(work_dir, assertion)
    if not targets_blob:
        # For absence-style rubrics (e.g., no_premature_promotion), zero matches IS the pass state.
        # Hand the judge a placeholder describing the absence and let the rubric + agent_response decide.
        targets_blob = (
            f"(No files matched the target glob: {target_summary}.\n"
            f"The agent may have intentionally NOT written anything matching this glob. "
            f"Decide PASS/FAIL using the rubric and the agent's response text above.)"
        )

    agent_response = scenario_context.get("agent_response") or "(no agent response available — final-state or pre-turn context)"
    # Cap agent_response so a verbose turn doesn't blow the prompt budget.
    if len(agent_response) > MAX_AGENT_RESPONSE_CHARS:
        agent_response = agent_response[:MAX_AGENT_RESPONSE_CHARS] + "\n\n[TRUNCATED]"

    prompt = JUDGE_PROMPT_TEMPLATE.format(
        rubric=rubric_path.read_text(encoding="utf-8"),
        scenario=scenario_context.get("scenario", "?"),
        turn=scenario_context.get("turn", "?"),
        input=scenario_context.get("input") or "(final state)",
        expected_meaning=assertion.get("expected_meaning", "(none provided)"),
        must_not=assertion.get("must_not", "(none provided)"),
        agent_response=agent_response,
        targets=targets_blob,
    )

    model = assertion.get("model") or default_model

    flake_attempts: list[str] = []  # short error codes from any retried-over invocations, for audit
    invocation = None
    verdict = "UNPARSED"
    reason = ""
    for attempt in range(1, JUDGE_RETRY_MAX + 1):
        if attempt > 1:
            time.sleep(JUDGE_RETRY_BACKOFF_S[min(attempt - 2, len(JUDGE_RETRY_BACKOFF_S) - 1)])
        invocation = invoke_claude(prompt, cwd=work_dir, timeout_s=judge_timeout_s, model=model)
        # Always track cost — every attempt that hit the API consumed quota even if it returned nothing.
        cost_tracker.add("judge", judge_name, invocation["cost_usd"])
        verdict, reason = _parse_verdict(invocation["result_text"])
        if not _is_flake_invocation(invocation, verdict, reason):
            break
        flake_attempts.append(invocation.get("error") or "empty-response")

    passed = verdict == "PASS"
    detail_bits = [f"verdict={verdict}", f"target={target_summary}"]
    if reason:
        detail_bits.append(f"reason={reason}")
    if invocation and invocation.get("error"):
        detail_bits.append(f"error={invocation['error']}")
    if flake_attempts:
        # Surface how many retries were burned and why, so a snapshot reader can tell signal from noise.
        detail_bits.append(f"flake_retries={len(flake_attempts)}({','.join(flake_attempts)})")
    return _result(f"judge:{judge_name}", passed, " | ".join(detail_bits))


def _is_flake_invocation(invocation: dict, verdict: str, reason: str) -> bool:
    """
    True iff this invocation's failure looks like a subprocess-level flake (worth retrying),
    not a real model output (must NOT retry — would mask genuine misses).

    Flake signatures:
      - invocation.error in {claude_not_found, timeout}
      - empty result_text (parsed as UNPARSED with the 'empty judge response' reason)

    Not flakes (do not retry):
      - verdict in {PASS, FAIL, UNCERTAIN} — the model answered
      - UNPARSED with a non-empty response that simply lacked a VERDICT line — the model
        produced output but mis-followed the instruction; that's a quality signal, not noise.
    """
    if invocation.get("error") in _FLAKE_ERROR_CODES:
        return True
    if verdict == "UNPARSED" and reason == "empty judge response":
        return True
    return False


# ============================================================
# Helpers
# ============================================================

def _resolve_rubric_path(judges_dir: Path, ref: str | None) -> Path | None:
    """expected.yaml writes `rubric: judges/foo.md`. Strip the leading 'judges/' and look it up here."""
    if not ref:
        return None
    name = Path(ref).name  # accept 'judges/foo.md' or 'foo.md'
    p = judges_dir / name
    return p if p.is_file() else None


def _gather_targets(work_dir: Path, assertion: dict) -> tuple[str, str]:
    """
    Resolve target_file or target_glob from assertion into a single text blob.
    Returns (blob, summary). Summary is a short string for assertion detail.
    """
    target_file = assertion.get("target_file")
    target_glob = assertion.get("target_glob")

    files: list[Path] = []
    summary = ""

    if target_file:
        p = work_dir / target_file
        if p.is_file():
            files = [p]
        summary = f"file:{target_file}"
    elif target_glob:
        alternatives = [a.strip() for a in re.split(r"\s+OR\s+", target_glob, flags=re.IGNORECASE) if a.strip()]
        seen: set[Path] = set()
        for alt in alternatives:
            for p in work_dir.glob(alt):
                if p.is_file() and p.name not in {"INDEX.md", "_SCHEMA.md"} and p not in seen:
                    seen.add(p)
        files = sorted(seen)
        summary = f"glob:{target_glob} ({len(files)} match)"
    else:
        # No explicit target — provide a directory listing so the judge can still answer
        # navigability-style questions like audit_trail.md.
        summary = "no-target (using work_dir listing)"
        listing_lines = []
        for p in sorted(work_dir.rglob("*.md")):
            if ".git" in p.parts:
                continue
            rel = p.relative_to(work_dir)
            listing_lines.append(str(rel).replace("\\", "/"))
        return ("# work_dir listing\n\n" + "\n".join(listing_lines))[:MAX_TARGET_CHARS], summary

    if not files:
        return "", summary

    blocks = []
    used = 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            text = f"(could not read: {e})"
        rel = f.relative_to(work_dir)
        header = f"\n\n----- FILE: {str(rel).replace(chr(92), '/')} -----\n\n"
        chunk = header + text
        if used + len(chunk) > MAX_TARGET_CHARS:
            remaining = MAX_TARGET_CHARS - used
            if remaining > len(header) + 200:
                blocks.append(chunk[:remaining] + "\n\n[TRUNCATED]\n")
            break
        blocks.append(chunk)
        used += len(chunk)

    return "".join(blocks), summary


# Reason group uses a tempered greedy token: any char that isn't the start of another
# VERDICT marker. This lets finditer return EVERY verdict in the text, not just the
# first one — without it, the greedy `.*` swallows the rest of the string and finditer
# stops after match 1.
_VERDICT_RE = re.compile(
    r"VERDICT\s*:\s*(PASS|FAIL|UNCERTAIN)\b\s*"
    r"(?:[—\-:]\s*((?:(?!VERDICT\s*:)[^\n])*))?",
    re.IGNORECASE,
)


def _parse_verdict(text: str) -> tuple[str, str]:
    """
    Returns (verdict, reason). verdict is PASS/FAIL/UNCERTAIN/UNPARSED.
    Takes the LAST `VERDICT:` token anywhere in the text. Judges sometimes write a
    reasoning chain that contains multiple "VERDICT: X" tokens (often self-correcting
    after re-reading the rubric) and the final one is the actual call.
    """
    if not text:
        return "UNPARSED", "empty judge response"
    matches = list(_VERDICT_RE.finditer(text))
    if not matches:
        return "UNPARSED", f"no VERDICT line found in: {text[:160]!r}"
    m = matches[-1]
    verdict = m.group(1).upper()
    reason = (m.group(2) or "").strip().rstrip(" -—:.")
    return verdict, reason


def _result(name: str, passed: bool, detail: str) -> dict:
    return {"name": name, "passed": bool(passed), "detail": detail}
