# Scenario 05 — Stakeholder cadence flags

You're Sasha Rao, PM for **Lumenscope**, a B2B analytics platform serving mid-market SaaS companies (~280 paying accounts, ARR ~$11M). One of Lumenscope's older features, *Custom Dashboards*, is on the chopping block — adoption is flat and engineering wants to retire it to free up the visualization stack for a rebuild. You're going to draft a deprecation decision this week. Today is **2026-05-17**.

This scenario exercises **stakeholder cadence flags**: the brain's ability to notice that a stakeholder relevant to a current load-bearing decision has gone too long without contact — and to surface that gap as a *targeted* risk, not as generic relationship-debt nagging.

The trick the brain has to pull off: there are five stakeholders, three of them are overdue for contact, but only two of the overdue ones are implicated in the Custom Dashboards decision. The brain must flag the relevant overdue stakeholders and stay silent about the irrelevant overdue one in this turn's context. Relevance, not staleness alone, is the filter.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed prior state (5 stakeholder files + 1 active hypothesis + 1 ingestion record) | Turn 1 (bulk-ingest) | Structural |
| Decision-context recall (Q&A turn, no writes) | Turn 2 | Structural (no-op) + content trail |
| `/review` surfaces overdue stakeholders WITH decision context | Turn 3 | Content (LLM judge) — both relevant-flagged and irrelevant-NOT-flagged |
| Decision drafted with pre-launch stakeholder check | Turn 4 | Structural + content |

## Lifecycle moves NOT exercised here

- Hypothesis promotion / demotion via contradicting evidence (covered by 01 and 03)
- Bulk migration (covered by 02)
- Drift detection on aged hypotheses (covered by 03)

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Seed stakeholders + state | Recreate 5 stakeholder files with real `Last touched` dates (3 recent, 2 stale), plus the `custom-dashboards-usage-decline` hypothesis and one ingestion record summarizing the case for deprecation. |
| 02 | Decision context | Sasha asks: "I'm planning to draft a deprecation decision for Custom Dashboards this week. Walk me through what we know." Brain recalls the evidence trail; no writes required. |
| 03 | `/review` | Sasha asks for a weekly sweep with explicit framing: *"anything I should be aware of as I draft the Custom Dashboards decision?"* The right answer surfaces Diana (CS VP, last 1:1 2026-03-22) and Marcus (Sales, last 1:1 2026-04-12) as needing contact before the decision lands. CFO (also overdue, but not implicated) should NOT be flagged in this context. |
| 04 | Decision draft | Sasha asks the brain to draft the deprecation decision. The decision file gets created (status `proposed`), AND the response / decision file names Diana and Marcus as "should-talk-to-before-this-lands" with their last 1:1 dates. CFO again does NOT appear in the pre-launch check. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.50 = ~$2 single-run; ~$10 for `--runs 5`. Higher-than-baseline per-turn cost because turn 1 seeds 5 stakeholder files + 1 hypothesis + 1 ingestion record in a single shot.
