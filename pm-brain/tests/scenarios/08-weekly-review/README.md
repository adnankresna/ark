# Scenario 08 — Holistic weekly /review

You're Aria Sharma, PM for **LogLens**, a B2B observability SaaS used by mid-market platform engineering teams (~190 paying accounts, ARR ~$9M). You're two months into a roadmap commitment to "make alerts trustworthy again" — the headline bet being smarter on-call alert routing and noise reduction. Today is **2026-05-17** (Friday). You're about to do your weekly `/review` and your brain is genuinely busy: there's drift, there's a stale relationship that matters, there's a decision whose reversal-condition window is closing, there's an aging insight, AND there's a healthy hypothesis quietly accumulating evidence.

This scenario exercises **holistic /review**: the brain's ability to surface multiple *different categories* of finding in one pass — drift, stale-stakeholder, expiring-reversal, aging-insight, healthy — and **prioritize them** by what blocks current work first, what's drifting next, what's healthy noted last. Not flatten everything into a single narrative thread. Not flag everything equally.

This scenario is **distinct from scenarios 03 and 05**:

- Scenario 03 tests `/review` surfacing ONE thing (drift) on an aged hypothesis.
- Scenario 05 tests `/review` surfacing ONE thing (stakeholder cadence) filtered by relevance.
- **Scenario 08 tests `/review` surfacing 4-5 DIFFERENT categories of finding simultaneously, ordered correctly.**

The trick the brain has to pull off: name each category with a specific artifact (not "some hypotheses are drifting"), order by what should be on the PM's Monday list, AND resist the temptation to put the healthy hypothesis in the action column.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed busy brain (5 simultaneous things-worth-surfacing) | Turn 1 (bulk-ingest ~6-8 artifacts) | Structural |
| Fresh signal ingestion (partly contradicting evidence) | Turn 2 (May 12 customer call) | Structural + content |
| Holistic `/review` surfaces ALL categories, ORDERED | Turn 3 | Content (LLM judge × 4) |
| Prioritize action — pick top-two with reasoning | Turn 4 | Structural (no-write) + content |

## Lifecycle moves NOT exercised here

- Hypothesis promotion from a single strong signal (covered by 01)
- Full drift reversal (covered by 03 — here the contradiction is partial, not a full reversal)
- Bulk migration (covered by 02 / 07)
- Persona emergence (covered by 04)
- Maintenance sweep with compression / archival (covered by 06)

## Seeded state — what the brain holds at start of turn 3

1. **Drift candidate** — `hypotheses/alert-noise-reduction.md`, status `promoted` (promoted 2026-03-18 based on March on-call survey). A 2026-05-12 customer call (Turn 2) partly contradicts it: the 60% noise-reduction target the hypothesis names may be wrong — customers want 80%. NOT a full reversal; the *direction* still holds, the *threshold* is suspect.
2. **Aging insight** — `knowledge/users/insights.md` carries an entry from **2026-01-29** ("on-call engineers want alert grouping by service") sourced from a single January 2026 user interview, with no corroborating evidence since. Not contradicted, just unrefreshed for ~4 months.
3. **Stale-and-relevant stakeholder** — `stakeholders/ravi-chen.md`, Eng Lead and engineering owner for the alert-noise-reduction roadmap commitment. `Last touched: 2026-03-30` (~7 weeks stale).
4. **Expiring reversal condition** — `decisions/2026-03-10-on-call-rotation-rework.md`, status `decided`, with reversal condition "if NPS among on-call engineers drops below 32 by end of May 2026, revisit the rotation model." Today is 2026-05-17 — deadline is **2026-05-31**, two weeks out.
5. **Healthy** — `hypotheses/api-latency-p99-vs-p95.md`, status `proposed`, accumulating evidence from three independent customer signals (Feb, April, May), no concerning signals. Just quietly working.

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Seed busy brain | Bulk-ingest ~6-8 artifacts establishing all 5 conditions above. All seeded artifacts are dated Jan-April 2026 (today is May 17). |
| 02 | Add fresh signal | PM attaches the 2026-05-12 customer call transcript that partly contradicts alert-noise-reduction's 60% threshold. Brain ingests, adds an evidence-against row, does NOT yet draw /review conclusions. |
| 03 | Weekly /review | PM asks: "It's Friday. Walk me through what's on the brain right now — what's drifting, what needs attention, what looks healthy. Order it by what should be on my Monday list." |
| 04 | Prioritize action | PM asks: "Pick the top two for me to act on this week. Why those two?" Brain commits to two with defensible reasoning. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.50-0.75 = ~$2-3 single-run; ~$10-15 for `--runs 5`. Turn 1 is the largest (seeds the most state).
