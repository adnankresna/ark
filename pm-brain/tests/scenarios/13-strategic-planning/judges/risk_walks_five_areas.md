# Judge: risk_walks_five_areas (scenario 13 — strategic-planning, turn 3)

## What we're checking

Turn 3 invokes `/risk weekly-snapshot`. The command spec says it walks all 5 risk areas and, under default autonomy ("act and tell"), drafts stub hypotheses for any area with no coverage. Risks with active hypotheses and fresh evidence are not touched.

The seeded `weekly-snapshot` feature has NO linked hypotheses. So all 5 areas should be flagged as either implicit-coverage-but-no-hypothesis (value) or explicit-gap (feasibility, viability, other). Stubs should land for the gaps.

The right behavior:

- All 5 risk areas walked by name (value, usability, feasibility, viability, other) with a status marker like `[have hypothesis | stub drafted | confirmed | demoted]`.
- For each: one line on what's missing.
- Stubs drafted for the gap areas — at least 2 new hypothesis files should land (typically Feasibility, Viability, possibly Usability or Other).
- No new stub is auto-promoted. All have status `candidate` or `active`. NOT `promoted`, NOT `partially-validated`.
- 1-3 highest-leverage tests called out.
- Any non-goal the feature might violate is named (per the spec).

## You will be given

- The agent's full turn-3 response.
- Any new hypothesis files created this turn.
- The updated feature file `knowledge/product/features/weekly-snapshot.md`.

## Pass criteria

ALL of the following must be true:

- All 5 risk areas are walked explicitly: Value, Usability, Feasibility, Viability, and Other (the fifth area; acceptable labels include "Other", "Partnership/ecosystem", "Timing", "Strategic", etc., AS LONG AS the schema-canonical "Other" slot is filled with something).
- Each risk area is marked with status (have hypothesis / stub drafted / confirmed / demoted) and one line of context.
- At least one NEW hypothesis stub file lands for a gap area (feasibility OR viability OR other). The hypothesis files must reference `weekly-snapshot` in some form.
- No new stub has status `promoted` or `partially-validated`. All are `candidate`, `active`, or `proposed`.
- At least one of the 1-3 highest-leverage tests is named.

## Fail criteria (must_not)

- Fewer than 5 risk areas are walked (e.g., only 3 or 4 named).
- The response is read-only (no new hypothesis stubs drafted for the gap areas — the spec is explicit: default autonomy = act and tell).
- A new stub hypothesis is created with status `promoted` or `partially-validated`.
- The response confuses risk areas with arbitrary categories (e.g., invents "Ethical" as a separate top-level area when the schema uses Other for that).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
