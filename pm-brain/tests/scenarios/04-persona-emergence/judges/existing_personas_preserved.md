# Judge: existing_personas_preserved (scenario 04 — persona emergence)

## What we're checking

The scenario seeds two confirmed personas at turn 1 (Recruiter, Hiring Manager), each with a Last-revised date of 2026-04-02, a job-to-be-done statement, observed behaviors, and pain points tagged to source/ interview artifacts from March 2026. Across turns 2-4, two new interviews surface a third role pattern. The PM's explicit instructions at turns 2, 3, and 4 are that the existing two personas are NOT to be edited — the new signal is additive, not a re-org.

The failure mode this judge guards against: the agent quietly folding the new operational-coordination signal into the Recruiter persona (the closest existing match) by appending a pain row, a behavior observation, or a sub-archetype note. That move loses the signal (Sam and Maya are not Recruiters; they explicitly said so) and corrupts the Recruiter persona's audit trail (claims would now be supported by interviews that aren't about recruiters).

The right behavior: at end of turn 1, exactly two persona files exist with their seeded content. At end of turn 4, three persona files exist — the original two unchanged plus the new candidate persona. The Recruiter and Hiring Manager files at turn 4 should be content-identical to their turn-1 form: same JTBD, same behaviors list, same pain-point rows, same Last revised: 2026-04-02.

## You will be given

- The target file(s): all `.md` files under `knowledge/users/personas/` at the assertion's turn.
- The turn context: turn 1 (initial seed) or turn 4 / final state (additive third persona, originals unchanged).

## Pass criteria

ALL of the following must be true:

**At turn 1:**
- Exactly two persona files exist under `knowledge/users/personas/`: a Recruiter file and a Hiring Manager file (filenames may vary slightly — `recruiter.md`, `hiring-manager.md` are the expected slugs).
- Each persona file contains: a job-to-be-done statement, an observed-behaviors list, a pain-points list (with provenance tags pointing at March 2026 source/ interview artifacts), a Last revised: 2026-04-02 line.
- No third persona file exists.

**At turn 4 / final state:**
- At least three persona files exist: the original two (Recruiter, Hiring Manager) AND the new candidate (Hiring Operations / Talent Operations / close variant).
- The Recruiter and Hiring Manager files are content-identical to their turn-1 form: JTBD unchanged, observed-behaviors unchanged, pain-points unchanged, Last revised: 2026-04-02 unchanged. No rows about scheduling, panel composition, or interviewer logistics have been appended to either.
- The new candidate persona file is clearly marked `proposed` or `candidate`; the two original personas are at their pre-existing confirmed/active status.

## Fail criteria (must_not)

- A Recruiter or Hiring Manager persona file has been edited at any turn after turn 1 — new pain rows added, behaviors expanded, JTBD reworded, or Last revised date bumped.
- The new persona is implemented as a section appended to an existing persona file rather than as a standalone file.
- The two original personas are folded into a single combined file at turn 1, or merged at any later turn.
- A pain row in Recruiter or Hiring Manager cites Sam Chen's or Maya Okonkwo's interview as evidence (those interviews are not about recruiters or hiring managers).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
