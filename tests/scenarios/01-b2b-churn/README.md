# Scenario 01 — B2B churn investigation

You're the PM for a B2B SaaS compliance tool (mid-market, six active features). Over a four-week period, you investigate why mid-market churn is up 4 points QoQ. You run customer interviews, sit in on engineering meetings, ingest support trends, and eventually draft a decision to defer real-time alerts.

This scenario is the MVP for the eval suite. It exercises the lifecycle moves most likely to break: hypothesis promotion from accumulating evidence, hypothesis flagging on contradicting evidence, contradiction surfacing rather than silent overwrite, and decision drafting from a complete evidence trail.

## Lifecycle moves exercised

| Move | Where it happens | Assertion |
|---|---|---|
| Cold start → baseline structure | Turn 1 (first ingestion into empty brain) | Structural |
| Single anecdote should NOT promote | Turn 1 (one interview is not enough) | Structural + content |
| 3+ supporting evidence → hypothesis promoted | Turns 1, 4, 9 — three independent observations of the weekly-batch pattern | Content (LLM judge) |
| Contradicting evidence → existing hypothesis flagged | Turn 6 — a customer says they DO want real-time | Content (LLM judge, must-not check on silent overwrite) |
| Contradiction surfaced explicitly | Turn 6 → surfaced in the agent's response, not buried | Content (LLM judge) |
| Decision drafted from evidence trail | Turn 10 → references H2, lists reversal condition | Structural + content |

## Lifecycle moves NOT exercised here

These need their own scenarios:

- Drift detection (old hypothesis loses support over time)
- New persona emergence (pattern crosses threshold mid-scenario)
- Stakeholder cadence flags
- Maintenance sweep behavior (`/review`)
- Migration mode (bulk-ingest of pre-existing artifacts)

## Turn map

| Turn | Kind | Summary | Purpose |
|---|---|---|---|
| 01 | Interview — Acme Ops Lead | Weekly batch preference for SOC2 evidence. Strong anecdote, single source. | Should propose H2, should NOT promote insight yet. |
| 02 | Meeting — Eng sync | Feasibility of real-time alert pipeline. Engineering says doable but 6-week build. | Updates feasibility risk on the alert feature. |
| 03 | Analytics — Support ticket trend | Mid-market churn up 4pp QoQ. Top reason cited: "notification overload." | Adds market/product signal. Doesn't directly bind to H2 yet. |
| 04 | Interview — Stripe Compliance Lead | Second independent observation of weekly batch pattern. | Strengthens H2 evidence. Insight still 2-of-3, not promoted. |
| 05 | Slack — Pricing channel | Side conversation about real-time pricing tier. Low signal for H2 specifically. | Should land in adhoc/ or pricing notes; should NOT update H2 falsely. |
| 06 | Interview — Brex Ops | Says they DO want real-time alerts for fraud team. Direct contradiction to H2's framing. | Should surface contradiction, NOT silently demote H2. |
| 07 | Decision trigger | PM asks: should we defer real-time? | Tests whether agent draws on full evidence trail, surfaces the contradiction from turn 6, names what's still ambiguous. |
| 08 | Market — Competitor changelog | Vanta ships real-time as paid add-on. | Adds market signal. Should bind to viability risk, not value risk. |
| 09 | Interview — Notion Ops | Third independent observation of weekly batch pattern (now 3-of-3, but contradicted by Brex). | Should promote insight WITH the dissent preserved (not flattened). |
| 10 | Decision moment | PM confirms direction. | Should draft decision file with full evidence trail and a specific reversal condition. |

## Pass criteria

- **Structural assertions:** must pass 100% (1.0). These are deterministic — failure means a real bug.
- **Content assertions:** must pass ≥ 80% (4 out of 5 runs). LLM-judge non-determinism makes 100% unrealistic; 80% catches systematic failures while tolerating noise.

If content rate drops below 0.8 across runs, the scenario is failing — investigate before adjusting the threshold.

## Files

```
01-b2b-churn/
├── README.md          # This file
├── expected.yaml      # Ground-truth assertions
└── inputs/
    ├── turn-01-interview-acme-ops.md           # Single anecdote — hypothesis proposed, NOT promoted
    ├── turn-02-meeting-eng-sync.md             # Feasibility scoping (6-week build, on-call posture)
    ├── turn-03-analytics-churn-snapshot.md     # Mid-market churn +4pp QoQ, correlational
    ├── turn-04-interview-stripe-compliance.md  # 2nd observation of weekly-batch pattern
    ├── turn-05-slack-pricing-thread.md         # Internal chatter — low signal, must not promote
    ├── turn-06-interview-contradicting.md      # Brex wants real-time — direct contradiction
    ├── turn-07-decision-trigger.md             # PM prompts synthesis (no decision yet)
    ├── turn-08-market-vanta-changelog.md       # Competitor signal → viability, not value
    ├── turn-09-interview-notion-ops.md         # 3rd observation, plus dissent confirmation
    └── turn-10-decision-moment.md              # PM prompts decision draft, status pending
```

All inputs are authored, realistic PM-shaped, ~300-600 words each. Turns 07 and 10 are direct PM prompts (not artifacts to ingest) — the harness should treat them as agent instructions rather than ingestion sources.
