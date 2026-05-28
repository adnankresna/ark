# Interview

Run before scaffolding. Ask in **batches of 3–4 questions**, not one-by-one. Tone: short, direct, no lecturing.

In migration mode, **skip batches already covered by source artifacts** and ask only the unknowns. Tell the PM what you already know before asking what you don't.

## Batch A — Context
1. Company name, product, and one-line description of what it does.
2. Stage (pre-PMF / scaling / mature) and rough scale signal (users, ARR, team size — whatever they know).
3. Their role scope: which surfaces / squads / domains do they own?
4. Top 3 strategic priorities for the next 1–2 quarters (rough is fine; we'll refine).

## Batch B — People
1. Name + role of their top 5–10 stakeholders (manager, eng lead, design lead, key execs, key customers if applicable).
2. Which 2–3 of those are **highest-friction or highest-leverage** right now?
3. Cadence — any standing 1:1s / rituals worth encoding?

## Batch C — Work in flight
1. What features / initiatives are **active** right now? (list 2–6, slug-ify them)
2. What's the next **big bet** being scoped but not started?
3. Any recent **shipped** thing they're still measuring?

## Batch D — Inputs
1. What data sources do they touch weekly? (analytics tool, interview transcripts, support tickets, sales calls, Slack channels, etc.)
2. Do they run customer interviews? If yes, roughly how often, and where do transcripts live?
3. What competitor / market signals do they track?

## Batch E — Operating preferences
1. Autonomy level: should the system **act and tell** (default), or **propose and wait**? Recommend "act and tell" for anything reversible. Stored in `CLAUDE.md § Operating preferences § Autonomy mode`.
2. Maintenance cadence preference: weekly review? on-demand only? both? Stored in `CLAUDE.md § Operating preferences § Maintenance cadence`.
3. Anything explicitly **off-limits** beyond the defaults? Defaults: avoid PII (addresses, phone numbers, financial details, government IDs, medical info). Synthetic names, work emails, and organizational context are allowed. Stored in `CLAUDE.md § Off-limits`.

## After the interview

1. **Summarize back what you heard in 6–10 bullets.**
2. **Surface contradictions.** Examples: "You said pre-PMF but listed 8 active features — which is real?" "Your top stakeholder is high-friction *and* you said cadence is monthly — is that the right rhythm?"
3. **Confirm before scaffolding.** Do not move on without explicit confirmation.

## What the answers feed

| Batch | Question | Populates |
| --- | --- | --- |
| A | Q1-2 company/product/stage | `knowledge/strategy.md` (top section), `README.md` (product line, optional) |
| A | Q3 role scope | `knowledge/org/team.md` |
| A | Q4 priorities | `knowledge/strategy.md § 1–2 quarter priorities` |
| B | Q1 stakeholders | `stakeholders/<slug>.md` (one per person), `stakeholders/INDEX.md` (roster) |
| B | Q2 friction/leverage | `stakeholders/<slug>.md § Snapshot` (influence + friction), `stakeholders/INDEX.md` |
| B | Q3 cadence | `knowledge/org/rituals.md` |
| C | Q1 active features | `knowledge/product/features/<slug>.md` (one per feature), `knowledge/product/roadmap.md § Now` |
| C | Q2 next big bet | `knowledge/product/roadmap.md § Next` |
| C | Q3 recent shipped | `knowledge/product/roadmap.md § Now` (with status: measuring), feature file |
| D | Q1 data sources | `knowledge/org/tools.md`, `rules/data.md § Source of truth per metric` |
| D | Q2 interview cadence | `rules/discovery.md § Cadence`, `rules/discovery.md § Where transcripts live` |
| D | Q3 market signals | `knowledge/market/landscape.md`, `knowledge/market/trends.md` |
| E | Q1 autonomy | `CLAUDE.md § Operating preferences § Autonomy mode` |
| E | Q2 maintenance cadence | `CLAUDE.md § Operating preferences § Maintenance cadence` |
| E | Q3 off-limits | `CLAUDE.md § Off-limits` |

Keep provenance: every populated field should be traceable back to a specific Batch question or a source artifact. If a Batch answer has no clear home, flag it in the post-scaffold "immediate next moves" rather than silently dropping it.

## Provenance vocabulary, not provenance workflow

When you write claims into hypotheses, insights, or decisions, tag each row with a provenance marker from the enum in `hypotheses/_SCHEMA.md`. Claims born in this interview (no artifact behind them) are legitimate inputs — tag them `(stakeholder-verbal, <PM>, <date>)` or `(chat, no artifact)` rather than fabricating an ingestion record. The auditability promise is "every claim wears its source," not "every claim went through synthesis."
