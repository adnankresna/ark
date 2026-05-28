# Judge: contradiction_resolved_with_audit

## What we're checking

At turn 6, Maya asks the agent to resolve the strategy-vs-draft-roadmap contradiction, having confirmed with the CEO that strategy v3 remains the live strategy and the draft was never adopted. The agent must resolve the conflict **with full audit trail** — both artifacts retained, status fields updated, cross-links established, and any hypotheses that may have been over-weighted toward the withdrawn direction are walked back with the resolution context.

The wrong behavior is: silently deleting the draft, or rewriting strategy to absorb the draft's framing, or leaving the conflict unresolved despite the explicit ask.

## You will be given

- The agent's response text from turn 6.
- Target files: knowledge/strategy*.md and/or knowledge/strategy/*.md and roadmap files (typically under knowledge/ or a dedicated roadmaps/ tree).

## Pass criteria

ALL of the following must be true:

- The draft Q4 roadmap artifact is still present in the brain (NOT deleted). Its status field is updated to something explicit like `superseded` / `withdrawn` / `not-adopted` with a note explaining why.
- The strategy v3 artifact remains live; its status was not changed to absorb the draft's framing.
- The agent's response or the artifact files establish **bidirectional linkage** between the two artifacts — the draft links to the strategy as the reason it was withdrawn; the strategy notes a draft was attempted and rejected (so a future PM can find it).
- The agent ingested today's conversation with Naomi as a new artifact (e.g., in source/ + ingestion/), making the resolution itself part of the audit record.
- The agent's response names any hypotheses or candidate insights it had previously opened based on the draft direction, and walks them back with the resolution context (or confirms there were none).

## Fail criteria (must_not)

- The draft is silently deleted or hidden.
- The strategy is rewritten to incorporate the draft's social/AI framing.
- The resolution leaves no audit trail (no new ingestion artifact for Naomi conversation, no status field updates, no cross-links).
- The agent claims hypotheses are unaffected without checking, when in fact prior turns produced ones biased by the draft.

## Important

Status field updates can be implemented as a frontmatter field, an explicit `**Status:**` line, or a clearly marked section — any of those is fine. What matters is that the file's role is now machine- and human-readable.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
