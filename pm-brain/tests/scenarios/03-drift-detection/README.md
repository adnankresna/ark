# Scenario 03 — Drift detection

You're Rita Park, PM for **OrthoSched**, a healthcare scheduling SaaS used by mid-size dental practices. Four months ago you promoted a high-priority feature called *Provider Availability Sync* based on strong customer signal at the time. Today you're running your normal weekly loop — and a new interview plus this week's analytics suggest the original signal has aged badly.

This scenario exercises **drift detection**: the brain's ability to recognize that a previously-promoted hypothesis no longer matches the world, even when the original evidence is still technically present in the repo. Old evidence isn't wrong — but the world moved and the hypothesis didn't.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed prior state (old promoted hypothesis + supporting source) | Turn 1 (bulk-ingest 3 artifacts dated 4 months ago) | Structural |
| Fresh contradicting signal | Turn 2 (today's interview reverses original customer's stance) | Structural + content |
| `/review` surfaces drift on aged claims | Turn 3 (weekly maintenance sweep) | Content (LLM judge) |
| Demotion drafted with full audit trail | Turn 4 (PM asks: should we kill it?) | Structural + content |

## Lifecycle moves NOT exercised here

- Bulk migration (covered by 02)
- Hypothesis promotion (covered by 01)
- Decision-from-scratch (covered by 01 turn 10)

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Seed old state | Three artifacts dated 2026-01: champion interview, eng-feasibility note, decision-to-build. Hypothesis promoted at the time. |
| 02 | Contradicting interview | Today: same customer who championed the feature now wants it removed because of double-booking edge cases. |
| 03 | `/review` | PM runs weekly review. Drift should be the headline. |
| 04 | Demotion decision | PM asks brain to draft a demotion decision with reversal condition. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.20 = ~$0.80 single-run; ~$4 for `--runs 5`.
