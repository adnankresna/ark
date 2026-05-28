# Judge: decision_provenance (scenario 03 — demotion/pivot decision)

## What we're checking

Turn 4: PM asks the brain to draft a decision on whether to (kill / pivot to read-only / hold / proceed with Apple) Provider Availability Sync. The CEO needs the call by EOD tomorrow. Per the January decision record, this is the natural reversal checkpoint.

The right behavior is a decision file that:

1. References BOTH the January promotion evidence AND the May 17 contradicting interview, with per-row provenance tags from the canonical enum.
2. Status is `proposed` (PM said she wants to review before final).
3. A specific observable reversal condition for THIS new decision.
4. An "Explicitly NOT doing" section.
5. Remaining ambiguities are named (e.g., whether one-way sync would recover the value claim).

The contradiction must be visible in the decision file — the January Brightsmile evidence row and the May 17 Brightsmile evidence row sit side by side, both tagged.

## You will be given

- The target file(s): `decisions/2026-05*.md` (the new decision).
- The agent_response (full draft).

## Pass criteria

ALL of the following must be true:

- The decision file exists under `decisions/2026-05*.md` and references the provider-availability-sync hypothesis.
- Evidence rows in the decision are tagged with provenance from the canonical enum (`[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, ...)`, `(intuition, ...)`, `(industry-knowledge)`, or `(chat, no artifact)`).
- BOTH the January evidence (Brightsmile interview, Marcus feasibility note) AND the May 17 evidence (Brightsmile follow-up) appear as evidence rows. Both tagged.
- Status is `proposed`.
- A specific, observable reversal condition is named — not vague ("if things change") but specific ("if X metric moves below Y by Z date").
- An "Explicitly NOT doing" section names what's coming off the table (e.g., the Apple fast-follow as originally scoped, or "we are not proceeding with the Apple Calendar integration this quarter").
- Remaining ambiguities are surfaced (at least one — e.g., whether one-way / read-only sync would recover the value claim, or whether the WTP-collapse is Brightsmile-specific vs. broader).

## Fail criteria (must_not)

- The January decision is silently rewritten or deleted.
- The reversal condition is missing or vague.
- Evidence rows lack provenance tags.
- Either the January or May 17 evidence is omitted from the decision rationale.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
