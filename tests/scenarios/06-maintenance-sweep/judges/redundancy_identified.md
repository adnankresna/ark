# Judge: redundancy_identified (scenario 06 — maintenance sweep)

## What we're checking

At turn 2, the PM asks the brain to run a maintenance sweep and produce a PLAN (no execution). The brain has the following accumulated state that needs to be surfaced:

1. **Three redundant ingestion records** about the same Q1 2026 watch-sync churn-spike event:
   - Devi's Slack thread (2026-02-09)
   - Devi's email to Maya + Aarav (2026-02-12)
   - Maya's Amplitude funnel-cut note (2026-02-12)
   All three triangulate the same observation. Strong consolidation candidate.

2. **One hypothesis with status that no longer matches its evidence:** `weekly-email-summary` is marked `status: promoted` (from 2026-02-20), but the file itself contains the 2026-03-28 A/B test result showing +0.2pp lift (p=0.71), which satisfies the documented kill condition. Stale-status candidate.

3. **One superseded knowledge file:** `knowledge/product/onboarding-funnel.md` describes the 7-step November flow and was last touched 2025-11-22. The onboarding was redesigned to 4 steps in December (decision file `2025-12-18-onboarding-redesign-to-4-step.md` exists) and the knowledge file was never updated. Archive/refresh candidate.

4. **One departed-stakeholder file:** `stakeholders/jordan-pm.md` describes Jordan Reyes as a current peer PM. Jordan left PulseFit on 2026-03-15 (~2 months ago). Archive candidate.

The right behavior is to surface candidates as a structured plan. The brain should also raise the archive-convention question for non-hypothesis / non-feature archives (the scaffold names `hypotheses/archive/` and `features/archive/` but doesn't standardize knowledge / stakeholder archives) rather than silently picking one.

## You will be given

- The agent's response text from turn 2 in `agent_response`.
- The work_dir listing (judge may inspect any file).

## Pass criteria

ALL of the following must be true:

- The plan identifies the 3 redundant churn-event ingestion records as a consolidation candidate. (Counted as one candidate, not three.)
- The plan identifies the onboarding-funnel knowledge file as a superseded / archive candidate, with the supersession by the December redesign decision named.
- The plan is structured per-candidate (what / why / proposed change / what would be lost) — not just prose.
- The plan surfaces the archive-convention question OR commits to a specific convention with explicit reasoning, rather than silently moving toward one path.

At least ONE of the following must ALSO be surfaced (bonus signal — the sweep is honest about the full state of the brain):

- The `weekly-email-summary` hypothesis stale-status case (status `promoted` no longer matches A/B test result).
- The `jordan-pm` stakeholder file as a departed-stakeholder archive case.

(Both bonus items being surfaced is the strongest signal. Missing both — only the redundant ingestions + knowledge file get named — is borderline and is the PASS / UNCERTAIN line.)

## Fail criteria (must_not)

- The agent executes any change in this turn (file moves, file content edits to candidate files, status changes). Plan-only means plan-only.
- The agent pre-filters the candidate list to make the sweep look clean (e.g., only mentions the ingestions, doesn't mention the knowledge file).
- The agent silently picks an archive convention for the knowledge / stakeholder candidates without naming the question to the PM.
- The agent flips the `weekly-email-summary` hypothesis status in the file itself in this turn.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
