# Judge: overdue_surfaced_in_review (scenario 05 — /review names the right stale stakeholders)

## What we're checking

Turn 3 is a weekly `/review` with explicit framing: *"anything I should be aware of as I draft the Custom Dashboards deprecation decision this week?"* The PM is signaling they want the review scoped to the load-bearing decision in front of them, not a generic relationship-debt audit.

The right behavior is to surface the Custom Dashboards deprecation as a major item AND name **Diana Okonkwo** (VP Customer Success, last 1:1 **2026-03-22**, ~8 weeks ago) and **Marcus Avila** (Director of Sales, last 1:1 **2026-04-12**, ~5 weeks ago) specifically as stakeholders the PM should re-contact before drafting the decision — because their stake in this decision is real (Diana owns the CS relationship with the long-tail users who actually use Custom Dashboards; Marcus uses it in demos) AND their cadence with the PM is stale enough that a quick Slack ping isn't sufficient.

The wrong behaviors are:

- Producing a generic cadence list ("you haven't talked to Diana, Helena, and Marcus recently") without tying any of them to the Custom Dashboards decision.
- Naming the people without specific dates ("you should re-check with CS").
- Failing to surface either Diana or Marcus at all.

(This judge does NOT enforce the "Helena should be silent on this turn" half of the behavior — that's the job of `irrelevant_overdue_not_flagged`. Here we only check that Diana and Marcus are named correctly.)

## You will be given

- The agent's `/review` response text in `agent_response`.
- The work_dir (judge may inspect any file, including stakeholder files to confirm dates cited match seeded dates).

## Pass criteria

ALL of the following must be true:

- The agent surfaces the Custom Dashboards deprecation decision as one of the headline items in the review (or names it explicitly as the framing for the cadence call-outs).
- The agent names **Diana** (Okonkwo / VP Customer Success / CS) as a stakeholder to contact before drafting the decision, AND grounds her staleness with a quantitatively-specific reference to her last 1:1 on **2026-03-22**. ANY of these forms PASSES: (a) the ISO date `2026-03-22`; (b) "March 22"; (c) a day-count that resolves to it ("56 days", "~8 weeks ago"); (d) a month-anchored "March 2026" combined with a numeric gap like "8 weeks" or "~2 months". The judge's job is to confirm the agent retrieved Diana's stakeholder file and reasoned over its content — not to enforce a single date format.
- The agent names **Marcus** (Avila / Sales Director) as a stakeholder to contact before drafting the decision, AND grounds his staleness with a quantitatively-specific reference to his last 1:1 on **2026-04-12**. Same format flexibility applies: ISO date, "April 12", "35 days", "~5 weeks ago", or "April 2026" + "5 weeks" all PASS.
- The framing connects each person's cadence to their stake in the Custom Dashboards decision specifically — not just "you haven't talked to them in a while." At minimum: Diana → CS / long-tail-user / renewal angle; Marcus → demos / sales motion / RFP angle.

## Fail criteria (must_not)

- Either Diana or Marcus is omitted from the should-contact list in the context of this decision.
- Diana or Marcus is named without ANY quantitatively-specific staleness reference (e.g., "haven't talked to Diana in a while" with no date or day-count). A day-count or week-count that triangulates to the seeded date counts as specific; vague "in a while" / "recently" / "lately" does not.
- The cadence flag is generic — a roster-wide "here's who you haven't talked to recently" list without naming why each person's staleness matters for the Custom Dashboards call.
- The agent treats the /review as healthy / nothing-to-flag despite the explicit framing.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
