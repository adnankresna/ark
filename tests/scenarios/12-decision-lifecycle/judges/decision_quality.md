# Judge: decision_quality (scenario 12 — decision-lifecycle, turn 4)

## What we're checking

Turn 4 invokes `/decide ship-auto-approve-under-50 --resolves <hypothesis-slug>`. The `/decide` spec has hard constraints:

1. **COUNT-THE-TAGS** — every Evidence row + every "Explicitly NOT doing" row must carry a provenance tag from the enum.
2. **Reversal condition is mandatory AND observable.** Vague conditions ("if things change", "if market shifts") fail. The condition must name a measurable signal — a metric crossing a threshold, a stakeholder withdrawing support, a competitor shipping a feature.
3. Decision file uses the full schema: status, context, decision, evidence rows, "Explicitly NOT doing", stakeholders signed off, reversal condition, remaining ambiguities.
4. The resolved hypothesis flips status (`promoted` if the decision validates it) AND adds a Resolution row linking back to the decision file.

The PM was explicit on turn 4: status is `decided` (Diana signed off this morning, this isn't pending). The reversal-condition examples the PM offered are specific and observable (2% fraud-anomaly threshold, Diana withdrawing sign-off, 15% customer disable-rate within 60 days). The "Explicitly NOT doing" section should have at least 2 items.

## You will be given

- The decision file (target_glob: `decisions/2026-05-17*auto-approve*.md OR decisions/2026-05-17*ship*.md`).
- The resolved hypothesis file (it should now show status `promoted` and a Resolution row linking to this decision).

## Pass criteria

ALL of the following must be true:

- Decision file has `status: decided` (NOT `pending`, NOT blank).
- Every Evidence row in the decision file carries a provenance tag from the canonical enum (path-typed `[ingestion/...]` / `[source/...]`, or the parenthetical forms).
- An explicit, observable reversal condition is present — names at least one measurable signal (a specific metric threshold, a named stakeholder withdrawing, a specific customer behavior). Vague phrases like "if things change", "if market shifts", "if we get pushback" alone do NOT pass.
- An "Explicitly NOT doing" section exists with at least 2 enumerated items.
- Diana Okonkwo AND Jordan Liu are both named as signed-off stakeholders.
- A working link (path or markdown reference) from the decision file back to the resolved hypothesis file exists.
- The resolved hypothesis status field is now `promoted` (was `active` before this turn), AND the hypothesis file references this decision (a Resolution row or a `Decision:` field linking to the decision file).

## Fail criteria (must_not)

- Reversal condition is vague (no observable threshold, no named stakeholder withdrawal signal, no specific behavior).
- Any Evidence row in the decision file lacks a provenance tag.
- The "Explicitly NOT doing" section is missing or has fewer than 2 items.
- The hypothesis status was silently flipped to `promoted` without the decision file linking back to the hypothesis (silent hypothesis promotion).
- Decision status was left as `pending` (the PM explicitly said this is decided).
- Either Diana or Jordan is missing from the signed-off stakeholders.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
