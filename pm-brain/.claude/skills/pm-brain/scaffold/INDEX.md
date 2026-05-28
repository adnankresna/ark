# PM Brain — Master Index

Start here. Every task begins by routing through this file.

## Areas

| Area | Path | Load when |
| --- | --- | --- |
| Strategy | [knowledge/strategy.md](./knowledge/strategy.md) | Planning, prioritization, drift checks |
| Product | [knowledge/product/](./knowledge/product/) | Feature work, metrics review, roadmap |
| Users | [knowledge/users/](./knowledge/users/) | Discovery, interview synthesis, segmentation |
| Market | [knowledge/market/](./knowledge/market/) | Competitive analysis, positioning |
| Org | [knowledge/org/](./knowledge/org/) | Team / process / tooling questions |
| Stakeholders | [stakeholders/](./stakeholders/) | Prep for any 1:1 or cross-functional touchpoint |
| Hypotheses | [hypotheses/](./hypotheses/) | Pre-ship feature work, experiment design, post-launch evaluation |
| Decisions | [decisions/](./decisions/) | Anything that commits future effort or reverses a prior choice |
| Rules | [rules/](./rules/) | How this PM runs discovery, prioritization, shipping, writing |
| Ingestion | [ingestion/](./ingestion/) | Customer interviews, meeting notes, market intel, ad-hoc dumps — synthesized records |
| Source | [source/](./source/) | Verbatim audit anchors for every ingested artifact — never edited |
| Maintenance | [maintenance/](./maintenance/) | Weekly/periodic system reviews |

## Workflows

See [docs/workflows.md](./docs/workflows.md) for the full slash command list and ingestion mode reference.

## Quick triggers

- `/ingest interview <file>` — process a customer interview transcript
- `/ingest meeting <file>` — process meeting / 1:1 notes
- `/ingest market <url-or-file>` — process competitor / market intel
- `/ingest adhoc` — free-form "just learned this" dump
- `/prep <stakeholder-slug>` — load stakeholder + recent context for an upcoming touchpoint
- `/hypothesize <feature-slug>` — generate or refresh hypotheses for a feature (works pre-ship OR post-ship from data)
- `/decide <slug>` — log a decision (interactive prompt)
- `/review` — run full maintenance sweep
- `/strategy-check` — drift check between recent decisions/ingestions and `knowledge/strategy.md`
- `/ideate <problem>` — generate evidence-grounded solution directions
- `/risk <feature-slug>` — 5-area risk scan; drafts hypothesis stubs for gaps
- `/plan <objective>` — turn an objective into discovery questions, hypotheses, experiments, decision points

Conversational equivalents work for all of these. Commands are optional.
