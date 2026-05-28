# PM Brain

A durable reasoning and memory architecture for a product operator — a PM, product lead, founder, or anyone accountable for one product or initiative with judgment-heavy work and scattered inputs.

Not a notes app. Not a chatbot with memory. An agent-native, markdown-native operating layer that preserves context, reasons across time, and resists the slow collapse that happens when product knowledge gets scattered across Slack, Notion, dashboards, docs, and memory.

PM Brain optimizes for continuity, judgment, synthesis, and long-term product memory — not for generation.

## The problem with most AI memory systems

They fail in predictable ways: accumulate without synthesizing, flatten contradictions into false consensus, drift from strategy silently, lose decision context, overload context windows, become documentation graveyards.

The two outcomes: a passive store nobody trusts, or a noisy assistant generating shallow outputs from fragmented context.

PM Brain was designed specifically to avoid both.

## Five things that make PM Brain different

### 1. Epistemic boundaries

Most systems never define what counts as evidence, what counts as interpretation, what deserves promotion into durable knowledge, or when the agent should escalate. PM Brain does, along two orthogonal axes:

- **Epistemic type:** every piece of content is tagged as one of **observation**, **interpretation**, **hypothesis**, **assumption**, **decision**.
- **Provenance:** every load-bearing claim wears a tag from a small enum — `[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, <name>, <date>)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, `(chat, no artifact)`.

The provenance axis is what keeps the brain honest when work is messy. PM intuitions, off-the-record stakeholder conversations, and industry priors are legitimate inputs — they just have to wear their actual provenance. The system enforces the **vocabulary**, not the workflow.

A Slack comment is not automatically truth. A customer quote is not automatically strategy. The system preserves provenance, confidence, and contradictions instead of pretending certainty exists where it doesn't.

### 2. A maintenance model that actually runs

Storage alone is insufficient. The weekly `/review` sweep flags stale evidence, surfaces unresolved tensions, tracks decision debt, synthesizes recurring patterns, compresses duplicates, preserves meaningful contradictions, and archives low-signal history.

Memory systems fail at month three because nothing sweeps. PM Brain was designed around that reality from day one. See [system-evolution.md](./system-evolution.md) for the 8 failure modes the sweep is designed to catch.

### 3. Flag, never gate

The system flags missing hypotheses, strategic tensions, stale assumptions, unresolved decisions, and relationship debt. It does not block execution. The operator remains the decision-maker.

This is a reasoning system, not a compliance system. The moment it starts blocking work, it dies.

### 4. Inspectable architecture

No embeddings, hidden retrieval, auto-generated ontologies, vector databases, or invisible memory layers. PM Brain is markdown-native, repo-native, version-controllable, fully auditable.

You can always inspect what the system believes, why it believes it, where the evidence came from, what changed, and which contradictions remain unresolved. Inspectability creates trust. Trust is the hidden bottleneck in long-running AI systems.

### 5. Resists complexity creep

Many AI operating systems collapse under their own architecture: taxonomies, agent swarms, graph ontologies, embedding pipelines, auto-tagging. PM Brain stays opinionated, lightweight, retrieval-oriented, operational. The goal is not maximum sophistication — it's durable reasoning quality a real operator can maintain consistently.

## What PM Brain is not for

Not fully autonomous product management — supports judgment, doesn't replace it. Not enterprise knowledge management — one accountable operator, one product or initiative. Not perfect truth reconstruction — preserves provenance and contradictions, doesn't resolve genuinely ambiguous reality. Not maximum information capture — throws things out deliberately.

Explicitly avoided: vector databases, opaque memory layers, mandatory metadata, process-heavy workflows, ontology sprawl, multi-agent orchestration, auto-tagging.

## How to start

Don't backfill everything. Begin with what you can use this week:

1. Ingest one real customer interview today.
2. Prep your next stakeholder conversation with `/prep <slug>`.
3. Run `/review` on Friday.

Active features, current stakeholders, recent interviews, important decisions. Let the system compound through ingestion and the weekly sweep. The brain learns the shape of your work as you work.
