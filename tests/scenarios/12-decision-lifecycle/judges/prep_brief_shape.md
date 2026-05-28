# Judge: prep_brief_shape (scenario 12 — decision-lifecycle, turn 2)

## What we're checking

Turn 2 invokes `/prep diana-okonkwo`. The `/prep` command spec says it is **read-only at call time** — load the stakeholder file plus recent context, and produce a prep brief in the response. The only file mutation allowed is updating the `Last touched:` field on the stakeholder file.

A good prep brief surfaces, in order:

1. **Last-touched date and cadence** — is the PM on or off schedule? (The seed has Diana at 2026-04-22 last touched, biweekly cadence; today is 2026-05-17, so the PM is overdue by about a week.)
2. **What Diana cares about** + the specific concerns the auto-approve-under-$50 feature is going to trip — Diana's seeded watch-outs are (a) audit trail, (b) fraud-detection signal, (c) per-org opt-out. A good brief names all three (or close).
3. **The strongest customer evidence** for the feature, cited by specific brain artifact — the BrillStone (Marcus Lee) interview is the only seeded evidence and should be named by path or by reference.
4. **2-3 questions Diana will push on**, tied to her historical pattern (the 2025 manager-bypass block is in her file; she will pressure-test SOX/compliance/fraud).
5. **Any conflict surfaced** — non-goals, prior decisions, stakeholder dynamics that pull against the feature.

The brief should NOT draft a new hypothesis file, NOT draft a new decision file, and NOT update any durable knowledge beyond the `Last touched:` field. Those are turn-3 and turn-4 work.

## You will be given

- The agent's full text response to turn 2.

## Pass criteria

ALL of the following must be true:

- The response names Diana's last-touched date or her cadence (acceptable: ISO date, "5 weeks", "biweekly", "overdue by ~1 week").
- The response names at least 2 of Diana's 3 seeded concerns (audit trail, fraud-detection signal, per-org opt-out).
- The response references the BrillStone / Marcus Lee interview by name or by path (e.g., `[source/interviews/2026-04-30-marcus-lee-brillstone.md]` or "the Marcus Lee interview" or "BrillStone interview").
- The response lists at least 2 specific questions Diana will push on, tied to her stake (compliance, fraud, audit trail).
- The response does NOT include a drafted hypothesis file or decision file (these are turn-3 and turn-4 work). The brief lives in the response text.

## Fail criteria (must_not)

- A new hypothesis file or decision file is drafted this turn.
- The response names none of Diana's specific concerns (audit trail, fraud signal, opt-out).
- The response fails to cite the BrillStone interview (or any customer evidence at all).
- The response is generic stakeholder-prep boilerplate not tied to Diana's seeded file.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
