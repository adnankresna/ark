# judges/

LLM-judge rubrics. Each `.md` file in this directory is a tight prompt that takes the work_dir state (or a specific target file) and returns one of: `PASS`, `FAIL`, `UNCERTAIN`.

`UNCERTAIN` counts as FAIL for that run. Aggregate pass-rate across N runs handles the noise.

## Rubric format

Each rubric file is a markdown prompt with this shape:

```markdown
# Judge: <name>

## What we're checking
<one sentence>

## You will be given
- The target file content
- The scenario context (which turn this is, what came before)
- The expected meaning (from expected.yaml)

## Pass criteria
<bulleted list of what MUST be true>

## Fail criteria (must_not)
<bulleted list of what must NOT be true>

## Output format
Exactly one line:
  VERDICT: PASS
  VERDICT: FAIL — <one-line reason>
  VERDICT: UNCERTAIN — <one-line reason>

Do not output anything else.
```

## Rubrics in this directory

Scenario `01-b2b-churn` uses these 11 rubrics:

| Rubric | What it checks | Turn(s) |
|---|---|---|
| `hypothesis_proposed.md` | Hypothesis proposed but NOT promoted after one observation | 1 |
| `insight_promotion.md` | Insight held back when below threshold, promoted only when met | 1, 4, 9 |
| `risk_area_updated.md` | Eng feasibility evidence routed to feasibility risk, not value | 2 |
| `risk_area_routing.md` | Vanta competitor signal routed to viability, not value | 8 |
| `market_signal.md` | Analytics signal added without fabricating causal claims | 3 |
| `low_signal.md` | Internal Slack chatter not promoted to customer evidence | 5 |
| `contradiction_surfaced.md` | Brex contradiction surfaced, not flattened or silently overridden | 6 |
| `decision_trigger.md` | Synthesis references full trail INCLUDING the contradiction | 7 |
| `insight_promoted_with_dissent.md` | Promoted insight is specific (compliance-ops) + preserves dissent | 9 |
| `decision_quality.md` | Decision file: evidence by name, dissent named, specific reversal | 10 |
| `audit_trail.md` | Walk decision → hypothesis → ingestion → source/ via working links | final |

Scenario `02-inherited-folder` adds these rubrics (post-bulk-ingest migration behaviors):

| Rubric | What it checks | Turn(s) |
|---|---|---|
| `bulk_ingest_caution.md` | High-volume ingest, low-volume promotion; provenance/age tagging | 1 |
| `tensions_enumerated.md` | Conflict list with provenance, not smoothed prose | 2 |
| `contradiction_resolved_with_audit.md` | Strategy/draft resolved with both artifacts retained + cross-linked | 6 |
| `staleness_flagged.md` | Calibrated staleness — distinguishes age from staleness | 7 |
| `decision_provenance.md` | Decision rows tagged inherited vs Maya-collected vs functional | 9 |

## Why so many rubrics

PM Brain's value claims are mostly qualitative: "the system surfaces contradictions instead of flattening them," "decisions carry their reversal conditions." These can't be checked structurally; they need judgment. Each rubric encodes one of those value claims as a testable pass/fail.

The cost of writing rubrics is one-time. The benefit is repeatable, version-controlled checks on whether the skill is doing the qualitative thing we claim it does.
