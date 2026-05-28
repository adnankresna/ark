# PM prompt — bulk import of inherited folder

**Date:** 2026-05-04
**From:** Maya Chen (new senior PM, Tally)
**To:** the brain
**Type:** direct request

---

## Context for the brain

I'm Maya Chen. I joined Tally yesterday as senior PM on the core budgeting product (B2C, ~120k MAU, freemium with a Pro tier at $7/mo). My predecessor Alex Reyes left abruptly six weeks ago — not on great terms, no formal handoff, and the team has been holding the line without a PM since. I have his folder. It's a mix of things he wrote, things he inherited from the PM before him (Jordan, who left 14 months ago), and things from other functions (eng, CS, marketing) that he was using as reference.

I want to ingest **all of it** into the brain. But I want you to be careful about it:

- Preserve every artifact verbatim in `source/`. Even if it looks contradictory to other artifacts. I want the originals findable.
- Do not over-promote anything. Most of these are one source, sometimes anonymous, sometimes months old. A claim that appears in three artifacts is not three independent observations if the same person wrote all three.
- Tag each artifact with its **provenance** (Alex / Jordan / function / external) and its **age** (how old at time of ingestion). Both matter for trust-weighting later.
- Pay attention to authorship. Alex's draft Q4 roadmap is not the same kind of artifact as the live strategy doc or the CS monthly. Treat drafts as drafts.
- Note contradictions but do **not** try to resolve them yet. I'll work through resolution with you in the next session. I just want a clear "here's what conflicts with what" picture.
- If a hypothesis is worth opening based on what's in here, open it as candidate/proposed only. Nothing gets promoted from bulk-import alone. We'll need fresh evidence to confirm.

I'll paste each artifact below as a separate section. Some are short (Slack threads), some are longer (the strategy doc, the personas research). After you've ingested everything, give me back: (1) what landed where, (2) a list of candidate hypotheses, (3) a *short* note of the most obvious tensions you noticed — without trying to resolve them.

---

## Artifact 1 — strategy-v3.md

**Author:** Alex Reyes
**Date written:** 2025-11-15 (about 6 months old)
**Status:** "Approved by leadership, last reviewed Nov '25"

