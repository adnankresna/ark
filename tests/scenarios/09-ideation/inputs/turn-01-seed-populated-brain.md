# Bulk import: 4 months of accumulated PM Brain state

I'm Sam Liu, PM for FlowExpense (B2B SaaS expense management, ~280 mid-market customers, ARR ~$11M). I've been operating PM Brain for four months. Today is **2026-05-17**. Below are eight artifacts from **January through April 2026** that represent the current state of the brain — three customer interviews, an insights entry I wrote up after the second interview, a competitor note, a CS monthly, an entry in our roadmap with an open question I've been sitting on, and one hypothesis file I promoted in February that has gone quiet since.

I want all of it ingested faithfully — original dates preserved, provenance tagged, the stalled hypothesis kept as-is (don't auto-update its status). This is the brain's current state. I'll work with you on it tomorrow.

Don't synthesize anything new beyond what's in these eight artifacts. Don't open new hypothesis files. Don't promote anything. Just get the state into the brain accurately so I can ask you questions about it.

---

## Artifact 1 — Customer interview, Northstar Logistics, 2026-01-22

**Interviewee:** Dana Velasquez, Controller, Northstar Logistics (180-employee 3PL based in Atlanta). On FlowExpense ~10 months.
**Interviewer:** Sam Liu (PM)
**Format:** 40-min Zoom, recorded with consent.

**Sam:** Walk me through your monthly close. Where does FlowExpense fit, and where does it break down?

**Dana:** It's mostly fine. The pain point is receipts. Our drivers and ops managers expense things in the field — fuel, tolls, ad-hoc repairs, customer dinners. They upload receipts when they remember. Then on closing week, my AP person has to match every receipt to a charge on the corporate card statement. We have maybe 400-500 receipts a month and roughly the same number of card transactions. The matching is mostly manual.

**Sam:** Is FlowExpense doing any of the matching today?

**Dana:** It tries. Your auto-match catches the easy ones — exact dollar amount, same date, same vendor name. But anything where the receipt says "Shell #4471" and the card statement says "SHELL OIL ATLANTA GA" — your system doesn't connect them. Or when there's a tip on the receipt that's not on the card auth. We probably manually reconcile 60% of receipts.

**Sam:** What would good look like?

**Dana:** A smart match. Fuzzy on vendor name, tolerant on amount within X%, suggestion-with-confirm rather than auto-merge. My AP person wants to be in the loop on edge cases but doesn't want to type "Shell" into a search bar 300 times a month.

**Sam:** How much time?

**Dana:** AP person spends two days of close-week on receipt matching. So roughly 16 hours a month. If you halved that I'd notice.

**Sam:** Anything else?

**Dana:** That's the headline. Everything else — categorization, approvals, reporting — works fine.

---

## Artifact 2 — Customer interview, Brillstone Consulting, 2026-02-18

**Interviewee:** Marcus Hill, Director of Finance, Brillstone Consulting (90-employee management consulting firm, NYC). On FlowExpense ~14 months.
**Interviewer:** Sam Liu (PM)
**Format:** 35-min Zoom.

**Sam:** What's the friction you'd most want gone?

**Marcus:** Receipt matching during month-end. It's a chore. Our consultants travel constantly — flights, hotels, client dinners. Each consultant has maybe 30-40 receipts a month, and we have 60 consultants. So 2,000-ish receipts a month, similar number of card line items. The matching itself eats time.

**Sam:** Does FlowExpense's existing auto-match help?

**Marcus:** A bit. Honestly we've stopped trusting it for anything where the vendor name doesn't match exactly. Hotels are the worst — the receipt says "Hyatt Regency San Francisco" and the card says "HYATT REG SF SAN FRA." Half the time auto-match misses it. So our finance team treats auto-match as a suggestion and re-verifies everything.

**Sam:** What would a fix look like?

**Marcus:** Fuzzy vendor matching with confidence scoring. Show us "this receipt is a 92% match to this charge" and let us click confirm. We don't need it to be perfect. We need it to be confident enough that confirming is faster than searching.

**Sam:** Have you considered switching products?

**Marcus:** We looked at Brex when they shipped their auto-matching thing in March — well, actually I think their announcement said March, our procurement looked in April. It does look better than what you have. But switching expense systems is a six-month project and our team hates the idea. So I'd rather you ship the fix.

**Sam:** Any other friction worth mentioning?

**Marcus:** Not really. Categorization works. Reports are fine. Approvals work. It's just the matching.

---

## Artifact 3 — Customer interview, Pacific Greens Co-op, 2026-04-09

**Interviewee:** Jenna Okafor, Finance Manager, Pacific Greens Co-op (regional grocery chain, 11 stores in WA/OR, ~140 employees including store managers). On FlowExpense ~7 months.
**Interviewer:** Sam Liu (PM)
**Format:** 30-min Zoom.

**Sam:** What's the biggest pain on FlowExpense right now?

**Jenna:** Honestly? Receipts. Our store managers buy ad-hoc stuff for the stores — replacement equipment, cleaning supplies, the occasional emergency thing — and they expense it on the corporate card. Most of them are bad at the receipt-upload part. So we get to month-end with maybe 200 unmatched charges across all 11 stores, and our part-time bookkeeper has to chase down each store manager for the receipt.

**Sam:** What does the matching workflow look like when receipts DO come in?

**Jenna:** It's manual. Your system's auto-match isn't reliable for our case — store managers shop at a lot of small local vendors, hardware stores, that kind of thing. Vendor names on receipts often don't look like the card statement strings at all. So our bookkeeper does it by eyeballing the amount and date.

**Sam:** If we fixed this, how would you measure it?

**Jenna:** If receipts were matched faster — even just suggested with high confidence — our bookkeeper could close two days earlier in the month. That's real to me.

**Sam:** Anything else?

**Jenna:** No, that's the one. The chasing-down-store-managers part is separate — that's a behavior problem on our end. But once they upload, the matching should be smoother.

---

## Artifact 4 — Insights entry, knowledge/users/insights.md, written 2026-02-22

**Author:** Sam Liu (PM)
**Triggered by:** Brillstone interview (Feb 18) + reflection on internal CS data.

> ## Insight: Finance teams batch receipt processing on Fridays
>
> Across our two largest customer interviews so far (Northstar in Jan, Brillstone in Feb) and corroborated by our Q1 product-usage telemetry, finance teams concentrate receipt-matching and reconciliation work on Fridays. Brillstone's Marcus said "month-end close-week is brutal but our weekly cadence is Fridays — we batch a week of receipts every Friday afternoon." Telemetry shows 38% of weekly receipt-matching activity happens on Fridays (vs. ~20% you'd expect from uniform distribution).
>
> **Why it matters:** if we ever build smarter receipt workflows, the design surface should account for batch behavior, not just one-at-a-time entry. A "process this week's receipts" mode would fit the actual workflow better than a per-receipt UI.
>
> **Confidence:** medium. Two interviews + one telemetry signal. Not yet promoted to a hypothesis.
>
> Provenance: `[ingestion/interviews/2026-01-22-northstar.md](../../ingestion/interviews/2026-01-22-northstar.md)`, `[ingestion/interviews/2026-02-18-brillstone.md](../../ingestion/interviews/2026-02-18-brillstone.md)`, `(intuition, PM, 2026-02-22)` for the telemetry framing.

