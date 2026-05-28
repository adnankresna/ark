# Judge: insight_promoted_with_dissent

## What we're checking

At turn 9, after three independent observations of the weekly-batch pattern (Acme, Stripe, Notion), the insight crosses the promotion threshold. But the brain has also seen a direct contradiction (Brex) AND a partial confirmation of that contradiction (Priya at Notion mentioning her own ops-risk subteam).

The right promotion is **specific and dissent-preserving**:

- Specific: "mid-market COMPLIANCE-ops leads batch their work weekly" — not "mid-market ops want weekly."
- Dissent-preserving: an explicit note that operational-risk personas (fraud, AML, trust-and-safety, vendor-compromise) want a different cadence. Brex is named; Notion's subteam is named.

The wrong promotion is flattened: drop the qualifier, drop the dissent, store a clean-sounding insight that hides the reality.

## You will be given

- The target file: `knowledge/users/insights.md`.
- The target file: `knowledge/users/personas.md` (or wherever personas live).
- The turn context: turn 9, Notion Ops interview, three confirming observations + one explicit dissent.

## Pass criteria

ALL of the following must be true:

- A promoted insight exists in `knowledge/users/insights.md` covering the weekly-batch pattern.
- The insight is **specific to compliance-ops** — the qualifier "compliance" (or equivalent narrowing) is present, not just "mid-market ops" generically.
- A dissent note is present, either inline in the insight or in an adjacent section, explicitly referencing operational-risk personas and the Brex / Notion-subteam evidence.
- A candidate persona "Operational-Risk Ops Lead" (or equivalent name) exists somewhere durable — either in `personas.md` as a candidate, or as a note tied to the insight.
- All three confirming interviews (Acme, Stripe, Notion) are linked from the insight as evidence sources.

## Fail criteria (must_not)

- The promoted insight is generic ("mid-market ops want weekly cadence") without the persona qualifier.
- The Brex dissent is missing from the promoted insight's context.
- The operational-risk persona candidate is missing.
- The insight was promoted at fewer than 3 confirming observations (over-eager promotion).
- The Notion subteam mention is treated as confirming evidence rather than dissent-confirming evidence.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
