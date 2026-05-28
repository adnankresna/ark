# Judge: five_risk_areas_covered (scenario 12 — decision-lifecycle, turn 3)

## What we're checking

Turn 3 invokes `/hypothesize auto-approve-under-50`. The `/hypothesize` spec says pre-ship hypothesis generation MUST cover all 5 risk areas (value, usability, feasibility, viability, other), even if the answer for some areas is "no risk identified, monitor." Silent gaps are themselves a risk.

The right behavior:

- Hypothesis file exists at `hypotheses/auto-approve-under-50.md` (or close variant).
- All 5 risk areas are explicitly addressed. For each: either a hypothesis (belief + evidence row + test plan + decision trigger) OR an explicit "no risk identified, monitor" call-out.
- The **viability** area wires in Diana's fraud-risk concern — that's the most directly load-bearing risk on this feature, and the seed material made it impossible to miss.
- Every Evidence row carries a provenance tag from the canonical enum.
- All hypotheses are status `active` or `candidate`. NONE are `promoted` or `partially-validated` — testing has not begun.

## You will be given

- The hypothesis file (target_glob: `hypotheses/*auto-approve*.md OR hypotheses/*auto_approve*.md`).

## Pass criteria

ALL of the following must be true:

- All 5 risk areas are addressed by name (value, usability, feasibility, viability, other). Acceptable variants: "Other" can be labeled "ethical / partnership / regulatory / timing" or similar. The five area NAMES must each appear in some form.
- For each of the 5, either a substantive hypothesis is opened OR an explicit "no risk identified, monitor" (or equivalent) call-out is written. A risk area that's just absent fails.
- The viability area names Diana's fraud-risk concern (acceptable: "fraud risk", "fraud anomaly", "Diana's audit-trail concern", "finance compliance risk").
- All hypothesis rows in the file have status `active` or `candidate` (or `proposed`). NONE are `promoted` or `partially-validated`.
- Every Evidence row has a provenance tag from the canonical enum (path-typed `[ingestion/...]` / `[source/...]`, or the parenthetical forms).

## Fail criteria (must_not)

- One or more of the 5 risk areas is silently missing (no hypothesis AND no "no risk identified" call-out).
- Any hypothesis is created with status `promoted` or `partially-validated`.
- The viability area exists but does NOT mention fraud, audit, compliance, or Diana's concern.
- One or more Evidence rows lacks a provenance tag.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
