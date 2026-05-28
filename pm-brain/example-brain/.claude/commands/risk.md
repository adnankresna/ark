# /risk

Run the 5-area risk scan on a feature or plan. Surface which risks have no hypothesis, draft stubs for the gaps.

## Input

A feature slug (`/risk weekly-digest`), a plan name, or a draft PRD pasted into the call.

## Loads

- `knowledge/product/features/<slug>.md` if the feature exists
- All `hypotheses/<slug>.md` files linked to it
- `knowledge/users/insights.md` (value and usability evidence)
- `knowledge/strategy.md § Non-goals` (does this violate one?)
- `decisions/` filtered to ones that constrain this feature
- `rules/discovery.md` for any risk-area discovery rules

## Updates

`/risk` is not read-only. For any of the 5 risk areas with no hypothesis, it drafts a stub (status: `candidate`) with the open question and the suggested first test. Behavior depends on autonomy mode (`CLAUDE.md § Operating preferences § Autonomy mode`):

- **Act and tell (default).** Stubs are saved to `hypotheses/<slug>.md` and the feature file's `## Linked § Hypotheses` is updated to reference them. The operator triages on next `/review` or earlier.
- **Propose and wait.** Stubs are presented as drafts. Nothing saved until the operator confirms.

Risks with active hypotheses and fresh evidence are not touched.

**Hard constraints when drafting stubs:**

- Every Evidence-row in a new stub must carry a provenance tag from the enum in `hypotheses/_SCHEMA.md`. If the stub is opening a risk area with no concrete artifact yet, tag the row honestly: `(intuition, PM, <YYYY-MM-DD>)` or `(industry-knowledge)`. If you are citing a strategy clause, the row must include a working path-typed link like `[knowledge/strategy.md]` — not a bare paraphrase. Untagged rows fail the `no_orphan_evidence` audit.
- New stubs are status `candidate` (or `active` with confidence `low`) — never `promoted` or `partially-validated` at creation.
- Update `hypotheses/INDEX.md` in the SAME turn for every new stub. A new hypothesis file without an INDEX row is half-saved.

## Surfaces

The five risk areas, each with status and the top item:

1. **Value** — will it solve a real, frequent, valuable problem? Evidence for / against / gap
2. **Usability** — can the target user complete the core flow? Evidence for / against / gap
3. **Feasibility** — can the team build it given current capability? Evidence for / against / gap
4. **Viability** — does it work for the business (revenue, ops, legal, regulatory)? Evidence for / against / gap
5. **Other** — anything not in the canonical four (partnership, ecosystem, timing)

Format per area: `[have hypothesis | stub drafted | confirmed | demoted]` + one line on what's missing.

- 1-3 highest-leverage tests across all five areas
- Any non-goal this feature might violate
