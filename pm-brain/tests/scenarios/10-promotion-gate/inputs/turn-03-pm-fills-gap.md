# Filling the gaps you flagged — feasibility memo + business case

You flagged two specific gaps last turn: (a) the feasibility concern from Sam was uninvestigated, and (b) there's no business-viability evidence at all. I've now got artifacts for both. Please ingest them and update the hypothesis file's Feasibility and Viability sections with new evidence rows.

After ingesting, tell me where things stand now — are we closer to a promotable state? You don't need to re-walk all 5 risk areas in full; focus on what changed.

---

## Artifact A — Engineering feasibility memo, 2026-05-12

**Author:** Sam Whitford, Eng Tech Lead, BrightSched.
**Re:** Same-day rebooking flow — refactor scope estimate
**Date:** 2026-05-12 (delivered to Casey 2026-05-13)

I scoped this. Summary:

**Scope.** Three sprints (6 weeks) of focused work for two engineers. Breakdown:
- Sprint 1: Calendar subsystem refactor — replace the current pessimistic-lock model with optimistic locking + slot version tokens. This is the load-bearing piece. Has good test coverage already (78% line coverage on the calendar module), so the refactor is mechanical, not exploratory.
- Sprint 2: Waitlist data model + queue management API + opt-in granularity per patient (addressing Maria's notification-fatigue concern from her April interview).
- Sprint 3: Push notification pipeline + front-desk one-click refill UI + integration tests + soft launch to 5 design-partner accounts.

**Risk areas I'm tracking, but consider manageable:**
- The calendar refactor *will* touch the appointment-confirmation flow. We have integration tests but real-world edge cases (concurrent edits across timezones, recurring appointments getting split) may surface. Budget: ~3 days of post-launch firefighting baked into Sprint 3.
- Push notification deliverability on iOS — we depend on APNs. Standard infra, but if Apple changes provider auth policy (as they did in 2024) we're exposed.

**What I'm no longer worried about:** The "shim it on top and regret it" path I warned about in April. With the refactor scoped properly, we're doing it right. I'm confident in this estimate within ±1 sprint.

**Recommendation from eng:** Proceed. The refactor is overdue independent of this feature — the calendar code's brittleness is going to bite us within two quarters on something else if not this. Doing it now means we get the refactor AND the feature for the price of the feature.

---

## Artifact B — Business case analysis, 2026-05-15

**Author:** Casey Ito (PM), with input from Priya Vasquez (Finance Analyst).
**Re:** Same-day rebooking flow — retention and revenue model
**Date:** 2026-05-15

**Method.** I pulled the last 4 quarters of churn data from Salesforce, segmented by account size (number of providers) and tagged churn reasons from CS's exit interviews. I asked Priya to sanity-check the retention math.

**Findings.**

1. **Retention lift, modeled.** Mid-market accounts (3-10 providers, ~62% of our ARR) churn at 11.4% annualized. CS exit-interview data tags "manual workflow burden" as a contributing reason in 38% of those churns. If even one-third of those marginal churners would stay given a credible refill workflow, that's roughly a **+2.1pp retention lift** on the mid-market segment — equivalent to ~$420k/year in retained ARR by year 2 (the lift compounds because retained accounts also expand).

2. **Direct revenue, customer-side.** Using Westside's numbers as a ceiling and Bayfront's as a floor, a typical mid-market account recovers $1,800-$4,200/month in chair-hour revenue with a working refill flow. We don't capture that directly, but it materially strengthens the WTP signal — customers can rationally pay us 10-20% more for a feature that returns 5-10x our subscription fee in recovered revenue.

3. **Pricing.** Two options. (a) Bundle into existing Pro tier (~no immediate ARR lift but supports retention thesis). (b) Add as $80/seat/month upsell — at conservative 30% attach across mid-market, that's ~$520k/year incremental ARR. Recommend (b) for new sales, (a) grandfathered for existing Pro customers (avoid the "they're charging us for something we already had to ask for" backlash).

4. **Cost.** Per Sam's memo: 3 sprints × 2 engineers ≈ $180k fully loaded. Breakeven at ~Q2 of year 2 under model (b), faster under retention math alone.

**Priya's sign-off note (verbal, 2026-05-15):** "Numbers are conservative. The retention math is the load-bearing piece — if the +2.1pp lift holds, this is a no-brainer. I'd want to revisit after 2 quarters of post-launch data to recalibrate, but the case to ship is solid."

**Confidence:** Medium-high on the cost number, medium on the retention lift (the 38% churn-reason tag is an interpretation, not a verified causal link), medium on the pricing attach rate.

---

## What I want from you on this turn

1. Preserve both artifacts under `source/` with their actual dates (2026-05-12 for the feasibility memo, 2026-05-15 for the business case). The feasibility memo is an `adhoc` or `meetings` kind (eng deliverable, not a customer interview). The business case is `adhoc` (internal PM analysis).
2. Create matching `ingestion/` synthesis records for both — these are load-bearing artifacts that will inform a promotion decision, they earn the synthesis treatment.
3. Update `hypotheses/same-day-rebooking-flow.md`:
   - Add new evidence rows under **Feasibility risk** citing the feasibility memo (path-typed link to the ingestion record).
   - Add new evidence rows under **Viability risk** citing the business case (path-typed link to the ingestion record). Note Priya's verbal sign-off as a separate `(stakeholder-verbal, Priya Vasquez, 2026-05-15)` row.
   - Update the `Last updated:` field to 2026-05-17.
   - DO NOT change the `status:` field. Still `proposed`. The promotion question itself is the next turn.
   - Preserve all existing evidence rows. The April evidence and the May evidence sit side by side.
4. In your response, tell me: which risk areas now have evidence vs. which don't, and whether your read on promotability has changed.
