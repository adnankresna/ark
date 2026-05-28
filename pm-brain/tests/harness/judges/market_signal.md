# Judge: market_signal

## What we're checking

At turn 3, the PM ingests an analytics snapshot showing mid-market churn up 4 percentage points QoQ, with notification overload cited as a top exit-survey reason. This is correlational, not causal.

The agent should:

- Land the signal in the right durable area (product metrics or market layer).
- NOT bind it directly to the existing hypothesis as if it were proof of the value-risk claim. The sample is small (5/18 churn responses), the cohort is tiny (n=12), and confounders exist.

A causal leap here would inflate confidence on a hypothesis that's still single-source on the customer side.

## You will be given

- The target file: `knowledge/product/metrics.md` (or wherever the agent put the analytics).
- The target file(s): all markdown files under `hypotheses/`.
- The turn context: turn 3, churn snapshot.

## Pass criteria

ALL of the following must be true:

- A durable file in `knowledge/product/` or `knowledge/market/` was updated with the churn signal.
- The signal is recorded with its caveats — sample size, correlational nature, or "watch item" framing.
- The hypothesis's evidence rows were NOT promoted to higher confidence on the basis of this signal alone.

## Fail criteria (must_not)

- The agent fabricates a causal claim ("notifications are driving mid-market churn" — overreach from this data).
- The signal is added as a high-confidence evidence row on the value-risk hypothesis without caveats.
- The signal is dropped or lost (ingested but not propagated to any durable area).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
