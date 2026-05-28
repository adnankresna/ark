/risk weekly-snapshot

Run the 5-area risk scan on the Weekly Snapshot feature. Per the spec, this is NOT read-only — for any risk area without a hypothesis, draft a stub (status: `candidate` or `active`) and link it from the feature file's `Linked § Hypotheses` section.

The feature is at design stage. Value risk has some implicit coverage from adjacent interview signals, but feasibility (PDF generation cost, ETL dependency), viability (does email delivery affect our pricing model?), and "other" (timing — Q3 is locked on the research-segment deepening priority) are all uncovered.

Surface back:

- All 5 risk areas, each marked `[have hypothesis | stub drafted | confirmed | demoted]` + one line on what's missing.
- 1-3 highest-leverage tests across all 5 areas.
- Any non-goal this feature might violate (check `knowledge/strategy.md § Non-goals`).
