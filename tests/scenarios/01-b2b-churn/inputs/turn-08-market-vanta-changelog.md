# Market — Vanta competitor changelog excerpt

**Date:** 2026-05-08
**Source:** Vanta product blog (https://www.vanta.com/blog — public post, excerpted)
**Captured by:** PM (you), pasted into ingestion
**Format:** key excerpts from the post + PM's notes

---

## Excerpt from Vanta blog post

> **Introducing Vanta Real-Time Alerts — for Enterprise plans**
>
> Today we're announcing Real-Time Alerts as part of the Vanta Enterprise plan. Real-Time Alerts deliver in-app, Slack, and PagerDuty notifications within 60 seconds of an evidence-collection state change, with configurable rule routing and escalation paths.
>
> Real-Time Alerts is available as an Enterprise add-on, starting at $5,000/year on top of your base Enterprise subscription.
>
> Real-Time Alerts is built for security operations teams who need to know within minutes — not days or weeks — when a control fails, a misconfiguration appears, or a critical evidence artifact goes stale.

(Customer testimonial included in the post.)

> "We run a 24/7 fraud-detection desk. Knowing within 60 seconds that a key control just flipped means we can route to the on-call analyst before the next batch of flagged transactions clears. Weekly was killing us. Vanta Real-Time fits how our team actually works."
> — Head of Security Ops at a mid-size payments company

(Pricing FAQ excerpted.)

> Q: Why is Real-Time Alerts an add-on instead of part of the base Enterprise plan?
> A: Real-Time Alerts requires additional infrastructure on our side (event streaming, SLO-backed delivery, 24/7 oncall) and serves a specific subset of our customer base. We've priced it as a separate add-on so customers who don't need it aren't subsidizing the cost.

---

## PM notes after reading

- Vanta has just validated **exactly** the Brex use case Sam described last week. Operational-risk teams (fraud, security ops) buying a real-time tier from a compliance-tooling vendor.
- The $5K/year add-on price is a useful anchor for our own pricing if/when we ship this.
- The way Vanta frames the trade-off — "additional infrastructure, 24/7 oncall, served as a separate add-on so customers who don't need it aren't subsidizing" — is the same operational concern Yuki raised in our eng sync. It's an operational responsibility shift, not just a feature add.
- Crucially: **Vanta did NOT make real-time the default.** They kept their existing cadence as the default and added real-time as an opt-in. That's structurally the same as the "weekly-default, real-time opt-in" direction I've been forming.
- This signal binds to **VIABILITY risk** on the alert-cadence hypothesis (can we monetize a real-time tier? — yes, Vanta proves a $5K/year price point works) — NOT to value risk. Value risk for real-time was about whether ops-risk personas want it (Brex showed they do). Viability is whether they'll pay (Vanta showed they will).
- Do not bind this to value risk on the compliance-ops side. That would be a category error. Compliance ops (Acme, Stripe) and ops-risk (Brex, Vanta's testimonial) are two distinct personas with different value functions.
- Also worth flagging: Vanta is the strongest competitor in our segment. Their move here might pull mid-market customers our way if they don't want to pay an extra $5K, OR away from us if they decide they need real-time and we can't offer it. Two-sided pressure.

## Where this should land

- `source/market/2026-05-08-vanta-real-time-alerts.md` (immutable excerpt)
- `ingestion/market/2026-05-08-vanta.md` (tagged observations)
- `knowledge/market/landscape.md` or `knowledge/market/competitors/vanta.md` (durable competitor state)
- Hypothesis viability risk — strengthened evidence
- Should NOT touch value-risk evidence