> # Tally Strategy v3 — North Star: habit formation
>
> ## Why we exist
> Most people who download a budgeting app abandon it within 14 days. They don't fail to budget because the math is hard — they fail because the habit doesn't stick. Tally's job is to build the habit. Everything else is downstream.
>
> ## Core thesis
> Habit > optimization. A user who checks Tally three times a week and gets two budget categories slightly wrong is more valuable than a user who configures perfect categories once and never returns.
>
> ## Strategic priorities (Nov '25 → Jun '26)
> 1. **Daily check-in loop**: get the median user from 1.2 to 3+ sessions/week.
> 2. **Single-screen simplicity**: every additional decision the user has to make in the app is a tax on the habit. Default aggressively. Hide complexity behind disclosure.
> 3. **Solo-user focus**: our user is one person managing their own money. We've considered couples and family use cases — they're real, but they pull us toward complexity and away from the habit loop. Defer until 2027 at earliest.
>
> ## Anti-priorities
> - Investment tracking (Mint did this, didn't move retention).
> - AI-driven financial advice (regulatory risk, not our wheelhouse).
> - Social features (vanity engagement, doesn't reinforce the habit).

---

## Artifact 2 — roadmap-q3-2026.md

**Author:** Alex Reyes (with eng lead Devon Park)
**Date written:** 2026-02-08
**Status:** "Shipped Q3" — already in market

> # Q3 2026 Roadmap (Apr-Jun)
>
> ## Theme: stickier daily loop
>
> 1. **Streak counter** — visible on home screen. Tracks consecutive days the user logged at least one transaction or checked their budget. Shipped 2026-04-12.
> 2. **Smart category suggestions v2** — ML-improved guesses for uncategorized transactions. Shipped 2026-05-01.
> 3. **Push notification rework** — single morning nudge at user-chosen time, replacing the previous 3-per-day cadence. Shipped 2026-04-28.
> 4. **Goal-progress widget** (iOS) — home-screen widget showing % toward monthly savings goal. In QA, expected ship 2026-05-20.
>
> No social, no AI, no couples — consistent with strategy v3.

---

## Artifact 3 — roadmap-q4-draft.md

**Author:** Alex Reyes
**Date written:** 2026-03-22 (last edit; ~6 weeks before he left)
**Status:** **DRAFT — never shared with eng or leadership**

> # Q4 2026 Roadmap (Jul-Sep) — DRAFT
>
> ## Theme: social engagement
>
> The retention numbers from Q2 worry me. Daily check-in loop is plateauing. I think we need a step-change, and I think it's social.
>
> 1. **Friend leaderboards** — opt-in. Compare savings progress with friends. Drives weekly engagement.
> 2. **Shared challenges** — "Save $200 this month" group challenges.
> 3. **Public goals (optional)** — share a savings goal publicly, get accountability.
> 4. **AI insights v1** — weekly "your money story" summary, generated by an LLM.
>
> ## What I'm worried about
> This is a real departure from strategy v3. I think the strategy needs an update. The habit-loop framing is right at the small scale, but I don't think it's enough at the scale we're at now. Need to sell this to leadership.

---

## Artifact 4 — personas-2024-research.md

**Author:** Jordan Lee (previous PM, before Alex)
**Date written:** 2024-09-10 (about 20 months old)
**Status:** "Used as reference doc; never formally re-validated"

> # Tally Personas (Sept 2024 research)
>
> Based on 24 interviews and n=400 segmentation survey, summer 2024.
>
> ## Persona 1: The Saver (estimated 35% of active base)
> Has a clear financial goal (down payment, debt payoff, emergency fund). Uses Tally to feel in control and to track progress. Values: simplicity, visible progress, no friction. Will not tolerate: clutter, social pressure, gamification that feels childish.
>
> ## Persona 2: The Spender (estimated 40% of active base)
> Doesn't have a specific goal but feels guilty about spending. Uses Tally aspirationally — wants to "be more responsible." Inconsistent engagement. Values: gentle nudges, non-judgmental tone, easy re-entry after a lapse. Will not tolerate: shame mechanics, complex setup.
>
> ## Persona 3: The Achiever (estimated 25% of active base)
> Treats budgeting like a game. Loves streaks, badges, comparison. Often power users. Values: leaderboards, progress visualization, optimization. Will not tolerate: dumbed-down UX, missing data.
>
> ## Note from Jordan
> Personas should be re-validated annually. As of Sept 2024 the Achiever segment is the loudest in support tickets but the smallest in revenue. Optimize for Saver + Spender; don't let Achiever asks drive the roadmap.

---

## Artifact 5 — interview-2026-02-15-priya.md

**Interviewer:** Alex Reyes
**Interviewee:** Priya M., Pro tier, 18-month customer, classified as Saver
**Date:** 2026-02-15

> Priya's main complaint: the app is getting more complicated. She used to log in, see her three category totals, log out. Now there's a streak counter, smart category suggestions she has to dismiss when wrong, and the new home widget. She said: "I don't want gamification. I want a calculator with categories."
>
> When asked about social/leaderboards (Alex floated it): "Absolutely not. My money is private. I would uninstall the app the day you turn that on."
>
> When asked about couples: "I share rent with my partner but we keep finances separate. I wouldn't use a shared budget. My sister might — she's married — but that's not me."
>
> Renewal risk: low. She likes the core. Annoyance at additions, not the foundation.

---

## Artifact 6 — interview-2026-03-22-tom.md

**Interviewer:** Alex Reyes
**Interviewee:** Tom K., free tier (3 months in), classified as Spender
**Date:** 2026-03-22

> Tom is younger (26), uses Tally on phone only, logs in maybe 2x/week. He likes the streak counter ("makes it feel less like a chore").
>
> When asked what he wished Tally did that it doesn't: **"Honestly? Export to a spreadsheet. I want to do my own analysis sometimes. Or share a budget with my girlfriend — we just moved in together, and we're trying to split rent and groceries fairly but neither of us wants to do it in Notes."**
>
> When asked about AI insights: shrugged, "Maybe? I don't really trust AI with money stuff. But I'd try it."
>
> When asked about leaderboards: "My friends would mock me. Hard no."

---

## Artifact 7 — competitor-analysis-2024-11.md

**Author:** unclear — looks like a contractor deliverable, no attribution
**Date:** 2024-11
**Status:** Was in Alex's "reference" subfolder

> # Competitive landscape — personal finance apps, Nov 2024
>
> ## Top competitors
> - **Monarch** — premium, $14/mo, family-focused, strong on shared budgets. Growing.
> - **Copilot** — premium, $13/mo, iOS-first power-user tool. AI insights feature shipped Oct '24.
> - **YNAB** — premium, $15/mo, methodology-driven, strong retention. No social.
> - **Rocket Money** — freemium ads-heavy, broad-but-shallow.
>
> ## Trends
> 1. **Social and shared budgets are table stakes** for premium apps targeting users 25-40. Monarch's growth driven by couples segment.
> 2. **AI insights** rolling out across the market. Copilot's launch widely covered.
> 3. **Streak/gamification** mechanics are commoditizing.
>
> ## Recommendation
> Tally should add shared budgets and AI insights to remain competitive in premium.

---

## Artifact 8 — metrics-snapshot-2026-04.md

**Author:** analytics (auto-generated, Alex pinned it)
**Date:** 2026-04-30

> # Tally metrics snapshot — April 2026
>
> ## Retention (W4 cohort retention)
> - W4 retention: **14.2%** (down from 22.1% in same month 2025)
> - W12 retention: 7.8% (down from 11.3% in 2025)
>
> ## Engagement
> - Median sessions/week: 2.1 (Q1 '25: 2.4; trending down)
> - Streak counter: 38% of MAU have an active streak of 3+ days
> - Goal-progress widget: 4% of iOS MAU installed it (only 2 weeks in market)
>
> ## Revenue
> - Pro conversion: 4.3% of MAU (flat YoY)
> - Pro churn: 6.1%/mo (up from 4.8% last year)
>
> ## Top features added in last 90 days (by % of MAU touching)
> - Smart category suggestions v2: 71%
> - Push rework: 100% (default)
> - Streak counter: 64%
>
> ## Notes
> Retention drop is real and concerning. Doesn't correlate cleanly with any single feature ship.

---

## Artifact 9 — slack-thread-pricing-export.md

**Source:** #product-discuss, Slack
**Date:** 2026-03-30
**Participants:** Alex, Devon (eng lead), Riya (CS lead), Sam (marketing)

> **Sam:** Two support tickets this week asking about spreadsheet export. Worth adding?
>
> **Devon:** Trivial to build. Few days of work.
>
> **Riya:** It's a recurring ask in CS. Maybe 8-10 tickets a month. Not top-3 but persistent.
>
> **Alex:** It's an Achiever ask. We're trying to deprioritize Achiever. Soft no for now.
>
> **Sam:** OK. Separate thought — should export be a Pro-tier-only feature when we do build it? Pricing lever?
>
> **Alex:** Maybe. We can revisit when we revisit Pro packaging. Q3 conversation.

---

## Artifact 10 — eng-feasibility-note-2026-03.md

**Author:** Devon Park (lead eng), in response to Alex's ask
**Date:** 2026-03-25
**Status:** Email forwarded into the folder

> Alex —
>
> You asked me to ballpark social + shared budgets + AI insights for Q4.
>
> Rough numbers:
> - **AI insights (weekly summary)**: ~3 weeks. We can ship a v1 on top of the existing transaction data with an LLM call. Real cost concern: per-user inference costs at MAU scale. Need pricing model first.
> - **Friend leaderboards (opt-in)**: ~6 weeks. Requires friend graph (new), privacy model (new), comparison UI (new). New attack surface for harassment vectors — needs trust & safety review.
> - **Shared budgets (couples)**: ~10 weeks. This is the big one. Requires multi-user data model migration, permission model, conflict resolution UX, billing model (one Pro covers two users? both pay?). I've been pushing back on this whenever it's come up because the data model migration alone is risky.
>
> Honest take: any one of these is doable. All three in a quarter is not.
>
> — Devon

---

## Artifact 11 — cs-monthly-2026-04.md

**Author:** Riya Sundaram (CS lead)
**Date:** 2026-04-30
**Status:** Internal CS monthly summary, shared with PM

> # CS Monthly — April 2026
>
> ## Top customer requests (this month, ranked by volume)
> 1. **Budget alerts before I overspend** (47 tickets) — users want a heads-up when they're approaching category limits.
> 2. **Spreadsheet/CSV export** (31 tickets) — persistent, see prior months.
> 3. **Shared budgets for couples/roommates** (28 tickets) — has been climbing steadily for 4 months.
> 4. Smart category suggestions: getting it wrong (24 tickets, complaints)
> 5. iOS widget bugs (18 tickets)
>
> ## Trends worth flagging
> - Couples/shared has been growing steadily — was #8 in Jan, #5 in Feb, #4 in Mar, #3 in Apr.
> - Almost zero asks for: leaderboards, social, AI insights.
> - Pro churn reasons (exit survey, n=42): "too simple now feels like it's getting cluttered" (12), "switched to Monarch for couples" (9), "didn't use it enough" (8), "price" (4), other (9).
>
> ## Recommendation
> Whatever the Q4 roadmap is, please consider budget-alerts and shared-budgets. The signal is strong and stable.

---

## End of inherited artifacts

That's everything from Alex's folder. Process it carefully. I'll be back tomorrow to walk through what you found.
