# Judge: healthy_not_overhyped (scenario 08 — weekly /review)

## What we're checking

The `hypotheses/api-latency-p99-vs-p95.md` hypothesis is the scenario's deliberately-healthy item: three independent corroborating signals (Linnea Systems support ticket 2026-02-14, Datapeak interview 2026-04-18, Sam Tran hallway 2026-05-05), no contradictions, status `proposed` while engineering scoping continues. There is nothing actionable about it this week.

The right behavior is to mention it briefly in the /review so the PM knows it's tracked, and to characterize it as healthy / on-track / quietly accumulating evidence. The wrong behavior is to either (a) over-flag it by placing it alongside the drift / stakeholder / decision items in the action column, or (b) pick it as one of turn 4's top-two action items just because it's mentioned in the review.

The failure mode this judge is calibrated for: brains that have learned "be thorough" too aggressively and treat *every* item in the /review as needing comparable PM attention. A useful /review distinguishes "tracked, no action" from "needs decision this week" — flagging the healthy item as actionable is noise, exactly the noise a holistic /review is supposed to filter out.

This judge is applied to BOTH turn 3 (the /review) AND turn 4 (the top-two pick).

## You will be given

- For the turn-3 application: the agent's `/review` response text in `agent_response`.
- For the turn-4 application: the agent's top-two-pick response text in `agent_response`.
- The work_dir (judge may inspect `hypotheses/api-latency-p99-vs-p95.md` or equivalent to confirm the hypothesis is indeed in the seeded healthy state).

## Pass criteria

ALL of the following must be true:

**For turn 3:**

- The api-latency-p99-vs-p95 hypothesis is mentioned in the /review — by name or by clear topical reference ("the P99 latency hypothesis," "the latency-on-alert-ingest hypothesis"). The PM should know it's tracked.
- The hypothesis is characterized as healthy / on-track / quietly accumulating / no concerns — language that signals "no action needed this week." Acceptable phrasings include: "healthy," "on track," "building quietly," "no concerns yet," "tracked, nothing to do this week," or comparable.
- The hypothesis is placed in a section / position that signals "noted, not action-required" — not interleaved with the drift / stakeholder / decision items, not at the top of the response. The `priority_ordering` judge enforces the positional rule; this judge enforces the framing rule.

**For turn 4:**

- The top-two action picks do NOT include the api-latency-p99-vs-p95 hypothesis.
- If api-latency is mentioned in turn 4's response at all, it is mentioned only as an explicit *non-pick* with reasoning ("api-latency is healthy and doesn't need attention this week — that's why I didn't pick it"). It does NOT appear as a candidate that lost to a tiebreaker, because there is no tiebreaker — the time-pressured items dominate.

## Fail criteria (must_not)

- Turn 3 frames the api-latency hypothesis as needing action this week.
- Turn 3 places api-latency in the action column / top section / "things to do Monday" tier alongside the drift / stakeholder / decision items.
- Turn 3 omits api-latency entirely (it should be mentioned briefly so the PM knows it's tracked — silent dropping is a different failure mode, and this judge fails on it too).
- Turn 4 includes api-latency in the top-two picks.
- Turn 4 treats api-latency as a candidate that almost made the cut — it shouldn't have, because the time-pressured items are obviously more urgent.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
