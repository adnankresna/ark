# Judge: evidence_quality_evaluated (scenario 10 — promotion gate)

## What we're checking

At turn 2, the PM asks the brain whether to promote `same-day-rebooking-flow` from `proposed` to `promoted`. The PM explicitly asks for provenance-tier counts on the evidence. The brain's value here is that it does NOT treat evidence as an undifferentiated pile — it counts and weighs by trust tier from the canonical enum. Path-typed `[ingestion/...]` and `[source/...]` rows are highest trust; `(stakeholder-verbal, ...)` is medium; `(intuition, PM, ...)` and `(industry-knowledge)` are low; `(chat, no artifact)` is low.

The hypothesis as seeded in turn 1 has roughly: 2 path-typed ingestion records supporting the value claim (Westside, Bayfront customer interviews); 1 stakeholder-verbal supporting (Jordan / VP Customer Success on Q1 ticket data); 1 intuition row from the PM herself supporting; 1 industry-knowledge row supporting (competitor analogs and the +5pp utilization rule of thumb); 1 stakeholder-verbal against on the feasibility side (Sam / Eng Tech Lead flagging the calendar-refactor concern). Total: ~5 supporting + ~1 against, across at least 4 distinct provenance tiers.

The right behavior is a response that names actual counts per tier and treats the highest-trust evidence as carrying more weight than the lowest-trust evidence — not "5 vs 1, looks supportive" but something like "2 high-trust supporting + 1 medium + 2 low; 1 medium against (uninvestigated)."

## You will be given

- The agent's turn-2 response text in `agent_response`.
- The target file(s): all markdown files under `hypotheses/` (so the judge can cross-check evidence-row counts if it wants).

## Pass criteria

ALL of the following must be true:

- The agent's response NAMES specific counts of evidence rows broken out by provenance tier — not as a single aggregated count. At minimum: distinguishes path-typed (`[ingestion/...]` / `[source/...]`) from non-path-typed (stakeholder-verbal, intuition, industry-knowledge).
- The agent treats higher-trust tiers as carrying more weight than lower-trust tiers in its evaluation — not just lists the counts but reasons from them.
- The agent identifies the Sam-feasibility row as a stakeholder-verbal evidence-against (or "concern flagged") row, not as undifferentiated noise.
- The accounting is roughly consistent with the seeded state (the response doesn't claim a tier count that doesn't exist on the hypothesis — e.g., it doesn't claim 4 ingestion records when only 2 exist).

## Fail criteria (must_not)

- The response treats evidence as a single aggregated count ("we have 5 pieces of evidence supporting" with no tier breakdown).
- The response weighs intuition / industry-knowledge as equivalent to path-typed evidence.
- The response invents evidence rows or tier counts that the hypothesis doesn't actually contain.
- The response omits the tier breakdown entirely and just summarizes qualitatively ("we have strong customer signal").

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
