# /hypothesize

Generate or refresh hypotheses for a feature. Works **pre-ship** (proactive, organized by the 5 risk areas) or **post-ship** (data-derived from analytics / interviews / churn — "why is retention dropping?"). Same schema either way; the `Origin` field distinguishes them.

## Input

A feature slug (`/hypothesize weekly-digest`), a problem statement (`/hypothesize "mid-market onboarding drop-off"`), or an existing hypothesis file to refresh (`/hypothesize hypotheses/weekly-digest.md`).

If the feature has no existing file yet, the command creates one. If it does, the command refreshes — opening new candidate hypotheses where evidence has accumulated, and surfacing any existing ones whose evidence has gone stale.

## Loads

- `hypotheses/<slug>.md` if it exists (refresh mode)
- `knowledge/product/features/<slug>.md` (if the feature exists in product knowledge)
- `knowledge/strategy.md` — non-goals, priorities, north-star (so the hypotheses don't violate strategic constraints)
- `knowledge/users/insights.md` and any relevant `personas.md` / `segments.md`
- Recent `ingestion/` filtered to this feature / problem space (interviews, meeting notes, market signals — last ~10 entries)
- `decisions/` filtered to ones that constrain or invalidate hypothesis space for this feature
- `hypotheses/_SCHEMA.md` — load before writing or refreshing any hypothesis file

## Updates

- `hypotheses/<slug>.md` — created (new feature) or appended (refresh mode). Each new hypothesis carries: belief, origin (proactive | data-derived from `<source>`), confidence (always start at `low` for new hypotheses), evidence-for / evidence-against (tagged), open questions, test plan, decision trigger, status (`active`).
- `hypotheses/INDEX.md` — add the file under the appropriate status section if newly created; update status if a hypothesis flipped state.
- Maintenance log entry — one-line note that hypotheses were generated/refreshed for `<feature>` with a count of new and modified.

**Hard constraints:**

- Never promote a hypothesis at creation time. New = `active` / `low` confidence. Promotion requires evidence accumulation through subsequent `/ingest` cycles.
- Cover all 5 risk areas (value, usability, feasibility, viability, other) for pre-ship hypotheses, even if the answer for some areas is "no risk identified, monitor." Silent gaps are themselves a risk.
- Every Evidence-row tag follows the provenance enum in `hypotheses/_SCHEMA.md`. If you're generating a hypothesis from intuition with no external signal yet, use `(intuition, PM, <YYYY-MM-DD>)` honestly — do not fabricate an ingestion record.
- Aggregation/meta rows ("N=3 interviews, mixed sentiment") go under `Open questions / caveats:`, never under Evidence.
- **`hypotheses/INDEX.md` must be updated in the SAME turn as any new hypothesis file write.** Add a row under the appropriate status section (Active / Partially-validated / Promoted / Demoted / Archived). A new hypothesis file without an INDEX row is half-saved — the next session's retrieval will miss it. Do this BEFORE returning the routing summary.

## Surfaces

- Count of new hypotheses opened, grouped by risk area
- Count of existing hypotheses refreshed (evidence added, status changed, or marked stale)
- The 1-2 hypotheses with the strongest evidence (most likely to promote next cycle) named explicitly
- Any risk area where NO hypothesis exists — explicit gap flag
- One open question if a hypothesis touches a strategic non-goal or contradicts a recent decision
