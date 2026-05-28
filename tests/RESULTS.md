# Test results: most recent per-scenario runs

> One row per scenario, latest run. Snapshots committed under [`results/snapshots/`](results/snapshots/). Open any JSON to see the per-turn structural checks, judge verdicts, agent responses, and cost breakdown.

The harness spins up a fresh PM Brain scaffold in a temp dir, replays the scenario's cached `turn-NN-*.md` inputs through `claude -p`, runs structural checks after every turn, and runs LLM-judge checks at the end. There is no cherry-picking inside a run. Every check defined in `expected.yaml` is evaluated. See [`TESTING.md`](TESTING.md) for the design.

## Headline

- **404 of 406 individual checks pass across the 17 snapshots (≈99.5%), on Claude Sonnet 4.6.** The split:
  - **Structural: 329 / 329 (100%).** Every mechanical check (files exist, links resolve, evidence rows tagged with provenance, decision schemas valid, no orphan evidence, no silent demotions) passes on every snapshot. The brain's scaffolded foundation holds without exception.
  - **Content (LLM judges): 75 / 77 (≈97%).** Two judges miss on the two longest scenarios (01 b2b-churn T9 and 02 inherited-folder T5). Specific judges and remediation status in [§ Known residuals](#known-residuals).
- **15 of 17 scenarios pass cleanly** (every structural + every judge `verdict=PASS`); the other 2 pass all structural and all but one content judge each.
- **Total spend** to produce the snapshot set: **~$37** of API-equivalent cost on Claude Sonnet 4.6, including the LLM judges. The committed `*-opus.json` snapshots for scenarios 01 and 02 are Opus comparison runs from when we suspected the residuals were model-limited. Opus didn't change the verdict on either, so the headline numbers stand on pure Sonnet 4.6. See [`docs/testing-decisions.md`](../docs/testing-decisions.md) for the cost-vs-quality reading.

## Scoreboard

| # | Scenario | Status | Turns | Structural | Content (judges) | Cost | Date |
|---|---|---|---|---|---|---|---|
| 01 | [b2b-churn](results/snapshots/01-b2b-churn.json) | ⚠ partial | 10 | 24/24 | 10/11 | $5.13 | 2026-05-17 |
| 02 | [inherited-folder](results/snapshots/02-inherited-folder.json) | ⚠ partial | 10 | 31/31 | 10/11 | $6.37 | 2026-05-17 |
| 03 | [drift-detection](results/snapshots/03-drift-detection.json) | ✅ pass | 4 | 17/17 | 5/5 | $2.16 | 2026-05-17 |
| 04 | [persona-emergence](results/snapshots/04-persona-emergence.json) | ✅ pass | 4 | 15/15 | 7/7 | $1.54 | 2026-05-17 |
| 05 | [stakeholder-cadence](results/snapshots/05-stakeholder-cadence.json) | ✅ pass | 4 | 16/16 | 6/6 | $1.60 | 2026-05-17 |
| 06 | [maintenance-sweep](results/snapshots/06-maintenance-sweep.json) | ✅ pass | 4 | 32/32 | 4/4 | $1.91 | 2026-05-17 |
| 07 | [migration-mode](results/snapshots/07-migration-mode.json) | ✅ pass | 4 | 16/16 | 5/5 | $1.48 | 2026-05-17 |
| 08 | [weekly-review](results/snapshots/08-weekly-review.json) | ✅ pass | 4 | 23/23 | 6/6 | $2.00 | 2026-05-17 |
| 09 | [ideation](results/snapshots/09-ideation.json) | ✅ pass | 4 | 20/20 | 4/4 | $1.25 | 2026-05-17 |
| 10 | [promotion-gate](results/snapshots/10-promotion-gate.json) | ✅ pass | 4 | 17/17 | 5/5 | $2.22 | 2026-05-17 |
| 11 | [ingest-shapes](results/snapshots/11-ingest-shapes.json) | ✅ pass | 4 | 16/16 | 0/0 | $1.73 | 2026-05-17 |
| 12 | [decision-lifecycle](results/snapshots/12-decision-lifecycle.json) | ✅ pass | 4 | 16/16 | 3/3 | $1.60 | 2026-05-17 |
| 13 | [strategic-planning](results/snapshots/13-strategic-planning.json) | ✅ pass | 5 | 22/22 | 4/4 | $2.31 | 2026-05-17 |
| 14 | [install-greenfield](results/snapshots/14-install-greenfield.json) | ✅ pass | 1 | 34/34 | 1/1 | $2.04 | 2026-05-17 |
| 15 | [evidence-hierarchy](results/snapshots/15-evidence-hierarchy.json) | ✅ pass | 4 | 21/21 | 2/2 | $1.72 | 2026-05-17 |
| 16 | [corrupt-state-recovery](results/snapshots/16-corrupt-state-recovery.json) | ✅ pass | 3 | 19/19 | 2/2 | $0.92 | 2026-05-17 |
| 17 | [no-artifact-flow](results/snapshots/17-no-artifact-flow.json) | ✅ pass | 4 | 10/10 | 1/1 | $1.04 | 2026-05-17 |
| | **Totals** | | **77** | **329/329** | **75/77** | **~$37** | |

"Structural" = mechanical assertions (files exist, links resolve, evidence rows tagged, status transitions valid). "Content" = LLM-judge assertions on substance (was the contradiction surfaced with citation? was the dissent preserved? was the cadence flag relevance-filtered?). Both run on every applicable turn plus a final-state pass.

## Known residuals

Two per-judge failures persist on the longest scenarios. Both are documented in [`docs/testing-decisions.md`](../docs/testing-decisions.md). Neither is hidden: they appear as `passed: false` in the snapshot JSON.

### 01-b2b-churn → T9 `insight_promoted_with_dissent_preserved`

The judge checks that when a recurring user-insight gets promoted to `knowledge/users/insights.md`, the **dissenting** evidence (the one interview that disagreed) is preserved as a row under `## Contradictions`, not flattened into the synthesis. In the snapshot run, the agent promoted the insight with two of three supporting interviews but the third (Notion / Priya's ops-risk subteam) was missing from both the `## Active themes` evidence rows AND the dissent block.

**Remediation status:** the `CLAUDE.md § Memory promotion` rule already requires "Counter-signals get preserved under `## Contradictions` in the same file, not flattened". The prompt covers the case but the agent collapsed the third source. The next sharpening pass would add an explicit promotion checklist ("N supporters listed? all named by source slug? any non-supporters from the same population? if so, dissent row required"). Pending; not done in this snapshot.

### 02-inherited-folder → T5 `risk_area_updated`

The judge target is "after a risk-relevant ingestion, the affected hypothesis or feature file shows an updated `Risks` / `Open questions` block." Across 9 reruns, the failure mode varies: sometimes the agent updates the right file but uses paraphrasing the judge doesn't accept as evidence of the update; sometimes the judge call itself returns `error=claude_not_found` (a transient harness subprocess flake, not a quality fail).

The same scenario also produced an `all_internal_links_valid` failure in earlier runs. Agent used `../product/metrics.md` from `knowledge/strategy.md` (one too many `..`'s, pointing above `knowledge/` to a non-existent top-level `product/`). The linking-rules table in `CLAUDE.md` did not have a row for depth-1 files like `knowledge/strategy.md`, so the agent extrapolated wrong. **Fixed in this commit:** `scaffold/CLAUDE.md` and `example-brain/CLAUDE.md` now have the depth-1 row and a worked example calling out the failure pattern. A re-run with the patch is queued; if it lands cleanly the snapshot will be updated and this section will move to docs/testing-decisions.md as a resolved fix.

## How to reproduce

```bash
# One scenario (~2-6 minutes, $1-6 depending on length)
python tests/harness/run_scenario.py tests/scenarios/03-drift-detection

# All 17 scenarios, one run each (~30-60 minutes, ~$35-45)
python tests/harness/run_all.py

# Same but 5 runs per scenario (stability check; gated by --max-cost)
python tests/harness/run_all.py --runs 5 --max-cost 100
```

Each invocation writes a fresh JSON under [`results/`](results/) (gitignored by default). The committed [`results/snapshots/`](results/snapshots/) directory is the latest representative run per scenario. Re-running locally will produce timestamped peers, not overwrites.

## Model

All 17 primary scenario snapshots and their LLM judges ran on **Claude Sonnet 4.6**. No mixed split.

The committed `*-opus.json` snapshots for scenarios 01 and 02 are Opus comparison runs from when we suspected the content-judge failures were model-limited. Opus didn't change the verdict on either; both residuals persist. The Opus opt-in is preserved in `expected.yaml` per-assertion for future investigations, but the headline numbers stand on pure Sonnet 4.6.

See [`CLAUDE.md § Model strategy`](../CLAUDE.md#model-strategy) for the cost rationale and [`docs/testing-decisions.md`](../docs/testing-decisions.md) for what the Opus runs taught us about which failure modes are model-limited (none of these two, as it turns out) vs. scaffold-limited.
