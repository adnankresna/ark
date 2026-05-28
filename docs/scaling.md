# How PM Brain scales

The brain is built to stay performant on a working PM timescale: one PM, one product, accumulating context over time. This page explains why, and what the system does on your behalf as the folder grows.

## Three layers, three growth shapes

| Layer | What's in it | How fast it grows | Why that's OK |
|---|---|---|---|
| **Raw** | `source/`, `ingestion/` (one pair per artifact ingested) | Linear with PM activity | Cold storage by default. The agent doesn't read these unless a citation points at them. |
| **Active** | `hypotheses/`, `decisions/`, `stakeholders/` | Sub-linear. Hypotheses promote, demote, archive. Stakeholders are bounded by team size. Decisions are append-only but small. | This is the working set. Lifecycle keeps it small even when the raw layer grows. |
| **Durable** | `knowledge/strategy.md`, `knowledge/product/`, `knowledge/users/insights.md`, `knowledge/market/` | Logarithmic *by design*. The promotion rule folds many observations into one stable claim. | This is the compressed layer. It's what `/ideate`, `/plan`, `/risk` actually load. |

The brain's typical task touches files in the active and durable layers only. A `/prep` reads one stakeholder file. A `/risk` reads the feature + its hypothesis file. An `/ideate` reads strategy + insights + active hypotheses. Brain age doesn't change what these commands read.

## What the agent reads by default

Pulled directly from `CLAUDE.md § Context budget`:

> Under context pressure, prioritize: (1) current feature, (2) active hypotheses, (3) strategy. **Drop historical ingestion logs first. They are reference, not default context.**

And from `CLAUDE.md § Retrieval-first behavior`:

> Prefer targeted retrieval over broad retrieval. Search filenames, INDEX entries, and linked references before opening large documents. Load the smallest sufficient context needed to act correctly.

In other words: the agent navigates through `INDEX.md` → the named active file → its direct references. It does not scan whole folders. This is why the active read set is bounded by the *task*, not the *brain size*.

## What the agent reads on demand

Old material gets pulled into context only when one of these four things happens:

1. **A provenance link points at it.** Every load-bearing claim in `insights.md`, hypothesis evidence rows, and decision evidence rows is tagged with a `[ingestion/...]` or `[source/...]` link. When you ask "why does the brain believe X?", the agent follows the link. This is what the raw layer is *for*: audit trail, not default context.
2. **Contradiction detection on `/ingest`.** When a new artifact comes in, the agent inspects the most relevant prior ingestion (not the most recent, not all) to decide "new signal vs. third confirmation of an existing pattern."
3. **Promotion synthesis.** When a hypothesis crosses the promotion bar, the agent reads each cited ingestion file to write the synthesis row in `insights.md` with named supporters.
4. **`/review` drift surfacing.** When weekly maintenance finds new evidence contradicting an already-`promoted` hypothesis, it must cite the original premise by name, so it reads the originals. This is expensive on purpose; it's how drift becomes visible to you.

For everything else (routine `/prep`, `/ideate`, `/risk`, `/plan`) old material stays cold.

## What the system compresses

Compression is the explicit design choice that lets the durable layer grow logarithmically while the raw layer grows linearly. Four mechanisms, all in `CLAUDE.md`:

| Mechanism | What it does | Where it lives |
|---|---|---|
| **Memory promotion** | Items in `ingestion/` are working memory. Only recurring / decision-relevant / strategy-relevant items get promoted to `knowledge/`. One-offs stay in ingestion and never reach the durable layer. | `CLAUDE.md § Memory promotion` |
| **Insight synthesis** | When 2+ independent signals say the same thing, they fold into one row in `knowledge/users/insights.md`. The originals stay as citations under that row. N observations become 1 claim. | `CLAUDE.md § Memory promotion: Where promotion lands` |
| **Hypothesis lifecycle** | `active` → `promoted` (spawns a decision) → `archived` (moves to `hypotheses/archive/` 90 days after the feature ships). `demoted` / `killed` stay in place but exit the active roster in `hypotheses/INDEX.md`. | `hypotheses/_SCHEMA.md § Lifecycle` |
| **/review archival sweep** | The weekly sweep auto-archives shipped features past 90 days and compresses duplicate insights. Stale strategy assumptions, decision debt, and major hypothesis demotions are drafted for your sign-off. | `commands/review.md § Surfaces` |

The net effect: as you accumulate more signals, the durable layer stays roughly constant in size because the promotion rule keeps demanding *recurring + decision-relevant* before anything lands there. Noise filters itself out.

