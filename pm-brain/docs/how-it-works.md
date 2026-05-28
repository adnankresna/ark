# How PM Brain works

A worked example, end to end. One real-shaped customer interview, six files touched, one audit trail.

## The setup

You're the PM for a B2B SaaS compliance tool. Mid-market. Six active features. You've just finished a 45-minute interview with the Ops Lead at Acme Corp.

You drop the transcript into your working directory and run `/ingest`.

## What the agent does, step by step

### Step 1: Detect shape

The agent reads the artifact. Sees: speaker labels, customer name, length, question/answer structure. Classifies it as `interview`. Routes to `ingestion/interviews/`.

### Step 2: Copy the source

```
source/interviews/2026-04-22-acme-ops-lead.md
```

Immutable. Read-only from this point on. The original stays in your Drive. This copy is the audit anchor.

### Step 3: Tag observations

The agent creates the working-memory record:

```
ingestion/interviews/2026-04-22-acme.md
```

Inside, observations tagged with their epistemic type:

- **observation**: direct quote, factual claim from the interviewee
- **interpretation**: agent's framing of what the observation means
- **hypothesis**: testable belief generated from the conversation
- **assumption**: implicit claim the interview didn't validate

Example entry:

```markdown
- **observation**: "We batch our SOC2 evidence collection on Fridays. Daily would
  break our workflow." - Ops Lead, 2026-04-22, transcript line 47
- **interpretation**: Mid-market ops leads appear to prefer weekly batch over
  real-time for compliance work. Third independent observation of this pattern
  (see also: 2026-03-15 Stripe interview, 2026-04-08 Notion interview).
- **hypothesis** (proposed): H2. Real-time alerts have negative value for the
  ops-lead persona below team size N.
```

Provenance stays explicit. The interpretation links to the observation. The hypothesis links to the interpretation.

### Step 4: Propagate to durable layer (in parallel)

The same ingestion updates four durable destinations:

**1. `knowledge/users/insights.md`**: promotes a new insight:
> *"Ops leads in mid-market batch their compliance reviews weekly, not daily."*
> Confidence: high (3 independent observations). Promoted 2026-04-22 from
> ingestion/interviews/2026-04-22-acme.md (with cross-links to 2026-03-15 and 2026-04-08).

Promotion threshold met: 3 independent observations of the same pattern, all from the same persona.

**2. `hypotheses/weekly-digest.md § Evidence`**: strengthens H2 (value-risk):

```markdown
## H2. Value risk: real-time alerts may have negative value for ops leads

**Evidence for:** (was 0.4) → 0.7
- 2026-04-22 Acme Ops Lead: "Daily would break our workflow."  [ingestion/interviews/2026-04-22-acme.md](../ingestion/interviews/2026-04-22-acme.md)
- 2026-04-08 Notion Ops: "We don't want more interruptions."  [ingestion/interviews/2026-04-08-notion.md](../ingestion/interviews/2026-04-08-notion.md)
- 2026-03-15 Stripe Compliance: "Batch is how we operate."  [ingestion/interviews/2026-03-15-stripe.md](../ingestion/interviews/2026-03-15-stripe.md)

**Decision trigger:** if confidence > 0.8 across 5+ independent observations,
draft decision to defer real-time alerts.
```

Each evidence row carries a provenance tag from the canonical enum. Most here are path-typed (`[ingestion/...]`). The link walks to the synthesis record, which itself links to the raw `source/` transcript. The vocabulary also allows non-path tags like `(stakeholder-verbal, <name>, <date>)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, and `(chat, no artifact)` for claims that legitimately exist without an artifact behind them. See `hypotheses/_SCHEMA.md` for the full enum.

Confidence raised. Decision trigger documented but not fired yet.

**3. `stakeholders/acme-ops.md § Touchpoints`**: logs the conversation:

```markdown
## Touchpoints

- 2026-04-22: 45-min customer interview. New concern: SOC2 evidence cadence.
  Last touched: 2026-04-22. Next nudge: 2026-06-22.
  [ingestion](../ingestion/interviews/2026-04-22-acme.md)
```

The "Last touched" date drives the stakeholder cadence check in the weekly sweep.

**4. `decisions/2026-04-25-defer-realtime-alerts.md`**: drafted as `pending`:

```markdown
# Defer real-time alerts

**Status:** pending (drafted by agent, awaiting PM confirmation)
**Date:** 2026-04-25
**Driver:** H2 confidence raised to 0.7. Pattern recurring across 3 mid-market
ops interviews.

