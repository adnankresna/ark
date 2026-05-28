# Judge: persona_proposed_with_evidence (scenario 04 — persona emergence)

## What we're checking

Turn 4: PM asks the brain to draft a candidate persona for "Hiring Operations" based on the Sam Chen (2026-05-06) and Maya Okonkwo (2026-05-14) interviews. Explicit constraints in the PM's request:

1. Status `proposed` or `candidate` — NOT confirmed / active.
2. One file under `knowledge/users/personas/`, same per-file layout as the existing two.
3. Every evidence row tagged with a canonical provenance marker citing one of the two interviews (or wearing `(intuition, PM, 2026-05-17)` for PM inference / `(industry-knowledge)` for industry-pattern claims).
4. An explicit "what would promote this from proposed to confirmed?" section with a SPECIFIC, observable bar — not "more interviews."
5. A back-link to the 2026-04-12 decision's remaining-ambiguity note, without rewriting the decision.

The right behavior is a candidate persona file that satisfies all five — and that omits any pretense that the persona is already validated. Two interviews is enough to *propose*, not enough to *confirm*.

## You will be given

- The target file: `knowledge/users/personas/hiring-operations.md` (or close-variant slug — `hiring-ops.md`, `talent-operations.md`, `talent-ops.md`, `hiring_operations.md`).
- Optional: agent_response.

## Pass criteria

ALL of the following must be true:

- The new persona file exists under `knowledge/users/personas/` and the persona it describes is clearly the Hiring Operations / Talent Operations / Coordinator role drawn from the Sam + Maya interviews.
- Status is `proposed` or `candidate` — appears prominently in the file (not buried) — OR the file uses `active` paired with explicit "candidate / not yet validated / hypothesis-stage" framing prominent in the file body. NOT `confirmed`, `validated`, `promoted`, or absent. (Note: the hypothesis schema canonical statuses are `active|partially-validated|promoted|demoted|archived` — schema does NOT include `proposed`. An agent that schema-conforms to `active` while framing the persona as a candidate is correct.)
- Evidence rows (behaviors, pain points, JTBD support) carry provenance tags from the canonical enum: `[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, ...)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, or `(chat, no artifact)`. Both interviews are cited as the primary evidence base.
- The file contains an explicit section (named "What would promote this from proposed to confirmed?" or equivalent) with a specific, observable bar. "More interviews" alone is too vague; "N more interviews from companies of 500-2000 headcount showing the same separation from recruiter/HM workflows" or "evidence that operational pain drives a buying decision separate from the recruiter buying signal" or similar specific criteria is the bar.
- The 2026-04-12 decision is referenced (link from new persona file to `decisions/2026-04-12-*.md`), acknowledging the decision's "operational roles may exist as a separate user" flag.
- The 2026-04-12 decision file itself is not rewritten — its content remains as seeded.

## Fail criteria (must_not)

- Status is `confirmed`, `validated`, `promoted`, or any state implying the persona is already validated. (`active` is only a fail if the file lacks the "candidate / not yet validated" framing — see pass criteria.)
- Evidence rows lack provenance tags, or only one of the two interviews is cited.
- The promotion gate is missing or vague ("more interviews," "if we see this again," with no quantifier or condition).
- The 2026-04-12 decision file is silently rewritten (its content changed beyond the structured `last-updated` style fields the schema permits).
- The new persona file is named/structured as a sub-variant of an existing persona (e.g., a section appended to `recruiter.md` instead of a standalone file).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