## What about irrelevant ingestion?

Not everything you ingest will turn out to matter. A meeting note that goes nowhere, a market snapshot that doesn't connect, a Slack thread that resolved offline. The design accommodates this without penalty:

- **Irrelevant ingestion stays in `ingestion/`.** It never promotes to `knowledge/` because it doesn't clear the bar (recurring, decision-relevant, strategy-relevant, repeatedly observed).
- **It doesn't pollute the active read set.** Default loads target the durable layer + the directly-relevant active file. The agent doesn't open ingestion files that nothing cites.
- **It stays available for audit.** If a question comes up later ("did we ever hear from X?") the file is grep-able and date-organized.

Cost of an irrelevant ingestion: disk space and one folder entry. Cost to your day-to-day brain operation: zero.

This is the deliberate trade. The system would rather you over-capture than under-capture. The promotion rule does the relevance-filtering.

## What `/review` surfaces to you

You don't have to remember to act on growth pressure. `/review` watches for it on your behalf, weekly. Six checks (`commands/review.md`):

1. **Stale knowledge**: files not updated in 6+ weeks.
2. **Stale evidence**: market past 30-60 days, interviews past 90, strategy assumptions past quarterly.
3. **Hypothesis hygiene**: active hypotheses with no evidence in 30+ days, promoted hypotheses without decisions, triggered "what would reverse this" conditions.
4. **Stakeholder cadence + strategy tensions**: high-influence stakeholders not touched in 3+ weeks, drift between recent decisions and strategy.
5. **Knowledge synthesis**: recurring patterns ready to promote, recurring contradictions, candidates for `strategy.md § Tensions`.
6. **Archival sweep**: shipped features past 90 days, resolved hypotheses, old market intel.

What `/review` does automatically (when autonomy mode is `act and tell`): archive shipped-feature hypotheses past 90 days, compress duplicate insights, update last-touched timestamps, fix small things.

What it surfaces for your call: anything that requires PM judgment, such as strategy changes, tension resolution, major hypothesis promotion or kill, decision debt, archiving a feature.

You don't have to monitor brain size. The brain monitors itself and tells you what needs your attention.

## The realistic envelope

The system is sized for one PM running one product. Concrete numbers from typical PM workloads:

- **Interviews:** A PM running active discovery does ~2-4 customer interviews per week, with quiet stretches. That's ~50-100 ingested interviews in a busy year, not 500. Inherited material from migration mode adds a one-time burst, but inherited interviews compress fast. Many turn out to be redundant with each other.
- **Meeting notes / Slack captures / ad-hoc:** Highly variable, but the average PM doesn't capture every meeting. They capture the ones that matter. A few per week.
- **Hypotheses:** Active set rarely exceeds 10-20. Most features get 3-5 hypothesis rows; few features are under hypothesis investigation simultaneously.
- **Decisions:** ~10-30 substantive decisions per year per active PM. Append-only, small files, rarely re-read.
- **Stakeholders:** Bounded by your team and partners. 10-30 files is a realistic upper bound for one role.

At those volumes, after a year of active use, you have a few hundred files total. Well inside what the agent can navigate via INDEX-first routing without scanning the raw layer.

## Time is on your side

The architecture is markdown-in-git. That choice ages well in two specific ways:

- **Model context windows expand.** What requires careful folder-bounded retrieval today becomes load-the-whole-active-layer tomorrow. PM Brain doesn't need to be re-architected to take advantage; the same files just get more of them loaded at once.
- **The data format doesn't depend on the model.** Markdown files in a git repo are forward-compatible with every future Claude, every future Cursor, every future agent. The brain you build today doesn't get locked to today's tooling.

This is the architectural payoff of refusing vector DBs and embedded retrieval. Those choices bind you to the tooling generation you built against. Plain markdown does not.

## Summary

- Default reads are folder-bounded, not brain-bounded. Brain age doesn't change what routine commands load.
- The durable layer (`knowledge/`) compresses logarithmically by design.
- The raw layer (`source/`, `ingestion/`) grows linearly but stays cold unless cited.
- Irrelevant ingestion costs disk space, not context. The promotion rule filters it out automatically.
- `/review` watches for staleness and drift weekly. You don't have to monitor the brain; it surfaces what needs your call.
- Models improve faster than your brain grows. The format is portable.

The system is built for the working timescale of an actual PM role, with explicit compression and surfacing mechanisms doing the work you'd otherwise have to do yourself.
