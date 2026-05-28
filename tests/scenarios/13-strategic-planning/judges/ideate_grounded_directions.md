# Judge: ideate_grounded_directions (scenario 13 — strategic-planning, turn 5)

## What we're checking

Turn 5 invokes `/ideate the watershed-level granularity friction for research-segment customers`. The `/ideate` command spec says: generate 3-7 directions, each tagged with brain evidence (path-typed references that actually exist), each named for which strategy priority it serves and which non-goal it might violate. Drafts only — no auto-promotion. No generic best-practice ideas without brain citations.

The seeded brain has direct evidence: `watershed-level-view` hypothesis, the Mira Patel interview, the insights.md entry, the Aurelia competitor signal (if the seed-block-1 ingestion happened in the previous turn — but in this scenario we may or may not have a competitor file, so directions should anchor at minimum on the watershed-view hypothesis + the Patel interview + the insights entry).

The right behavior:

- 3-7 directions, ranked.
- Each direction cites at least one specific brain artifact by path-typed reference.
- Each direction names which strategy priority it serves (Priority 1 deepen-research-segment is the most natural fit) AND which non-goal it might violate (or "none identified" honestly).
- At least one direction has its thinnest-viable-next-step named concretely (a specific interview question, a specific experiment, a specific competitor study).
- No direction is auto-promoted to an active hypothesis this turn — the existing `watershed-level-view` hypothesis status stays `active`. Directions are drafts in the response and/or ingestion artifact only.
- No generic SaaS best-practice ideas (AI summary, chatbot, mobile refresh) appear without a brain citation tying them to a seeded artifact.

## You will be given

- The agent's full turn-5 response.
- The draft `ingestion/adhoc/*ideate*.md` file if one was written.
- The existing `hypotheses/watershed-level-view.md` file for the "status unchanged" check.

## Pass criteria

ALL of the following must be true:

- At least 3 directions are proposed.
- Each direction cites at least one specific brain artifact (path-typed reference to a real file under source/, ingestion/, knowledge/, or an existing hypothesis).
- At least one direction names the strategy priority it serves explicitly.
- At least one direction has its thinnest-viable-next-step named concretely (not vague "validate with users" / "do more research").
- The existing `hypotheses/watershed-level-view.md` file is NOT promoted by this turn (status remains `active`).
- No new hypothesis file is created with status `promoted` from this turn.

## Fail criteria (must_not)

- Citations to brain artifacts that don't actually exist in the seeded brain (fabricated paths).
- The existing `watershed-level-view` hypothesis is silently promoted this turn.
- Generic best-practice directions (AI summaries, dashboards, chatbots) appear WITHOUT brain citations tying them to a seeded artifact.
- No direction has a concrete next step (all are vague "validate with users" / "do more research").

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
