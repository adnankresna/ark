# Judge: multiple_categories_surfaced (scenario 08 — weekly /review)

## What we're checking

Turn 3 is a holistic weekly `/review`. The PM has explicitly asked for a walkthrough of what's drifting, what needs attention, what's stale-but-not-yet-drifting, and what looks healthy. The brain holds five simultaneous things-worth-surfacing, deliberately seeded across different categories of finding:

1. **Drift** — `hypotheses/alert-noise-reduction.md` (promoted) is partly contradicted by the 2026-05-12 Helio Networks interview: the 60% noise-reduction target the hypothesis names may be wrong — Toby's argument is 80% is the real bar.
2. **Stale-and-relevant stakeholder** — `stakeholders/ravi-chen.md`, Eng Lead and engineering owner for the alert-noise-reduction roadmap commitment, `Last touched: 2026-03-30` (~7 weeks stale).
3. **Expiring reversal condition** — `decisions/2026-03-10-on-call-rotation-rework.md`, with reversal condition "NPS among on-call engineers drops below 32 by end of May 2026, revisit." Today is 2026-05-17; deadline is ~2 weeks out.
4. **Aging insight** — `knowledge/users/insights.md` entry dated 2026-01-29, single-source (Mendoza interview), "on-call engineers want alert grouping by service." Not contradicted, just unrefreshed for ~4 months.
5. **Healthy** — `hypotheses/api-latency-p99-vs-p95.md`, proposed, three independent corroborating signals across ~3 months, no concerns.

The right behavior is to name AT LEAST 4 of the 5 categories by **specific artifact**. The wrong behavior is to flatten into generic phrasing ("some hypotheses are drifting," "a few things are aging") or to omit categories — the failure mode is collapsing the diversity of the brain into a single narrative thread.

## You will be given

- The agent's `/review` response text in `agent_response`.
- The work_dir (judge may inspect any file to verify the artifacts named in the response actually exist with the seeded characteristics).

## Pass criteria

ALL of the following must be true:

- The /review response names AT LEAST 4 of the following 5 categories, each by specific artifact:
  1. **Drift on alert-noise-reduction** — the hypothesis is named by file or slug AND the 60%-vs-80% threshold question (or equivalent specific framing of the partial contradiction) is referenced. Not just "alert-noise hypothesis has some new evidence."
  2. **Stale-relevant stakeholder Ravi Chen** — Ravi is named, his role (Eng Lead / engineering owner for alert-noise-reduction) is named, AND a specific date (`2026-03-30` or "~7 weeks ago" or "late March") is cited. Not just "you have a stale stakeholder."
  3. **Expiring reversal condition on March-10 decision** — the decision is named (by file path or by topic — on-call rotation rework / March-10 decision) AND either the deadline (end of May / 2026-05-31) or the metric (NPS < 32) is named. (Stronger version of this is enforced by `expiring_reversal_flagged`.)
  4. **Aging insight on alert grouping by service** — the insight is named specifically (the alert-grouping-by-service theme), AND its single-source / unrefreshed / ~4-months-old character is noted. Not just "you have an aging insight somewhere."
  5. **Healthy api-latency-p99-vs-p95** — the hypothesis is named specifically AND characterized as healthy / on-track / accumulating-without-concern. (Stronger version of this — that it doesn't get over-flagged — is enforced by `healthy_not_overhyped`.)
- Each named category must be specific to the seeded artifact, not generic — the phrase "some hypotheses are drifting" without naming alert-noise-reduction does NOT count as surfacing drift.

## Fail criteria (must_not)

- The /review produces a flat "everything's fine" sweep that surfaces zero or one of the five categories.
- Two or more of the five categories are omitted entirely.
- The categories are named only generically ("you have aging insights," "some hypotheses are drifting") without specific artifacts attached.
- The review collapses into a single narrative thread that only discusses one category in depth (e.g., spends the entire response on the alert-noise drift and never mentions the March-10 decision, Ravi, the aging insight, or api-latency).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
