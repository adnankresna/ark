# Adnan's AI Brain — what it is, what it does

## One paragraph

I'm setting up a product memory system that lives in a git repo on my laptop. Every meeting note, customer call, Slack thread, stakeholder ask, and decision gets stored in plain markdown files with a tag saying where it came from and when. Claude reads the whole thing before answering anything, writes to it after, and sweeps it weekly for contradictions, drift, and forgotten follow-ups. It connects directly to Slack — I can pull any channel's messages without copy-pasting.

Nothing changes about how the team works. You keep using Slack, Notion, Jira. I ingest the signal after our meetings and calls. The brain cross-references it and catches things humans miss.

---

## What it does, mapped to our week

| Day | What happens | What the brain does |
|---|---|---|
| **Mon** — Sprint planning + product priorities | I ingest sprint decisions and priority changes | Brain checks: does this sprint align with the roadmap? Flags if not |
| **Tue** — Design cadence (what's needed, clarify constraints) | I ingest design notes, user testing findings | Brain links Alex's finding to Mark's pipeline data and Rafi's tech flag — connects signals across functions |
| **Wed** — Progress check (unblock, adjust scope) | I walk in with cross-referenced context | Brain surfaces: what changed since Monday, what contradicts what, what's still blocked |
| **Thu** — Design review + dev handoff | I ingest scope gaps, spec decisions | Brain catches: "these two features share the same spec debt" before it becomes a QA bug |
| **Fri** — Weekly sweep | I run `/review` | One page: what moved this week, what's drifting, what's stale, what to bring to Monday |

---

## Concrete examples

**"Didn't someone mention that before?"**
Mark flags document-upload friction in a broking pipeline review. Six weeks later, Alex sees the same drop-off in user testing. The brain connects them automatically — I don't have to remember the pipeline review. Two independent signals, one problem, surfaced together.

**"Why did we decide X?"**
Every decision is stored with: the evidence for it, the evidence against it, who was involved, and what would make us reverse it. When someone asks "why did we kill feature Y?" — one file, full reasoning chain, 30 seconds.

**"That request came in on Slack and I forgot"**
Mateus suggests a 1-week spike in a DM. I ingest it. It's now stored next to the customer evidence and design notes on the same problem. Findable in the next sprint planning, not buried in Slack history.

**"The roadmap says one thing but we're building something else"**
Brain cross-checks the Notion roadmap against Jira ticket history. If the stated strategy says "activation" but 80% of shipped tickets are "enterprise permissions" — it flags the gap on day one.

**"Miguel says we need to rebuild the landing page urgently"**
Brain puts the request next to the documented evidence: last time bounce spiked it was a UTM bug fixed in 2 days, not a redesign. Both tagged for what they are — one verbal claim vs. documented data. No argument, just context.

---

## How it affects you

**You don't need to do anything differently.** The brain is my tool. Here's what changes for you:

- **Meetings get sharper.** I walk in with evidence, not memory. Progress checks have data behind them.
- **Your input doesn't get lost.** Something you said in a standup, a design review, or a DM — if it matters, it's stored and findable.
- **Decisions are traceable.** No more "I think we discussed this in March somewhere."
- **New people ramp faster.** The brain is a browseable history of what we learned, decided, and why.

---

## What it can't do

- **Not a Slack bot.** It doesn't listen passively or respond automatically. I pull from Slack when I need to.
- **Not a team wiki.** One operator (me), one product. Not replacing Notion or Confluence.
- **Not autonomous.** It surfaces evidence and drafts recommendations. I make the decisions.
- **Not real-time.** Updates when I ingest something, not syncing live.
- **Not magic.** Quality depends on what I put in. Skip it for a month, it goes stale.

---

## Slack integration

Claude connects directly to our Slack workspace. I can:

- Search any channel for messages by date, keyword, or person
- Pull standup updates, async Friday reports, pipeline notes
- Ingest relevant messages into the brain with one command

No Slack bot installed. No bot presence in channels. Just me pulling what I need, when I need it.

---

## Where this could go next

These aren't commitments — just possibilities worth knowing about:

- **Passive Slack listener:** Tag @Adnan in Slack → AI processes the request automatically (store a summary in Notion, update a ticket, answer a question from the brain)
- **Team read access:** Brain repo on GitHub. Anyone can browse decisions, evidence trails, and stakeholder context
- **Cross-tool sync:** Connect Notion and Jira via MCP. Brain pulls from all tools, not just Slack

---

## Questions?

Grab me in Slack or in any of our regular cadences. Happy to walk through it live.
