# Scenario 04 — Persona emergence

You're Dana Liu, PM for **HireFlow**, a B2B SaaS hiring platform used by ~180 mid-market employer accounts (200-2000 headcount). The brain already has two confirmed personas — *Recruiter* and *Hiring Manager* — and a recent prioritization decision that leaned on both. Over the past two weeks, a different role kept showing up in discovery interviews. Today, after the second one, you want the brain to tell you honestly whether you're looking at a variant of an existing persona or a genuinely new one.

This scenario exercises **new persona emergence**: the brain's ability to recognize signals that don't fit any existing persona, accumulate them across multiple interviews without forcing them into the closest match, and then — and only then — propose (not auto-create) a new persona file with the evidence trail intact. The existing personas must remain unedited.

## Lifecycle moves exercised

| Move | Where | Assertion |
|---|---|---|
| Seed prior state (two personas + one supporting decision) | Turn 1 (bulk-ingest 4 artifacts: 2 personas, an insights file, a decision) | Structural |
| Misfit signal recognized, NOT forced into an existing persona | Turn 2 (first Coordinator interview) | Structural + content |
| Second misfit signal corroborates pattern, still no premature persona file | Turn 3 (second Coordinator interview + explicit "fit check?" question) | Structural + content |
| Candidate persona drafted with evidence trail, existing personas untouched | Turn 4 (PM asks for a `proposed` persona draft) | Structural + content |

## Lifecycle moves NOT exercised here

- Hypothesis promotion / demotion (covered by 01 and 03)
- Bulk migration (covered by 02)
- Drift on aged claims (covered by 03)
- Stakeholder cadence flags
- Maintenance sweep behavior

## Turn map

| Turn | Kind | Summary |
|---|---|---|
| 01 | Seed prior state | Four artifacts: Recruiter persona, Hiring Manager persona, insights file referencing both, and a 2026-04 decision that leaned on both personas. |
| 02 | First misfit interview | Sam Chen, Hiring Operations Coordinator at MidCo. Cross-team calendaring + interviewer logistics dominate her work; she does not source candidates and does not make hire/no-hire calls. PM asks the brain to ingest. |
| 03 | Second misfit interview + fit check | Maya Okonkwo, Talent Operations Lead at LargeCo. Same coordination pattern. PM explicitly asks: "does this fit either persona we have, or are we seeing something new?" |
| 04 | Propose new persona | PM asks the brain to draft a candidate persona file for "Hiring Operations" — status `proposed`, evidence trail from both interviews, and an explicit gate for what would promote it to confirmed. |

## Pass criteria

- **Structural assertions:** 1.0
- **Content assertions:** ≥ 0.8

## Cost

~4 turns × ~$0.20 = ~$0.80 single-run; ~$4 for `--runs 5`.
