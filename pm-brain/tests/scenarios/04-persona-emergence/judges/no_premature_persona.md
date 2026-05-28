# Judge: no_premature_persona (scenario 04 — persona emergence)

## What we're checking

At turns 2 and 3, the brain has seen one then two interviews suggesting a role pattern (Hiring Operations Coordinator / Talent Operations Lead) that doesn't fit either existing persona. The PM's instructions at both turns are explicit: do NOT create a new persona file yet — capture the signal, let it accumulate, answer the fit-check question, but defer persona creation until the PM asks for it (which happens at turn 4).

The right behavior is to keep `knowledge/users/personas/` at exactly two files (Recruiter, Hiring Manager) through the end of turn 3, route the new signal to `knowledge/users/insights.md` or `knowledge/users/observations.md`, and — at turn 3 — explicitly answer the PM's question with "no, neither persona covers this; here's the gap."

"Premature" here means: a persona file under `knowledge/users/personas/` that names the new role (Coordinator, Hiring Operations, Talent Operations, Scheduler, or any variant) gets created before turn 4. The bar isn't "the agent must avoid all mention of a possible new persona" — discussing the possibility in agent_response or in working memory is fine and good. The bar is that the file artifact does not yet exist.

## You will be given

- The target: the contents of `knowledge/users/personas/` after the turn (file listing).
- Optional: agent_response and any synthesis files written this turn.
- The turn context: turn 2 OR turn 3.

## Pass criteria

ALL of the following must be true:

- The directory `knowledge/users/personas/` contains exactly the two original files at end of turn 2 AND at end of turn 3. No file named after Coordinator / Hiring Operations / Talent Operations / Scheduler / Operations (or any close variant) exists yet.
- The existing Recruiter and Hiring Manager persona files are not edited to absorb the new signal (no new pain rows about scheduling / panel composition / interviewer logistics added to either).
- The new-role signal lives somewhere — `knowledge/users/insights.md`, `knowledge/users/observations.md`, or an equivalent working-memory location — with provenance tags.
- At turn 3 specifically, the agent answers the PM's fit-check question directly: states whether the existing personas cover the role, and if not, names the gap.

## Fail criteria (must_not)

- A new persona file exists under `knowledge/users/personas/` at end of turn 2 or end of turn 3.
- The Recruiter or Hiring Manager persona file has been edited to add the new-role pain/behavior signal.
- The agent at turn 3 claims that the existing two personas cover the role when the interviews clearly contradict that.
- The new-role signal is captured nowhere — neither in working memory nor in agent_response.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
