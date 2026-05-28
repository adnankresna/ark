# Customer interview — Notion, Ops Lead

**Date:** 2026-05-12
**Duration:** 35 minutes
**Interviewer:** PM (you)
**Interviewee:** Priya Iyer, Ops Lead, Notion (compliance + a small operational-risk subteam under her)
**Channel:** Zoom, recorded with consent, transcribed
**Context source:** booked deliberately as the third mid-market compliance-ops conversation, to test the weekly-batch pattern with one more independent source before deciding whether to promote it.

---

## Transcript (abridged, key sections only)

**PM:** Priya, thanks for making time. Walk me through how your team uses our product.

**Priya:** Sure. I lead the ops function — primarily compliance, SOC2 + ISO 27001 cycles. The way I use your tool is the weekly Friday rhythm. Friday is when I do compliance. The rest of the week I'm doing real ops work — incident postmortems, vendor reviews, internal audits, the actual work.

**PM:** So the tool fits the Friday rhythm cleanly?

**Priya:** It fits the Friday rhythm cleanly because I made it fit. I have a rule that auto-archives anything from your tool except the digest. Otherwise the volume of in-app and Slack alerts would drown out things that actually need my attention during the week. I'm not the only one — three or four of my peers in the ops-lead Slack community have set up similar filters.

**PM:** Would your team pay more for a tier that delivers only the weekly digest, with the rest of the noise off by default?

**Priya:** Genuinely yes. We're not a price-sensitive account on this tool. We're sensitive on a tool that adds workflow friction. A "calm mode" or "compliance-only mode" tier would be an easy budget conversation for me.

**PM:** One thing I want to test. We've heard from one customer — Brex — that their fraud team specifically wants real-time alerts from us. Different use case, different cadence. Does that resonate with anything in your team?

**Priya:** Actually, yes. I have a two-person operational-risk subteam under me — they handle vendor compromise, account takeover incidents, that kind of thing. They've separately asked me if we can get real-time alerting from your tool. I told them we can't, and they've routed around it by piping data from your tool into their own SIEM.

**PM:** So if we offered real-time as an opt-in feature, gated to the right roles, your ops-risk subteam would want it?

**Priya:** Yes, probably. But — and this is important — I would NOT want that to be the default for my compliance team. We've spent 18 months tuning out the noise. If real-time alerts became the default, even with an opt-out, I'd be back to fighting filters.

**PM:** That's exactly the design direction I'm forming. Weekly digest as the default, real-time as an opt-in gated to ops-risk personas. Does that sound right?

**Priya:** That sounds like the right shape, yeah. Default-on real-time would be a deal-breaker for compliance teams like mine. Default-off real-time with an opt-in path would serve the ops-risk subteams without breaking the compliance workflow.

**PM:** Anything else I should know before I draft this?

**Priya:** Just — please make sure the opt-in is per-user, not per-account. If it's per-account, I'd have to choose between my compliance workflow and my ops-risk subteam, and that's not a choice I want to make.

---

## PM notes after the call

- Third independent observation of the weekly-batch pattern (Acme, Stripe, now Notion). Threshold for insight promotion met (3+ independent observations from the same persona).
- BUT — and this is critical — Priya independently surfaces the same persona-split insight that came from Brex: within a single mid-market account, there can be compliance-ops users (weekly cadence) AND ops-risk users (real-time cadence). Same account, different personas.
- This means the persona-split is not a fluke from one Brex conversation. It's a real structural distinction. The Brex dissent was not noise; it was a signal that the persona model needed splitting.
- Promotion direction: yes, promote "mid-market compliance ops batch their work weekly" to a durable insight. BUT preserve the dissent: the "compliance ops" qualifier is load-bearing. Don't promote a flattened version like "mid-market ops want weekly cadence."
- Priya's per-user vs per-account design constraint is important and should land in the eventual decision draft, not just as a feature note.
- Stakeholder note: Priya is mid-touch, low-friction. Renewal not until next year. Worth treating as a design partner for the calm-mode rollout if it ships.

## Where this should land

- `source/interviews/2026-05-12-notion-ops.md` (immutable)
- `ingestion/interviews/2026-05-12-notion.md` (tagged observations)
- `knowledge/users/insights.md` — PROMOTE: "Mid-market COMPLIANCE-ops leads batch their compliance work weekly; treat weekly as the natural cadence for this persona." With explicit dissent preservation: "Note: mid-market OPERATIONAL-RISK personas (fraud, AML, trust-and-safety, vendor-compromise) want a real-time cadence. Same account can contain both."
- `knowledge/users/personas.md` — propose new persona: "Operational-Risk Ops Lead" alongside the existing "Compliance Ops Lead" persona. Status: candidate, needs one more independent observation.
- Hypothesis value-risk evidence: strengthened for the weekly-default direction; dissent row preserved.
- Stakeholder file for `notion-ops.md`.

## What this turn does NOT do

- Does NOT draft a decision. That's the next turn.
- Does NOT collapse the Brex dissent into the promoted insight. The dissent is part of the durable knowledge now.
- Does NOT promote the new "Operational-Risk Ops Lead" persona to confirmed. Brex + Priya's subteam = 2 observations from the same persona type, threshold is 3.
