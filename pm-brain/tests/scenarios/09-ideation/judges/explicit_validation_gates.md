# Judge: explicit_validation_gates (scenario 09 — ideation)

## What we're checking

Turn 4 requires the new hypothesis file to include explicit validation gates — what would need to be true for this candidate to get promoted, and what would kill it. The PM was specific: "Be specific. Name observable thresholds. Not 'promote when there's more evidence.'"

The right behavior is a hypothesis file with a clearly-named promotion gate AND a clearly-named demotion / kill condition, both written as observable thresholds tied to specific evidence types. Per the hypothesis schema, these live under `Open questions / caveats:` and the per-H `Decision trigger:` field — but the judge does not require a specific section name as long as the conditions are unambiguously present in the file body.

Examples of **specific** gates:
- "Promote when 2+ additional customer interviews from the field-services segment validate that fuzzy vendor-name matching with confirm-step UX would cut their close-week time by ≥30%."
- "Promote when a 2-week spike against the existing matching engine shows fuzzy matching at >85% precision on a sample of 500 receipt-card pairs."
- "Kill if fuzzy matching benchmarks below 70% precision OR if customer interviews surface a preference for manual control over speed."

Examples of **vague** gates that should FAIL:
- "Promote when there's more evidence."
- "Validate with users."
- "Confirm with more interviews."
- "TBD — needs more research."

## You will be given

- The target file: the new receipt-matching hypothesis file under `hypotheses/*.md` (excluding `INDEX.md`, `_SCHEMA.md`, and `auto-categorization.md`).

## Pass criteria

ALL of the following must be true:

- The file contains an explicit promotion condition (or "what would promote this") that names at least one observable, measurable threshold — a specific count of interviews, a specific metric value, a specific customer-segment validation, or a specific test result.
- The file contains an explicit kill / demote condition (or "what would kill this") with comparable specificity.
- The gates are written as forward-looking statements about future evidence, not as vague aspirations ("we'd want to validate", "more research needed").

## Fail criteria (must_not)

- The file's validation gates are vague placeholders like "more evidence needed", "TBD", "validate with users", or absent entirely.
- The file lists only a promotion gate without a kill condition, or only a kill condition without a promotion gate.
- The gates reference unmeasurable / unfalsifiable conditions ("when it feels right", "when stakeholders are convinced").

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
