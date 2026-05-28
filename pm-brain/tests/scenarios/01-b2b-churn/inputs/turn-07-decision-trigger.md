# PM prompt to the brain — synthesize the case so far

**Date:** 2026-05-07
**Type:** direct request from the PM to the agent
**Context:** Three weeks into the investigation. Three customer interviews complete (Acme, Stripe, Brex), one eng sync, one analytics snapshot, one internal Slack thread, one stakeholder ask still pending. The PM is asking the agent to synthesize before drafting any decision.

---

## Prompt

> Look at everything we've ingested in the last three weeks on the alert-cadence question. Three customer interviews (Acme, Stripe, Brex), the eng scoping sync, the churn analytics, the internal pricing thread.
>
> I want you to walk through the case. Specifically:
>
> 1. What's the strongest evidence for deferring real-time and shipping calm mode as the default?
> 2. What's the strongest evidence against?
> 3. What's still ambiguous?
> 4. If we shipped weekly-as-default and real-time as opt-in, who would we be serving and who would we be excluding?
>
> Do NOT draft a decision yet. I want to see the case laid out before I commit. Pay special attention to the Brex contradiction — I don't want it buried in the synthesis.

---

## What the PM expects back

A structured response that:

- References each ingested artifact by name (interview slugs, meeting slug, analytics note, slack thread).
- Names the hypothesis (H2 or whatever the agent slugged it as) and its current confidence + risk-area breakdown.
- Explicitly addresses the Brex interview as a contradiction to the dominant pattern, not a footnote.
- Flags what's still missing: the third compliance-ops interview hasn't happened yet, no segmentation pass on what fraction of mid-market customers are ops-risk vs compliance, no quantitative test of the churn-cause hypothesis.
- Names the persona-split insight that emerged from the Brex interview (mid-market ops is actually two personas, not one).
- Does NOT draft a decision file.
- Does NOT recommend a direction yet.

## What the PM does NOT want

- Decision drafted prematurely.
- Brex contradiction flattened into "most customers want weekly, one wanted real-time."
- Vague summary with no traceable references.
- A claim of higher confidence than the evidence supports (only two observations of weekly-batch pattern at this point; not three yet — Notion interview is upcoming).
