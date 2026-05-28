/strategy-check

Run a full sweep. I want to know: is anything in the recent decisions, hypotheses, or ingestion drifting from `knowledge/strategy.md`?

Per the `/strategy-check` spec:

- **Read-only by default.** Do NOT edit `knowledge/strategy.md` directly. Any proposed new tension or strategy edit is a draft, not a committed change.
- **Cite the specific strategy clause** for every drift call. "Hypothesis X drifts from strategy" without naming WHICH priority or non-goal is noise. Acceptable: "Hypothesis `admin-billing-portal` may pressure Priority 1 (deepen research-segment workflow fit) — mid-market self-serve isn't research-segment work" — naming the clause makes the call legible.
- **Cite the specific evidence** for every drift call (provenance tag from the canonical enum).
- **Apply the tension threshold honestly.** Don't promote a one-off anecdote into a new strategy tension. Recurring + high-confidence + decision-relevant only.
- **Distinguish drift from divergence.** The mobile-UI defer decision is divergence (explicit override) not drift — don't flag it as a contradiction.

You may write `maintenance/log/2026-05-17-strategy-check.md` as a dated drift report.

Surface back: the report sections per spec — strategy clauses under pressure, drifting decisions, drifting hypotheses, watch items, any new tension drafts, closed-loop check. End with "Apply any of these strategy edits? (name which / no)".
