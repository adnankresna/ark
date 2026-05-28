# Prior art

PM Brain didn't appear from nowhere. It borrows from four traditions, rejects one common pattern, and adds two ideas that are specific to PM work.

## What it borrows

### Zettelkasten (Niklas Luhmann, 1960s-)

The original "personal knowledge system designed to think with, not just store in." Atomic notes, explicit links between notes, emergence over time, the writer maintains it manually.

**What PM Brain borrows:** the inspectability stance. Plain-text notes. Explicit links. The system is a tool for thought, not a database to query.

**What it doesn't borrow:** the unstructured graph. PM work has bounded contexts (strategy, product, users, market, org) and a clear lifecycle (hypothesis → decision). Forcing all of that through a flat note graph loses the structure that makes PM judgment legible.

### RAG / vector-DB memory (2023-)

Embed every document, retrieve by semantic similarity at query time. The dominant pattern in 2023-2025 AI memory systems.

**What PM Brain rejects:** the opaque retrieval layer. Embeddings flatten provenance. You can't easily ask "why does the system believe X?" when the answer is "these five chunks scored highest in cosine similarity." For PM judgment work, provenance matters more than recall breadth.

**What it borrows:** the recognition that retrieval is the bottleneck, not generation. PM Brain bounds retrieval through explicit knowledge areas instead of through fuzzy similarity scoring. Same goal, different mechanism.

### Agent OS / CLAUDE.md patterns (2024-)

The CLAUDE.md operating manual pattern, where a single file in the repo root tells the agent how to work there. Popularized by Anthropic's Claude Code and the broader agentic-IDE movement.

**What PM Brain borrows:** the operating manual as code. CLAUDE.md survives sessions, models, and tools. It's version-controlled. It's reviewable. It scales with the project.

**What it adds:** the lifecycle layer (hypotheses, decisions, stakeholders) on top of the knowledge layer. CLAUDE.md alone tells the agent how to act. PM Brain tells it what's true, what's tested, and what's committed.

### Continuous Discovery + the four product risks (Teresa Torres + Marty Cagan)

The discovery cadence and the canonical four risks (value, usability, feasibility, viability) come from product management's existing literature. PM Brain encodes them as scaffold defaults. Every hypothesis file has the 5 risk areas as sections (the four canonical risks plus "other" for the ones that don't fit).

**What PM Brain borrows:** the conceptual framework PMs already use.

**What it adds:** the file structure that makes the framework operate by default instead of by convention.

## What's specific to PM Brain

### 1. The hypothesis / decision split

Most knowledge systems mash bets and commitments together. PM Brain separates them:

- **Hypotheses** are bets being tested. Mutable. Evidence accrues. Confidence shifts.
- **Decisions** are commitments made. Append-only. Every decision has a "what would reverse this" field.

This split is what makes the audit trail useful three months later. When a decision's reversal condition triggers, the maintenance sweep surfaces it.

### 2. Promotion is judgment work, not automation

Most memory systems auto-consolidate. PM Brain proposes promotions and asks for sign-off. The agent identifies recurring patterns (3+ independent observations from the same persona, for example) and drafts the insight. The PM accepts, edits, or rejects.

The cost: a small amount of friction per promotion.

The benefit: the durable layer doesn't fill with noise. Rubber-stamp everything and you've lost the benefit. Reject everything and the system never learns. The friction is the feature.

## What's deliberately out of scope

- **Multi-team coordination.** PM Brain assumes one accountable operator, one product. Enterprise knowledge management is a different problem with different trade-offs.
- **Auto-integration with CRM / analytics / ticketing.** PM Brain ingests transcripts, screenshots, and notes. It doesn't reach into your stack. You can plug it in via custom skills, but that's an additive choice, not the default.
- **Perfect truth reconstruction.** The system preserves provenance and contradictions. It does not pretend to resolve genuinely ambiguous reality.
- **Fully autonomous PM.** The system supports judgment. The PM still makes the calls. The agent is staff support, not a replacement.

## Adjacent ideas worth comparing

| Idea | Closest to PM Brain in | Different from PM Brain in |
|---|---|---|
| Roam Research / Obsidian | Plain text, links, inspectable graph | Not agent-native. No operating manual. No lifecycle layer. |
| Notion AI | One workspace, AI can read it | Closed format. No provenance. Auto-everything tends to fail at month three. |
| LangChain / LlamaIndex memory | Same retrieval-is-the-bottleneck insight | Opaque retrieval. No lifecycle. Built for chat, not for judgment work. |
| Cursor / Aider rules files | Operating-manual-as-code stance | Per-codebase, not per-product. No knowledge or lifecycle layer. |
| AutoGPT / BabyAGI agent loops (2023) | Persistent task memory | Optimized for autonomous task completion. PM Brain is built for human-in-loop judgment, not autonomy. |

## What we want to learn next

The eval suite (`tests/`) is where ideas from adjacent systems get tested against PM Brain. When a scenario fails in a way that suggests a borrowed pattern would do better, document the gap here and consider adapting.

Document drift in this file when:

- A new system in this space ships something genuinely novel worth comparing.
- A scenario fails in a way that highlights an architectural limitation worth naming.
- A user adapts PM Brain in a direction we hadn't considered.

This page is allowed to be opinionated. Don't false-balance: if a pattern is bad for PM judgment work, say so and explain why.