---

## Artifact 5 — Competitor note, knowledge/market/competitors.md entry, 2026-03-15

**Author:** Sam Liu (PM)
**Source:** Brex's March 12 product blog post + my own product walkthrough on March 14.

> ## Brex — auto-matching feature shipped March 2026
>
> Brex shipped "Smart Match" on March 12 2026. From their announcement and my walkthrough:
>
> - Fuzzy vendor name matching across receipt OCR and card statement strings (handles "Hyatt Regency SF" ↔ "HYATT REG SF" variants).
> - Confidence-scored suggestions, not auto-merge. AP team confirms each suggested match above 80% confidence in one click.
> - Brex's announcement claimed **40% adoption** in their customer base within two weeks of launch — they characterized it as their fastest-adopted feature in 18 months.
> - Pricing: included in their existing plan tiers, no separate SKU.
>
> **My read:** Brex correctly identified a high-frequency pain point. Our customers (Northstar, Brillstone) have independently named the same pain. We don't have a comparable feature — our auto-match is exact-match-only.
>
> Provenance: `(industry-knowledge)` for the Brex announcement framing, `(intuition, PM, 2026-03-15)` for the read.

---

## Artifact 6 — CS monthly summary, 2026-04-15 (covers March 2026)

**Author:** Priya Iyer (CS lead)
**Status:** Internal monthly summary, shared with PM.

