# Bulk import: prior PM-Brain state from 4 months ago

I'm Rita Park, PM for OrthoSched (B2B SaaS, ~340 mid-size dental practice accounts, ARR ~$8M). I started using PM Brain six months ago. Today is **2026-05-17**. Below are three artifacts from **January 2026** that established our top-priority hypothesis for Q1: *Provider Availability Sync*. The feature shipped to GA on **2026-03-20**. I want all three artifacts ingested faithfully — they happened in January, please preserve dates accurately so we know how old this evidence is.

After ingesting, the active hypothesis should be `provider-availability-sync` with status `promoted` (it WAS promoted in January based on this evidence; the resulting feature has been live for ~8 weeks). The decision that came out of this hypothesis should be a real decision file.

Don't synthesize anything new beyond what's in these three artifacts. The point is to get the January state into the brain accurately so future signals can challenge it. Tag everything with January 2026 dates.

---

## Artifact 1 — Customer interview, Brightsmile Dental, 2026-01-08

**Interviewee:** Dr. Linda Park, owner/lead dentist, Brightsmile Dental (4-chair practice, 6 providers, suburban Denver). Practice has been on OrthoSched for ~14 months.
**Interviewer:** Rita Park (PM, no relation)
**Format:** 45-min Zoom, recorded with consent.

**Rita:** What's the single biggest scheduling pain right now?

**Linda:** Honestly? Provider availability. We have six providers — two full-time, three part-time, one who only does Tuesdays and Thursdays. Their availability changes constantly. Maternity leave, kid pickup days, CE conferences. Our front desk keeps a paper calendar of "actual availability this week" and re-types it into your system every Monday morning. It's two hours of work. Sometimes they miss a change and we end up double-booked or with a provider sitting idle.

**Rita:** What would good look like?

**Linda:** Each provider would have their availability in one place — their own phone, ideally — and it would sync to your system automatically. We trust providers to keep their own calendar. We don't trust the front-desk re-typing.

**Rita:** Any specific calendar tool you'd want to sync from?

**Linda:** Google Calendar mostly. A couple use Apple Calendar. The two associates are on Outlook because they came from a corporate practice.

**Rita:** If we built this — sync provider availability from Google/Apple/Outlook to OrthoSched — how would that change your week?

**Linda:** It would save my front desk two hours a week and prevent maybe two double-bookings a month. Two double-bookings is roughly $400 in lost chair time. So call it $700-800/month per practice in soft savings. I'd pay another $50/seat for it. Easily.

**Rita:** Would you switch off OrthoSched if a competitor offered this and we didn't?

**Linda:** I've been getting Dentrix emails about a similar thing. I haven't switched because OrthoSched's billing module is better. But it's on the table if you don't ship this.

---

## Artifact 2 — Engineering feasibility note, 2026-01-15

**Author:** Marcus Wei, Eng Lead
**Re:** Provider availability sync — feasibility & estimate

Spent a day looking at this. Summary:

- **Google Calendar:** their API is well-documented, OAuth flow is standard, we already have OAuth infra from the patient-portal SSO work. Two weeks of work for a working integration.
- **Apple Calendar:** harder. No official server API. We'd have to use CalDAV with app-specific passwords. Workable but flakier; another two weeks plus support overhead.
- **Outlook:** Microsoft Graph API, similar to Google. Two weeks.
- **Sync engine itself:** we need a poll-and-merge layer that handles edits on both sides. Two weeks plus a week of edge-case work (recurring events, all-day events, timezone shifts).

Total estimate: **8-10 weeks** for all three calendar providers + sync engine. Could ship Google-only in 4 weeks if we want a faster signal.

Risks:
- Conflict resolution when a provider edits availability in both their personal calendar AND OrthoSched — we'd need a clear "source of truth" rule per slot. Recommend: personal calendar wins.
- Privacy: providers may not want their personal calendar visible to front desk. We should sync ONLY busy/free, not event titles.

No major blockers. Recommend we build Google + Outlook first; defer Apple to a fast-follow.

---

## Artifact 3 — Decision record, 2026-01-22

**Decision:** Build Provider Availability Sync (Google + Outlook in v1, Apple in fast-follow).
**Driver:** Rita Park (PM). Approved by Naomi Reyes (CEO), Marcus Wei (Eng Lead).
**Status:** decided (2026-01-22). Build kicks off 2026-01-26. Target GA: 2026-03-20.

**Why:**
- Strong direct customer signal: Brightsmile interview (2026-01-08) — willingness to pay $50/seat, competitive switching risk named.
- Eng feasibility confirmed: 8-10 weeks, no major blockers (2026-01-15 note).
- Aligns with Q1 strategy theme "operational efficiency wins for the front desk."
- CS team's December monthly listed "provider scheduling" as the #2 churn-cited reason in exit interviews (3 of 11 departing accounts named it).

**What we expect to see post-ship:**
- Adoption: ≥40% of practices with >3 providers enable the integration within 8 weeks of GA.
- Engagement: ≥70% of enabling practices keep it enabled at week 8 (no rage-uninstall).
- Outcome: measurable reduction in double-bookings reported to CS (baseline ~12/month across all accounts; target ≤8/month by week 8 post-GA).

**What would reverse this decision:**
- If adoption is < 20% at week 8 post-GA AND the practices that DID enable it report negative experience, we revisit before investing in the Apple integration. The Apple work is the next $100k of eng cost — that's the natural reversal checkpoint.

**Reversal condition:** Adoption < 20% at week 8 post-GA OR support-ticket volume from enabled practices > 2x baseline.

---

That's the January state. Please ingest all three, preserve them under `source/` with January dates, create the hypothesis file and the decision file, and confirm the hypothesis status is `promoted` (with the resolution noted as "decision made 2026-01-22"). Don't do anything beyond ingesting.
