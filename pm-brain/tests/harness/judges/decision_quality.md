# Judge: decision_quality

## What we're checking

At turn 10, the PM asks the agent to draft a decision file. The decision is to ship weekly digest as default and real-time as a per-user opt-in paid add-on. The PM's prompt explicitly lists what the decision file must contain.

The decision file is the load-bearing artifact of the entire scenario. If the brain produces a clean decision file with full evidence trail and a specific reversal condition, the system has done its job. If it produces a vague file or buries the dissent or skips the reversal condition, the brain failed at exactly the moment it was supposed to deliver value.

## You will be given

- The target file(s): all markdown files under `decisions/`.
- The turn context: turn 10, decision moment.
- The PM's prompt requirements (from the input file).

## Pass criteria

ALL of the following must be true:

- A decision file exists in `decisions/` with a date and clear slug in the filename (e.g., `2026-05-13-defer-real-time-default-add-opt-in.md`).
- The file contains a "what we're deciding" paragraph in plain language.
- The file contains a "why" section that references the supporting evidence by name: at minimum the three customer interviews (Acme, Stripe, Notion), the eng sync, and the Vanta market signal.
- The file contains a "what we explicitly considered and rejected" section covering BOTH extremes (ship real-time as default; don't ship real-time at all).
- The Brex dissent is **named explicitly** in the decision file — not buried, footnoted, or omitted. The decision must acknowledge that Brex wanted real-time and explain how the chosen direction serves them.
- The file contains a "what would reverse this" field with a **specific, observable** condition. Vague conditions ("if customer feedback changes," "if things change") fail this criterion. The condition must be something a weekly `/review` sweep could mechanically check.
- The decision status is `pending` (the PM explicitly said don't mark it decided).
- The file links to: the hypothesis file, the three interview ingestion records, the eng sync, the Vanta market source. Links are working markdown (relative paths that resolve).

## Fail criteria (must_not)

- No reversal condition.
- Vague reversal condition.
- Brex dissent omitted, buried, or flattened.
- Decision status marked as `decided` instead of `pending`.
- Made-up evidence rows (citing artifacts not actually in the brain).
- Decision file claims more certainty than the evidence supports.
- Links broken (target paths don't resolve).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
