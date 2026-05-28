# Stakeholder File Schema

Filename: `<slug>.md`. One file per stakeholder. Slug is lowercase, hyphenated (e.g., `jane-cooper.md`).

```markdown
# <Name> — <Role>

## Snapshot
- Role:
- Reports to / works with:
- Influence on my work: low | medium | high
- Friction level: low | medium | high

## What they care about
<!-- Their goals, what they're measured on, what makes them look good -->

## Concerns / watch-outs
<!-- What worries them, what triggers them, what they push back on -->

## Communication style
<!-- Async vs sync, terse vs detailed, data-first vs narrative-first -->

## Open asks
<!-- Things I owe them, things they owe me -->

## Touchpoint log
<!-- Paths are relative to THIS file's location (stakeholders/<slug>.md). -->
- YYYY-MM-DD — <one-line summary, link to `../ingestion/meetings/<file>` if applicable>

## Last touched
YYYY-MM-DD <!-- maintained automatically. Leave blank if no touchpoint has been captured yet. Do NOT write "TODO" — TODO is reserved for fields the PM is expected to fill in. -->
```

## TODO discipline

Schema fields fall into two categories:

- **PM-fillable.** Fields the PM is expected to populate (communication style, concerns, open asks). When unknown, write `TODO` plus a one-line note about what's needed.
- **Auto-maintained.** Fields the system updates as work flows through (`Last touched`, touchpoint log). When no data exists yet, leave the field blank or write `—`. Do not write `TODO` for these.

Maintenance treats `TODO` as a knowledge-gap signal. Filling auto-maintained fields with `TODO` corrupts that signal.
