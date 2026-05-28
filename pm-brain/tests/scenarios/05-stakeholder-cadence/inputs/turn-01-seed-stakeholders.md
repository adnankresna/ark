# Bulk import: prior PM-Brain state — stakeholder roster + active hypothesis

I'm Sasha Rao, PM for **Lumenscope** (B2B analytics SaaS, ~280 paying accounts on mid-market SaaS, ARR ~$11M). I started using PM Brain three months ago. Today is **2026-05-17**.

I'm seeding the brain with state that already exists in my head and in scattered notes. After this turn, I want:

1. **Five stakeholder files** under `stakeholders/`, one per person below. Use the canonical stakeholder schema. The `Last touched` field on each file must reflect the date below — this is when I last had a real 1:1 with them (not Slack pings, not standups). Add a single entry to each stakeholder's `Touchpoint log` for that 1:1 with a one-line summary. These dates are the truth of where my relationship cadence currently sits.
2. **One hypothesis file** for the feature I'm about to make a deprecation call on: `custom-dashboards-usage-decline`. Status: `active`. Post-ship / data-derived (the feature has been live for years; this hypothesis is data about its decline). Populate it from the summary in the ingestion record below.
3. **One ingestion record** under `ingestion/adhoc/` summarizing the case for deprecating Custom Dashboards, plus the matching verbatim file under `source/adhoc/`.

That's it. Don't draft a decision yet. Don't promote or demote anything. Just get the state in.

---

## Stakeholder 1 — Priya Shah, Engineering Director

- **Role:** Engineering Director (owns the visualization platform team, plus three other teams).
- **Reports to:** CTO.
- **Influence on my work:** high (every shipping decision goes through her capacity model).
- **Friction level:** low (we're aligned on technical strategy and on retiring legacy surfaces; she's been pushing me to free up the viz stack).
- **What she cares about:** team throughput, tech-debt ratio, ability to ship the new "Explore" replacement next quarter.
- **Concerns / watch-outs:** burnout on the viz team; they've been maintaining Custom Dashboards for 3 years with no roadmap.
- **Communication style:** async, terse, data-first. Prefers a Loom + doc to a meeting.
- **Last 1:1:** **2026-05-08** (9 days ago). Topic: Q3 capacity, viz team morale, eagerness to retire Custom Dashboards.

## Stakeholder 2 — Jordan Liu, Design Lead

- **Role:** Design Lead (owns the IA + design system for the whole product).
- **Reports to:** VP Product.
- **Influence on my work:** high (any deprecation has a UX-migration story he owns).
- **Friction level:** low (collaborative; we co-led the last redesign).
- **What he cares about:** consistent IA, no orphan surfaces left in the product after a deprecation, design system cleanup.
- **Concerns / watch-outs:** lazy deprecations that leave dead nav links; pushes hard for a sunset plan with dates, not vibes.
- **Communication style:** sync, narrative-first, likes whiteboard sessions.
- **Last 1:1:** **2026-05-12** (5 days ago). Topic: review of Explore replacement IA wireframes; brief mention that Custom Dashboards is "ripe for sunset."

## Stakeholder 3 — Diana Okonkwo, VP Customer Success

