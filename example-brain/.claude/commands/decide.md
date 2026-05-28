# /decide

Log a decision. Drafts a complete decision file from the existing evidence trail and surfaces it for PM sign-off.

## Input

A decision slug (`/decide ship-weekly-digest`) or a one-line decision framing (`/decide "kill auto-categorize, ship receipt-matching instead"`). If a hypothesis is being resolved by the decision, include or infer its slug: `/decide ship-weekly-digest --resolves H-V1`.

## Loads

- `decisions/_SCHEMA.md` — load before writing the decision file
- `hypotheses/<slug>.md` for any hypothesis the decision resolves (the decision MUST link back to it)
- `knowledge/strategy.md` — priorities, non-goals, tensions (does this decision honor strategy? create new tension?)
- Recent `ingestion/` and `source/` referenced as evidence (every Evidence row in the decision file needs a provenance tag pointing at a real artifact)
- `stakeholders/<slug>.md` for any stakeholder named in the decision (Naomi confirmed Q3, Helena flagged budget, etc.)
- `decisions/INDEX.md` to check for prior decisions this one supersedes or depends on

## Updates

- `decisions/YYYY-MM-DD-<slug>.md` — created with the full schema: status (`pending` or `decided`), context, decision, evidence rows (each tagged), explicitly NOT doing, stakeholders signed off, reversal condition (observable + specific), remaining ambiguities. Drafted, not committed.
- `decisions/INDEX.md` — add under `## Pending` if `status: pending`, otherwise under `## Recently decided`
- `hypotheses/<slug>.md` — if the decision resolves a hypothesis, mark that hypothesis `promoted` (if decision validates it) or `demoted` (if decision goes the other way), with a Resolution row linking to the new decision file
- `hypotheses/INDEX.md` — reflect the hypothesis status change

**Hard constraints:**

- **COUNT-THE-TAGS** before saving — every Evidence row + every "Explicitly NOT doing" row carries a provenance tag from the enum in `hypotheses/_SCHEMA.md`. Orphan rows fail the audit.
- **Reversal condition is mandatory and observable.** "If things change" / "if market shifts" / "if we get pushback" are not acceptable. The condition must name a specific, measurable signal (a metric crossing a threshold, a stakeholder explicitly withdrawing support, a competitor shipping a specific feature). The audit check `all_decisions_have_reversal_condition` rejects vague reversal conditions.
- **Commentary, gaps, and "things we don't yet know"** go under `## Remaining ambiguities`, NOT under `## Evidence`. Aggregation/meta rows ("N=3 customers, mixed sentiment") are not evidence — they go under Remaining ambiguities too.
- Default to `status: pending` unless the PM explicitly said "this is decided." Pending invites stakeholder sign-off; decided implies the choice has been made and is being recorded for the audit trail.

## Surfaces

- The decision file path + a 1-line summary of what was committed (or proposed if pending)
- Which hypothesis (if any) this resolves and how its status flipped
- The reversal condition, in one line
- Any stakeholder named in the file who has NOT yet been touched on this decision — explicit "you should loop in X before this lands" flag
- Any contradiction with strategy or with a prior decision — surfaced, not silently smoothed
- The PM-sign-off prompt: "Apply this decision as drafted? (y / edit / no)"
