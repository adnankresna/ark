# Customer interview — Brightsmile Dental follow-up, 2026-05-17

Same customer as the January 2026 interview. Provider Availability Sync shipped to GA on 2026-03-20 — ~8 weeks ago. Brightsmile enabled it on day one. This is a scheduled check-in.

**Interviewee:** Dr. Linda Park, Brightsmile Dental (4 chairs, 6 providers — same as before).
**Interviewer:** Rita Park (PM).
**Format:** 30-min Zoom, recorded with consent.

---

**Rita:** Eight weeks in. How's the availability sync working for you?

**Linda:** Honestly? I want to turn it off. We probably will next week.

**Rita:** Oh. What happened?

**Linda:** The sync works technically. The problem is what *kind* of availability our providers actually keep in their personal calendars. They put "BLOCKED — admin time" and "BLOCKED — lunch with rep" and "BLOCKED — case prep." None of those are actually unavailable for a patient if it's an emergency or a high-value case. But the system marks them busy. So we've gone from front-desk re-typing — which was annoying but accurate — to the system thinking the providers have zero open slots half the time, when they really have three.

**Rita:** So the front desk still has to manually override?

**Linda:** They have to manually override MORE. Before, they re-typed once a week and we lived with what they typed. Now they're constantly fighting the sync. Every time a provider edits their calendar, OrthoSched re-pulls and overwrites their manual adjustments. It's worse than what we had.

**Rita:** Did the double-bookings go down?

**Linda:** No. We had three last month, two the month before. About the same as before we enabled it. The bookings we miss aren't because front-desk re-typed wrong, they're because providers don't always tell us about last-minute schedule changes. The sync doesn't help with that — providers who don't update their personal calendar in time still don't update it in time.

**Rita:** What about the $50/seat you said you'd pay for it?

**Linda:** I wouldn't pay $50/seat for what we got. I might pay $10/seat if it was a smarter version that understood "BLOCKED — admin" doesn't mean "patient can't be added if needed." Or if it was just one-way — show our front desk what providers are doing, but let the front desk be the source of truth in OrthoSched. The bidirectional sync is what's hurting us.

**Rita:** Are you still considering the competitor?

**Linda:** Dentrix? I asked one of their reps. Their version is read-only — they pull from the provider's calendar and *display* it to front desk as a hint, but the OrthoSched-equivalent calendar in their system is still front-desk-controlled. That actually sounds better than what we built.

**Rita:** If we made ours one-way / display-only, would that help?

**Linda:** Way more useful. The bidirectional thing is the bug. We trusted the providers' calendars to be authoritative. They're not — providers use those calendars as personal scratchpads.

---

**My internal note:** This is the customer who championed the feature. Her stance has reversed. I want this ingested cleanly. Don't auto-demote anything yet — but please flag the tension explicitly. The January evidence said one thing; today's evidence says another. The hypothesis file should pick up an evidence-against row, and the original promotion should be visibly in tension with this new signal.
