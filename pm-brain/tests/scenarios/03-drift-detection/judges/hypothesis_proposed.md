# Judge: hypothesis_proposed (scenario 03 — seed historical state)

## What we're checking

Turn 1 of scenario 03 ingests three January 2026 artifacts (Brightsmile interview, Marcus eng feasibility note, January decision record) that established the **Provider Availability Sync** hypothesis. The PM explicitly asks the brain to recreate the January state faithfully — including dates, so the brain knows how old the evidence is.

The right behavior is to create the hypothesis file with status `promoted` (because it WAS promoted in January based on this evidence), preserve the January 2026 dates on the source/ingestion artifacts, and tag the evidence rows with provenance from the canonical enum.

## You will be given

- The target file(s): all markdown files under `hypotheses/` (excluding `INDEX.md` and `_SCHEMA.md`).
- The turn context: turn 1. Three January artifacts ingested. Today is 2026-05-17.

## Pass criteria

ALL of the following must be true:

- A hypothesis file exists for provider-availability-sync (or equivalent slug).
- The hypothesis status reflects the **January 2026** promotion — `promoted` or equivalent — NOT `proposed` / `active`. This is a historical re-creation, not a fresh hypothesis.
- The evidence rows under the hypothesis carry provenance tags from the canonical enum (e.g., `[source/interviews/2026-01-08-brightsmile.md](...)` or `[ingestion/...]`).
- The January 2026 dates are preserved on the source artifacts (`source/interviews/2026-01-08-*.md` or similar), NOT relabeled to 2026-05-17.

## Fail criteria (must_not)

- The hypothesis is created with status `proposed` / `active` (ignoring that it WAS promoted in January based on this evidence).
- January 2026 dates are silently relabeled to May 17 2026 (loses the "this evidence is 4 months old" signal that the next turn depends on).
- Evidence rows have no provenance tags.
- The decision record from 2026-01-22 is not represented in `decisions/`.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
