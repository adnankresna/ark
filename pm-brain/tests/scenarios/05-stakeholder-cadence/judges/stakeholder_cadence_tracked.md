# Judge: stakeholder_cadence_tracked (scenario 05 — cadence data preserved)

## What we're checking

Scenario 05 depends on stakeholder cadence dates being durable, inspectable state. The seed turn gives the brain five specific `Last touched` (last 1:1) dates — three recent, two stale. Every downstream behavior the scenario tests (the /review surfacing in turn 3, the pre-launch check in turn 4) requires that these dates are still in the brain, in a parseable form, when the brain is asked to reason about them.

The right behavior is that every stakeholder file has a parseable `Last touched` date (or equivalent last-1:1 field) carrying the value the PM seeded, and that the brain has NOT silently relabeled any of them to "today" / 2026-05-17 just because the file was created today. The seeded date IS the truth.

The five expected dates:

| Stakeholder | Last 1:1 |
|---|---|
| Priya Shah (Eng Director) | 2026-05-08 |
| Jordan Liu (Design Lead) | 2026-05-12 |
| Diana Okonkwo (CS VP) | 2026-03-22 |
| Marcus Avila (Sales Director) | 2026-04-12 |
| Helena Vargas (CFO) | 2026-03-08 |

## You will be given

- The target file(s): all markdown files under `stakeholders/` (excluding `INDEX.md` and `_SCHEMA.md`).
- The turn context (turn 1 for the initial-seed run, or final state).

## Pass criteria

ALL of the following must be true:

- Five distinct stakeholder files exist, one for each of the people named above.
- Each file has a `Last touched` field (or a clearly equivalent named field — `Last 1:1`, `last_1on1`, etc.) carrying a parseable `YYYY-MM-DD` date.
- The five dates match the seed exactly: Priya 2026-05-08, Jordan 2026-05-12, Diana 2026-03-22, Marcus 2026-04-12, Helena 2026-03-08. (Additional touchpoint-log entries dated later in the scenario are allowed — the `Last touched` field itself should reflect the most recent meaningful touchpoint, but if the scenario only adds context-recall conversations, the seeded date should still stand.)
- The dates are NOT silently relabeled to 2026-05-17 / "today" / a vague placeholder.

## Fail criteria (must_not)

- Any of the five stakeholder files is missing.
- Any of the five `Last touched` values has been overwritten with today's date or a fabricated more-recent date, without a real touchpoint event in the scenario backing it.
- The `Last touched` field has been removed or replaced with `TODO` (the schema reserves TODO for PM-fillable fields; `Last touched` is auto-maintained).
- The brain renamed the canonical `Last touched` field in a way that loses its parseability (e.g., replacing the date with prose like "a while ago").

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
