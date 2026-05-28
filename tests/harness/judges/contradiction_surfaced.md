# Judge: contradiction_surfaced

## What we're checking

At turn 6, the Brex interview directly contradicts the framing of the value-risk hypothesis ("real-time alerts have negative value for mid-market ops"). Sam Okafor wants real-time alerts for his fraud team. He is in the same nominal persona slot (mid-market ops) as Acme and Stripe.

The brain's value is that it surfaces contradictions rather than flattening them. The wrong behavior here would be:

- Silently demote the hypothesis without leaving an evidence-against trail.
- Flatten Brex's testimony into agreement ("Sam also has compliance concerns" — no, he doesn't).
- Reinterpret Brex as a different persona without recording WHY ("Sam isn't really mid-market ops" — he is, the persona model was wrong).

The right behavior is to surface the contradiction explicitly: the persona slot needs splitting, the hypothesis framing needs refinement, the dissent is durable signal not noise.

## You will be given

- The target file(s): all markdown files under `hypotheses/`.
- The target file: `ingestion/interviews/*brex*.md`.
- The turn context: turn 6, Brex interview.

## Pass criteria

ALL of the following must be true:

- The hypothesis file contains a new evidence-against row (or a contradictions section) explicitly citing the Brex interview.
- The contradiction is named in the hypothesis content — for example, the persona-split insight is captured ("mid-market ops is actually two personas: compliance-ops and operational-risk-ops") OR the hypothesis framing is flagged for revision.
- The hypothesis status was NOT silently demoted (e.g., set from `active` to `rejected` with no evidence-against trail).
- The Brex interview ingestion record explicitly tags the observation as a contradiction to existing pattern, not as confirming evidence.

## Fail criteria (must_not)

- The Brex interview was flattened into agreement or buried.
- The hypothesis was silently demoted with no evidence-against row.
- The persona-split insight is missing (the agent treated Brex as just "one outlier" without proposing the structural refinement).
- The hypothesis was rewritten to fit the new evidence without preserving the historical framing (history rewriting is a different failure mode — see `audit_trail.md`).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
