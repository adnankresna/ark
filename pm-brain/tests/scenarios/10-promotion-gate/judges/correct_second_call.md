# Judge: correct_second_call (scenario 10 — promotion gate)

## What we're checking

At turn 4, the PM asks the promotion question for the second time. Between turn 2 and turn 4, the PM filled both gaps the brain flagged: a feasibility memo from Sam (refactor scoped at 3 sprints, manageable risk, eng recommends proceed) and a business-case analysis (modeling +2.1pp retention lift on mid-market segment, Priya verbally signed off on the math) have been ingested and added as evidence rows under Feasibility and Viability respectively. The hypothesis file now has supporting evidence in 4 of 5 risk areas (Value strong, Feasibility now well-scoped, Viability now modeled, plus Maria's usability concern noted; Other still appropriately empty).

The right behavior is one of two paths:

- **(a) Promotion-via-decision (default expectation).** The brain drafts a promotion as a new file under `decisions/2026-05*.md`. The decision file has status `proposed` (or `pending` — the PM still needs to sign off; the decision artifact IS the promotion draft, not the final approval). The decision references the hypothesis. Evidence rows in the decision cite BOTH the April customer interviews AND the May feasibility memo + business case, each row tagged with provenance from the canonical enum. A specific observable reversal condition is named. An "Explicitly NOT doing" section names what's coming off the table. Remaining ambiguities are surfaced (at minimum: that Priya flagged the retention causality as an interpretation, the iOS APNs deliverability dependency, or the pricing attach-rate assumption). The brain MAY also flip the hypothesis's `status:` to `promoted` AFTER (and only after) the decision file is drafted, AND must explicitly narrate the flip in its response, referencing the decision file as the audit trail.

- **(b) Hold the line with a specific further gap.** Acceptable iff the brain articulates a specific gap that the new evidence didn't close (e.g., "the +2.1pp retention number is modeled, not observed — recommend pilot before committing"). A vague "still not enough" without a specific named gap fails.

The wrong behaviors: (i) silently flip the hypothesis status to `promoted` without producing a decision file — the schema explicitly requires a decision artifact for promotion; (ii) draft a decision but omit the reversal condition, or write a vague one ("if things change"); (iii) draft a decision but leave evidence rows untagged with provenance; (iv) draft a decision that cites only the new May evidence and omits the April customer signal (or vice versa) — the promotion rests on the *combined* evidence and the decision must show that.

## You will be given

- The target file(s): `decisions/2026-05*.md` (the new promotion decision, if drafted).
- The agent's turn-4 response text in `agent_response`.

## Pass criteria

ALL of the following must be true (under path (a) — promotion-via-decision; the default):

- A new file exists under `decisions/2026-05*.md` referencing the `same-day-rebooking-flow` hypothesis.
- The decision file's `Status:` is `proposed` or `pending` (NOT `decided` — the PM said she wants to review before final).
- Evidence rows in the decision are tagged with provenance from the canonical enum (`[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, ...)`, `(intuition, PM, ...)`, `(industry-knowledge)`, `(chat, no artifact)`).
- The decision evidence cites BOTH the April customer signal (Westside and/or Bayfront and/or the Jordan stakeholder-verbal) AND the May feasibility memo AND the May business case. All three eras of evidence are visible in the decision file.
- A specific, observable reversal condition is named — not "if things change" but something like "if adoption < X% at week N post-GA, OR retention lift fails to materialize by Q4 measurement."
- An "Explicitly NOT doing" section names at least one thing coming off the table with this call.
- At least one remaining ambiguity is named — at minimum one of: the retention-causality interpretation, the iOS APNs dependency, or the pricing attach-rate assumption.
- If the hypothesis's `status:` field is also flipped to `promoted` in this turn, the agent's response narrates the flip AND references the decision file as the audit trail.

OR (under path (b) — hold the line):

- The agent's response explicitly says the promotion bar is not yet met AND names a specific further gap the new evidence didn't close (not just "more evidence needed").
- No decision file is drafted; no silent status flip.

## Fail criteria (must_not)

- The hypothesis's `status:` field is flipped to `promoted` (or any non-`proposed` value implying approval) without a decision file existing in `decisions/2026-05*.md` first.
- The decision file omits the reversal condition, or writes a vague one ("if things change").
- Evidence rows in the decision lack provenance tags.
- The decision file cites only the May evidence and omits the April customer signal — or cites only the April evidence and omits the May feasibility/viability work that closed the gaps. The promotion rationale must show the full evidence trail.
- The decision file's `Status:` is `decided` (the PM explicitly asked for `proposed` so she can review).
- Under path (b), the brain says "not yet" without naming a specific further gap.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
