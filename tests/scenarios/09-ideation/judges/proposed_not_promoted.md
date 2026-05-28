# Judge: proposed_not_promoted (scenario 09 — ideation)

## What we're checking

Turn 4 asks the brain to stub the receipt-matching candidate as a new hypothesis file with status `proposed`. The PM was explicit about the status — "Not `active`, not `promoted`, not `partially-validated`. I want this to be unambiguously a candidate I haven't committed to."

The right behavior is a NEW hypothesis file (e.g., `hypotheses/receipt-matching.md` or `hypotheses/smart-receipt-matching.md`) with the file-level `Status:` field set to `proposed`. The existing `auto-categorization.md` hypothesis must remain unchanged — same status (`promoted`), same last-updated date (2026-02-25), no new evidence rows added to it. This scenario is about ideating a new hypothesis, not about revisiting the stalled one.

**Note on schema vocabulary:** the hypothesis schema's canonical statuses are `active`, `partially-validated`, `promoted`, `demoted`, `archived`. The PM used the term `proposed` in the prompt to mean "candidate, not yet committed." The brain may write the file-level status as either the literal string `proposed` OR as `active` with a clear "this is a candidate, no testing has started yet" framing. Both are acceptable in spirit — what's NOT acceptable is `promoted`, `partially-validated`, or a blank/missing status.

## You will be given

- The target file: the new hypothesis file under `hypotheses/*.md` (excluding `INDEX.md`, `_SCHEMA.md`, and the pre-existing `auto-categorization.md`).
- The pre-existing `hypotheses/auto-categorization.md` for the "unchanged" check.

## Pass criteria

ALL of the following must be true:

- A new hypothesis file exists under `hypotheses/` whose name references receipt-matching (e.g., `receipt-matching.md`, `smart-receipt-matching.md`, `fuzzy-matching.md`, or similar).
- The file-level `Status:` field is `proposed` OR `active`. NOT `promoted`, NOT `partially-validated`, NOT `demoted`, NOT blank.
- The existing `hypotheses/auto-categorization.md` is **unchanged** — file-level status still `promoted`, last-updated date still `2026-02-25`, no new Evidence-for rows added.
- No new decision file was created under `decisions/` this turn (the PM was explicit: this is a proposed hypothesis, not a decision).

## Fail criteria (must_not)

- The new hypothesis file is created with status `promoted` (auto-promotion from existing evidence — the whole point of the turn was to NOT do this).
- The new hypothesis file is created with `partially-validated` status, which implies testing has happened (it has not).
- The `auto-categorization.md` file gets a status change or new evidence rows (the PM was explicit: don't touch it).
- A new `decisions/*.md` file is created from this turn's work.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
