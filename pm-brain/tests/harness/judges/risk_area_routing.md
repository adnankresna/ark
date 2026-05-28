# Judge: risk_area_routing

## What we're checking

At turn 8, a market signal arrives — Vanta has shipped real-time alerts as a paid Enterprise add-on at ~$5K/year. This is a **viability** signal (we can monetize a real-time tier, market has validated the price point). It is NOT a value-risk signal (Vanta doesn't tell us anything new about whether our customers want real-time — Brex already gave us that).

The agent should route this evidence to the viability risk area, not the value risk area. Mis-routing here would conflate two distinct risks and weaken the reasoning trail.

## You will be given

- The target file(s): all markdown files under `hypotheses/`.
- The target file: `knowledge/market/competitors/vanta.md` (or wherever the agent put it).
- The turn context: turn 8, Vanta competitor changelog.

## Pass criteria

ALL of the following must be true:

- The hypothesis's **viability** risk section contains new evidence referencing the Vanta ingestion (turn 8).
- The evidence row captures the price point ($5K/year) or the structural choice (real-time as opt-in add-on).
- The hypothesis's **value** risk section was NOT modified by this turn.
- A competitor record exists for Vanta under `knowledge/market/` (file location may vary — `landscape.md`, `competitors/vanta.md`, or `trends.md` all acceptable).

## Fail criteria (must_not)

- Vanta evidence landed in value-risk ("Vanta proves customers want real-time" — wrong, that's a viability/willingness-to-pay signal, not a value signal).
- Vanta evidence landed in feasibility ("Vanta proves it's buildable" — Vanta doesn't speak to our eng team's capacity).
- Vanta evidence is missing from durable market knowledge.
- The agent overstates the signal ("Vanta confirms real-time is the future" — overreach; Vanta confirms a paid opt-in tier works).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