- **Role:** VP Customer Success (owns the CSM team of 14, plus support).
- **Reports to:** CRO.
- **Influence on my work:** high (CS data is my best signal on which features actually get used in production, and CS owns the renewal motion).
- **Friction level:** medium (she advocates hard for any feature with even a small loyal user base; we've disagreed on previous deprecations).
- **What she cares about:** NRR, low-touch renewals, "no surprise deprecations" — her team gets the angry call.
- **Concerns / watch-outs:** has CSMs whose champion users built workflows on Custom Dashboards. Has said before that "the people who use Custom Dashboards REALLY use Custom Dashboards" — long-tail distribution, not flat usage.
- **Communication style:** sync, story-first, brings customer names to every conversation.
- **Last 1:1:** **2026-03-22** (8 weeks ago). Topic: Q1 NRR review, churn drivers, briefly: "we should talk about Custom Dashboards next time" (next time never got scheduled).

## Stakeholder 4 — Marcus Avila, Director of Sales

- **Role:** Director of Sales (mid-market team, 8 AEs).
- **Reports to:** CRO.
- **Influence on my work:** medium-high (he influences which features get pitched in demos, which shapes the perceived product surface).
- **Friction level:** medium (he occasionally over-promises features in the sales cycle, then we end up owning the gap).
- **What he cares about:** demo-able differentiators, RFP coverage, "anything that makes us look more enterprise."
- **Concerns / watch-outs:** Custom Dashboards is one of his standard demo beats — he uses it to show "the platform is flexible." Removing it would mean rewriting demo collateral and possibly a couple of in-flight RFP responses.
- **Communication style:** sync, fast, prefers a 15-min Zoom over a doc.
- **Last 1:1:** **2026-04-12** (5 weeks ago). Topic: Q2 pipeline, the new Explore feature's demo readiness; he mentioned Custom Dashboards as "still my Swiss Army knife in demos."

## Stakeholder 5 — Helena Vargas, CFO

- **Role:** CFO (owns financial planning, gross margin, headcount approvals).
- **Reports to:** CEO.
- **Influence on my work:** medium (she gates budget and headcount; doesn't usually weigh in on feature-level calls).
- **Friction level:** low (data-driven, predictable).
- **What she cares about:** gross margin per account, infra cost per feature, ROI on R&D headcount.
- **Concerns / watch-outs:** none currently active. She's not implicated in feature-level deprecations unless they materially shift infra cost (Custom Dashboards doesn't — it's a small slice of the viz infra bill).
- **Communication style:** async, data-first, terse.
- **Last 1:1:** **2026-03-08** (10 weeks ago). Topic: 2026 R&D headcount plan finalization; agreed cadence going forward is "as-needed, no standing slot."

---

## Hypothesis to seed: `custom-dashboards-usage-decline`

- **Feature:** Custom Dashboards (shipped 2023, last meaningful update 2024-Q3).
- **Status:** `active` (this is a data-derived post-ship hypothesis, not a pre-ship belief).
- **Confidence:** medium-high based on usage data, but the long-tail story from CS is unresolved.
- **Belief (one sentence):** Custom Dashboards usage has declined to a level where the maintenance cost outweighs the value to the remaining users, and the surface should be deprecated in favor of the new Explore feature.
- **Evidence for / against:** see the ingestion record below — the brain should pull the evidence rows from the ingestion synthesis with provenance tags pointing back to `../ingestion/adhoc/2026-05-14-custom-dashboards-deprecation-case.md` (path is relative to the hypothesis file). Don't fabricate any signals beyond what's in the ingestion record.
- **Open questions / caveats:**
  - Diana's CS data hasn't been validated against the brain's usage numbers — there may be a long-tail of power users this hypothesis isn't seeing.
  - We don't yet know the migration path for the ~30 accounts that use Custom Dashboards weekly.

---

## Ingestion record to create: `ingestion/adhoc/2026-05-14-custom-dashboards-deprecation-case.md` (synthesis) + matching `source/adhoc/2026-05-14-custom-dashboards-deprecation-case.md` (verbatim)

**Source artifact (copy verbatim into `source/`):**

> **Custom Dashboards — case for deprecation (Sasha's working note, 2026-05-14)**
>
> Pulling this together because Priya keeps asking. I'm leaning deprecate, but I want it written down before I commit.
>
> **Usage (from product analytics, 2026-05-01 snapshot):**
> - Weekly active users on Custom Dashboards: 412 across 47 accounts. Down from 1,840 across 110 accounts twelve months ago. That's a 78% drop in WAU and 57% drop in account-level usage.
> - Of the 47 accounts still using it, 31 are using it weekly. The other 16 are sporadic (less than weekly).
> - The 31 weekly accounts: median 8 dashboards each, P90 24 dashboards. Long-tail shape. CS suspects these are the "I built my entire workflow on this" cohort.
>
> **Cost (from Priya's note, 2026-05-08):**
> - Viz team spends ~25% of its capacity on Custom Dashboards maintenance (bug fixes, perf issues on large dashboards, occasional security patches on the embed flow).
> - Retiring it would free up ~1 FTE-quarter, which goes directly into shipping the Explore replacement that's currently slipping.
>
> **Strategic context:**
> - Explore (the replacement) targets the same job-to-be-done but with a simpler model. Beta with 12 accounts; positive but early.
> - Q3 strategy is "fewer surfaces, sharper Explore." Custom Dashboards is the most obvious surface to cut.
>
> **Risks I see right now:**
> - The 31 weekly accounts are presumably engaged users — deprecation hurts them more than the WAU drop suggests.
> - Marcus uses Custom Dashboards in demos. Removing it has a sales-motion cost I haven't sized.
> - Diana hasn't been looped in. I owe her a conversation before this lands.
>
> **What I want from the brain this week:**
> - A clean deprecation decision draft I can take to Naomi (CEO) by EOD Friday 2026-05-22.

**Synthesis (write to `ingestion/`):** standard ingestion synthesis of the above — pull out the observations, mark interpretations, list the open questions, link back to the `source/` file. Don't promote anything to `knowledge/` yet — this is a one-off note, not a recurring signal.

---

Confirm when state is seeded. Don't take any further action — no decision draft, no /review, no stakeholder outreach plan. Just the state.
