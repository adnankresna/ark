# /ideate

Generate solution directions for a problem, grounded in what the brain already knows. Not a brainstorm. A synthesis.

## Input

A problem statement, an opportunity, or a `knowledge/users/insights.md § <theme>` reference. Example: `/ideate onboarding drop-off in mid-market`.

## Loads

- `knowledge/strategy.md` (priorities, non-goals, north-star)
- `knowledge/users/insights.md` and any matching `personas.md` / `segments.md`
- Active `hypotheses/` files in the same area
- Recent `decisions/` that constrain or invalidate options
- `knowledge/market/competitors/` and `trends.md` for adjacent moves
- `rules/discovery.md` and `rules/prioritization.md` if present

## Updates

Drafts only. Nothing committed at call time.

- A draft `ingestion/adhoc/<date>-ideate-<slug>.md` capturing the session
- Hypothesis candidates queued under `hypotheses/<slug>.md § Candidates` (PM confirms before promotion)

## Surfaces

- 3-7 solution directions, each tagged with the evidence supporting it (insight, hypothesis, decision, or market signal)
- For each direction: which strategy priority it serves, which non-goal it might violate, which active hypothesis it would test or contradict
- 1-2 directions explicitly marked as **off-strategy** if surfaced, so the operator can decide whether to pivot strategy or reject the direction
- The thinnest viable next step for the top 2 (a discovery question, an experiment, a competitor study)

Anti-pattern: do not generate directions that ignore the strategy doc or the non-goals. If the evidence forces an off-strategy direction, surface the tension instead of swallowing it.
