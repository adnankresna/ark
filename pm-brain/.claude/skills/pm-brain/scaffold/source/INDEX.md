# Source — verbatim originals

This is the **audit anchor** for everything that enters the brain. Every ingested artifact gets a verbatim copy here *before* any synthesis happens elsewhere.

## Why this exists

`ingestion/` holds **synthesized** records — extracted observations, tagged claims, links to affected hypotheses. Synthesis is lossy and opinionated. When a future PM or agent re-reads a hypothesis a year from now and wants to know *what was actually said*, the synthesized record is not enough.

`source/` answers that question. Nothing in here is edited after creation. It is the chain-of-custody for the brain's claims.

## Layout

```
source/
├── interviews/   # transcripts, raw notes from customer / user interviews
├── meetings/     # raw notes from 1:1s, syncs, reviews
├── market/       # full-text snapshots of articles, tweets, changelogs (URL + retrieved-at)
└── adhoc/        # anything else captured verbatim before routing
```

## Naming

`source/<kind>/YYYY-MM-DD-<slug>.md` — same date + slug as the matching `ingestion/<kind>/` file, so they line up alphabetically.

## Rules

- **Verbatim only.** No edits, no cleanup, no commentary. Wrap the original content in a fenced block if it's anything other than plain prose.
- **Header is metadata-only.** Source URL, retrieved-at timestamp, participant(s) if applicable, the matching `ingestion/` file path. That's it.
- **One file per artifact.** Do not concatenate sources.
- **Never delete from `source/`.** Even after a hypothesis is killed and its ingestion record is archived, the source stays.

Every `ingestion/<kind>/<file>.md` should link back to its `source/<kind>/<file>.md`. If a synthesized claim cannot be traced to a source file, that claim has no provenance and should be flagged.
