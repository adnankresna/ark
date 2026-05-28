# /plan

Turn a new team objective into a concrete plan: what we know, what we assume, who to interview, which hypotheses to open, which experiments to run, what decision would unlock execution.

## Input

An objective statement. Example: `/plan reduce onboarding drop-off by 20% in Q3`.

## Loads

- `knowledge/strategy.md` (priorities, non-goals, north-star, tensions)
- `knowledge/product/metrics.md` (current values, definitions)
- `knowledge/product/features/` filtered to ones touching the objective
- `knowledge/users/insights.md`, relevant `personas.md` / `segments.md`
- All active `hypotheses/` in the area
- `decisions/` filtered to relevant prior commitments
- `stakeholders/` filtered to people who'd influence or block the plan
- `rules/discovery.md`, `rules/prioritization.md`, `rules/data.md`

## Updates

- A draft `ingestion/adhoc/<date>-plan-<slug>.md` capturing the planning session
- `hypotheses/<slug>.md` — drafts for any value/usability/feasibility/viability/other risk that needs testing (status: `candidate`)
- `decisions/<date>-<slug>.md` — drafts for go/no-go points (status: `pending`)
- `stakeholders/<slug>.md § Open asks` — drafts for the alignment conversations the plan implies

Nothing committed without operator confirmation per autonomy mode.

## Surfaces

Six blocks, in this order:

1. **What we already know** — citations to insights, hypotheses, decisions, metrics
2. **Assumption vs evidence** — explicitly tagged, with provenance for each
3. **Who to interview** — segments, personas, specific named users; recent coverage gaps
4. **Hypotheses to open** — across the 5 risk areas, with the test for each
5. **Experiments to run** — sequenced, with success criteria and what would invalidate
6. **Decision points** — the go/no-go moments and what evidence would unlock each

Plus:

- Constraints from `strategy.md § Non-goals` that bound the plan
- Stakeholder alignment conversations the plan requires (linked to `/prep`)
- One paragraph on what would make the plan unwise (so the operator can falsify it early)
