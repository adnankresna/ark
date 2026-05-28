# Customer interview — Brex, Ops Lead (fraud team)

**Date:** 2026-05-06
**Duration:** 40 minutes
**Interviewer:** PM (you)
**Interviewee:** Sam Okafor, Ops Lead supporting Brex's internal fraud team (mid-market segment for our product, ~120 employees total but the fraud team is 8 people running 24/7 coverage)
**Channel:** Zoom, recorded with consent, transcribed

---

## Context

Sam reached out via Customer Success specifically requesting a call. The trigger was a feature-request email he sent two weeks ago asking about real-time alert capability. He's been a customer for 7 months on the mid-market tier.

This interview was deliberately scheduled in the same week as the Acme and Stripe conversations to keep mid-market findings consistent. The expectation going in was that this would be another data point for the "weekly batch" pattern. It wasn't.

---

## Transcript (abridged, key sections only)

**PM:** Thanks for the time, Sam. I saw your feature request — wanted to understand the use case before we look at it.

**Sam:** Yeah, so — the way I run this team is different from a typical compliance ops setup. We're fraud, not SOC2. Our window from "something looks wrong" to "we need to act" is measured in minutes, not days. If your tool catches an anomaly in our flagged-transaction review pipeline, I need to know within ten minutes. Otherwise I'd rather not have the alert at all.

**PM:** That's the opposite of what I've been hearing from other mid-market ops folks. Most of them want weekly batched digests, not real-time. Can you help me understand the difference?

**Sam:** I think you're talking to compliance ops. Compliance is a weekly job. Fraud is not. Our entire job is real-time response. If I'm using your tool the same way an Acme or a Stripe is using it, then yes, daily is too much. But if I'm using it to backstop my fraud-detection workflow, then weekly is too slow to be useful.

**PM:** So you're using the same feature set as a compliance ops team, but applying it to a fundamentally different operational tempo.

**Sam:** Exactly. We bought this product because the evidence-collection layer is solid and we needed something to feed our internal SOC. The fact that everyone else uses this for monthly audits and weekly reviews is fine for them. We need something with a different cadence. If real-time isn't on the roadmap, we'd seriously look at building something internal or moving to a tool that does it natively. We have budget. The pricing tier doesn't matter — we'll pay for the right cadence.

**PM:** How many other customers do you think are using the product the way you are?

**Sam:** Honestly? I don't know. Fraud teams in mid-market companies are a small slice. But I'd bet there are more of us than you think — anyone running fraud, risk, AML, trust-and-safety in a mid-market company has a similar tempo. The compliance-ops branding probably hides us.

**PM:** Last question — if we shipped weekly digest as the default and made real-time an opt-in feature, would that work for you?

**Sam:** That would be ideal, actually. I don't want to fight your defaults for the rest of our contract. Let me opt in to the cadence I need. Let everyone else have the calm version.

---

## PM notes after the call

- This is a direct contradiction to the pattern I've been building from Acme and Stripe. Sam is also mid-market. He also runs an ops function. He is the exact persona slot. But his use case is fundamentally different.
- The right framing is NOT "Sam is an outlier, ignore him." It's "the persona slot I've been treating as one — mid-market ops lead — is actually two: compliance ops (weekly tempo) and operational-risk ops (real-time tempo). I've been over-generalizing."
- Critical: the hypothesis I opened after the Acme interview said "value risk: real-time alerts have negative value for mid-market ops." That framing is now wrong. The framing should be "negative value for mid-market COMPLIANCE ops, positive value for mid-market OPERATIONAL-RISK ops."
- Do NOT silently demote the hypothesis. The Acme/Stripe pattern is real for compliance ops. What I need to do is split the persona and re-scope the hypothesis. The dissent here is the signal, not the noise.
- Sam volunteered the "opt-in real-time" design. That's the synthesis of both patterns: weekly batch as default (Acme/Stripe), real-time as opt-in (Brex). Worth opening as a candidate decision direction, not committing to it yet.
- Pricing signal: "the pricing tier doesn't matter — we'll pay for the right cadence." Tag as viability evidence, separate from the value-risk reframe.
- Open follow-up: how many of our mid-market customers are operational-risk vs compliance ops? Need to ask Customer Success for a segmentation pass. The persona split should be evidence-backed before it becomes durable.
