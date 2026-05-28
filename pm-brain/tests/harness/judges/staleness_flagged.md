# Judge: staleness_flagged

## What we're checking

At turn 7, Maya asks for a staleness pass — which artifacts in the brain should she be careful about treating as current, and what should she do about them (retire / refresh / flag-and-keep).

The agent's job is to apply **calibrated staleness judgment**, not blanket-age-based. For example: strategy v3 is 6 months old but was confirmed live yesterday → flag-and-keep. The personas research is 20 months old and untested → refresh. The contractor competitor analysis is 18 months old with shifting market → retire-or-refresh.

The wrong behavior is: marking everything stale by age, OR ignoring the staleness ask, OR proposing aggressive deletion without flagging context.

**Judge the agent's response text directly.** Synthesis-style turn.

## You will be given

- The agent's response text from turn 7.
- The work_dir markdown listing.

## Pass criteria

ALL of the following must be true:

- The response addresses each of the artifacts Maya explicitly named (personas, strategy v3, competitor analysis, Q3 roadmap, Devon's feasibility note) and labels each with a clear recommendation: retire / refresh / flag-and-keep (or equivalent action).
- The response distinguishes **age** from **staleness** somewhere — e.g., strategy v3 is 6 months old but should be flag-and-keep (just confirmed by CEO), while personas at 20 months should be refresh (drives roadmap, untested).
- For each "refresh" recommendation, the response names *what* would need re-running (e.g., personas → segmentation survey + small-n interview round; competitor analysis → fresh scan including Monarch's couples-segment numbers).
- The response surfaces at least one staleness-flag the PM did NOT name explicitly — e.g., one of Alex's 2026 interviews could be flagged as "single source, no follow-up, low-strength" if not already done.

## Fail criteria (must_not)

- Blanket "everything over 12 months should be retired" — that's mechanical, not judgment.
- Ignores the explicit instruction to be conservative ("rather over-keep than over-retire").
- Recommends retiring strategy v3 despite Naomi's explicit confirmation yesterday.
- Produces a flat list with no recommendations attached.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
