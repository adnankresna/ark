# Customer interview — Stripe Compliance, Compliance Lead

**Date:** 2026-04-29
**Duration:** 30 minutes
**Interviewer:** PM (you)
**Interviewee:** Marcus Adelana, Compliance Lead, Stripe (the SOC2 / SOX subteam, which runs as a mid-market unit for our tool)
**Channel:** Zoom, recorded with consent, transcribed
**Context source:** scheduled as part of follow-up sweep after the Acme interview; Customer Success suggested Marcus because Stripe is on the renewal cycle next quarter and Marcus has historically been responsive to research requests.

---

## Transcript (abridged, key sections only)

**PM:** Marcus, thanks for the time. I'm trying to understand how your team uses our product day-to-day. Walk me through a typical week.

**Marcus:** Sure. So our SOC2 evidence cycle is weekly. Every Friday, my team — there's four of us — pulls all the evidence that's accumulated, files it in our GRC system, and updates the control owners. Your tool feeds that. The way I use it is: I open the Friday digest, scan the deltas from last week, and dispatch anything that needs attention.

**PM:** When you say "scan the deltas" — are you opening individual items, or is the summary enough?

**Marcus:** Summary is enough 90% of the time. The point of weekly batching is that I'm doing context-switching once a week, not constantly. If your tool sent me real-time alerts, I genuinely would mute them. We've already muted the in-app alerts. The daily emails I have filtered into a folder I check Friday morning.

**PM:** What about the cases where something is time-sensitive?

**Marcus:** SOC2 evidence is point-in-time. Nothing in our compliance workflow needs response in less than a day. The thing that needs real-time response — actual control failures, incident response — has its own tooling and its own on-call. Your tool is one input into the weekly compliance cycle, not a fire alarm.

**PM:** What would make your weekly review better?

**Marcus:** A clear "what changed this week" view. Right now I'm scrolling through a list of items and having to compare mentally to last week. If the digest highlighted "these 3 items are new, these 2 items changed state, these 47 are unchanged," I'd save 20 minutes a week. That's the high-leverage improvement.

**PM:** Anything else?

**Marcus:** Not really. Honestly, the product works for us. Renewal will be straightforward. I just want less noise, not more features.

---

## PM notes after the call

- Second independent observation of the weekly-batch pattern. Specifics differ from Acme — Marcus is more measured, didn't escalate the way Jamie did — but the underlying behavior is the same: weekly cadence is the natural unit of compliance work, real-time has negative value for this use case.
- Marcus is the second consecutive interviewee to mention they've already MUTED real-time channels. That's the same behavioral signal Jamie surfaced ("we've stopped acting on anything daily"). Two data points isn't a pattern, but the consistency is notable.
- The "what changed this week" request is a feature ask in the digest cadence direction, not in the real-time direction. Adds weight to the calm-mode hypothesis, not the real-time hypothesis.
- Did NOT volunteer willingness to pay for a calm-mode tier. Different from Acme. Don't extrapolate Acme's pricing signal to Marcus's persona without evidence.
- Stakeholder note: low-touch, healthy. Mark renewal as straightforward. Next nudge: 6 weeks before renewal.
- Insight status: weekly-batch pattern now at 2 independent observations. Threshold for promotion is 3. Still working memory, not durable yet.
