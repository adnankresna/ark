# /ingest

Route a new artifact into the brain. Four shapes, one verb.

## Input

A pasted transcript, a file path, a screenshot, a URL, or a free-form note. The agent infers the shape:

- **interview** — customer call, user research session, sales call with prospect signal
- **meeting** — 1:1, exec review, roadmap discussion, kickoff, retro
- **market** — competitor article, screenshot, tweet, changelog, analyst note
- **adhoc** — anything else worth capturing that doesn't fit the other three

If shape is ambiguous, ask one question. Don't guess.

## Loads

- `knowledge/strategy.md`
- The matching area for the inferred shape: `knowledge/users/insights.md` (interview), `stakeholders/<slug>.md` (meeting), `knowledge/market/` (market), nothing extra (adhoc)
- Active `hypotheses/<slug>.md` files that the artifact might touch
- Last 3 entries in `ingestion/<shape>/` for pattern comparison

## Updates

- `source/<shape>/<date>-<slug>.md` — immutable copy of the original artifact
- `ingestion/<shape>/<date>-<slug>.md` — observations tagged (observation / interpretation / hypothesis / assumption / decision)
- One or more durable destinations per the cognition pipeline: `knowledge/`, `hypotheses/`, `decisions/`, `stakeholders/`
- Maintenance log if structural (a new persona, a new competitor, a new stakeholder)

Promotion to durable layers follows the memory promotion bar in `CLAUDE.md § Memory promotion`. One-off observations stay in `ingestion/` until they accumulate.

## Surfaces

- Where the artifact landed (source, ingestion, and which durable destinations)
- 1-3 themes promoted, or "no promotion this round"
- Any contradictions with prior evidence (preserved, not resolved)
- One open question if the operator's judgment is needed
