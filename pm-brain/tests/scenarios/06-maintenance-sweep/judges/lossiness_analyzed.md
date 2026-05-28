# Judge: lossiness_analyzed (scenario 06 — maintenance sweep)

## What we're checking

At turn 3, the PM asks the brain to walk through what specifically would be lost by each candidate change from turn 2. The PM is explicit that she wants **concrete answers, not generic safety theater**. "No signal lost" is a valid answer where true — but it must be justified ("the same observations are preserved verbatim under `source/...`") rather than asserted.

The right behavior is per-candidate lossiness analysis along the dimensions the PM named:
1. Signal loss (would a distinct quote / number / claim disappear?)
2. Link loss (would any inbound reference go dead?)
3. Audit trail loss (would a downstream artifact still resolve to something meaningful?)
4. For the 3 redundant ingestions specifically: what would the consolidated record need to preserve to keep all 3 perspectives readable (Devi's CS framing, Marco's ticket pattern, Maya's Amplitude funnel cut).
5. For the weekly-email-summary hypothesis specifically: what would demotion erase vs. leave it.
6. For the onboarding-funnel knowledge file specifically: do the November funnel numbers survive elsewhere (e.g., in the December redesign decision's evidence rows).
7. For the jordan-pm stakeholder file specifically: any active reference to Jordan in any current decision / hypothesis / knowledge that would break.

## You will be given

- The agent's response text from turn 3 in `agent_response`.
- The work_dir listing (judge may inspect any file to verify the lossiness claims).

## Pass criteria

ALL of the following must be true:

- The agent addresses each candidate from the turn 2 plan individually — not as a single "all changes are safe" block.
- For the 3 redundant ingestion records, the agent names what the consolidated record would need to preserve to keep the 3 perspectives (CS framing, ticket pattern, Amplitude funnel-cut numbers) readable — OR explicitly references that the 3 source/ artifacts stay untouched and would remain the audit anchor.
- For the onboarding-funnel knowledge file, the agent addresses whether the November numbers survive (typically: yes, they're cited in the 2025-12-18 redesign decision's evidence rows; OR the November file is preserved in archive, so the numbers don't disappear).
- For the jordan-pm stakeholder file, the agent addresses inbound references — either by naming specific files that reference Jordan, or by stating "no active references found" (a verifiable statement the structural check can confirm).
- Where the agent says "no signal lost," there is a specific reason given (path to where the signal survives, structural argument for why the loss is bounded). Bare assertions of safety fail.

## Fail criteria (must_not)

- Generic answers like "all proposed changes are safe" / "no major losses" without per-candidate breakdown.
- Skipping any candidate from the prior turn (if turn 2 named 4 candidates, turn 3 must address 4).
- Claiming a number / quote survives elsewhere without naming where.
- Resolving the hypothesis situation here (this turn is still analysis, not execution — and the PM hasn't approved anything yet).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
