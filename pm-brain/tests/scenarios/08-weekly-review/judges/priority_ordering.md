# Judge: priority_ordering (scenario 08 — weekly /review)

## What we're checking

The PM has explicitly asked the brain to "order what you surface by what should be on my Monday list — what blocks active work first, what's drifting next, what can wait noted last." A holistic /review that names all five categories but treats them as equally important fails the actual ask — the value is not just surfacing, it's prioritizing.

The right ordering, given the seeded state, puts time-pressured / active-work-blocking items first:

- **Tier 1 (blocking active work / time-pressured):** the stale-relevant stakeholder Ravi Chen (7 weeks since last 1:1, owns the engineering risk on the bet that just took a partial contradiction) AND the expiring March-10 reversal condition (2 weeks until the NPS deadline). The drift on alert-noise-reduction is also in this tier — it directly affects the headline Q2 commitment.
- **Tier 2 (drifting / worth questioning but not urgent):** the aging insight on alert-grouping-by-service. Single-source, 4 months old, not contradicted — worth questioning whether it should still be in the active themes section, but waiting another week costs nothing.
- **Tier 3 (healthy / noted for tracking only):** the api-latency-p99-vs-p95 hypothesis. Quietly working. Noted at the end, not in the action column.

The ordering must be **explicit** — a numbered list, section headers ("Blocking this week / Drifting / Aging / Healthy"), tier labels, "first / then / finally" prose, or comparable structure. A flat unordered dump that names all five but does not signal priority fails this judge.

This judge is applied to BOTH turn 3 (the review itself) AND turn 4 (the top-two pick). For turn 4, the pass criterion is that the top-two picks are drawn from Tier 1 items, not from Tier 2 or Tier 3.

## You will be given

- For the turn-3 application: the agent's `/review` response text in `agent_response`.
- For the turn-4 application: the agent's top-two-pick response text in `agent_response`.

## Pass criteria

ALL of the following must be true:

**For turn 3:**

- The /review response uses an explicit ordering structure (numbered list, ordered headers, tier labels, or comparable). A flat bullet list with no priority signal fails.
- At least one of {stale-relevant-Ravi, expiring-reversal-March-10} appears in the response BEFORE the aging insight on alert-grouping-by-service. (Both before is stronger; one is the floor.)
- The healthy api-latency-p99-vs-p95 hypothesis appears in the response AFTER all the items in Tiers 1 and 2 — not at the top, not interleaved with the action items.
- The drift on alert-noise-reduction appears either in Tier 1 (with the stakeholder + reversal items) OR explicitly framed as the headline finding that drives Tier 1's urgency — not buried below the aging insight.

**For turn 4:**

- The top-two picks are both drawn from {stale-relevant-Ravi, expiring-reversal-March-10, drift-on-alert-noise-reduction} (the time-pressured / active-work-blocking set).
- The healthy api-latency hypothesis is NOT in the top two.
- The aging insight (alert grouping by service) is NOT in the top two, UNLESS the brain has made an explicit defended case for why it leapfrogs the time-pressured items (e.g., a new corroborating signal arrived that the judge missed). Default: not in top two.

## Fail criteria (must_not)

- Turn 3 produces a flat unordered list of five items with no priority signal.
- Turn 3 places the aging insight or the healthy hypothesis ahead of the stale-relevant stakeholder AND the expiring reversal condition.
- Turn 4 picks the healthy api-latency hypothesis as one of the top two.
- Turn 4 picks the aging insight without a defended case for why it leapfrogs the time-pressured items.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
