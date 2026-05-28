# Final piece — decide

I just got off the Diana 1:1. She's a soft yes — she'll approve the auto-approve-under-$50 feature provided we ship it with: (a) a clear audit-trail UI showing every auto-approved item, (b) a fraud-anomaly signal that flags any user whose auto-approved volume exceeds 2x their 90-day baseline, and (c) a per-org admin toggle so customers who want stricter policies can disable auto-approval. She wants to revisit in 90 days post-launch to confirm the fraud-anomaly signal is firing as expected.

Engineering capacity: confirmed (Jordan signed off this morning).

I'm ready to log this as a decision. Use the slash command:

/decide ship-auto-approve-under-50 --resolves <use the slug of the value-risk hypothesis from turn 3>

Per the `/decide` spec:

- Create the decision file at `decisions/2026-05-17-ship-auto-approve-under-50.md` using the full schema in `decisions/_SCHEMA.md`.
- Status: `decided` (Diana signed off this morning; this isn't pending).
- Every Evidence row carries a provenance tag from the canonical enum. COUNT THE TAGS before saving — orphan rows fail the audit.
- The reversal condition must be **observable and specific**. Concretely: "if the fraud-anomaly signal fires on more than 2% of users in any month post-launch, OR if Diana / Finance withdraws sign-off, OR if customer auto-approve disable-rate exceeds 15% within 60 days." Not "if things change."
- "Explicitly NOT doing" section: enumerate at least 2 scopes we're explicitly not pursuing (e.g., raising the threshold above $50, auto-approving line items over $50 with manager override, retroactively auto-approving pending items).
- Stakeholders signed off: Diana Okonkwo (Finance), Jordan Liu (Eng).
- Reflect the hypothesis-status change: the resolved hypothesis flips to `promoted` with a Resolution row linking to this decision file.
- Update `decisions/INDEX.md` and `hypotheses/INDEX.md`.

Surface back: the decision file path + 1-line summary, which hypothesis flipped status, the reversal condition in one line, and the "Apply this decision as drafted? (y / edit / no)" prompt. (For this scenario, assume y.)
