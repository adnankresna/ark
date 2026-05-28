# Scenario 11 — Ingest shapes (all 4 kinds, literal slash commands)

You're Riley Chen, PM for **TerraDash**, a B2B climate-analytics product (~140 enterprise customers). Today is **2026-05-17**. You're putting raw artifacts through the brain across all four ingestion kinds in a single sitting: an interview transcript, a meeting note, a competitor market signal, and an ad-hoc Slack-thread dump.

This scenario exercises **the `/ingest` command across all four registered kinds**: `interview`, `meeting`, `market`, and `adhoc`. It tests that:

1. The slash command is **recognized literally** (not requiring a long English prompt to dispatch correctly).
2. Each kind produces **both a `source/<kind>/` audit anchor and a `ingestion/<kind>/` synthesis record**.
3. Each ingestion routes evidence to the right durable areas (insights, market landscape, stakeholder file, etc.) per the kind's conventions.
4. Provenance tags survive the audit.

This is a **commands-coverage scenario** — its job is to prove the registered `/ingest` shapes work, not to test deep judgment. The judgment scenarios (01, 02, 04, 09, 10) cover synthesis quality.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| `/ingest interview` literal dispatch | Turn 1 | Structural (source + ingestion files exist; insights touched) |
| `/ingest meeting` literal dispatch | Turn 2 | Structural (source + ingestion files exist; stakeholder file touched or created) |
| `/ingest market` literal dispatch | Turn 3 | Structural (source + ingestion files exist; market landscape or competitor file touched) |
| `/ingest adhoc` literal dispatch | Turn 4 | Structural (source + ingestion files exist; routing summary returned) |

## Lifecycle moves NOT exercised here

- Decision drafting (12-decision-lifecycle)
- Hypothesis generation via `/hypothesize` (12-decision-lifecycle)
- Strategy drift / `/strategy-check` (13-strategic-planning)
- Deep synthesis-quality judging (covered by 01, 02, 04, 09, 10)

## Turn map

| Turn | Command | Summary |
|---|---|---|
| 01 | `/ingest interview` | A customer interview transcript with Dr. Mira Patel from a research-university customer; surfaces a recurring "missing per-watershed view" pain. |
| 02 | `/ingest meeting` | 1:1 notes with the head of Customer Success (Carlos Rivera) on rising support volume for two specific dashboards. |
| 03 | `/ingest market` | A competitor product announcement — Aurelia Climate ships a watershed-level dashboard. |
| 04 | `/ingest adhoc` | Free-form Slack-thread dump where an engineer flags a data-pipeline reliability concern. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** none (commands-coverage scenario; quality covered elsewhere)

## Cost

~4 turns × ~$0.25 = ~$1.00 single-run; ~$5 for `--runs 5`.
