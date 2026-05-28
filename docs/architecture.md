# Architecture

PM Brain is two architectural decisions and one operating loop. Everything else follows.

## Decision 1: Deterministic scaffold + adaptive prompts

The skill is split into two layers that evolve independently.

| Layer | Lives in | Behavior | Why |
|---|---|---|---|
| **Static structure**: schemas, `CLAUDE.md`, `INDEX.md`, folder tree, file templates | `.claude/skills/pm-brain/scaffold/` | Deterministic. Same every install. | Copy-paste reliability. No generation drift. Schemas can evolve without touching reasoning. |
| **Adaptive reasoning**: mode detection, migration, interview, post-scaffold self-test | `.claude/skills/pm-brain/prompts/` | Probabilistic. Depends on inputs. | Reasoning can improve without rewriting schemas. Behavior evolves in `prompts/`, structure stays stable. |
| **Orchestration**: when to load what | `.claude/skills/pm-brain/SKILL.md` | Glue. | Single entry point. |

The first version of this skill mixed both layers in one prompt. Forcing deterministic content through probabilistic generation caused inconsistencies, formatting drift, occasional missing files, path errors. Splitting them eliminates that whole class of failure.

## Decision 2: Markdown files in a git repo, no vector layer

Most "AI memory" systems reach for embeddings, vector databases, hidden retrieval. PM Brain reaches for markdown files the PM can read, edit, version-control, and grep.

| What we picked | What we rejected | Why |
|---|---|---|
| Plain markdown | Vector DB / embedded chunks | Inspectable. Editable. No black box. |
| Git for versioning | Hidden auto-snapshots | The PM can see what changed and revert. |
| Explicit promotion (PM signs off) | Automatic memory consolidation | Memory promotion is judgment work. Auto-promotion fills the durable layer with noise. |
| One `CLAUDE.md` per repo | Long system prompts in chat history | The operating manual is part of the codebase. It survives sessions, models, and tools. |
| Five knowledge areas + three lifecycle areas | One flat note library | Bounded retrieval. The agent loads the relevant area, not half the repo. |

The cost of this choice: no fuzzy semantic search out of the box. The benefit: every claim the system makes traces to a specific file. That trade-off is right for PM judgment work, where provenance matters more than recall breadth.

## The architecture map

```
knowledge/                 (durable, synthesized)
├── strategy.md            North-star metric, priorities, non-goals, tensions
├── product/               Metrics (AARRR + north-star), features, roadmap
├── users/                 Personas, segments, synthesized insights
├── market/                Landscape, competitors, trends
└── org/                   Team, rituals, tools

hypotheses/                (durable, evidence-state)
└── <feature-slug>.md      One file per feature, 5 risk areas as sections

decisions/                 (durable, append-only)
└── <date>-<slug>.md       One file per decision, with "what would reverse this"

stakeholders/              (durable, people-state)
└── <slug>.md              One file per person, with touchpoint log

ingestion/                 (working memory)
├── interviews/            Customer interviews
├── meetings/              1:1s, reviews, syncs
├── market/                Competitor screenshots, articles
└── adhoc/                 "Just learned this" dumps

source/                    (immutable copies of inputs)
maintenance/log/           (dated sweep reports)
rules/                     (PM-specific rules: discovery, data, prioritization, shipping, writing)
docs/                      (workflow + schema reference)
```

## The cognition pipeline

Evidence flows in one direction. It fans out at the durable layer.

```
source/            →   ingestion/        →   knowledge/      (synthesized observations, durable facts)
(immutable copy)       (working memory)      hypotheses/     (testable beliefs, evidence accrual)
                                             decisions/      (committed choices, append-only)
                                             stakeholders/   (people state, touchpoint log)
```

The same ingestion can update multiple durable destinations in parallel. A 45-minute customer interview might touch six files: one source copy, one ingestion record, one insight promoted to `knowledge/users/`, one hypothesis strengthened, one stakeholder touchpoint logged, one decision drafted as `pending`.

## Provenance: a vocabulary, not a workflow

Every load-bearing claim in `hypotheses/`, `decisions/`, and `knowledge/users/insights.md` carries a **provenance tag** from a small canonical enum:

| Tag | Trust |
|---|---|
| `[ingestion/<path>](...)` | Highest. Went through synthesis, links back to `source/`. |
| `[source/<path>](...)` | High. Direct citation to a raw artifact. |
| `(stakeholder-verbal, <name>, <date>)` | Medium. Heard from a person, no recording. |
| `(intuition, PM, <date>)` | Low for external defense, useful internally. |
| `(industry-knowledge)` | Low. Accepted background, flag for replacement. |
| `(chat, no artifact)` | Low. Synthesized in-session, nothing written down. |

The system enforces the **vocabulary**, not the workflow. Real PM work is messy: PMs have intuitions, hear things off-the-record from execs, and inherit claims with no clear pedigree. Those are legitimate inputs. The brain just makes them wear their actual provenance instead of laundering them through a fake `ingestion/` record. The auditability promise is "every claim wears its source," not "every claim was synthesized."

A path-typed tag walks (in two clicks) from a decision back to a `source/` artifact. A non-path tag tells you honestly that no artifact exists. Both are auditable; only the missing tag is a bug.

## The hypothesis / decision split

This is the load-bearing distinction.

**Hypotheses are bets being tested.** Feature-scoped. Each file has the 5 risk areas as sections (value, usability, feasibility, viability, and "other" for the ones that don't fit the canonical four: regulatory, partnership, and so on). Each hypothesis has evidence-for, evidence-against, confidence, a test, and a decision trigger.

**Decisions are commitments made.** Append-only log. Every shipped feature has at least one. Every decision has a "what would reverse this" field, which is the most useful field a decision record can have.

When a hypothesis is confirmed, it gets promoted and a decision record is auto-drafted (status: `pending`, waiting for PM sign-off). When a decision's "what would reverse this" condition triggers, the maintenance sweep surfaces it.

Most systems mash these together. They become useless.

## What survives sessions

The operating manual (`CLAUDE.md`) and the durable layer. Not the chat history. Not the agent's working memory. Not whatever model you happened to use that week.

The portability test: clone the repo to a fresh machine, open Claude Code, ask "what's the current state of feature X?". If the answer comes from files (not chat history), the system is doing its job.
