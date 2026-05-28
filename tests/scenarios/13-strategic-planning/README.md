# Scenario 13 — Strategic-planning verbs (literal `/strategy-check`, `/risk`, `/plan`, `/ideate`)

You're Riley Chen, PM for **TerraDash**, a B2B climate-analytics product (~140 enterprise customers). Today is **2026-05-17**. You're stress-testing four planning verbs across a single sitting against a brain that has 2 months of seeded context.

This scenario exercises **the four planning-level slash commands** end to end:

1. `/strategy-check` — drift check between recent decisions / hypotheses / ingestion and `knowledge/strategy.md`. Read-only by default.
2. `/risk <feature-slug>` — 5-area risk scan; drafts stub hypotheses for gaps.
3. `/plan <objective>` — turns an objective into discovery questions, hypotheses, experiments, decision points.
4. `/ideate <problem>` — generates evidence-grounded solution directions; drafts only.

It tests that:

- Each slash command is **recognized literally** as a verb.
- `/strategy-check` cites specific strategy clauses for any drift call (no vague "decision X drifts from strategy") and does NOT silently rewrite `strategy.md`.
- `/risk` walks all 5 risk areas and drafts stubs for gaps under default autonomy.
- `/plan` produces the six expected blocks (what we know, assumption-vs-evidence, who to interview, hypotheses to open, experiments, decision points).
- `/ideate` proposes evidence-grounded directions with brain citations and does NOT auto-promote.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed: strategy.md with priorities + non-goals, 1 prior decision, 2 active hypotheses, recent ingestion | Turn 1 | Structural |
| `/strategy-check` literal dispatch, read-only drift report | Turn 2 | Structural (no silent strategy.md edits) + content judge on cite-the-clause |
| `/risk` literal dispatch on a feature with mixed coverage | Turn 3 | Structural (stub hypotheses drafted for gap areas) + content judge on all-5-areas-walked |
| `/plan` literal dispatch on a new objective | Turn 4 | Structural (planning artifact drafted under ingestion/adhoc) + content judge on the 6-block shape |
| `/ideate` literal dispatch on a problem | Turn 5 | Structural (no auto-promotion) + content judge on brain-grounded directions |

Five turns total — slightly heavier than the other two commands-coverage scenarios because four verbs need exercise.

## Lifecycle moves NOT exercised here

- The 4 `/ingest` kinds (11-ingest-shapes)
- `/prep`, `/hypothesize`, `/decide` decision-lifecycle trio (12-decision-lifecycle)
- Deep evidence-promotion or drift-detection judgment (10-promotion-gate, 03-drift-detection)

## Turn map

| Turn | Command | Summary |
|---|---|---|
| 01 | Seed | Populate strategy.md with 3 priorities + 2 non-goals, drop 1 prior decision file, 2 active hypotheses (one in-priority, one off-priority), recent ingestion that tensions one of the non-goals. |
| 02 | `/strategy-check` | PM asks for a drift sweep. Read-only. Expects: every drift call names a specific strategy clause; no silent edit to strategy.md; any proposed new tension is drafted, not committed. |
| 03 | `/risk weekly-snapshot` | PM asks for the 5-area risk scan on a feature that has hypothesis coverage on Value but gaps on Feasibility, Viability, Other. Expects: stub hypotheses drafted for the gap areas under default autonomy. |
| 04 | `/plan reduce-weekly-dashboard-load-time` | PM asks for a plan around a new objective. Expects: the 6-block plan in the response + drafts under ingestion/adhoc + hypothesis stubs for the risk areas. |
| 05 | `/ideate watershed-level-research-segment-friction` | PM asks for evidence-grounded solution directions. Expects: directions cite specific brain artifacts; no auto-promotion. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~5 turns × ~$0.30 = ~$1.50 single-run; ~$7.50 for `--runs 5`.
