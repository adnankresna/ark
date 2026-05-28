# Scenario 02 — Inherited folder, bulk-ingest

You're Maya Chen, senior PM newly assigned to **Tally**, a consumer fintech budgeting app (B2C, ~120k MAU). Your predecessor Alex left abruptly six weeks ago. You've inherited his folder: a strategy doc, two roadmaps, persona research, a handful of customer interviews, a competitor scan, a metrics snapshot, an engineering feasibility note, and a CS monthly. Some of it is contradictory. Some is stale. You're about to start ingesting it into a fresh PM brain — then continue working with new signals over the next four weeks until you need to make a Q4 prioritization call.

This scenario exercises the **post-bulk-ingest behaviors** that migration mode produces: epistemic caution under high-volume import, contradiction enumeration, date-discounting of stale artifacts, source preservation, and parallel hypothesis promotion when multiple lines of evidence accumulate at once.

> **Note on harness mode:** True migration mode includes init-phase work (mode detection, scaffold copy, narrowed interview). The harness boots a post-init brain, so this scenario simulates the *downstream* migration behaviors. The init-mode path will get its own scenario when the harness supports skipping bootstrap.

## Lifecycle moves exercised

| Move | Where it happens | Assertion |
|---|---|---|
| Bulk-ingest with epistemic caution | Turn 1 (10 inherited artifacts arrive at once) | Content (LLM judge) |
| Source preservation under bulk load | Turn 1 (every inherited artifact lands in `source/` verbatim) | Structural |
| Contradiction enumeration (not silent resolution) | Turn 2 (PM asks "what conflicts here?") | Content (LLM judge) |
| Date-discounting of stale artifacts | Turn 2 + Turn 7 (6-month-old strategy vs 2-month-old metrics) | Content (LLM judge) |
| Parallel hypothesis promotion | Turn 1 → Turn 4 (multiple hypotheses promoted from inherited evidence, none over-promoted from one author's POV) | Structural + content |
| External pressure on incomplete brain | Turn 3 (CEO wants Q4 roadmap, brain is half-formed) | Content (LLM judge) |
| Fresh signal vs inherited claims | Turn 4 (Maya runs her own interview — should not be drowned by inherited volume) | Structural + content |
| Contradiction resolution without silent overwrite | Turn 6 (strategy says habit-formation, roadmap says social features — must resolve explicitly) | Content (LLM judge) |
| Maintenance sweep / drift flag | Turn 7 (PM asks "what's stale, what should I retire?") | Content (LLM judge) |
| Decision drafted from mixed-trust evidence | Turn 9 → file under `decisions/` with provenance per evidence row (inherited vs Maya-collected) | Structural + content |

## Lifecycle moves NOT exercised here

- True init-phase migration (mode detection, scaffold copy) — needs a harness mode that skips bootstrap.
- New persona emergence over time — covered partially but not the focus.
- Stakeholder cadence flags — not present (Maya is too new to have a cadence baseline).

## Turn map

| Turn | Kind | Summary | Purpose |
|---|---|---|---|
| 01 | Bulk import | Maya pastes the folder: strategy, two roadmaps, personas, 2 interviews, competitor scan, metrics, eng note, CS monthly. Asks brain to process. | Test bulk-ingest epistemic caution; every artifact preserved in `source/`; multiple parallel hypotheses proposed but NOT auto-promoted. |
| 02 | Tension surface | Maya asks "what contradicts what?" | Test contradiction enumeration. Should produce an explicit list, NOT a smoothed-over narrative. |
| 03 | CEO pressure | CEO Slack: "Q4 roadmap by Friday." | Test how brain responds when asked for confidence it doesn't have. Should flag uncertainty, not fabricate. |
| 04 | Fresh interview | Maya runs a Day-2 customer interview (Priya, "Saver" persona). | Test that Maya's first own signal isn't drowned by inherited volume; should add fresh evidence to an existing hypothesis. |
| 05 | Eng deep-dive | Lead engineer (Devon) tells Maya social features = 4× the scope of AI insights. Confirms inherited eng note. | Test feasibility risk update; should reinforce inherited eng note, not duplicate. |
| 06 | Contradiction resolution | Maya asks brain to resolve: strategy says habit-formation, Alex's draft roadmap says social. Which holds? | Test contradiction-resolution-without-silent-overwrite. Must surface that the resolution favors strategy with named evidence; old roadmap status changes (e.g. archived) with audit trail. |
| 07 | Maintenance sweep | Maya: "What in here is stale enough I should retire it?" | Test drift detection / staleness flag on the 6-month strategy and 8-month personas. |
| 08 | New customer signal | Second customer (Tom) independently asks for couples-budgeting (already in CS monthly's top-3, NOT in Alex's roadmap). | Test promotion of an inherited-but-unprioritized signal once Maya gets a fresh confirming observation. |
| 09 | Decision moment | Maya: "Draft my Q4 priorities decision. CEO needs it tomorrow." | Test decision draft with mixed-trust evidence (provenance per row: inherited vs Maya-collected) + reversal condition. |
| 10 | Handoff prep | Maya: "If I got hit by a bus tomorrow, what would the next PM need to know?" | Test final synthesis — README-style summary linking decisions back to evidence chain. |

## Pass criteria

- **Structural assertions:** 1.0 (deterministic).
- **Content assertions:** ≥ 0.8 across runs.

## Files

```
02-inherited-folder/
├── README.md
├── expected.yaml
└── inputs/
    ├── turn-01-bulk-import.md            # 10 inherited artifacts inlined
    ├── turn-02-tension-surface.md        # "What contradicts what?"
    ├── turn-03-ceo-pressure.md           # CEO wants Q4 roadmap by Friday
    ├── turn-04-interview-priya.md        # Maya's first own interview
    ├── turn-05-eng-devon.md              # Eng deep-dive on social vs AI
    ├── turn-06-resolve-strategy-vs-roadmap.md  # Contradiction resolution
    ├── turn-07-maintenance-sweep.md      # Staleness check
    ├── turn-08-interview-tom.md          # Second couples-budgeting signal
    ├── turn-09-q4-decision.md            # Decision draft
    └── turn-10-handoff-prep.md           # Synthesis for next PM
```

Turn 01 is unusually long (~3500 words) because it inlines an entire inherited folder. The remaining turns are 200-600 words each, in line with scenario 01.
