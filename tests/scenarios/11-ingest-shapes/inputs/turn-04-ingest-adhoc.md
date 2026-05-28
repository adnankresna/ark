/ingest adhoc

# Quick dump — Slack thread from #eng-data-pipeline, 2026-05-16

Sasha (data eng) pinged me in Slack about a reliability concern she's been sitting on. Pasting the thread verbatim — capture as ad-hoc, route as you see fit. I haven't done anything with this yet.

---

**Sasha Volkova (Senior Data Engineer)** — 2026-05-16, 09:47 AM

@riley heads up — the basin-level aggregation job has been throwing transient timeouts about 1-2x/week for the last month. Doesn't fail outright; just delays the morning dashboard refresh by 30-90 min. Customers haven't escalated yet, but it's getting more frequent. Root cause is probably the new geospatial join I added in March — it's not well-indexed for the larger basins (Mississippi, Columbia, Yukon).

I have a fix queued — proper spatial indexes — but it's a 1-week eng project I can't fit until after the Q2 release. Wanted you to know before any customer notices.

**Riley** — 2026-05-16, 10:02 AM
Thanks for the heads up. Is this a "will eventually break" thing or a "will degrade gradually" thing?

**Sasha** — 2026-05-16, 10:05 AM
Honestly, both. Probability of an outright job failure goes up as we add more customers in the western basins. We have 14 active customers querying the Columbia basin daily and that's our hot spot.

**Riley** — 2026-05-16, 10:07 AM
Got it. Will park this — let me think about whether it changes Q3 prioritization. Don't change anything yet on your end.

---

For the brain: this is engineering-debt context, not a customer-evidence signal. But it's relevant to any decision about new dashboard work — adding a watershed-level aggregation on top of an already-flaky basin-level job is structurally riskier than it looks on paper. Capture and route accordingly.
