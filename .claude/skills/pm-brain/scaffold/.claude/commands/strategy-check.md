# /strategy-check

Drift check between recent decisions / ingestions / active hypotheses and `knowledge/strategy.md`. Read-only synthesis. Surfaces tensions for the PM to resolve; does NOT silently edit strategy.

## Input

None for a full sweep, or an optional scope:

- `/strategy-check decisions` — last ~10 decisions vs. strategy priorities and non-goals
- `/strategy-check hypotheses` — active hypotheses vs. strategy priorities and non-goals
- `/strategy-check ingestion` — last ~14 days of ingestion vs. strategy (new market shifts, persona evidence, recurring customer signal)

## Loads

- `knowledge/strategy.md` — priorities, non-goals, north-star, current tensions (the anchor — every drift call traces back to a specific clause)
- `decisions/INDEX.md` and the last ~10 decision files under `decisions/`
- `hypotheses/INDEX.md` and all hypotheses with `status: active` or `status: promoted`
- Last ~14 days of `ingestion/` (interviews, meetings, market intel, adhoc)
- `knowledge/market/landscape.md` and any `knowledge/market/competitors/<slug>.md` flagged as moved recently
- `knowledge/users/insights.md` — recurring themes that may pressure a priority or non-goal

## Updates

`/strategy-check` is **read-only by default**. It does NOT edit `knowledge/strategy.md` (per CLAUDE.md "Ask the PM before changing strategy.md").

What it MAY write:

- `maintenance/log/<date>-strategy-check.md` — the dated drift report
- Drafts (not committed) for any proposed `strategy.md § Tensions` entry that crosses the **recurring + high-confidence + decision-relevant** bar from CLAUDE.md § Strategy tension threshold

What it MUST NOT do:

- Silently rewrite priorities, non-goals, or north-star
- Promote a one-off market signal or a single interview into a strategy tension (CLAUDE.md § Strategy tension threshold rejects one-off anecdotes)
- Resolve an existing tension on its own — surface the new evidence, let the PM decide

## Hard constraints

- **Cite the specific strategy clause** for every drift call. "Decision X drifts from strategy" without naming WHICH priority or non-goal is noise. Format: `Decision 2026-05-12-ship-weekly-digest contradicts strategy § Non-goals: "no proactive notifications until Q4"`.
- **Cite the specific evidence** for every drift call. Provenance tag per the enum in [`hypotheses/_SCHEMA.md`](../../hypotheses/_SCHEMA.md). A drift claim without a tagged source is itself orphan evidence.
- **Apply the tension threshold honestly.** Do not draft a new `strategy.md § Tensions` entry unless the signal is recurring (≥2 independent sources), high-confidence (survives the correlational-vs-causal check in CLAUDE.md), AND decision-relevant. One-off anecdotes get logged in the drift report under "watch items" — not promoted.
- **Distinguish drift from divergence.** A decision that explicitly overrides a strategy clause (with a documented reason) is divergence, not drift — surface it, but don't flag it as a contradiction. Drift is when a decision or pattern accumulates *without* anyone noticing it crosses a strategy line.

## Surfaces

The drift report, in this order:

1. **Strategy clauses under pressure** — each named clause (priority, non-goal, north-star, existing tension), with the count of decisions/hypotheses/ingestion items pressuring it, and the strongest single piece of evidence
2. **Decisions that may drift** — recent decisions whose evidence trail or scope conflicts with a named clause. One line per decision: which clause, what specifically conflicts, link to the decision file
3. **Hypotheses that may drift** — active or promoted hypotheses whose belief or test plan contradicts a named clause
4. **Ingestion signals worth watching** — recurring themes from the last ~14 days that pressure a clause but haven't yet crossed the tension threshold
5. **Proposed new tensions (drafts only)** — for any signal that DOES cross the threshold, a one-paragraph draft for `strategy.md § Tensions` with provenance, ready for PM sign-off. Default: do not apply.
6. **Closed-loop check** — any existing `strategy.md § Tensions` entry whose triggering evidence has resolved or grown stale (candidate for archival on next `/review`)

End with: "Apply any of these strategy edits? (name which / no)" — the PM's call, not yours.
