# Commands

Operator-facing verbs. Each command is a thin spec: input, files to load, files to update, what to surface. The agent reads the spec, executes against the brain, and reports back per `CLAUDE.md § Operating loop`.

| Verb | When to run it |
| --- | --- |
| [`/ingest`](./ingest.md) | Any new artifact lands — interview, meeting notes, market signal, ad-hoc note |
| [`/prep`](./prep.md) | Before a 1:1, exec review, roadmap discussion, or any stakeholder conversation |
| [`/review`](./review.md) | Weekly maintenance sweep (default: Friday) |
| [`/hypothesize`](./hypothesize.md) | Generate or refresh hypotheses for a feature (pre-ship across the 5 risk areas, or post-ship from data) |
| [`/decide`](./decide.md) | Log a decision: draft the file from the evidence trail, surface for PM sign-off |
| [`/strategy-check`](./strategy-check.md) | Drift check between recent decisions / hypotheses / ingestion and `knowledge/strategy.md` |
| [`/ideate`](./ideate.md) | A problem needs solution directions grounded in existing evidence and hypotheses |
| [`/risk`](./risk.md) | A feature or plan needs the 5-area risk scan; maps to hypothesis hygiene |
| [`/plan`](./plan.md) | A new objective lands; turn it into discovery questions, interviews, experiments, hypotheses, decision points |

## Conventions

- Every command loads before acting and updates after. No blind drafting.
- Every command ends by surfacing 2-4 bullets per `CLAUDE.md § Operating loop § 7`.
- `/prep` is read-only at call time. The operator runs `/ingest` after the conversation. All other commands draft or update files per autonomy mode.
- Commands respect `CLAUDE.md § Operating preferences § Autonomy mode`. Under `propose and wait`, drafts are presented for approval before saving.
- All file paths in each spec are relative to the brain root.

## Scope: what these verbs are not

PM Brain is the memory and reasoning layer. PM workflows (JTBD interview structure, Kano analysis, RICE prioritization, opportunity solution trees, experiment design templates) belong in workflow-specific skills, not here. A workflow skill produces an artifact; PM Brain ingests it via `/ingest` and routes the evidence into durable layers. The split keeps each system thin.
