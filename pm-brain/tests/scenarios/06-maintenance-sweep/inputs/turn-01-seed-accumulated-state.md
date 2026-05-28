# Bulk import: ~6 months of accumulated PM Brain state

I'm Maya Chen, PM for **PulseFit** — a consumer fitness app (iOS + Android, ~180k MAU, freemium with a $9.99/mo premium tier called *PulseFit Plus*). I started using PM Brain six months ago, in November 2025. Today is **2026-05-17**.

Below are the artifacts that represent ~6 months of accumulation. I want them ingested faithfully — preserve every date as written so we know how old each piece is. **Don't synthesize beyond what's in the artifacts.** Don't auto-demote anything, don't auto-archive anything. Just ingest the state. We'll do maintenance work in later turns.

The artifacts:

1. **Three ingestion records about the same Q1 churn-spike event** (a Slack thread, a CS email summary, and an analytics export — all dated within 8 days of each other in February, all triangulating the same observation: ~22% week-2 churn jump tied to the Apple Watch sync release on 2026-02-04).
2. **One feature hypothesis** (`weekly-email-summary`) promoted on 2026-02-20 based on early signals, then quietly contradicted by an A/B test concluded on 2026-03-28. The hypothesis file is still marked `status: promoted` — nobody updated it after the A/B test.
3. **One knowledge file** (`knowledge/product/onboarding-funnel.md`) last touched 2025-11-22, describing the original 7-step onboarding flow. The onboarding was redesigned to a 4-step flow in December (decision file 2025-12-18 — also include that) and the knowledge file was never updated.
4. **One stakeholder file** for `jordan-pm.md` (Jordan Reyes, peer PM who owned the Marketplace surface). Jordan left PulseFit on 2026-03-15 to join a competitor. The file still describes them as "current."

Tag everything with the dates as written. Create the hypothesis file with `status: promoted` (it WAS promoted in February — preserve that historical fact, even though we'll later notice it's stale). Create the decision file for the December onboarding redesign. Don't link the redesign decision back into the onboarding-funnel knowledge file — that's part of the staleness we want to surface later.

---

## Artifact 1 — Slack thread, #cx-signal channel, 2026-02-09

**Posted by:** Devi Suresh (CS Lead)
**Channel:** #cx-signal
**Thread date:** 2026-02-09, 10:14 AM PT

> **Devi Suresh** (10:14 AM)
> Heads up team — we're seeing a real week-2 retention dip on the cohort that joined right after the Apple Watch sync launch (2026-02-04). Normally week-2 retention sits at ~58% for new free users. This cohort is at ~36%. That's not noise.
>
> **Marco Liang** (CS, 10:18 AM)
> I've been getting tickets specifically about the watch sync — people saying their workouts aren't appearing on the phone after they finish on the watch. About 40 tickets in 4 days. Way above baseline.
>
> **Devi Suresh** (10:20 AM)
> Yeah. Conjecture: people who specifically came in for watch sync, hit the bug, churn faster than people who came in for other reasons. Maya, want me to pull a cleaner cut?
>
> **Maya Chen** (PM, 10:22 AM)
> Yes please — segment by "enabled Apple Watch sync in onboarding" vs "didn't." If the dip is concentrated in the watch-sync segment that's strong signal.
>
> **Marco Liang** (10:31 AM)
> One more pattern: ~half the tickets mention that they tried the sync, it failed, they uninstalled within 2 days. Not a slow churn — an angry churn.

---

## Artifact 2 — Email from CS to product, 2026-02-12

**From:** Devi Suresh <devi@pulsefit.app>
**To:** Maya Chen, Aarav Joshi (Eng Director)
**Subject:** Watch-sync churn signal — fuller cut
**Date:** 2026-02-12

Maya, Aarav —

Following up on Monday's Slack thread. I pulled the cleaner cut.

**The pattern, in numbers:**
- New free users who enabled Apple Watch sync in onboarding (week of 2026-02-04 through 2026-02-11): 4,210 users.
- Their week-2 retention: 34%.
- New free users in the same week who did NOT enable watch sync: 11,580 users.
- Their week-2 retention: 56% (consistent with the 58% baseline, basically unchanged).
- So the dip is **fully concentrated in the watch-sync-enabled cohort**. Non-watch users are fine.

