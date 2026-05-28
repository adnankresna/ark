# Judge: risk_coverage_assessed (scenario 10 — promotion gate)

## What we're checking

At turn 2, the PM asks the brain whether to promote `same-day-rebooking-flow`. The hypothesis schema mandates 5 risk areas: **Value, Usability, Feasibility, Viability, Other**. A defensible promotion call requires that all 5 are considered — even when an area is empty, the emptiness is the signal.

As seeded in turn 1: **Value** has 5 supporting evidence rows across multiple provenance tiers. **Usability** is near-empty (Maria's notification-fatigue concern is the only related signal, more design-caveat than tested usability evidence). **Feasibility** has the single Sam stakeholder-verbal flagging a calendar-refactor concern — uninvestigated. **Viability** has zero evidence (no business case, no retention modeling, no pricing case). **Other** (regulatory, ethical, partnership-dependency, brand, security per the schema) is empty.

The right behavior is to walk through ALL FIVE risk areas — naming each by the schema's name — and for each one state whether evidence exists, what tier, and (if empty) call out the emptiness. Skipping a risk area is exactly the failure mode this judge is for: a promotion call that "feels strong on Value" but never asked about Viability is exactly the kind of judgment failure the brain exists to prevent.

## You will be given

- The agent's turn-2 response text in `agent_response`.
- The target file(s): all markdown files under `hypotheses/`.

## Pass criteria

ALL of the following must be true:

- The agent's response explicitly names and walks through ALL FIVE schema risk areas: Value, Usability, Feasibility, Viability, Other. Each is mentioned by the schema's name (or an unambiguous synonym — "Business viability" is acceptable for Viability; "business case" alone is not).
- For each risk area, the agent states whether evidence exists and at what tier, OR states explicitly that the area is empty.
- The agent identifies the two specific empty/under-covered risk areas — Viability (zero evidence) and Feasibility (one uninvestigated concern) — as gaps the promotion call must reckon with.

## Fail criteria (must_not)

- Walks only 3 or 4 of the 5 risk areas.
- Merges Viability into Value (treating customer WTP signals as a Viability case — they aren't; Viability is the *business* case, not the customer's case).
- Invents a risk area not in the schema (e.g., treats "Ethical" as a separate top-level area when the schema places ethical risks under Other).
- Walks all 5 areas but fails to call out which are empty / under-covered.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
