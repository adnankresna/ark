# Judge: irrelevant_overdue_not_flagged (scenario 05 — Helena is silent here)

## What we're checking

The whole point of cadence flags being useful (rather than nagging) is that the brain distinguishes **stale AND relevant to current work** from **stale generally**. Scenario 05 sets up the test deliberately: Helena Vargas (CFO) is the stakeholder with the **stalest** 1:1 cadence in the brain (2026-03-08, 10 weeks ago), but she is **NOT implicated** in the Custom Dashboards deprecation — Custom Dashboards is a small slice of infra cost; her own stakeholder file explicitly says she doesn't weigh in on feature-level deprecations unless infra cost shifts materially, and the agreed cadence with her is "as-needed, no standing slot."

The right behavior is that when the brain produces a context-scoped cadence flag (turn 3's /review framed around the Custom Dashboards decision; turn 4's pre-launch check on the decision file), **Helena is not on that list**. If the brain wants to mention Helena's general cadence in a separate, clearly-distinct general-roster section of /review, that's fine — but she must NOT be presented as a stakeholder the PM should contact before the Custom Dashboards decision lands.

The wrong behavior — and the one this judge specifically guards against — is the brain treating raw staleness as the signal and flagging every overdue stakeholder regardless of relevance. That's the moralizing failure mode: every PM has cadence debt all the time; a brain that surfaces all of it indiscriminately is noise.

## You will be given

- For the turn-3 application: the agent's `/review` response text in `agent_response`.
- For the turn-4 application: the decision file under `decisions/2026-05*.md` AND the agent_response text wrapping the draft.

## Pass criteria

ALL of the following must be true:

- Helena (Vargas / CFO) is NOT named in the list of stakeholders the PM should contact before the Custom Dashboards decision lands (in turn 3's review-with-decision-context output, OR in turn 4's pre-launch check section of the decision file/response).
- If the brain produces a separate, clearly-distinct general-cadence section (e.g., "Other cadence notes — not blocking this decision"), Helena appearing there is fine, AS LONG AS the decision-scoped section above is clean of her.

## Fail criteria (must_not)

- Helena appears in the should-talk-to-before-Custom-Dashboards-lands list in turn 3's review.
- Helena appears in the decision file's "Pre-launch checks" / "Talk to before this lands" section.
- The agent presents Helena's stale cadence as a blocker or pre-condition for the Custom Dashboards decision.
- The agent merges "stakeholders to contact before this decision" with "stakeholders who are generally overdue" into a single undifferentiated list — that collapses the relevance filter the scenario is testing.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
