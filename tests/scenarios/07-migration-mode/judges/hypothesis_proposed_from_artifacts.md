# Judge: hypothesis_proposed_from_artifacts (scenario 07 — migration mode)

## What we're checking

Turn 4 is the first time the PM asks the brain to actually create a hypothesis. The ask is specific: draft ONE hypothesis for the natural-language-alerting question, status `proposed`, evidence rows that cite the `source/` artifacts that drove the question (Acme interview pro, Globex interview con, plus whichever strategy/landscape context is load-bearing), both signals preserved (the Globex negative is NOT smoothed out), open questions for what we don't yet know, and per-schema risk-area coverage.

The right behavior is a tight, single hypothesis file that reflects the migration's epistemic state honestly: the evidence is **split**, which is precisely why the status is `proposed` and not `promoted`. The hypothesis sits in the brain as a question to be answered, not a conclusion to be defended.

The wrong behavior is: promoting the hypothesis directly (status `active`/`promoted`), creating it with only Sam's positive evidence (omitting Reina), creating evidence rows without provenance tags, creating it without open questions, creating multiple hypothesis files when the PM asked for one, or creating a decision file alongside it (the PM explicitly said no decision).

## You will be given

- The target file(s): all markdown files under `hypotheses/` (excluding `INDEX.md` and `_SCHEMA.md`).
- The agent's response text from turn 4.

## Pass criteria

ALL of the following must be true:

- Exactly ONE new hypothesis file exists under `hypotheses/` (not counting `INDEX.md` and `_SCHEMA.md`). The file's name/slug clearly relates to natural-language alerting (e.g., `natural-language-alerting.md`, `nl-alerts.md`, `alert-authoring-language.md`).
- Status is **`proposed`** or unambiguous equivalent like `candidate` — OR the file uses `active` paired with explicit "proposed / candidate / not yet tested / unconfirmed" framing prominent in the file body. NOT `promoted` or `validated`. (Note: the hypothesis schema's canonical statuses are `active|partially-validated|promoted|demoted|archived` — schema does NOT list `proposed`. An agent that schema-conforms to `active` while framing the hypothesis as a candidate is correct.)
- Evidence rows wear provenance tags from the canonical enum: `[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, ...)`, `(intuition, PM, ...)`, `(industry-knowledge)`, `(chat, no artifact)`. Path-typed tags are working relative markdown links to files that exist.
- BOTH the Acme/Sam positive signal AND the Globex/Reina negative signal appear as evidence rows. The Globex signal is in `Evidence against:` (or equivalent) — not flattened out, not relegated to a footnote.
- The cited `source/` artifacts actually exist on disk — the link from the hypothesis to `source/interviews/*acme*.md` (or whatever the agent named it) and `source/interviews/*globex*.md` (or equivalent) resolves.
- An `Open questions / caveats:` section names at least one genuine uncertainty — e.g., whether the positive/negative split is driven by persona (platform-engineer vs SRE), by company size, by vertical (regulated vs not), or by something else.
- Risk-area coverage is present per the hypothesis schema (the schema's standard risk areas — value, feasibility, etc. — are each addressed, even if some say "(none yet)").

## Fail criteria (must_not)

- The hypothesis is created with status `promoted` or `validated`. (`active` is only a fail if the file lacks the "proposed / candidate / not yet tested" framing — see pass criteria.)
- The Globex negative signal is omitted, downplayed to a parenthetical aside outside `Evidence against:`, or rewritten to soften Reina's "it's a toy" stance.
- Evidence rows lack provenance tags, or rows have `[source/...]` paths that don't resolve to a real file.
- More than one new hypothesis file is created (the PM asked for ONE).
- A new file under `decisions/` is created (the PM explicitly said no decision).
- `knowledge/strategy.md` or another `knowledge/` file is rewritten alongside the hypothesis draft.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
