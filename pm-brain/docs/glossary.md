# Glossary

Every term PM Brain uses, in plain English. If a word in the docs feels jargony, look it up here.

---

### Brain

A folder of markdown files in a git repo on your laptop. That's it. No database, no cloud, no embeddings. Your PM context written down so you and Claude can both read it.

### Ingest

To feed something (a transcript, a Slack thread, a doc, a quick note) into the brain so it's there for later. The skill copies the original under `source/`, writes a structured synthesis under `ingestion/`, and updates the durable areas (hypotheses, decisions, stakeholders) that the new signal touches.

You can ingest from a file (`/ingest transcript.md`), from a connected app (Notion, Jira, Slack via Claude's app connectors), or from a quick line in chat ("Capture that the eng lead pushed back on the Q3 scope in standup today").

### Provenance

Where a claim came from. Every load-bearing line in the brain wears a small tag that says how trustworthy it is and where to go to check it. Six forms, in rough order from strongest to weakest:

| Tag | Means |
|---|---|
| `[source/interviews/2026-05-19-northridge.md]` | A real artifact lives at that path. Go read it. |
| `[ingestion/interviews/...]` | A synthesis note exists; the original is one link away |
| `(stakeholder-verbal, rahul-pillai, 2026-05-20)` | Someone said this out loud or in a fast Slack message, no document behind it |
| `(intuition, PM, 2026-05-20)` | Your own hunch, captured honestly as a hunch |
| `(industry-knowledge)` | Generally known in the field, not from your specific product |
| `(chat, no artifact)` | Mentioned in chat with the agent, nothing else backs it |

The tag matters more than most people expect. A "we need dark mode" claim from one stakeholder verbal lands very differently than the same claim across 27 documented sales calls, even when both are technically "in the brain."

### Hypothesis

A statement about your product, users, or market that you're tracking the evidence for. It lives in `hypotheses/` and moves through statuses as the evidence accumulates or contradicts it.

Statuses, in order:

- **`candidate`**: fresh, just opened, may have one observation
- **`proposed`**: has two or three independent observations
- **`validated`**: enough evidence to act on
- **`demoted`**: evidence contradicts it; kept for the record, not for planning
- **`archived`**: resolved or stale, moved out of active rotation

### Decision file

A record under `decisions/` of a real call you made: what you decided, what evidence you had, what alternatives you considered, and the **reversal condition** (see below). Decisions are append-only in spirit: you don't quietly rewrite history when something changes; you add a new entry that links back.

### Reversal condition

The named, specific thing that would make you reopen a decision. "If three confirmed-lost deals cite enforced SSO as the primary blocker, reopen this." Not a vague "if circumstances change." Without a reversal condition, decisions either get reopened constantly on whim or get treated as immutable when they shouldn't be.

### Watch item

A signal that's interesting but doesn't (yet) clear the bar for action. The skill captures it, files it against the relevant decision or hypothesis, and lets you check on it during `/review`. The CEO saying "we might need to revisit SSO" in a 1:1, when the documented decision is to defer SSO, is a watch item.

### Audit trail

The path from any claim in the brain back to the original artifact. Click a link in a synthesis note, you get to the source. Click the source citation in a decision, you get to the interview. This is what makes the brain useful six months later: not just *what* you decided, but *what you knew at the time*.

### Contradiction

Two pieces of evidence in the brain that point opposite directions. The skill surfaces contradictions automatically. It doesn't resolve them. Resolution is a judgment call you make, often by going back to talk to the source or gathering new evidence.

### Drift

A hypothesis that's been on the books for a while and hasn't gained or lost evidence. `/review` flags drifting hypotheses so you can decide: revive, demote, or archive.

### `source/`

The folder where the original artifact lives, untouched. A transcript, a meeting note, a screenshot, a Slack export. Audit anchor. Never edited.

### `ingestion/`

The folder where the synthesis of an artifact lives: what the agent extracted, who said what, dates, links back to the source. Edited when something gets re-read with new context.

### `knowledge/`

The folder of durable area files: strategy, product, users, market, org. Stable picture of what you know. Updated more slowly than ingestion notes, because durable knowledge moves slower than fresh signals.

### `hypotheses/`

One file per open hypothesis. Status field, evidence rows, links to source.

### `decisions/`

One file per real decision. Decision, evidence cited, alternatives, reversal condition.

### `stakeholders/`

One file per person you work with regularly. Asks they've made, concerns they've raised, last touchpoint, communication preferences.

### The six commands

| Command | What it does |
|---|---|
| `/ingest <thing>` | Feed an artifact into the brain (file, paste, app export) |
| `/prep <stakeholder>` | One-page brief before a meeting: open asks, last unresolved concern |
| `/review` | Weekly maintenance sweep: what changed, what's drifting, what's next |
| `/ideate <problem>` | Synthesis pass: load strategy + insights + hypotheses, surface 3–7 directions |
| `/risk <feature>` | Five-area risk scan with stub hypotheses for uncovered areas |
| `/plan <objective>` | Six-block draft plan: what we know, assumption vs evidence, who to interview, hypotheses to open, experiments, decision points |

### Evidence hierarchy

The implicit ordering the skill uses when two pieces of evidence disagree:

> documented decision  >  documented research  >  documented stakeholder claim  >  verbal stakeholder claim  >  PM intuition

This isn't a rigid rule. It's a default. When something further down the list contradicts something further up, the brain surfaces both and tags the gap. You decide what to do with it.

### Migration mode

The mode the skill enters when you run `/pm-brain` in a directory with existing PM artifacts (a Notion export, a folder of meeting notes, a Jira CSV). It interviews you briefly about company / role / priorities, then reads what's there and produces an initial brain plus a short report on what it found, what it couldn't make sense of, and what questions you should answer this week.

### Greenfield mode

The mode the skill enters when you run `/pm-brain` in an empty directory. Same brief interview, scaffold goes in, you start fresh.

### Self-test

A short check the skill runs right after it scaffolds a new brain: a make-believe ingestion that exercises the read path, the write path, and the provenance tagging. If something's wrong with your install, you catch it in the first minute, not the first month.

---

If something else needs a definition, [open an issue](https://github.com/phuryn/pm-brain/issues). The glossary is meant to be exhaustive, and a missing term is a doc bug.
