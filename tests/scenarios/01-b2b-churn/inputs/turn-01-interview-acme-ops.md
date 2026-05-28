# Customer interview — Acme Corp, Ops Lead

**Date:** 2026-04-22
**Duration:** 45 minutes
**Interviewer:** PM (you)
**Interviewee:** Jamie Chen, Ops Lead, Acme Corp (mid-market, ~80 employees, SOC2 Type II)
**Channel:** Zoom, recorded with consent, transcribed

---

## Context

Acme has been a customer for 11 months. They came in on the standard mid-market tier. Their renewal is in 6 weeks. Customer Success flagged that Jamie had been less responsive in the last two sync calls and that her last NPS response dropped from 9 to 6. This interview was scheduled to understand what changed.

---

## Transcript (abridged, key sections only)

**PM:** Thanks for making time, Jamie. CS mentioned a few things felt off recently. What's the current state of the world for you?

**Jamie:** Honestly? It's the notifications. When we rolled this out last year, the daily digest was perfect — one email, scan it Friday afternoon, done. Now between the in-app alerts, the Slack integration, and the daily emails, we're getting pinged constantly. My team has started ignoring it.

**PM:** When you say constantly — how many a day?

**Jamie:** I haven't counted, but I'd guess 8-12 across all channels. The thing is, it's not that they're wrong. It's that none of them are urgent. SOC2 evidence collection is a weekly job for us. We batch it on Fridays. We don't need real-time anything.

**PM:** Walk me through how your week actually runs.

**Jamie:** Monday-Thursday I'm in customer calls and operational stuff. Friday afternoon is when I — and my two reports — sit down and do the compliance work. We pull evidence, file it, update the controls log, close out anything from the week. We need a clean view of "what changed this week" once. Not 12 pings spread across the week. We've stopped acting on anything daily because we know we'll just batch it Friday anyway.

**PM:** What about the cases where something IS urgent? A genuinely time-sensitive control failure, say.

**Jamie:** I mean, sure, those exist. But in 11 months we've had — maybe two? — events where I would have wanted to know within an hour. And in both cases, our own security tooling caught them first anyway. By the time your alert came in, we already had a ticket open.

**PM:** So if we built a "weekly digest only" mode and turned off everything else by default, would that be a win?

**Jamie:** Yes. That would put me back in the version of this product I liked. Daily would still break our workflow. Real-time would be a non-starter.

**PM:** Last thing — would your team pay more for less? If we had a "calm mode" tier.

**Jamie:** I'd argue internally for it, yeah. We're not price-sensitive on a tool that saves our SOC2 prep. We are sensitive on a tool that makes our team ignore notifications across the board.

---

## PM notes after the call

- Strong, specific signal on notification overload as the churn risk for this account.
- Jamie used the phrase "we've stopped acting on anything daily because we know we'll just batch it Friday anyway." That's behavior, not preference — bigger signal than a stated preference would be.
- Note the two emergency cases: she didn't say "we never need real-time." She said "two cases in 11 months, and our own tooling caught them first." This is nuance worth preserving — don't flatten to "ops doesn't want real-time, ever."
- She volunteered willingness to pay for less. That's the pricing-tier hypothesis worth following up on.
- This is one interview. Don't promote a pattern to insight from one source. Worth opening a hypothesis and watching whether the next 2-3 mid-market ops conversations look similar.
- Stakeholder note: re-engage in 4 weeks before renewal even if I have no news. Silence is the problem here, not the product.
