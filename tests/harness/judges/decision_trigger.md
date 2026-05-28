# Judge: decision_trigger

## What we're checking

At turn 7, the PM asks the agent to synthesize the case without drafting a decision yet. This is the "load and reason" step that should precede the actual decision write.

**Judge the agent's response text directly.** This is a synthesis turn; the load-bearing output is the chat-style response, not a new file. (Whether a decision file gets written prematurely is verified by a separate structural assertion at the turn level, not by this judge.)

## You will be given

- The agent's response (verbatim) from turn 7 — this is the primary signal.
- All markdown files under the brain (background context only; do NOT use file presence as evidence either way for this rubric).
- The turn context: turn 7, decision trigger.

## Pass criteria

ALL of the following must be true **in the agent's response text**:

- References every prior ingestion artifact by slug or by clear identifier: Acme/Jamie, Stripe/Marcus, Brex/Sam, eng sync, churn snapshot/analytics, Slack pricing thread.
- Names the Brex interview explicitly as a contradiction (not buried in a "diverse customer feedback" framing).
- Names the persona-split insight from Brex (mid-market ops splitting into compliance-ops and operational-risk-ops).
- Names at least one specific ambiguity or missing piece (e.g. third compliance-ops interview hasn't happened, no segmentation data, no quantitative churn-cause test).

## Fail criteria (must_not)

- The agent's response is a finalized decision write-up (not a synthesis) — the PM explicitly said "do not draft a decision yet."
- The Brex contradiction is flattened in the response ("most customers want weekly, one wanted real-time").
- The agent claims higher certainty than the evidence supports ("we now know that mid-market wants weekly").
- The synthesis is vague — no specific artifact references, just generalities.

## Important

Do NOT base your verdict on what files exist or don't exist in the workdir. The workdir snapshot you see may have been taken after later turns. The only file-state signal that matters is whether the agent's **response** itself reads like a decision write-up rather than a synthesis.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
