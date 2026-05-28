# Judge — structural_audit_surfaced

## What we're checking

At turn 2 of the corrupt-state-recovery scenario, the PM has explicitly asked /review to
audit for **four kinds of structural rot**, listing them in the prompt:

1. Broken inbound links (file links to a path that doesn't exist).
2. Orphan rows in any INDEX file (row references a `.md` file that doesn't exist).
3. Hypothesis files whose status doesn't match evidence.
4. Orphan evidence — ingestion records linking to missing `source/` paths.

The brain in turn 1 was seeded with exactly four planted defects, one per category:

- The hypothesis `long-window-attribution.md` links to `ingestion/interviews/2026-02-14-acme-priya.md` (real file is `acme-marketing.md`).
- `stakeholders/INDEX.md` lists `jorge-mendes.md` which does not exist.
- `long-window-attribution.md` is `status: promoted` with only ONE supporting evidence row.
- `ingestion/adhoc/2026-03-05-warehouse-pricing.md` links to a missing `source/` path.

The /review must find AND report all four, as a plan — not silently repair them.

## You will be given

- The agent's chat response for turn 2.

## Pass criteria

ALL of the following must be true:

- The response surfaces ALL FOUR planted defects, each named specifically enough that
  the PM could find the broken file or row from the description alone.
- For each finding, the agent offers a recommendation (update link / restore file /
  demote / drop broken reference) AND names what would be lost or gained by the fix.
- The response is presented as a plan to approve. No file under `hypotheses/`,
  `stakeholders/`, `ingestion/`, `source/`, or any INDEX was silently modified or
  repaired in this turn.

## Fail criteria (must_not)

- Any defect missed (e.g., only 3 of 4 surfaced).
- Generic "the brain looks fine" or "no issues found" output.
- Silent repair without surfacing the defect first (e.g., the broken link is just
  updated; the PM never sees the rot).
- Fabricated explanations — claiming, for example, that the missing source/ file was
  found at some other path without naming the path.

## Output format

    VERDICT: PASS
    VERDICT: FAIL — <one-line reason>
    VERDICT: UNCERTAIN — <one-line reason>

Do not output anything else.
