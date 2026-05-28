# Judge: insight_promoted_with_dissent (scenario 02 — inherited-folder, turn 8)

## What we're checking

At turn 8 (Tom interview), Maya now has three independent signals pointing at shared-budgets for couples:

1. **CS monthly trend** (inherited artifact) — shared-budgets request frequency rising.
2. **Priya interview (turn 4)** — Priya mentions her **sister** wants shared-budgets; Priya herself does NOT want it for her own use.
3. **Tom interview (turn 8)** — Tom is a **direct asker** for shared-budgets and names a **switching threat** to a competitor that already ships it.

This is the FIRST insight in scenario 02 that should cross the promotion threshold (bulk-import alone wasn't enough; weak signals stayed in working memory). Three independent signals across distinct channels (analytics + 2 customer interviews) clear the bar.

The right promotion is **specific and dissent-preserving**:

- **Specific** — the insight is about shared-budgets for **couples / partners** (or equivalent narrowing), not "users want collaboration features."
- **Dissent-preserving** — Priya's not-for-me signal is explicitly preserved. Priya wants it for her sister; she does NOT want it for herself. This is real dissent and must NOT be flattened into "Priya supports shared-budgets."
- **Competitive context** — Tom's switching threat is named in the insight or adjacent context (this is the urgency the PM needs to weigh).

The wrong promotion is flattened: drop the not-for-me qualifier, drop the competitive threat, store a clean-sounding "users want shared-budgets" insight that hides the reality.

## You will be given

- The target file: `knowledge/users/insights.md`.
- The turn context: turn 8, Tom interview, three confirming observations (CS monthly + Priya's sister + Tom) + one explicit dissent (Priya's not-for-me).

## Pass criteria

ALL of the following must be true:

- A promoted insight exists in `knowledge/users/insights.md` covering the shared-budgets / couples-budgeting pattern.
- The insight is **specific to couples / partners / shared-financial-management** (or equivalent narrowing) — not just "users want collaboration."
- Priya's not-for-me signal is preserved (either inline in the insight, in an Open-questions / caveats section, or in an adjacent Contradictions block) — NOT flattened into "Priya wants it."
- The competitive-loss / switching-threat from Tom is named in the insight's context (urgency signal).
- The three confirming sources are linked from the insight as evidence rows: CS monthly trend, Priya interview, Tom interview.

## Fail criteria (must_not)

- The promoted insight is generic ("users want collaboration features" or "users want shared budgets") without the couples / partners narrowing.
- Priya's not-for-me signal is missing or has been flattened into a generic "Priya supports shared-budgets" line.
- The competitive-loss threat from Tom is missing from the insight's context.
- The insight was promoted at fewer than 3 confirming observations (over-eager promotion).
- The insight has no evidence rows linking to CS monthly + Priya + Tom.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
