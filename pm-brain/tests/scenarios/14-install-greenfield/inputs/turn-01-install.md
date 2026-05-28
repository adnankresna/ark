Set up a PM Brain in this directory. Today's date is 2026-05-18.

**How to run the install:** The PM Brain skill is available at `.claude/skills/pm-brain/SKILL.md`. Load it and follow its workflow. (Equivalent to a user running `/pm-brain`.)

**About this working directory:** Treat it as **greenfield mode** — the only thing present is the `.claude/skills/pm-brain/` config (which mode detection explicitly ignores). There are no PM artifacts to migrate.

**Interview answers — already provided.** I'm answering all five batches inline so you don't have to ask. Use them verbatim. Do not ask follow-up clarifying questions; the answers below are complete.

## Batch A — Context

1. **Company / product:** Telemetron, an observability product for backend engineering teams. We sit between APM and log search — opinionated dashboards that auto-cluster anomalies across services.
2. **Stage / scale:** Post-seed, pre-Series-A. ~$400k ARR, 38 paying teams, 6 engineers + me (PM/founder).
3. **My role:** Sole PM. I own everything customer-facing and the roadmap. Eng is independent on infra.
4. **Top 3 priorities next 1-2 quarters:**
   - Reach $1M ARR by end of Q3 (north-star)
   - Land 3 lighthouse customers in DevTools or developer-platform companies (logo strategy)
   - Cut median time-to-first-insight from 9 min to under 3 min (activation metric)

## Batch B — People

1. **Stakeholders (top 8):**
   - **Naveen Rao** — CEO/co-founder. Final call on funding-related decisions.
   - **Cara Lin** — Co-founder, eng lead. Owns the technical architecture.
   - **Henrik Pauls** — Series A lead investor (Bowline Ventures), monthly check-in.
   - **Marcus Webb** — Head of Eng at Brillstone (paying customer, biggest logo).
   - **Priya Shah** — Senior PM at Cascadia Health (paying customer, design partner).
   - **Devon Park** — Eng lead on Telemetron's anomaly-detection service.
   - **Riya Bhattacharya** — Customer success lead (just hired, ramping).
   - **Tom Okonkwo** — Champion at Northbridge Logistics (prospect, ~$80k ACV pending).

2. **Highest-friction or highest-leverage right now:**
   - Naveen (leverage — funding decision in 6 weeks)
   - Marcus (friction — escalating about cluster-collapse bug for 2 weeks)
   - Henrik (leverage — quarterly check-in next week)

3. **Cadence:**
   - Weekly 1:1 with Naveen (Mondays)
   - Bi-weekly 1:1 with Cara (Wednesdays)
   - Monthly call with Henrik (first Tuesday)
   - Quarterly customer advisory board (next: late June)

## Batch C — Work in flight

1. **Active features (3):**
   - `anomaly-clustering` — the core differentiator, in production but quality is uneven
   - `slack-alerts` — shipped Mar 2026, currently measuring adoption (62% of teams enabled)
   - `query-builder` — beta, 8 customers using; deciding whether to GA in June

2. **Next big bet (scoped, not started):**
   - `runbook-suggestions` — when an anomaly fires, propose a runbook based on past incidents. Q3 target.

3. **Recently shipped, still measuring:**
   - `slack-alerts` (above)

## Batch D — Inputs

1. **Weekly data sources:**
   - PostHog (product analytics)
   - Linear (eng tickets, roadmap)
   - Intercom (support tickets + customer chats)
   - Stripe (revenue, expansion)
   - Slack #customer-feedback channel
   - Notion (interview transcripts live here today)

2. **Customer interviews:** 2-3 per week. Transcripts in Notion under `Customer Calls/2026/`.

3. **Market signals:** Datadog and Honeycomb release notes, the Observability Engineering subreddit, Honeycomb's o11y newsletter, and the SREcon proceedings.

## Batch E — Operating preferences

1. **Autonomy:** Act and tell.
2. **Maintenance cadence:** Weekly /review on Fridays + on-demand sweeps.
3. **Off-limits beyond defaults:** Nothing additional — defaults are fine. (No customer PII; no internal HR; no compensation data.)

---

**Critical instructions:**

- Run the install end-to-end in this single turn. Do not ask me follow-up questions; the answers above are complete.
- Detect greenfield mode, copy the scaffold (including the hidden `.claude/` directory with the hook and settings), populate placeholders from the answers above, run the self-test, and produce the hand-off.
- For the self-test, walk every internal link in the populated files and report broken ones.
- For the hand-off, lead with the three habit actions (ingest today / prep next 1:1 / `/review` Friday) with specific slugs and days based on the answers above.

Go.
