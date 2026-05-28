# Judge: decision_provenance

## What we're checking

At turn 9, Maya asks for a Q4 decision file with **per-row provenance** — each evidence row must let the reader see at a glance whether it was inherited-and-not-re-validated, vs Maya-collected-and-fresh, vs from a function (CS / eng).

This is the load-bearing migration-mode property: a decision drafted from mixed-trust evidence must wear its trust profile on its face. If a future stakeholder asks "how much of this is the new PM's read vs the old PM's leftover claims?", the decision file should answer that without spelunking.

## You will be given

- Target files: decisions/*.md
- The PM's turn-9 prompt for context.

## Pass criteria

ALL of the following must be true:

- The decision file exists under `decisions/` with a clear filename including date.
- Status is `pending` per the canonical decision schema (`pending | decided | superseded`), or `proposed` as a synonym — i.e., the decision is opened but not yet finalized. NOT `decided` (the PM explicitly said don't pre-decide).
- Each evidence row or citation in the decision file carries a **provenance tag** — visible markers like `(inherited, Alex's interview Feb '26)`, `(Maya-collected, May 11)`, `(CS data, monthly Apr '26)`, `(eng, Devon May 12)`. The mechanism can be inline parentheses, a dedicated provenance column in a table, or an `**Author:**` / `**Source-trust:**` field per row — any explicit, scannable form is fine.
- The decision honors the live strategy (habit-formation north star) and does NOT covertly pivot to the withdrawn social/AI direction. If the decision proposes anything that bends strategy, it is explicitly flagged as a strategy-amendment proposal, not absorbed silently.
- The decision contains a **specific, observable reversal condition** — e.g., "If, in the next 90 days, fewer than 15% of MAU enable the shared-budget invite flow once shipped, revisit" or similar. Vague conditions ("if things change") fail.
- The decision includes a "what we're explicitly NOT doing in Q4 and why" section, with evidence backing each NOT.
- The decision names at least one remaining ambiguity (e.g., persona data is 20 months old; AI insights pricing unresolved).

## Fail criteria (must_not)

- No provenance tagging — evidence rows cited without indicating inherited vs Maya-collected vs functional source.
- Status marked `decided`.
- Covertly resurrects the withdrawn Q4 draft direction (e.g., includes friend leaderboards without flagging it as a strategy bend).
- Vague or missing reversal condition.
- Made-up evidence rows not traceable to any artifact in the brain.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
