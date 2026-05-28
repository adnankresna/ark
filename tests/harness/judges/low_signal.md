# Judge: low_signal

## What we're checking

At turn 5, the PM ingests an internal Slack thread from #pricing in which sales, CS, and marketing discuss real-time vs calm-mode pricing. This is **internal chatter, not customer evidence**. Two of the references in the thread are restatements of customer interviews already in the brain (Acme, Brex via Sam Okafor).

The agent should:

- Land the thread in `ingestion/adhoc/` or a pricing-notes file.
- NOT add this thread as evidence on any hypothesis as if it were customer research.
- NOT double-count Acme's and Brex's previously-recorded positions just because they're mentioned in the thread.

The risk this judge guards against: the brain treats internal stakeholder discussion as customer evidence, inflating false confidence.

## You will be given

- The target file(s): all markdown files under `hypotheses/`.
- The target file: `ingestion/adhoc/*.md` or wherever the agent landed the thread.
- The turn context: turn 5, internal Slack thread.

## Pass criteria

ALL of the following must be true:

- The Slack thread is ingested and lives in `ingestion/adhoc/` (or another non-customer-research location).
- No new evidence rows were added to the hypothesis's value-risk or viability-risk sections on the basis of this thread.
- The Acme and Brex references in the thread did NOT create duplicate evidence rows (the customer evidence already lives in their respective interview ingestion records).
- If anything was promoted, it was the *constraint* from Riku's "tier sprawl" comment as stakeholder context — not as customer evidence.

## Fail criteria (must_not)

- The thread was promoted as customer evidence on any hypothesis.
- Acme or Brex were double-counted as evidence sources because they're mentioned in the thread.
- The thread was ignored entirely (no durable trace at all — should at least land in adhoc with a tagged observation).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
