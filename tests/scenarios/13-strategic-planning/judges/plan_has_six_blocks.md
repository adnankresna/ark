# Judge: plan_has_six_blocks (scenario 13 — strategic-planning, turn 4)

## What we're checking

Turn 4 invokes `/plan reduce weekly-dashboard load time by 40% in Q3`. The `/plan` command spec mandates six blocks in this order, plus three additional sections.

The right behavior:

The response (and/or the draft `ingestion/adhoc/...plan...md` artifact) contains all six blocks:

1. **What we already know** — with citations to insights, hypotheses, decisions, metrics.
2. **Assumption vs evidence** — explicitly tagged, with provenance per claim.
3. **Who to interview** — segments, personas, specific named users; recent coverage gaps.
4. **Hypotheses to open** — across the 5 risk areas, with a test for each.
5. **Experiments to run** — sequenced, with success criteria + what would invalidate.
6. **Decision points** — go/no-go moments and what evidence unlocks each.

Plus:

- Constraints from `strategy.md § Non-goals` that bound the plan (mobile UI, no pricing tiers).
- Stakeholder alignment conversations the plan requires (linked to `/prep`).
- A paragraph on what would make the plan unwise (so the PM can falsify it early).

## You will be given

- The agent's full turn-4 response.
- The draft `ingestion/adhoc/*plan*.md` file if one was written.

## Pass criteria

ALL of the following must be true:

- All 6 blocks are present in either the response or the draft artifact, in roughly the spec order. Acceptable variants on names: "Knowns" for #1, "Hypotheses" for #4, "Tests" for #5, "Gates" for #6 — as long as each block's substance maps to the spec.
- Block 1 ("what we know") cites at least one specific brain artifact (insight, hypothesis, decision, ingestion, metric).
- Block 4 ("hypotheses to open") names at least 3 of the 5 risk areas with a test for each.
- The non-goal constraint section names at least one specific strategy.md non-goal (mobile UI OR new pricing tiers).
- The "what would make this unwise" falsification paragraph is present.

## Fail criteria (must_not)

- Fewer than 6 blocks (one or more silently skipped).
- The "what we know" block has no brain citations (it's just paraphrased generic claims).
- The non-goal constraint section is missing or mentions no specific strategy.md non-goal.
- The "what would make this unwise" falsification paragraph is missing.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
