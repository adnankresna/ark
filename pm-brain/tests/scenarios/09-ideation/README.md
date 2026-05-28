# Scenario 09 — Ideation from existing knowledge

You're Sam Liu, PM for **FlowExpense**, a B2B fintech expense-management product (~280 mid-market customers, ARR ~$11M). You've been operating the PM Brain for four months and it's accumulated real evidence: customer interviews, a competitor note, a CS monthly, an insights entry, an open question in the roadmap, and one stalled hypothesis. Today is **2026-05-17**. You're not bringing fresh signal in — you're asking the brain a different kind of question: *given everything in here, what's under-explored?*

This scenario exercises **forward synthesis from existing brain state** — the brain's ability to triangulate evidence it already has into 1-3 candidate hypotheses nobody has framed yet. Every other scenario is REACTIVE (new signal arrives, brain captures/synthesizes/audits). This one is GENERATIVE: the brain proposes candidates grounded entirely in the existing corpus, with explicit validation gates, and without auto-promoting anything.

The right candidate the brain should surface: a **receipt-matching** hypothesis. Three interviews over three months mention friction around receipt matching, the insights entry flags Friday-batch processing behavior, CS monthly ranks receipt-matching as the #3 support ticket category, the competitor note records Brex shipping auto-matching, and the roadmap explicitly asks "what's the under-explored adjacency to expense capture?" The evidence is sitting in the brain — nobody has framed it as a hypothesis.

The seeded `auto-categorization` hypothesis is a deliberate distractor: it was promoted in February, mid-evidence, no recent signals. The brain should NOT propose more evidence for it (that's revisiting, not ideating).

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed populated brain (4 months of mixed evidence + a stalled distractor hypothesis) | Turn 1 (bulk-ingest 8 artifacts dated Jan-April 2026) | Structural |
| Inventory the brain's current state (no file changes) | Turn 2 (PM asks "what do we have right now?") | Structural |
| Forward synthesis: propose under-explored hypotheses from existing artifacts | Turn 3 (PM asks "what's under-explored?") | Content (LLM judge) |
| Stub a proposed hypothesis with explicit validation gates | Turn 4 (PM picks one, asks for a file with `status: proposed`) | Structural + content |

## Lifecycle moves NOT exercised here

- Bulk migration (covered by 02 and 07)
- Drift detection (covered by 03)
- Hypothesis promotion via fresh evidence (covered by 01)
- Decision drafted from confirmed hypothesis (covered by 01 and 03)
- Persona emergence (covered by 04)

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Seed populated brain | Bulk-import 8 artifacts establishing receipt-matching evidence across 3 interviews + insights entry + competitor note + CS monthly + roadmap open-question + the stalled auto-categorization hypothesis as distractor. Dates Jan-Apr 2026. |
| 02 | Inventory | PM asks brain to list current hypotheses, statuses, and recent signals. No file changes — establishes the "before" state and tests that the brain knows what's there. |
| 03 | Ideation prompt | PM asks "what's under-explored? Propose 1-2 candidates the existing evidence supports — cite the artifacts that motivate them." Brain proposes candidates in response text only. No new hypothesis files yet. |
| 04 | Pick and stub | PM picks the receipt-matching candidate. Brain creates ONE new hypothesis file with `status: proposed`, evidence rows citing existing brain artifacts via path-typed provenance tags, and explicit validation gates under `Open questions / caveats:`. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.20 = ~$0.80 single-run; ~$4 for `--runs 5`. Higher than 03 because turn 1 ingests 8 artifacts.
