# Judge: no_generic_slop (scenario 09 — ideation)

## What we're checking

Turn 3 is an ideation prompt. The PM was explicit: "No generic-best-practice ideas. No 'based on industry knowledge' candidates unless the industry knowledge is ALSO corroborated by something in the brain." The failure mode this judge guards against is the brain proposing plausible-sounding-but-unmotivated candidates — the kind of generic SaaS product ideas that a model could output without reading the brain at all.

The right behavior is candidates that are specifically motivated by SPECIFIC brain artifacts. The wrong behavior is candidates like:

- "Add AI summaries of monthly spend."
- "Build a spend-analytics dashboard."
- "Ship a mobile app refresh."
- "Add Slack integration."
- "Build a financial-insights chatbot."

These would be slop because nothing in the seeded brain motivates them. (The roadmap mentions a spend-analytics refresh in "Later (Q4+)" but that's an already-known item, not an under-explored adjacency.)

The right candidates are tied to evidence patterns the brain actually contains — receipt-matching friction across multiple interviews, the Friday-batch behavior pattern, the CS-monthly receipt-matching volume, the Brex competitive signal, the explicit roadmap open question.

## You will be given

- The agent's response text from turn 3 (`agent_response`).

## Pass criteria

ALL of the following must be true:

- Every proposed candidate is traceable to a specific brain artifact (the judge can identify, for each candidate, which seeded artifact(s) it draws from).
- The candidates are NOT generic SaaS / B2B product ideas without a specific motivating signal in the brain.
- If the agent proposes a second / weaker candidate alongside the receipt-matching one, that candidate is also brain-motivated (e.g., a "Friday-batch processing mode" hypothesis grounded in the insights entry and the telemetry framing). It is acceptable to propose only one candidate if the agent says explicitly that the others are not strongly enough motivated.
- The agent does not include a "things we could also consider" tail of unmotivated ideas. Hedging "here are some other directions we could explore — AI summaries, mobile redesign, etc." would count as slop even as a postscript.

## Fail criteria (must_not)

- A proposed candidate is a generic SaaS feature idea (AI summaries, dashboards, integrations, mobile refresh, chatbot, gamification, etc.) without a specific brain artifact motivating it.
- The agent appends an "also consider…" list of unmotivated ideas at the end of the response.
- The agent's motivation for a candidate is "industry knowledge" or "competitive necessity" only, without naming the specific brain artifacts that corroborate it.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
