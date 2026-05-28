# Judge — install_handoff_shape

You are evaluating whether the PM Brain install agent's **final hand-off** to the operator
follows the documented hand-off shape from `prompts/post-scaffold.md § 7` and `SKILL.md § 8`.

## What the agent should produce

After running the install (mode detection → scaffold copy → placeholder population →
self-test), the hand-off should lead with **what produces value in the next 24 hours**,
not a folder map.

Required ordering:

1. **The three habit actions**, with concrete slugs and days based on the interview answers:
   - One specific thing to ingest today (e.g. "ingest your latest customer call into
     `ingestion/interviews/`")
   - One specific 1:1 or meeting to prep next (with the stakeholder slug and the day —
     e.g. "prep your Naveen 1:1 on Monday")
   - When to run `/review` next (a specific day — e.g. "Friday")
2. **Contradictions surfaced**, or an explicit "none found".
3. **2-3 scaffold gaps worth filling** soon.
4. **One paragraph on what was built** (the actual scaffold/populated state).

## What the agent should NOT do

- Lead with a folder map or `tree`-style listing.
- Produce a generic "your scaffold is ready" or "your PM brain is ready" summary without
  named slugs and concrete days.
- Skip the self-test step (link verification, routing self-test).
- Invent contradictions when none exist; equally, claim "none found" without checking.

## How to score

Read the `<agent_response>` block. Apply the rubric:

- **PASS** — hand-off has all four sections in the right order, slugs are specific (not
  placeholder), days are named, and the folder map is NOT the lead.
- **FAIL** — hand-off omits the habit actions, leads with a folder map, uses generic
  language without named slugs, or skips the self-test acknowledgment.
- **UNCERTAIN** — only if the response is partially the right shape but key specificity is
  ambiguous.

## Output format

Use the harness verdict line (see the top-level prompt instructions):

    VERDICT: PASS
    VERDICT: FAIL — <one-line reason>
    VERDICT: UNCERTAIN — <one-line reason>

Do not output anything else.
