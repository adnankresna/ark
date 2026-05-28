# Scenario 10 — Promotion gate evaluation

You're Casey Ito, PM for **BrightSched**, a healthtech booking SaaS used by multi-provider outpatient clinics. Six weeks ago you opened a `proposed` hypothesis called *same-day-rebooking-flow* — when a patient cancels intraday, the front desk should be able to refill the slot from the cancellation queue in under 30 seconds. Evidence has accumulated unevenly. You've got strong direct customer signal on the value side, an unanswered feasibility concern from your eng lead, and zero business-case modeling. Today you want the brain to tell you, honestly, whether this thing is promotable yet.

This scenario isolates the **evaluative move**: given a `proposed` hypothesis with mixed-quality evidence, the brain must EVALUATE (count and weigh by provenance tier), CHECK COVERAGE (across the 5 schema risk areas), and RESIST premature promotion when the bar isn't met. "Not yet, here's what's missing" is a desired answer.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed `proposed` hypothesis with mixed-quality evidence across provenance tiers | Turn 1 (bulk-ingest 7 evidence rows) | Structural |
| Evaluate promotion-readiness, weighing evidence by provenance and risk-area coverage | Turn 2 (PM asks: should we promote?) | Content (LLM judge) |
| Resist premature promotion — return "not yet" with specific named gaps | Turn 2 | Content (LLM judge) — no file mutation |
| PM fills the gap, brain ingests new artifacts and updates hypothesis | Turn 3 (feasibility memo + business case) | Structural |
| Re-evaluate; promote via decision artifact (not silent status mutation) | Turn 4 (PM asks again) | Structural + content |

## Lifecycle moves NOT exercised here

- Bulk migration (covered by 02, 07)
- Drift detection on aged claims (covered by 03)
- Demotion via contradicting evidence (covered by 01, 03)
- Decision-from-scratch with no prior hypothesis (covered by 01 turn 10)

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Seed mixed-evidence hypothesis | `same-day-rebooking-flow` opened 6 weeks ago. Value risk well-covered (2 ingestion, 1 stakeholder-verbal, 1 intuition, 1 industry-knowledge — all supporting). Feasibility risk has one stakeholder-verbal concern, uninvestigated. Viability risk has zero evidence. |
| 02 | Promotion question | PM asks: promote `proposed` → `promoted`? Walk through evidence by provenance tier and risk-area coverage. Right answer: NOT YET. Name the specific gaps. No file mutation. |
| 03 | PM fills the gap | PM attaches eng feasibility memo (refactor scoped at 3 sprints) and business case (modeling +2.1pp retention). Brain ingests both, updates the hypothesis. |
| 04 | Second promotion pass | PM asks again. Right answer: PROMOTE via a `decisions/2026-05*.md` artifact (status `proposed` on the decision, PM still signs off), with reversal condition. No silent status flip on the hypothesis without the decision artifact existing first. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.50 = ~$2 single-run; ~$10 for `--runs 5`.
