# Judge: hypothesis_proposed

## What we're checking

After a single customer interview (turn 1, Acme Ops Lead), the agent should have proposed a candidate hypothesis about real-time alerts being negative-value for the customer's persona — BUT should NOT have promoted any insight to the durable knowledge layer.

A single observation is not a pattern. A hypothesis is the right shape; a promoted insight is premature.

## You will be given

- The target file(s): all markdown files under `hypotheses/` (excluding `INDEX.md` and `_SCHEMA.md`).
- The scenario context: this is turn 1. One interview ingested. Pre-existing brain state: empty scaffold.
- The expected meaning (from `expected.yaml`): "a value-risk hypothesis is proposed for real-time alerts (negative value for mid-market ops); status is candidate/proposed, NOT promoted."

## Pass criteria

ALL of the following must be true:

- At least one hypothesis file exists with a section addressing the alert-cadence / notification-volume question.
- The hypothesis's **value-risk** section contains evidence linking to the Acme interview (turn 1).
- The hypothesis status is `candidate`, `proposed`, `active`, or equivalent — anything other than `promoted` / `confirmed` / `decided`.
- Confidence (if scored) is low-to-moderate, reflecting the single-source nature of the evidence.

## Fail criteria (must_not)

ANY of the following triggers FAIL:

- No hypothesis file references the alert-cadence question.
- A `knowledge/users/insights.md` entry has been promoted on the basis of one interview (over-promotion).
- The hypothesis is marked `confirmed`, `promoted`, or `decided` after a single observation.
- Confidence is stated as high (>0.7) on a single-source hypothesis.

## Output format

Exactly one line. Nothing else.

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