> # CS Monthly — March 2026
>
> ## Top customer support ticket categories (by volume, March 2026)
>
> 1. **Login / SSO issues** (54 tickets) — concentrated in two enterprise accounts with quirky IdP setups.
> 2. **Card transaction not appearing in feed** (41 tickets) — bank-feed sync issues, mostly resolved within 24h.
> 3. **Receipt-matching problems** (38 tickets) — split between "auto-match got it wrong" and "no match suggested, had to do it manually." Steady volume for the last 4 months.
> 4. **Approval routing edge cases** (22 tickets)
> 5. **Report export formatting** (17 tickets)
>
> ## Trends
> - Receipt-matching has been stable at 35-40 tickets/month since December. Not growing, not shrinking. It's a persistent background pain across our customer base.
> - The split inside the receipt-matching category: ~60% "your auto-match got it wrong" (false-positive matches that AP had to undo), ~40% "no suggestion at all."
>
> ## Recommendation
> Worth a product look. Steady ~40/month is meaningful given our base size.

---

## Artifact 7 — knowledge/product/roadmap.md, current as of 2026-04-22

**Author:** Sam Liu (PM)

> # FlowExpense Roadmap — current as of 2026-04-22
>
> ## Now (May-Jun 2026)
> - Approval-routing v2 — supporting multi-level approval chains for enterprise (in dev).
> - Mobile receipt upload reliability — fixing the iOS background-upload bug (in QA).
>
> ## Next (Jul-Sep 2026)
> - SSO improvements for enterprise IdP edge cases.
> - Bank-feed reliability hardening.
> - **Open question — what's the under-explored adjacency to expense capture?** We've spent the last two quarters on the entry side of the funnel (capture, mobile, approvals). The processing side (matching, categorization, reporting) hasn't gotten a roadmap slot since the auto-categorization v1 work in Feb. Customer signals are pointing somewhere here but I haven't framed a specific bet yet.
>
> ## Later (Q4+)
> - Spend analytics dashboard refresh.
> - Multi-currency improvements.
>
> Provenance for the open question: `(intuition, PM, 2026-04-22)`.

---

## Artifact 8 — Hypothesis file, hypotheses/auto-categorization.md, last updated 2026-02-25

**Author:** Sam Liu (PM)
**Status:** promoted (Feb 2026). No updates since.

> # Hypotheses — auto-categorization
>
> ## Meta
> - Feature: `../knowledge/product/features/auto-categorization.md`
> - Status: promoted
> - Created: 2026-02-05
> - Last updated: 2026-02-25
>
> ## Value risk
> ### H-V1: Customers will adopt and trust ML-driven transaction categorization if accuracy is above 85%.
> - **Origin:** proactive
> - **Confidence:** medium
> - **Evidence for:**
>   - Northstar's Dana said categorization "works fine" in the Jan 22 interview, suggesting current heuristic-based categorization is at the floor of acceptability. `[ingestion/interviews/2026-01-22-northstar.md](../ingestion/interviews/2026-01-22-northstar.md)`
>   - Brillstone's Marcus said categorization is not a pain point. `[ingestion/interviews/2026-02-18-brillstone.md](../ingestion/interviews/2026-02-18-brillstone.md)`
> - **Evidence against:**
>   - (none yet)
> - **Open questions / caveats:**
>   - The Jan and Feb interviews suggest categorization is fine, NOT that ML-driven categorization would be a step-change. We promoted on the assumption that "above 85% accuracy" is the right bar — that's an assumption, not yet evidence.
> - **Test:** Ship ML-driven categorization to 5% of accounts, measure recategorization-rate as a proxy for trust.
> - **Decision trigger:** If recategorization rate drops > 30% vs. heuristic baseline, promote to GA. If unchanged, demote.
> - **Status:** promoted
> - **Resolution:** Promoted 2026-02-25 based on team consensus that ML categorization is a strategic bet worth taking. Engineering scoping in progress; no test results yet.

---

## End of artifacts

That's the eight. Please:

1. Preserve all eight under `source/` verbatim, with their original dates (Jan-April 2026, NOT 2026-05-17).
2. Route the three interviews through `ingestion/interviews/` as you would normally.
3. Route the competitor note and CS monthly through `ingestion/` (or directly into `knowledge/market/` and `knowledge/...` as appropriate).
4. Populate `knowledge/users/insights.md` with the insight entry (Artifact 4) as-is.
5. Populate `knowledge/product/roadmap.md` with the roadmap entry (Artifact 7).
6. Create the `hypotheses/auto-categorization.md` file exactly as written in Artifact 8 — status `promoted`, last-updated 2026-02-25, no new evidence rows.
7. Do NOT open any new hypothesis files. Do NOT promote anything. Do NOT add fresh signals.

After ingesting, give me back a one-paragraph confirmation of what landed where. I'll come back tomorrow with my real question.
