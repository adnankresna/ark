# Judge: tensions_named (scenario 07 — migration mode)

## What we're checking

Turn 3 is the first time in this scenario the PM (Aisha) asks the brain to surface cross-artifact tensions. The migrated folder contains several real contradictions, and the PM's prompt is explicit: name BOTH sides, cite the source artifacts on each side by path, do NOT resolve anything yet.

The brain has 8 migrated artifacts to work from. The genuine tensions baked into the migration are:

- **Natural-language alerting:** Sam Vega (Acme, March 2026 interview) said it would unlock a 30% renewal. Reina Cho (Globex, April 2026 interview) called it "a toy" and said her team would disable it. Source: `source/interviews/*acme*.md` vs `source/interviews/*globex*.md`.
- **Strategy vs. April 2026 reality (compliance / audit-trail):** The Q4 2025 strategy memo explicitly anti-prioritizes compliance / audit-trail features. The April 2026 Globex interview says audit-trail is the #1 thing blocking footprint expansion at a $140k → potentially $400k ACV customer in a regulated vertical. Source: `source/strategy/*.md` vs `source/interviews/*globex*.md`.
- **Roadmap commits vs. CFO budget cut:** The H1 roadmap doc and strategy memo both assume a +4 eng hiring plan for H2 2026 to ship SLO builder GA + service catalog + natural-language alerting GA. The CFO's April 22 email defers ~40% of H2 net-new headcount. Source: `source/roadmap/*.md` + `source/strategy/*.md` vs `source/exec/*.md` (or `source/adhoc/*.md`).
- **Persona ownership overlap:** Platform-engineer persona says they "own reliability of the platform itself." SRE persona says they "own reliability of production services." The line between these is fuzzy — and the strategy memo bets that platform engineers are the wedge buyer, while the SRE persona doc admits SREs often hold the economic-buyer role at enterprise scale. Source: `source/personas/*platform*.md` vs `source/personas/*sre*.md` (or equivalent paths).
- **Landscape "trend I'm watching" vs. strategy anti-bet:** Landscape doc (Feb 2026) notes that audit-trail / compliance asks are "climbing" in regulated industries. Strategy memo (Nov 2025) explicitly says we are NOT building compliance features. This is the same compliance tension visible from a third artifact.

The right behavior is an enumerated list naming at least 3 of these (the natural-language-alerting one is mandatory, and at least one strategy-vs-reality tension is mandatory), with both sides cited and zero attempts at resolution.

## You will be given

- The agent's response text from turn 3.
- The work_dir markdown listing (background context).

## Pass criteria

ALL of the following must be true:

- The response is **enumerated** (list, not prose). At minimum 3 specific tensions.
- The natural-language-alerting tension is named, with both sides cited to the respective interview artifacts by path.
- At least one strategy-vs-reality tension is named — either the compliance/audit-trail conflict (strategy memo's anti-bet vs Globex interview), OR the roadmap-vs-budget conflict (H1 roadmap's H2 assumptions vs CFO email), OR both.
- Each enumerated tension cites the source artifact(s) on each side by path (e.g., `source/interviews/2026-03-11-acme.md`). The reader can click through.
- The response did NOT propose resolutions to the tensions — explicitly stayed in the "list, don't fix" mode the PM asked for.

## Fail criteria (must_not)

- Prose narrative that buries the conflict list inside paragraphs (the PM explicitly asked for a list).
- The agent resolves one or more tensions on its own (e.g., "obviously we should build audit logs" — that's a future-turn move).
- The agent claims there are no significant contradictions, or downplays the natural-language-alerting split as "minor feedback variation."
- The agent invents tensions not actually present in the artifacts.
- Source citations are missing or vague (e.g., "the strategy memo says X" without a path link).

## Important

If the agent surfaces MORE than 3 tensions — including the persona-overlap one or the landscape-vs-strategy compliance triangulation — that's a stronger PASS, not a fail. The minimum bar is 3 with the natural-language-alerting one and at least one strategy-vs-reality one present.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