**What we're deciding:** ship weekly batch alerts only for v1. Defer real-time
to v2 pending evidence from larger team sizes.

**What would reverse this:** if 2+ enterprise customers (team size > 50)
explicitly request real-time and demonstrate intent-to-buy contingent on it.

**Evidence trail:**
- [hypothesis H2](../hypotheses/weekly-digest.md#h2)
- [insight: weekly batch pattern](../knowledge/users/insights.md)
- 3 supporting interviews (linked from H2)
```

The agent does not mark the decision as `decided`. It surfaces the draft for the PM's confirmation.

### Step 5: Close the loop

The agent reports back in 2-4 bullets:

> Resolved: 1 source copied, 1 ingestion record created, 1 insight promoted, 1 hypothesis strengthened (0.4 → 0.7), 1 stakeholder touchpoint logged.
>
> Drafted for your confirmation: `decisions/2026-04-25-defer-realtime-alerts.md`. Confidence on H2 crossed 0.7, decision trigger conditions are 80% met. Want me to mark this `decided`?
>
> Surfaced: H4 (feasibility risk on the alert pipeline) still has no evidence in 30+ days. Worth a feasibility check before deferring.
>
> Next time you `/prep acme-ops`, I'll surface the SOC2 cadence concern.

No dangling ambiguity. Every task ends with explicit closure.

## What this gets you

Three months later, your CTO asks: "Why did we kill real-time alerts?"

You open `decisions/2026-04-25-defer-realtime-alerts.md`. Every evidence row carries a provenance tag. Most are path-typed `[ingestion/...]` links to interview synthesis records, which themselves link to the raw `source/` transcripts. A few rows are tagged `(stakeholder-verbal, ...)` or `(intuition, PM, ...)`. They're legitimate inputs, just ones that never had an artifact behind them, and they wear that fact. The full reasoning chain on the path-typed rows is two clicks deep.

That's the audit trail. The vocabulary is what keeps it honest when real PM work is messy.

## The six verbs, briefly

`/ingest` is the workhorse. The other five operate on the durable layer:

- **`/prep <stakeholder>`**: read-only at call time. Surfaces open asks, last unresolved concern, suggested questions. After the meeting, `/ingest` the notes.
- **`/review`**: weekly maintenance sweep. Six checks. Edits where confidence is high; drafts where not.
- **`/ideate <problem>`**: loads strategy + insights + hypotheses + recent decisions, surfaces 3-7 solution directions tagged with evidence.
- **`/risk <feature>`**: 5-area risk scan. Drafts hypothesis stubs for any uncovered risk area.
- **`/plan <objective>`**: drafts a six-block plan: what we know, assumption vs evidence, who to interview, hypotheses to open, experiments, decision points.

## The maintenance sweep

Memory systems fail at month three because nothing sweeps. The weekly sweep is the most important operation in the system.

Six checks, dated report in `maintenance/log/`:

1. **Stale knowledge**: files not updated in 6+ weeks. Still true? Archive?
2. **Stale evidence**: market intel past 30-60 days, interviews past 90, stakeholder assumptions past 30, strategy assumptions past quarterly. Flags. Doesn't auto-decay.
3. **Hypothesis hygiene**: actives with no evidence in 30+ days; promoteds without decisions; decisions whose reversal condition triggered; pending decisions older than 14 days with blocker impact.
4. **Stakeholder cadence + strategy tensions**: high-influence stakeholders not touched in 3+ weeks; recent decisions diverging from strategy.
5. **Knowledge synthesis (compression)**: the highest-leverage step. Identifies recurring patterns AND recurring contradictions. Preserves minority signals. Compression is additive, never destructive.
6. **Archival sweep**: shipped features inactive 90+ days; resolved hypotheses; closed asks. Before archiving anything, extracts durable lessons.

20 minutes Friday afternoon. Skip it for a month and the system rots.

## What the system is not good at

- **Not fully autonomous PM.** Supports judgment. Doesn't replace it.
- **Not enterprise knowledge management.** One operator, one product.
- **Not maximum information capture.** Deliberately throws things out.
- **Stakeholder files feel awkward at first.** Writing down what your manager cares about can feel like treating people as objects. The reframe: this isn't about them, it's about your continuity. You forget. The file remembers.
- **The ad-hoc inbox tempts laziness.** Every ad-hoc item gets resolved in the same session. The folder is a sorting bench, not a backlog.

See [`docs/architecture.md`](./architecture.md) for the why behind the structural choices, and [`docs/testing.md`](./testing.md) for how we verify these dynamics with synthetic scenarios.
