# Why this matters

Most AI memory systems fail by month three. The same five failure modes show up across vector-DB memory, RAG over your docs, "AI second brain" apps, and most agent-memory frameworks. PM Brain is structured around five corresponding design choices, each one targeting a specific failure.

This page is the short version. The architecture choices behind each fix are in [`architecture.md`](./architecture.md). The lifecycle that operates them is in [`how-it-works.md`](./how-it-works.md). The growth-shape defense is in [`scaling.md`](./scaling.md).

## Five failure modes

These show up consistently across knowledge systems that look fine at month one and rot by month three.

1. **Accumulate, never synthesize.** Every interview, every Slack thread gets stored. Nothing compresses. The system becomes a landfill.
2. **Flatten contradictions into consensus.** Three interviews say three things, summarized into one bland insight. The disagreement was the signal.
3. **Drift silently from strategy.** Two months of decisions point one way, the strategy doc points another. Nobody surfaces the tension.
4. **Lose decision context.** Why did we ship X? What were the alternatives? Most systems store the decision and lose the reasoning.
5. **Overload context.** The agent loads too much, gets confused, generates shallow output.

## Five structural differences

Each PM Brain design choice maps to a failure mode above.

1. **Epistemic boundaries.** Every claim is tagged: observation, interpretation, hypothesis, assumption, decision. A Slack comment is not automatically truth. A customer quote is not automatically strategy. A meeting note is not automatically insight. *Addresses failures 2 and 4: contradictions stay distinct, decisions wear their reasoning.*
2. **A maintenance model that runs.** Weekly sweep. Stale evidence flagged, recurring patterns compressed, contradictions preserved. The compression is the synthesis. *Addresses failure 1: the system forgets on purpose.*
3. **Flag, never gate.** The system surfaces. The PM decides. The moment it becomes a blocker, it dies. Drift between recent decisions and strategy gets flagged on `/review`; you decide whether the doc or the work is wrong. *Addresses failure 3: drift becomes visible without forcing the answer.*
4. **Inspectable, not opaque.** Markdown, repo-native, editable, version-controllable. Trust is the bottleneck for any memory system; plain text is the highest-trust format. *Cross-cuts every failure: when the system is wrong, you can see why.*
5. **Resists complexity creep.** No taxonomies, no agent swarms, no graph ontologies. Opinionated and lightweight. The retrieval surface is bounded by named knowledge areas instead of fuzzy similarity. *Addresses failure 5: bounded loads, no context overflow.*

## The headline

Most systems store. Few forget on purpose.

PM Brain is built around the forgetting. The promotion rule keeps the durable layer compressed by demanding *recurring + decision-relevant + strategy-relevant* before anything lands there. The weekly sweep is the forcing function. Provenance tags are what keep it honest when real PM work is messy.

The rest of the docs explain how. Start with [`walkthrough.md`](./walkthrough.md) for a week-in-the-life story, or [`architecture.md`](./architecture.md) for the design choices stated cleanly.
