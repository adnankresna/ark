# Scenario 12 — Decision lifecycle (literal `/prep`, `/hypothesize`, `/decide`)

You're Sam Liu, PM for **FlowExpense**, a B2B fintech expense-management product (~280 mid-market customers). Today is **2026-05-17**. You're walking a feature from prep → hypothesis framing → decision draft over four turns, using literal slash commands at each step.

This scenario exercises **the three decision-lifecycle slash commands** end to end:

1. `/prep <stakeholder-slug>` — load a stakeholder + recent context for an upcoming 1:1, read-only.
2. `/hypothesize <feature-slug>` — generate hypotheses across the 5 risk areas, status `active`/`candidate`, never auto-promoted.
3. `/decide <slug>` — draft a decision file from the evidence trail, with provenance-tagged Evidence rows, an observable reversal condition, and PM-sign-off framing.

It tests that:

- Each slash command is **recognized literally** as a verb.
- `/prep` is read-only (no file mutations except `Last touched` field updates).
- `/hypothesize` covers all 5 risk areas, doesn't auto-promote, tags Evidence rows.
- `/decide` produces a decision file with the schema fields, an observable reversal condition, and a hypothesis-status flip if `--resolves <H-slug>` is used.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed: stakeholder file + feature folder + a prior interview | Turn 1 | Structural |
| `/prep` literal dispatch, read-only | Turn 2 | Structural (no new files; only `Last touched` updates) + content judge on prep-shape |
| `/hypothesize` literal dispatch | Turn 3 | Structural (hypothesis file created with all 5 risk areas) + content judge on risk-area coverage |
| `/decide` literal dispatch resolving a hypothesis | Turn 4 | Structural (decision file with reversal condition; hypothesis status flipped via the decision, not silently) + content judge on observable reversal condition |

## Lifecycle moves NOT exercised here

- The 4 `/ingest` kinds (11-ingest-shapes)
- `/strategy-check`, `/risk`, `/plan`, `/ideate` (13-strategic-planning)
- Deep evidence-promotion judgment (covered by 10-promotion-gate)

## Turn map

| Turn | Command | Summary |
|---|---|---|
| 01 | Seed | Drop a stakeholder file for the head of Finance (Diana Okonkwo), a roadmap entry for the "auto-approve under $50" feature, and a prior customer interview mentioning the friction. |
| 02 | `/prep diana-okonkwo` | PM asks for prep on an upcoming Diana 1:1 about the auto-approve feature. Read-only. |
| 03 | `/hypothesize auto-approve-under-50` | PM asks for hypotheses across the 5 risk areas. New hypothesis file, status `active`. |
| 04 | `/decide ship-auto-approve-under-50 --resolves <hypothesis-slug>` | PM asks for a decision draft. Decision file with observable reversal condition; hypothesis status flips to `promoted` via the decision. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.30 = ~$1.20 single-run; ~$6 for `--runs 5`.
