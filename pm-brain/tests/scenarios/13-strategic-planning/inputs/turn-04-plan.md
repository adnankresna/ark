/plan reduce weekly-dashboard load time by 40% in Q3

The morning-refresh delays Sasha flagged in adhoc ingestion (basin-level ETL throwing transient timeouts) are starting to affect customer experience. Jordan and I think we need an explicit Q3 objective on this — reduce weekly dashboard load time by 40% while maintaining the SLA.

Per the `/plan` spec, surface the six expected blocks:

1. **What we already know** — citations to insights, hypotheses, decisions, metrics.
2. **Assumption vs evidence** — explicitly tagged, with provenance per claim.
3. **Who to interview** — segments / personas / named users; recent coverage gaps.
4. **Hypotheses to open** — across the 5 risk areas, with a test for each.
5. **Experiments to run** — sequenced, with success criteria + invalidation conditions.
6. **Decision points** — go/no-go moments, what evidence unlocks each.

Plus:

- Constraints from `strategy.md § Non-goals` that bound the plan (mobile UI is out, pricing-tier changes are out).
- Stakeholder alignment conversations the plan requires (linked to `/prep`).
- A short paragraph on what would make the plan unwise.

Drafts are fine — nothing committed without my sign-off. You may write a draft `ingestion/adhoc/2026-05-17-plan-dashboard-load-time.md` capturing the planning session, and stub `hypotheses/` candidates for any risk area that doesn't yet have coverage.
