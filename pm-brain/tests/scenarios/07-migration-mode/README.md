# Scenario 07 — Migration mode (greenfield bulk-ingest)

You're Aisha Patel, PM for **OperatorOS**, a developer-tools company building an API monitoring product (B2B SaaS, mid-market focus). You've been doing the PM job for 18 months **without** a structured second brain — just a messy folder of Google Docs exports, Slack snippets, interview transcripts, a strategy memo, two persona docs, a competitive landscape doc, a roadmap planning doc, and a CFO email about budget cuts. Today is **2026-05-17**. You're invoking PM Brain for the first time, in migration mode, and dumping the folder into it.

This scenario exercises **migration mode itself** — the init-phase behavior promised by [`prompts/migration.md`](../../../.claude/skills/pm-brain/prompts/migration.md) when the working directory already contains pre-existing PM artifacts. It tests the *conservative ingestion contract*: route every artifact to `source/`, create matching `ingestion/` syntheses without inferring beyond the artifact, surface tensions without resolving them, and **do not auto-promote anything into `hypotheses/` or `knowledge/` until the PM explicitly asks**.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Bulk-route pre-existing artifacts to `source/` (verbatim, by kind) | Turn 1 (migrate folder, 8 attached artifacts) | Structural |
| Conservative ingestion synthesis (no inference past the artifact) | Turn 1 | Content (LLM judge) |
| Hold back on hypotheses / knowledge promotion until the PM signals | Turn 1 | Structural + content |
| Walk the routing logic on PM review | Turn 2 (Q&A turn) | Light structural |
| Surface cross-artifact tensions explicitly | Turn 3 (`/strategy-check`-style ask) | Content (LLM judge) |
| Draft first hypothesis on demand, citing source/ artifacts | Turn 4 | Structural + content |

## Lifecycle moves NOT exercised here

- Auto-promotion from accumulating evidence over time (covered by 01)
- Demotion from contradicting signal on a previously-promoted hypothesis (covered by 03)
- Inheriting an already-structured PM Brain from another PM (covered by 02 — that's a different shape: artifacts arrive pre-structured, here they arrive as a messy raw folder)
- Maintenance sweep / weekly review (covered by 03 turn 3, and partially 02)

## Distinction from scenario 02

Scenario 02 (Maya / Tally) tests **post-bulk-ingest behaviors** — what happens after a migration has landed and the PM works through tensions, fresh interviews, decisions over 10 turns. The artifacts in 02 arrive somewhat structured (Alex's named files, a strategy doc with sections, a CS monthly with rankings).

Scenario 07 tests **migration mode itself** — the from-scratch routing decision and the conservative-ingestion contract on day 0. Artifacts here are messier (Slack thread fragments, a CFO email, exec-style memos without templates). The eval focus is on what the brain *holds back* from doing, not what it produces. No hypothesis files should exist after turn 1.

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Migrate folder | Aisha attaches 8 messy artifacts spanning Q4 2025 → April 2026. Asks brain to route to `source/`, write `ingestion/` syntheses, but **not** promote anything yet. |
| 02 | Review routing | Aisha asks the brain to walk through what landed where and flag any artifact it wasn't sure about. |
| 03 | Surface tensions | Aisha asks the brain to list cross-artifact contradictions — the Q4 strategy bet vs Q2 reality, the roadmap commits vs the CFO budget cut, the conflicting interview signals on a feature, persona drift. |
| 04 | Propose first hypothesis | Aisha picks the most actionable tension and asks the brain to draft a candidate hypothesis with `proposed` status, citing `source/` artifacts. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns. Turn 1 is unusually large (8 artifacts inlined). Estimate ~$2-3 per single-run; ~$10-15 for `--runs 5`.
