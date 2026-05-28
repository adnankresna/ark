# Bulk seed — decision-lifecycle scenario

Sam here. I'm seeding three artifacts in one go so the brain has context for the next three turns. Process each in turn, preserve source, route to ingestion, and update durable knowledge where appropriate. Today is **2026-05-17**.

---

## Artifact 1 — Stakeholder file: Diana Okonkwo

Create `stakeholders/diana-okonkwo.md` with this profile (use the stakeholder schema):

- **Name:** Diana Okonkwo
- **Role:** Head of Finance
- **Influence:** High
- **Friction:** Medium — Diana is rigorous about expense-policy compliance; pushes back on anything that loosens approval workflows. She has historically blocked one feature (the "manager-bypass for travel under $200" proposal in 2025).
- **What they care about:** SOX compliance, audit-trail integrity, fraud-risk metrics, finance-team workload (her team reviews ~14K expense reports/month).
- **Concerns / watch-outs:** Diana will object to any auto-approval mechanism unless it ships with (a) a clear audit trail, (b) a fraud-detection signal, and (c) a per-org opt-out for customers who want stricter policies.
- **Last touched:** 2026-04-22 (Q2 budget review meeting)
- **Cadence:** Biweekly 1:1 — she prefers face-time on policy changes.

Also add a row to `stakeholders/INDEX.md`.

---

## Artifact 2 — Roadmap entry: auto-approve-under-$50

Add an entry under `knowledge/product/features/auto-approve-under-50.md` (or whatever the feature-folder convention is):

- **Feature:** Auto-approve expense reports under $50 per line-item.
- **Status:** Proposed.
- **Owner:** Sam Liu (PM).
- **Brief:** Currently every line-item, regardless of amount, requires manager approval. Customer feedback suggests this is friction for the 70%+ of line-items that are under $50 (coffee runs, parking, small office supplies). Auto-approving these would meaningfully reduce manager review time.
- **Open questions:** Does it create fraud risk? Does it conflict with Diana's policy guardrails? What's the customer-segment breakdown (mid-market vs enterprise tolerance)?

If the feature folder doesn't exist yet, create the file at `knowledge/product/features/auto-approve-under-50.md`.

---

## Artifact 3 — Source interview: Marcus Lee, BrillStone (Operations Manager)

Preserve at `source/interviews/2026-04-30-marcus-lee-brillstone.md`, route synthesis to `ingestion/interviews/2026-04-30-marcus-lee-brillstone.md`. Verbatim transcript follows:

> **Sam (PM):** What's the single biggest friction for you in FlowExpense right now?
>
> **Marcus Lee (Operations Manager, BrillStone — mid-market, ~$32K ARR):** Approval queue length. I'm a manager. I get notified to approve 30-50 line items a day, and 80% of them are like, a $4 coffee. I literally just click approve, approve, approve. It's not adding value. If we could auto-approve anything under, say, $50, my approval queue would drop by like 70% and I could spend that time on the actual policy edge cases.
>
> **Sam:** Would your finance team be OK with auto-approval under $50?
>
> **Marcus:** Our finance lead would love it. She's the one who keeps pinging me about my approval backlog slowing month-close. She'd want some kind of weekly review report on auto-approved items, just to spot-check, but she wouldn't object to the principle.
>
> **Sam:** Any concerns about fraud?
>
> **Marcus:** Honestly, at $50 per line-item, the fraud surface is tiny. Even if someone submitted ten $50 items a week, that's $500. We have employees who expense more than that on lunch with clients. The bigger fraud risks are way upmarket of $50.

In your synthesis, flag this as a recurring theme — I've heard variants of "auto-approve small items" from at least three other mid-market customers in the last two months. This is one of those signals worth tracking carefully.
