# Judge: expiring_reversal_flagged (scenario 08 — weekly /review)

## What we're checking

The `decisions/2026-03-10-on-call-rotation-rework.md` decision carries a specific reversal condition: **"if NPS among on-call engineers drops below 32 by end of May 2026, revisit the rotation model."** Today is 2026-05-17 — the deadline is ~2 weeks out. This is exactly the kind of expiring-condition signal a holistic /review should surface, with the **specific details intact** — not abstracted into "a decision is approaching review."

The wrong behavior is abstraction. "We have something coming up at end of month" is not surfacing — it's gesturing. The PM needs to know *which* decision, *what* the metric is, and *when* the deadline lands, because that's what determines whether action is needed (check the NPS data) and when.

This is a stricter version of one of the items checked by `multiple_categories_surfaced`. That judge passes if any one of {deadline, metric} is named; this judge requires both the deadline AND the metric AND the specific decision pointer.

## You will be given

- The agent's turn-3 `/review` response text in `agent_response`.
- The work_dir (judge may inspect the decision file under `decisions/` to verify the cited deadline / metric match what's in the file).

## Pass criteria

ALL of the following must be true:

- The /review response identifies the **specific decision**, by file path (`decisions/2026-03-10-on-call-rotation-rework.md` or equivalent) or by an unambiguous topic reference ("the March 10 on-call rotation rework decision," "the rotation-rework decision from March"). A bare "a decision" or "one of our March decisions" does not pass.
- The /review response names the **specific deadline**: end of May 2026, or 2026-05-31, or "in about two weeks," or an equivalent phrase that pins the time horizon to end of May. "Coming up" or "soon" does not pass.
- The /review response names the **specific metric**: NPS among on-call engineers below 32. The threshold value (32) AND the metric (on-call engineer NPS) must both appear. "If satisfaction drops" or "if NPS moves" without the 32 threshold does not pass.
- All three details (decision pointer, deadline, metric) appear together — clustered in the same paragraph / bullet / section, not scattered such that a reader can't tell they relate to the same decision.

## Fail criteria (must_not)

- The expiring reversal is described abstractly without the decision pointer ("a decision is approaching its reversal window").
- The deadline is described as "end of month" or "soon" without anchoring to end of May 2026 / 2026-05-31.
- The metric is mentioned only by shape ("if engagement drops") without the specific NPS-below-32 threshold.
- The decision pointer, deadline, and metric appear in the response but in places so disconnected that a reader cannot tell they belong to the same decision.
- The /review omits this category entirely.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
