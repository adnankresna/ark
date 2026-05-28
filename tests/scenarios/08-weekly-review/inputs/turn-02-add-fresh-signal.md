# Fresh customer signal — Helio Networks call, 2026-05-12

One new signal to ingest before I run /review on Friday. This is from earlier this week. Today is **2026-05-17**.

**Interviewee:** Toby Reyes, Director of SRE at Helio Networks (mid-market CDN, ~140 engineers, on LogLens for 22 months — large account, top-15 by ARR).
**Interviewer:** Aria Sharma.
**Format:** 45-min Zoom check-in, recorded with consent. Toby asked for the call after a rough on-call week.

---

**Aria:** Walk me through how on-call's been going.

**Toby:** Bad. Last week was the worst on-call rotation we've had in a year. The primary engineer ended up paging the whole team three different nights. I think people are starting to talk about whether LogLens is still the right choice for us.

**Aria:** What's driving it specifically?

**Toby:** Volume, mostly. The number of alerts that don't matter. Our on-call gets paged probably 15 times a night and maybe 2 of those are real things. The rest is just noise.

**Aria:** That tracks with what we've been hearing more broadly. We're working on alert-noise reduction as the Q2 headline — targeting around a 60% reduction in non-actionable alerts.

**Toby:** Sixty percent.

**Aria:** Yeah — that's the target we set based on the March survey.

**Toby:** That's not going to be enough. Honestly. If we go from 13 noise alerts a night to 5 noise alerts a night, my on-call is still getting paged 5 times a night for nothing. People still don't sleep. The bar for on-call sustainability isn't "less noise" — it's "the on-call engineer can sleep through the night unless something is actually on fire." For us that means we need to be down to maybe 1-2 non-actionable alerts a night, not 5. That's like 80% reduction from where we are, not 60%.

**Aria:** Hm. That's a meaningfully harder target.

**Toby:** I know it is. But I'm telling you what would actually change our calculus on LogLens. 60% gets us a better week. 80% gets us a sustainable on-call. They're different products in terms of impact.

**Aria:** What about grouping — would smarter grouping change the math?

**Toby:** Grouping helps if the underlying alerts are real and we're getting duplicates. Most of our noise isn't duplicates, it's just things that shouldn't be paging at all. Grouping doesn't fix that.

**Aria:** Anything else?

**Toby:** Honestly the 80% number is the headline. I'd rather you ship 80% reduction in six months than 60% reduction next month. The 60% target undersells the problem.

**Aria:** Got it. I'm going to take this back and rethink the target. Not committing to anything in this call but I want to make sure the team hears this.

---

**My internal note:** This is one customer, top-15 by ARR, with a directional but not fully-reversing signal on alert-noise-reduction. The DIRECTION still holds — alert noise IS the right problem to solve. But the 60% threshold I've been promising may be wrong — Toby is saying 60% is "a better week" and 80% is "a sustainable on-call." Those are different products.

Please ingest this:

- Verbatim under `source/interviews/2026-05-12-helio-networks-interview.md`.
- Synthesis under `ingestion/interviews/2026-05-12-helio-networks-interview.md`.
- Add an evidence-against (or partial-contradiction) row to the `alert-noise-reduction` hypothesis. Don't flip the status — this is one signal, the direction still holds, I want to think about it. Just capture the tension honestly. Note in `Open questions / caveats:` that the 60% threshold may be under-spec'd based on this one-signal-but-strong customer.

That's it for today. Don't do a /review yet — I'll ask for that next.
