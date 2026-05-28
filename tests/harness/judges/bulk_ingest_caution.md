# Judge: bulk_ingest_caution

## What we're checking

At turn 1, the new PM (Maya) bulk-imports an entire inherited folder — 10 artifacts of mixed type, mixed author, mixed age. The right behavior is **high-volume ingestion with low-volume promotion**: the brain should preserve every artifact verbatim, tag provenance and age, surface candidate hypotheses, and resist over-promotion driven by volume.

The wrong behavior is treating 10 inherited artifacts as 10 independent observations and walking out with a fully-formed model of the world after a single bulk turn.

**Judge the agent's response text AND the files it wrote.**

## You will be given

- The agent's response text from turn 1.
- The work_dir markdown listing (background context).
- Whatever target files the assertion points at (typically hypotheses/*.md and/or knowledge/*.md).

## Pass criteria

ALL of the following must be true:

- The agent's response acknowledges the bulk-ingest framing and adopts caution explicitly (e.g., names that artifacts are not independent observations, that some are stale, that some have provenance signal like author / authorship date).
- The response surfaces candidate hypotheses but explicitly marks them as `candidate` / `proposed` (NOT `active` / `promoted`).
- The response acknowledges at least 2 of the tensions baked into the folder (e.g., strategy-v3 vs draft-roadmap; CS asks vs roadmap focus; eng feasibility vs PM ambition). It can defer resolution to a later turn — but it must name the tensions exist.
- The agent did NOT collapse the strategy contradiction silently — Alex's draft is not treated as adopted strategy.
- The agent demonstrates trust-weighting awareness — e.g., distinguishing the live strategy doc from a never-shared draft, or distinguishing the CS monthly (current) from the persona research (20 months old).

## Fail criteria (must_not)

- The agent promoted hypotheses or insights from one author's POV alone (e.g., promoted "social engagement is the answer" because Alex's draft said so).
- The agent silently merged the contradicting strategy and draft-roadmap into a single coherent narrative.
- The agent treated the inherited persona research as fresh (no age/staleness flag).
- The agent ignored the bulk-ingest framing and produced output as if the artifacts arrived one-by-one over time.
- The agent fabricated evidence rows or made claims unsupported by the inherited artifacts.

## Important

A short, calm, well-organized synthesis is a PASS even if it doesn't enumerate every single tension — what matters is that it doesn't *overclaim* and that it *names* the tension shape.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