**Ticket pattern (Feb 4 – Feb 11):**
- 84 tickets mentioning watch-sync failure (workout completes on watch, doesn't sync to phone).
- 31 of those 84 users had already uninstalled by the time CS responded.
- Median time-from-ticket-to-uninstall: 1.8 days.

**Recommendation:**
This is bug-driven angry-churn, not a value-prop problem. Eng needs to fix the sync reliability before we promote watch sync as a flagship feature. Suggest we pull watch sync out of the onboarding flow until it's stable.

Looping Aarav for eng triage.

— Devi

---

## Artifact 3 — Analytics export note, 2026-02-12

**Author:** Maya Chen (PM)
**Format:** Personal notes from Amplitude export, retrieved 2026-02-12 4:30 PM PT.
**Re:** Q1 churn-spike — watch-sync cohort analysis

Pulled Amplitude on the cohort Devi flagged. Confirms her numbers and adds two things.

**Confirms:**
- Watch-sync-enabled cohort (week of 2026-02-04): 4,210 users, week-2 retention 34.2%. Matches Devi's 34%.
- Non-watch cohort same week: 11,580 users, week-2 retention 56.1%. Matches Devi's 56%.
- The 22-point gap is the largest single-feature cohort gap we've seen in the last 12 months.

**Adds:**
- **Time-to-churn within watch-sync cohort:** median 3.1 days. The histogram has a sharp spike at day 2-3 (matches Devi's "uninstall within 2 days" anecdote). Not a gradual fade — a cliff.
- **Funnel cut:** of the 4,210 watch-sync-enabled users, 2,847 (68%) triggered at least one "sync_attempt_failed" event before churning. The 32% who DIDN'T trigger that event had week-2 retention of 51% (still below baseline but not catastrophic). So the bug exposure is the mechanism, not just enabling watch sync as a categorical signal.

**Conclusion:** Same event Devi described. Same conclusion as her email. Same recommendation: pull watch sync from the default onboarding until eng stabilizes the sync, or churn keeps bleeding.

(These three artifacts — Devi's Slack post, Devi's email, my Amplitude pull — are all about the same Q1 churn-spike event. They were captured separately because the signal came in over a few days. They should each get their own ingestion record at the time, but a future maintenance sweep will probably want to consolidate them into one canonical churn-event record.)

---

## Artifact 4 — Hypothesis: weekly-email-summary, status `promoted` as of 2026-02-20

**Filename target:** `hypotheses/weekly-email-summary.md`
**Created:** 2025-12-08
**Last updated:** 2026-02-20 (when promoted)
**Status:** `promoted`

The premise: a weekly email summary of the user's workouts (sent Monday morning) would increase week-4 retention by reminding inactive users that they had a streak going. We promoted this on 2026-02-20 based on:

- **Evidence for (recorded at promotion time):**
  - 8 of 12 lapsed-user interviews (Nov–Dec 2025) named "I forget the app exists" as their reason for stopping. `(stakeholder-verbal, lapsed-user-interview-cohort, 2025-12-15)`
  - Competitor Strava added weekly email summaries in Q3 2025; their public Q4 earnings called it a retention win. `(industry-knowledge)`
  - Early internal smoke test (Dec 2025, 500-user send): 23% open rate, 6% click-through to the app. Reasonable engagement. `(intuition, PM, 2025-12-20)`

- **Decision trigger at promotion:** if a full A/B test (10k users, 4-week window) shows >3pp lift in week-4 retention, ship to all. If <1pp lift, kill it. Between 1pp and 3pp, iterate on subject lines and send time.

**The A/B test ran 2026-02-28 through 2026-03-28** (4-week window, 10k treatment / 10k control). The results were attached to the hypothesis file as a comment block when the test concluded, but **the hypothesis file's `status:` field was never updated**:

> **A/B test result (concluded 2026-03-28):**
> - Treatment (received weekly emails): week-4 retention 31.2%
> - Control (no weekly emails): week-4 retention 31.0%
> - Delta: +0.2pp. Not statistically significant (p = 0.71).
> - Open rate degraded over the 4-week window: week 1 = 21%, week 4 = 9%. Users were not engaging with the emails.
> - Per the decision trigger, this should kill the hypothesis. Filing under decision debt; needs PM to formally demote.
> *— Maya, 2026-03-28*

So the hypothesis is still marked `status: promoted` even though the A/B test result satisfies the documented kill condition. It's been sitting in that state for ~7 weeks. This is the kind of staleness the next maintenance sweep should catch — but I want it ingested AS-IS, with the A/B test result preserved in the file, so the sweep can find it.

---

## Artifact 5 — Knowledge file: `knowledge/product/onboarding-funnel.md`, last touched 2025-11-22

**Filename target:** `knowledge/product/onboarding-funnel.md`
**Last updated:** 2025-11-22
**Status:** still marked as "current" in the file's own header.

Content (this is the November snapshot of the onboarding flow):

> # Onboarding funnel — current as of 2025-11-22
>
> ## The 7-step flow
> 1. Email signup (no social login yet — that's on the roadmap for Q1)
> 2. Goal selection (lose weight / build muscle / general fitness)
> 3. Activity level question
> 4. Connect a wearable (Apple Watch, Fitbit, Garmin) — optional, skippable
> 5. Push notification permission
> 6. Choose first workout from recommended list
> 7. Land on home screen
>
> ## Funnel numbers (October 2025 cohort)
> - Step 1 → 2: 88% (12% bounce at signup)
> - Step 2 → 3: 96%
> - Step 3 → 4: 94%
> - Step 4 → 5: 78% (wearable step is high-friction)
> - Step 5 → 6: 81%
> - Step 6 → 7: 99%
> - End-to-end signup → first workout: 53%
>
> ## Known issues
> - Wearable connect step is the funnel's worst dropoff (Step 4 → 5: 78%)
> - First workout selection is forced — no "skip and explore" option

What this file does NOT mention (because it hasn't been updated): the onboarding flow was redesigned in December 2025 to a 4-step flow (we cut goal-selection and activity-level into a single "tell us about you" page, made wearable-connect a post-onboarding prompt instead of inline, and added a "skip and explore" option). The redesign shipped on 2025-12-22. New end-to-end signup → first workout is 68%. **None of that is reflected in this knowledge file.**

The redesign decision (artifact 6 below) was logged in `decisions/` but never back-linked into the knowledge file. This is the kind of canonical-ownership drift the next maintenance sweep should catch.

---

## Artifact 6 — Decision record: 2025-12-18 onboarding redesign

**Filename target:** `decisions/2025-12-18-onboarding-redesign-to-4-step.md`
**Status:** decided (2025-12-18). Shipped 2025-12-22.

**Decision:** Compress the 7-step onboarding to a 4-step flow.

**Why (recorded at decision time):**
- Step 4 → 5 dropoff (wearable connect, 22%) was the funnel's worst single step. `(stakeholder-verbal, analytics-team, 2025-11-22)` — same numbers later digested into artifact 5's knowledge file. The original export pre-dates PM Brain, so no source/ artifact exists for it.
- User research (5 sessions, Dec 1–8) showed the goal+activity questions felt "interrogative" — users wanted to "just get in." `(stakeholder-verbal, ux-research-team, 2025-12-10)`
- Eng estimated 2 weeks for the consolidation work. `(stakeholder-verbal, Aarav, 2025-12-12)`

**Expected outcome:** end-to-end signup → first workout improves from 53% to ≥60%.

**Reversal condition:** if the 4-step flow lands below 50% end-to-end conversion in the first 4 weeks post-ship, we revert. Otherwise we keep it and the 7-step flow goes into the design archive.

**Result (added to file 2026-01-20):** New flow shipped 2025-12-22. End-to-end conversion through January 2026: 68%. Comfortably above the 60% target. Decision validated.

---

## Artifact 7 — Stakeholder file: `stakeholders/jordan-pm.md`

**Filename target:** `stakeholders/jordan-pm.md`
**Last touched:** 2026-03-08 (a week before they left).

Content (the file as it stood when Jordan was last touched):

> # Jordan Reyes — peer PM, Marketplace surface
>
> ## Role
> PM for the Marketplace surface (workout content marketplace, in-app purchases of premium workouts from creators). Started at PulseFit 2024-08.
>
> ## Influence
> Medium. Owns a parallel product surface; we coordinate on shared roadmap items (especially around the home screen, where Marketplace cards compete with our content recommendations).
>
> ## Active asks / concerns
> - Wants more home-screen real estate for Marketplace cards. Pushed in Feb roadmap review.
> - Frustrated about shared analytics dashboard latency (a known eng debt item).
>
> ## Cadence
> - Biweekly 1:1 (Thursdays 2pm).
> - Last touched: 2026-03-08.

Jordan **left PulseFit on 2026-03-15** to join Strava. Their Marketplace surface was reassigned to Priya Nair. I haven't touched the stakeholder file since they left — it's sitting there describing Jordan as a current peer. The next maintenance sweep should catch this and propose archiving.

---

That's the bulk seed. Please ingest each artifact:

- Artifacts 1, 2, 3: route through `source/` (verbatim) + `ingestion/` (synthesized). Each gets its own pair. They're about the same event but were captured separately — that's the point; the sweep will later propose consolidating them.
- Artifact 4: create `hypotheses/weekly-email-summary.md` with status `promoted` and preserve the A/B test result as written.
- Artifact 5: create `knowledge/product/onboarding-funnel.md` with the November content as written. Do NOT update it to reflect the December redesign — the staleness is intentional.
- Artifact 6: create `decisions/2025-12-18-onboarding-redesign-to-4-step.md`. Do NOT back-link it into the knowledge file — the missing link is part of what the sweep should surface.
- Artifact 7: create `stakeholders/jordan-pm.md` with the March 8 content as written.

Confirm what you created in a short summary. Don't do anything beyond ingesting.
