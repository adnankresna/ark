# Judge: misfit_recognized (scenario 04 — persona emergence)

## What we're checking

Turn 2 ingests an interview with Sam Chen, Hiring Operations Coordinator at MidCo. Sam says explicitly: "I'm not a recruiter and I'm not a hiring manager." Her work is interview scheduling, panel composition, candidate logistics, and cross-team coordination — none of which appears in the JTBD or behaviors of either existing persona (Recruiter sources/screens/owns candidate experience; Hiring Manager makes the hire/no-hire call).

The right behavior is to **recognize the role-fit gap** explicitly — either in the agent's response, in the ingestion synthesis, or in the working-memory insights/observations update — and to **route the signal** to insights/observations rather than forcing it into the closest existing persona. A single interview is below the bar for creating a new persona file; the move at turn 2 is to capture the signal honestly and let it accumulate.

The PM's note in turn 2 explicitly asks the agent NOT to force-fit Sam into either existing persona. The wrong behavior is to (a) describe Sam as a "Recruiter (operational variant)" or "Hiring Manager support staff," (b) silently fold her pain into the Recruiter persona's pain list, or (c) drop the role-fit observation entirely and treat the interview as raw scheduling feedback.

## You will be given

- The target: agent_response and/or the synthesis file(s) written this turn.
- The turn context: turn 2. One interview ingested. Two pre-existing personas (Recruiter, Hiring Manager).

## Pass criteria

ALL of the following must be true:

- The agent's output (response text OR ingestion file OR insights/observations entry) explicitly names that Sam's role does NOT fit either existing persona — at minimum, names what's missing (e.g., "not a recruiter — does not source / screen," "not a hiring manager — does not make hire/no-hire calls").
- The signal from the interview is captured in working memory (`knowledge/users/insights.md` or `knowledge/users/observations.md` or equivalent), with provenance tag(s) from the canonical enum pointing at the source/ or ingestion/ Sam Chen artifact.
- No new persona file is created at this turn under `knowledge/users/personas/`. The directory still contains only the original two.
- The existing Recruiter and Hiring Manager persona files are NOT edited to absorb Sam's pain or behaviors.

## Fail criteria (must_not)

- The agent labels Sam as a sub-variant of Recruiter or Hiring Manager ("Recruiter — operational," "Hiring Manager support") in either the synthesis or in the existing persona files.
- The agent creates a new persona file from this single interview.
- The agent silently edits the Recruiter or Hiring Manager persona file to add Sam's pain points or behaviors.
- The role-fit signal is dropped entirely — the synthesis treats the interview as generic scheduling feedback without naming that the *person* doesn't fit known personas.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
