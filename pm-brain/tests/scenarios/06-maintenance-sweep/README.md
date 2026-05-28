# Scenario 06 — Maintenance sweep behavior

You're Maya Chen, PM for **PulseFit**, a consumer fitness app (iOS + Android, ~180k MAU, freemium with a $9.99/mo premium tier). You've been running PM Brain for six months. The brain has accumulated real state: real interviews, real meetings, real hypotheses, real stakeholders. Some of that state is now redundant (three different ingestion records all triangulating the same Q1 churn-spike event), some is silently stale (a hypothesis promoted in February that a March A/B test quietly contradicted but never got demoted), some is superseded (an onboarding-funnel knowledge file from November that the December redesign made obsolete), and one stakeholder file is for someone who left the company two months ago.

Today you're running `/maintenance-sweep` — and the brain has to clean up *without* destroying the audit trail.

This scenario exercises **maintenance sweep behavior**: the brain's ability to identify candidates for compression and archival, propose them as a *plan* (not silent execution), name what would be lost, preserve audit anchors when archiving, and **never** touch `source/` raw artifacts.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Bulk re-seed of ~6 months of accumulated state | Turn 1 (3 redundant ingestions + 1 stale hypothesis + 1 superseded knowledge file + 1 departed-stakeholder file) | Structural |
| Identify redundancy & staleness as a plan, not silent execution | Turn 2 (PM asks for maintenance sweep, plan only) | Structural (nothing changed) + content (LLM judge) |
| Name what would be LOST by each proposed change | Turn 3 (PM asks for lossiness analysis) | Structural (nothing changed) + content (LLM judge) |
| Execute approved subset, preserve audit trail | Turn 4 (PM approves a subset; brain consolidates ingestions + archives knowledge file + archives departed stakeholder + leaves hypothesis alone) | Structural + content (LLM judge) |

## Lifecycle moves NOT exercised here

- Hypothesis promotion (covered by 01)
- Drift detection / contradicting evidence on a single hypothesis (covered by 03)
- Bulk migration of inherited artifacts (covered by 02)
- Decision drafting from scratch (covered by 01 turn 10)

The hypothesis demotion candidate sits in the brain across all four turns but is **explicitly NOT executed** in turn 4 — the PM says she wants to think about it. That's deliberate: the scenario asserts the brain respects partial approval, not that it auto-fires every candidate it identified.

## Archive convention — note for the brain

The scaffold names `hypotheses/archive/` and `features/archive/` as conventions but does NOT pre-name a convention for archived **knowledge files** or **stakeholders**. The right behavior on first encountering this is to ask the PM how she wants to handle it (subfolder? frontmatter flag?), commit to a convention, and apply it consistently. The structural assertions accept any of: subfolder `archive/`, `_archive/`, or a frontmatter `status: archived` flag — but cross-link integrity (`all_internal_links_valid`) is non-negotiable.

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Bulk re-seed | ~6 months of accumulated state: 3 redundant churn-spike ingestions, 1 quietly-contradicted hypothesis, 1 superseded knowledge file, 1 departed stakeholder. |
| 02 | Maintenance sweep — plan only | PM asks: "Run a maintenance sweep. Show me what looks redundant, stale, or worth archiving — but draft this as a PLAN. Don't execute anything yet." |
| 03 | Lossiness analysis | PM asks: "For each proposed change, walk me through specifically what we'd lose. Is there any signal we'd erase? Any link that would break?" |
| 04 | Execute approved subset | PM approves: consolidate the 3 redundant ingestions + archive the knowledge file + archive the stakeholder. Leave the hypothesis alone. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.75 (4 judges; allow one borderline VERDICT: UNCERTAIN to not block)

## Cost

~4 turns × ~$0.50-$0.75 (turn 1 seeds more state than scenario 03) = ~$2-3 single-run; ~$10-15 for `--runs 5`.
