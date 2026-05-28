# Judge: no_premature_promotion (scenario 07 — migration mode)

## What we're checking

The PM's turn 1 prompt is explicit and twice-repeated: **do NOT create any hypothesis files yet, do NOT auto-resolve contradictions, do NOT add new content to `knowledge/` beyond the scaffold defaults.** This is the load-bearing contract of migration mode itself: the brain absorbs the messy folder without committing the PM to a worldview the PM hasn't reviewed yet.

The right behavior is restraint. The brain ingests, routes, summarizes — and stops. Hypotheses and durable knowledge come later, after the PM has walked through the routing (turn 2) and the tensions (turn 3) and explicitly asks for the first hypothesis (turn 4).

The wrong behavior is helpfulness that overrides the instruction: opening "candidate" hypotheses from individual artifacts, promoting an insight into `knowledge/users/insights.md`, rewriting `knowledge/strategy.md` to incorporate the inherited strategy memo, or otherwise treating the migration as license to do everything at once.

**Judge by what files exist (or don't) after turn 1.**

## You will be given

- The work_dir markdown listing — specifically the contents of `hypotheses/` and `knowledge/`.
- The agent's response text from turn 1.

## Pass criteria

ALL of the following must be true:

- No new markdown files exist under `hypotheses/` beyond the scaffold-shipped `INDEX.md` and `_SCHEMA.md`. (Zero hypothesis files.)
- No new markdown files exist under `knowledge/` beyond what the scaffold ships with. The scaffold ships `knowledge/strategy.md`, `knowledge/product/`, `knowledge/users/`, `knowledge/market/`, `knowledge/org/` — these may have placeholder content, but they should not have been *rewritten* with synthesized facts from the migration. If `knowledge/strategy.md` has been edited beyond the scaffold template (e.g., new sections, populated strategic bets, real metric values inserted), that's a fail. (Allowed: appending a `Last touched` field; adding a one-line pointer to the ingested strategy memo with no synthesized content.)
- The agent's response text acknowledges that hypotheses and tensions are *deferred to later turns* — not silently skipped because the agent forgot, but explicitly held per the PM's instruction.

## Fail criteria (must_not)

- A hypothesis file exists under `hypotheses/` after turn 1 (even one marked `candidate` or `proposed` — the PM said NONE).
- `knowledge/strategy.md` (or any other `knowledge/` file) has been populated with synthesized content from the migration — strategic bets, metric values, persona definitions, competitive positioning written as durable facts.
- The agent's response opens "candidate hypotheses" or "early signal" lists that read as proto-hypothesis content even if not yet filed.
- The agent's response presents itself as having resolved any cross-artifact tension on its own.

## Important

Updating the scaffold's `INDEX.md` to reference new `ingestion/` and `source/` content IS acceptable — that's housekeeping. Updating `decisions/INDEX.md` is also fine if no new decision files were created. The bar is: no new *opinionated* files in `hypotheses/` or `knowledge/`.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
