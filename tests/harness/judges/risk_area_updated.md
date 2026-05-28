# Judge: risk_area_updated

## What we're checking

When new evidence comes in, it should update the **right risk area** on the hypothesis. The five risk areas are value, usability, feasibility, viability, and other. Routing evidence to the wrong risk area is a structural error: it flattens the hypothesis's reasoning.

At turn 2 (engineering sync on real-time pipeline feasibility), the feasibility risk area on the alert-cadence hypothesis should be updated with the eng team's findings — 6-week build estimate, operational on-call posture change. The value risk area should NOT be modified by an eng-feasibility input.

## You will be given

- The target file(s): all markdown files under `hypotheses/`.
- The turn context: turn 2, engineering sync.
- The risk area expected to update: `feasibility`.

## Pass criteria

ALL of the following must be true:

- The hypothesis file's **feasibility** risk section contains a new evidence row referencing the eng sync ingestion (turn 2).
- The evidence row captures concrete details: 6-week build estimate, two engineers, or the on-call SLO trade-off.
- The hypothesis's **value** risk section was NOT modified by this turn (eng input has no value-risk content).

## Fail criteria (must_not)

- Eng feasibility findings landed in the value-risk section.
- Eng feasibility findings landed in viability section as a price/willingness-to-pay claim (eng didn't speak to viability).
- Feasibility evidence is vague ("eng says it's possible") without the specific build estimate or operational concern.
- The hypothesis file wasn't updated at all (eng sync was ingested but no propagation).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
