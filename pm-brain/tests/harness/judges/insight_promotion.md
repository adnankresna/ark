# Judge: insight_promotion

## What we're checking

The brain should promote insights to the durable `knowledge/users/insights.md` layer only when the threshold is met (3+ independent observations of the same pattern from the same persona). This judge runs at multiple turns and the pass condition depends on which turn it's called at.

## You will be given

- The target file: `knowledge/users/insights.md`.
- The turn number this is being called at (1, 4, or 9 in scenario 01-b2b-churn).
- The expected meaning (from `expected.yaml`) — the specific claim being checked.

## Pass criteria by turn

### At turn 1 or 4 (insight NOT promoted yet)

- `knowledge/users/insights.md` does NOT contain a promoted insight for the weekly-batch pattern.
- The pattern may appear in working memory (`ingestion/`) or as evidence on a hypothesis — but NOT as a durable insight.
- Rationale: 1 observation (turn 1) or 2 observations (turn 4) is below the 3-observation threshold.

### At turn 9 (insight promoted, with dissent)

- `knowledge/users/insights.md` DOES contain a promoted insight covering the weekly-batch pattern.
- The promoted insight is **specific** about the persona ("mid-market COMPLIANCE-ops" not "mid-market ops").
- The insight preserves the dissent — there must be an explicit note that an operational-risk subpopulation wants a different cadence (Brex testimony, Notion's ops-risk subteam).
- The insight links to all three supporting interview ingestion records (Acme, Stripe, Notion).

## Fail criteria (must_not)

- Premature promotion at turn 1 or turn 4.
- Flattened promotion at turn 9 ("mid-market ops want weekly cadence" without the compliance-ops qualifier).
- The Brex dissent is missing from the promoted insight or its surrounding context.
- The promoted insight has no evidence trail back to the source interviews.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
