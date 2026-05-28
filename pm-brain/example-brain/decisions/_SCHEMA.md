# Decision Record Schema

> **Read this schema before writing or editing a decision file.** Especially § *Provenance enforcement*. The `no_orphan_evidence` structural check rejects decision files where any `## Evidence` or `## Explicitly NOT doing` row lacks a provenance tag from the canonical enum.
>
> **Pre-save self-check** (run mentally before every write to a decision file):
> 1. **COUNT-THE-TAGS.** Count the number of bullet rows under `## Evidence` and `## Explicitly NOT doing` in your draft. Count the number of provenance tags in those rows. The two numbers MUST match. If you have 6 evidence rows and 4 tags, you have 2 orphans — add tags before saving (or move the bullets to `## Remaining ambiguities` if they aren't really evidence). This single check catches the most common failure mode: paraphrasing a claim from an ingestion record into an Evidence row and forgetting the tag.
> 2. Every row under `## Evidence` and `## Explicitly NOT doing` carries one tag from the provenance enum (`[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, <name>, <YYYY-MM-DD>)`, `(intuition, PM, <YYYY-MM-DD>)`, `(industry-knowledge)`, `(chat, no artifact)`).
> 3. Path-typed tags (`[ingestion/...]`, `[source/...]`) are written as markdown links (`[ingestion/...](../ingestion/...)`), not as parenthetical prose like `(Acme interview, 2026-04-22)`.
> 4. Each path-typed link, when followed from THIS file (`decisions/<file>.md`), resolves — i.e. `../ingestion/<rest>` or `../source/<rest>` (one `..`).
> 5. `## Status` is one of `pending | decided | superseded`. `proposed` is an accepted synonym for `pending`. Do not invent other values.
> 6. `## What would reverse this` is present and the condition is **specific and observable** (a metric threshold, a stakeholder signal, a date — not "if things change").
> 7. Commentary, gaps, and "things we don't yet know" belong under `## Remaining ambiguities`, NOT under `## Evidence`. Aggregation/meta rows ("N=3 customers, mixed sentiment") are not evidence — they go under `## Remaining ambiguities` too.

Filename: `YYYY-MM-DD-<slug>.md`

```markdown
# Decision: <one-line statement>

## Status
pending | decided | superseded

## Date
YYYY-MM-DD <!-- decided date, or date opened if pending -->

## Context
<!-- 2–4 sentences. What problem / fork in the road. -->

## Options considered
1.
2.
3.

## Decision
<!-- What we picked. Empty for pending. -->

## Why
<!-- The actual reasoning. Be specific. Empty for pending. -->

## Evidence
<!-- HARD RULE: every row MUST end with one tag from the provenance enum below. A row without a tag fails the `no_orphan_evidence` structural check. Examples in canonical form:
  - Acme ops lead said weekly batches are unusable  [source/interviews/2026-04-22-acme-ops.md](../source/interviews/2026-04-22-acme-ops.md)
  - Three customers asked for the same flow  [ingestion/interviews/2026-05-02-synthesis.md](../ingestion/interviews/2026-05-02-synthesis.md)
  - Naomi confirmed Q3 priority in 1:1  (stakeholder-verbal, Naomi, 2026-05-13)
  - Checkout friction reduces conversion  (industry-knowledge)
-->
- <claim>  `<provenance-tag>`
- <claim>  `<provenance-tag>`

## Explicitly NOT doing
<!-- HARD RULE: same provenance-tag requirement as Evidence rows. Each "not-doing" must wear its source. -->
- <not-doing>  `<provenance-tag>`

## What would reverse this
<!-- The most valuable field. The condition under which we'd revisit. Must be observable. -->

## Remaining ambiguities
<!-- Things we know we don't know. Often: stale evidence, unresolved pricing, untested assumptions. -->

## For pending decisions only
- **Blocker impact:** <what work this is currently blocking>
- **Deadline:** <when it needs to be resolved, or "no hard deadline">
- **Owner:** <who's driving the resolution>
- **Missing evidence:** <what we'd need to learn to decide>

## Linked
<!-- Paths are relative to THIS file's location (decisions/YYYY-MM-DD-<slug>.md). -->
- Hypotheses: `../hypotheses/<slug>.md`
- Strategy: `../knowledge/strategy.md` § <section>
- Stakeholders informed: `../stakeholders/<slug>.md`, …
```

## Provenance enforcement

The same enum used in hypotheses applies here. Each Evidence and Explicitly-NOT row MUST carry exactly one tag from:

- `[ingestion/...]` — went through synthesis
- `[source/...]` — direct citation to raw artifact
- `(stakeholder-verbal, <name>, <YYYY-MM-DD>)`
- `(intuition, PM, <YYYY-MM-DD>)`
- `(industry-knowledge)`
- `(chat, no artifact)`

A decision rendered from mixed-trust evidence (a common case during migration) MUST wear that mix on its face — a reader should not have to spelunk to learn how much of the reasoning is inherited-and-not-revalidated vs PM-collected-and-fresh.

## Rules

- Every shipped feature should have at least one decision record.
- When a hypothesis is `promoted`, a decision is auto-drafted (PM confirms).
- Decisions are append-only. To reverse, write a new decision that references and supersedes the old one (set the old one's status to `superseded`).
- **Decision debt:** decisions with `status: pending` are unresolved forks. Maintenance surfaces them — especially when their blocker impact is high or deadline is approaching.
