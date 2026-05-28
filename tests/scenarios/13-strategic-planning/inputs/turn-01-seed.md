# Bulk seed — strategic-planning scenario

Riley here. I'm seeding context for the four planning verbs we're going to exercise next. Process each block, preserve source where applicable, route to durable areas, update INDEXes. Today is **2026-05-17**.

---

## Block 1 — strategy.md

Populate `knowledge/strategy.md` (replace whatever placeholder content is there, but keep the schema sections). Use these values:

**North-star metric:** Weekly active research-customer count (researchers logging in 3+ days/week).

**Priorities (Q3 2026, in rank order):**

1. **Deepen the research-segment workflow fit** — every roadmap bet must demonstrably reduce friction for hydrologists, climate scientists, or watershed analysts.
2. **Protect dashboard reliability** — keep the morning-refresh SLA at >98% for our top 3 enterprise customers.
3. **Avoid surface-area expansion** — no new feature areas this quarter; deepen the existing three (Regional Climate Dashboard, Anomaly Detection, Sensor Health).

**Non-goals (this quarter — explicit, hard NO):**

1. **No mobile UI** — desktop-only stays this quarter. Researchers do not work on mobile.
2. **No new pricing tiers or upcharges** — pricing is frozen through Q3 to protect the research-segment-deepening priority.

**Current tensions:**

1. "Watershed-level granularity vs. data-pipeline reliability" — opened 2026-05-10 — a recurring customer ask for watershed-level views conflicts with our basin-level ETL's growing fragility (eng debt). Triggering evidence: 3+ customer interviews mentioning watershed friction; one engineering memo flagging that adding sub-basin aggregation on the current pipeline raises outage probability.

---

## Block 2 — A prior decision

Create `decisions/2026-04-30-defer-mobile-ui.md`:

- **Status:** `decided`
- **Date:** 2026-04-30
- **Decision:** Defer all mobile-UI investment through end of Q3 2026.
- **Context:** Quarterly planning surfaced repeated mobile-UI requests from the sales team. Strategic review confirmed researchers (our north-star segment) do not work on mobile — confirmed via interviews logged Jan-Apr 2026.
- **Evidence:**
  - `(stakeholder-verbal, Carlos Rivera, 2026-04-22)` — head of CS confirmed mobile asks come from sales prospects, not from existing research customers.
  - `(industry-knowledge)` — desktop-first analytics workflows are standard in research segments.
- **Explicitly NOT doing:** Mobile UI design work, mobile responsive CSS rebuild, mobile-specific feature parity.
  - `(stakeholder-verbal, Carlos Rivera, 2026-04-22)`
- **Stakeholders signed off:** Carlos Rivera (CS), Jordan Liu (Eng).
- **Reversal condition:** Reverse this decision if (a) >20% of active research-segment users log in from mobile in any 4-week window, OR (b) a top-3 enterprise customer makes mobile a renewal condition.
- **Remaining ambiguities:** None at decision time.

Add the row to `decisions/INDEX.md` under Recently decided.

---

## Block 3 — Two active hypotheses

Create `hypotheses/watershed-level-view.md`:

- Status: `active`
- Confidence: `medium`
- Belief: "Research-segment customers will adopt TerraDash more deeply (3+ logins/week) if we ship a watershed-level dashboard view."
- Origin: data-derived from 3 customer interviews + 1 competitor signal.
- Evidence for:
  - The Cascadia Watershed Institute (Mira Patel) interview, 2026-05-14 — `(stakeholder-verbal, Mira Patel, 2026-05-14)` — recurring "watershed-level granularity" pain.
  - The Stanford (Anand Iyer) public comment on Aurelia's blog, 2026-05-16 — `(industry-knowledge)` — current TerraDash customer publicly noting the gap.
- Evidence against: _(none yet)_
- Open questions: Will the data-pipeline reliability risk (tension 1) gate it? What's the design for HUC-12 selection UI?
- Test plan: Interview 5 more research-segment customers in next 4 weeks; ship a non-production prototype to 2 willing customers.
- Decision trigger: Promote if 5/5 additional interviews confirm + eng signs off on pipeline plan.

Create `hypotheses/admin-billing-portal.md`:

- Status: `active`
- Confidence: `low`
- Belief: "Mid-market customers want a self-serve admin portal to manage seats and billing without contacting CS."
- Origin: proactive (PM intuition + a couple sales-team requests).
- Evidence for:
  - `(intuition, Riley Chen, 2026-05-08)` — sales has flagged this 2-3 times; no customer interview backing yet.
- Evidence against: _(none yet)_
- Open questions: Does this serve the research segment at all? (Most research customers are enterprise-billed.)
- Test plan: TBD.
- Decision trigger: TBD.

Update `hypotheses/INDEX.md` accordingly.

---

## Block 4 — One ingestion artifact

Drop a customer interview at `source/interviews/2026-05-14-mira-patel-cascadia.md` (verbatim) + route synthesis to `ingestion/interviews/2026-05-14-mira-patel-cascadia.md`. Transcript:

> **Riley:** Walk me through how you used TerraDash this past month.
>
> **Mira (Senior Hydrologist, Cascadia Watershed Institute):** Regional climate dashboard mostly. Pulling anomaly readings. But I keep having to export and re-cut by watershed — there's no view that matches how hydrologists actually work. It's like having a city-level map when you need neighborhoods.
>
> **Riley:** Anyone else hitting this?
>
> **Mira:** All four of us on the team. Two have stopped using TerraDash for this work. I'd push to expand seats at renewal if we had watershed views.

In the synthesis, route the recurring theme to `knowledge/users/insights.md` under "Active themes" (with provenance back to the source file) — this is the third customer in 6 weeks raising the watershed friction. Update accordingly.

---

## Block 5 — The feature folder we'll exercise /risk on

Create `knowledge/product/features/weekly-snapshot.md`:

- **Feature:** Weekly Snapshot — a Friday-morning auto-generated PDF summary of the past week's anomaly readings for each customer's primary dashboard.
- **Status:** In design.
- **Owner:** Riley Chen.
- **Brief:** Send-on-Friday digest summarizing weekly anomalies, top-3 deltas vs the prior week, and any sensor health flags.
- **Linked hypotheses:** None yet (this is what /risk should expose — value coverage is implied by recurring customer ask in adjacent interviews, but feasibility/viability are completely untested).
- **Open questions:** Email-delivery rate? PDF generation cost at scale? Does it pull from the same fragile ETL job?
