# PM prompt to the brain — draft the decision

**Date:** 2026-05-13
**Type:** direct request from the PM to the agent
**Context:** Synthesis complete (turn 7). Third compliance-ops interview confirms weekly-batch pattern (turn 9). Vanta competitor signal confirms viability for the real-time tier (turn 8). Decision direction has emerged: weekly digest as default, real-time as opt-in. Time to commit it to a decision file.

---

## Prompt

> Draft the decision file. Direction:
>
> - Weekly digest becomes the **default** notification cadence for all customers.
> - Real-time alerts ship as an **opt-in** feature, gated to specific user roles (operational-risk personas: fraud, AML, trust-and-safety, vendor-compromise).
> - Opt-in is **per-user**, not per-account (per Priya's constraint at Notion).
> - Real-time is offered as a **paid add-on**, anchored to roughly Vanta's $5K/year price point (subject to pricing team's input).
>
> Status: **pending**. I'm not signing this off until I've reviewed and run it past the eng lead and pricing.
>
> The decision file must include:
>
> 1. **What we're deciding** — one paragraph, plain language.
> 2. **Why** — references to the supporting evidence by name (Acme, Stripe, Notion interviews; eng feasibility scoping; Vanta competitor signal; churn analytics).
> 3. **What we explicitly considered and rejected** — both extremes: (a) ship real-time as the default for everyone, (b) don't ship real-time at all.
> 4. **The Brex dissent** — name it explicitly. The decision should not pretend the case was unanimous. Brex wanted real-time and our chosen direction serves them via opt-in. Acknowledge the trade-off.
> 5. **What would reverse this** — a SPECIFIC, OBSERVABLE condition. Not vague ("if things change"). Something a maintenance sweep could detect.
> 6. **Decision date and status** — 2026-05-13, status: pending.
> 7. **Evidence trail** — working markdown links to: the hypothesis file, three customer interview ingestion records, the eng sync, the Vanta market source. Two clicks deep means I can walk decision → hypothesis → source/.
>
> Don't claim more certainty than the evidence supports. The persona-split insight is fresh (3 confirming + 1 dissent = 4 total observations); the operational-risk persona is still a candidate (2 observations, needs 3); the churn-cause hypothesis is still circumstantial. Be honest about all of that in the decision write-up.

---

## What the PM expects in the decision file

A markdown file under `decisions/` named with the date and a clear slug (e.g., `2026-05-13-defer-real-time-default-add-opt-in.md`). The 7 sections above, in order. Working links throughout. A reversal condition that's specific enough that the weekly `/review` sweep could check it.

## What the PM does NOT want

- A decision file with no reversal condition, or a vague one like "if customer feedback changes."
- The Brex dissent buried, footnoted, or left out.
- Overstated confidence ("we now know that...").
- Status marked as `decided` — the PM wants to review first.
- Made-up evidence rows. Only cite what's actually been ingested.
