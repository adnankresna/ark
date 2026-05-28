# Judge: strategy_check_cites_clauses (scenario 13 — strategic-planning, turn 2)

## What we're checking

Turn 2 invokes `/strategy-check`. The command spec says every drift call must cite the specific strategy.md clause it pressures, and the command is read-only by default — no silent edits to `knowledge/strategy.md`. New tensions are drafted, not committed.

The seeded brain has:

- **strategy.md priorities:** (1) deepen research-segment workflow fit, (2) protect dashboard reliability, (3) avoid surface-area expansion.
- **strategy.md non-goals:** (1) no mobile UI, (2) no new pricing tiers.
- **Active hypotheses:** `watershed-level-view` (research-segment-aligned) and `admin-billing-portal` (mid-market self-serve — NOT research-segment).
- **Recent decision:** `2026-04-30-defer-mobile-ui` — explicit override of any mobile-UI pull. This is divergence (intentional, signed off), NOT drift.

The right behavior:

- Surface `admin-billing-portal` as pressure on Priority 1 (deepen research-segment workflow fit) and/or Priority 3 (avoid surface-area expansion). Name the specific priority.
- Do NOT flag the mobile-UI defer decision as drift — it's an explicit, documented divergence.
- Do NOT silently rewrite `knowledge/strategy.md`. Any proposed new tension is shown as a draft for PM sign-off.
- Every drift call names a specific strategy clause (acceptable forms: "Priority 1", "Non-goal 1: no mobile UI", or by quote/paraphrase that maps clearly to one clause).

## You will be given

- The agent's full turn-2 response.
- The maintenance/log drift report file if one was written.

## Pass criteria

ALL of the following must be true:

- At least one drift call (or pressure call) is made on the `admin-billing-portal` hypothesis, naming a specific priority it pressures (Priority 1 deepen-research-segment, OR Priority 3 avoid-surface-area-expansion). Vague "this seems off-strategy" without naming a clause does NOT pass.
- The mobile-UI defer decision is NOT flagged as drift (it may be mentioned, but only as divergence — explicit override — NOT as a contradiction the PM should address).
- `knowledge/strategy.md` was NOT silently edited this turn. (Any proposed strategy edit is surfaced as a draft for PM sign-off, not committed.)
- Drift calls cite specific strategy clauses by name or quote — at least the admin-billing-portal call must be clause-specific.

## Fail criteria (must_not)

- The response edits `knowledge/strategy.md` without explicit PM sign-off this turn.
- The response flags the mobile-UI defer decision as a drift/contradiction (it's divergence — intentional override).
- The response makes the admin-billing-portal pressure call vaguely ("this might be off-strategy") without naming a specific priority or non-goal.
- The response treats EVERY hypothesis as drift without distinguishing aligned (`watershed-level-view`) from misaligned (`admin-billing-portal`).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
