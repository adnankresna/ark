# /prep

Surface what to ask, raise, or watch for in an upcoming conversation.

## Input

Stakeholder slug (`/prep acme-ops`), meeting name (`/prep weekly-exec-review`), or meeting type (`/prep 1:1`). If multi-attendee, pass the slug list or the meeting name.

## Loads

- `stakeholders/<slug>.md` for each attendee
- `decisions/` filtered to ones affecting them or the topic
- Active `hypotheses/<slug>.md` they care about or own
- Last 3 `ingestion/meetings/<slug>-*.md` with this person or this meeting type
- `knowledge/strategy.md § Tensions` if any tension intersects their concerns

## Updates

Nothing at call time. `/prep` is read-only. After the meeting, run `/ingest` on the notes.

## Surfaces

- Their open asks and last unresolved concern (with date)
- Decisions made since last touch that affect them
- Active hypotheses where their judgment matters
- One sentence on what changed in their world since last 1:1
- 3-5 suggested questions or talking points
- One flag if `Last touched` is older than 3 weeks for a high-influence stakeholder
