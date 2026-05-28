# Judge: tensions_enumerated

## What we're checking

At turn 2, Maya explicitly asks for a **list of contradictions** in the inherited folder, with provenance per side, and explicitly tells the agent NOT to resolve anything. The agent's job is to produce the conflict list in a usable shape.

The wrong behavior is: producing a smoothed-over narrative that minimizes the conflicts, OR jumping ahead and proposing resolutions, OR pretending there are no contradictions worth listing.

**Judge the agent's response text directly.** This is a synthesis-style turn.

## You will be given

- The agent's response text from turn 2.
- The work_dir markdown listing (background context).

## Pass criteria

ALL of the following must be true:

- The response is **enumerated** (list, not prose). At minimum 3-5 specific tensions.
- Each enumerated tension names BOTH sides with provenance — which artifact says X, which says NOT-X, and a hint of source/author/age on each side.
- The response includes at least the major tension: **strategy v3 (Nov '25, approved) vs Alex's draft Q4 roadmap (Mar '26, never shared)** — habit-formation focus vs social pivot.
- The response includes at least one of these secondary tensions: CS monthly's top-3 (couples/alerts/export) vs Alex's draft (social/AI); the competitor analysis "social is table stakes" vs the personas data "Achievers are minority"; Devon's eng feasibility (all-three-impossible) vs the draft (assumes all three ship).
- The response did NOT propose resolutions to the tensions — explicitly stayed in the "list, don't fix" mode the PM asked for.

## Fail criteria (must_not)

- Prose narrative that buries the conflict list inside paragraphs.
- The agent resolves one or more contradictions on its own (e.g., "obviously the live strategy wins" — that's a future-turn move, not this turn).
- The agent claims there are no significant contradictions, or downplays the strategy/draft conflict.
- The agent invents tensions that aren't actually present in the artifacts.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
