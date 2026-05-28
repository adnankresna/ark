# Judge: relevant_overdue_flagged_on_decision (scenario 05 — pre-launch check names the right people)

## What we're checking

Turn 4: PM asks the brain to draft the Custom Dashboards deprecation decision. The PM explicitly requests a "Pre-launch checks" section naming stakeholders to talk to before the decision lands, scoped to people who are (a) materially affected by THIS decision AND (b) stale on cadence.

The right behavior is that the drafted decision file (or the wrapping response text) names **Diana Okonkwo** (VP Customer Success, last 1:1 **2026-03-22**) and **Marcus Avila** (Sales Director, last 1:1 **2026-04-12**) as the should-talk-to-before-this-lands stakeholders, with their roles, last-1:1 dates, and the reason each is implicated in the deprecation.

The decision file should also satisfy the standard decision schema: status `proposed`, evidence rows tagged with provenance, a specific observable reversal condition, an "Explicitly NOT doing" section, and remaining ambiguities.

## You will be given

- The target file(s): `decisions/2026-05*.md` (the new deprecation decision).
- The agent_response (the full draft message wrapping the file).

## Pass criteria

ALL of the following must be true:

- The decision file exists under `decisions/2026-05*.md` and is about Custom Dashboards deprecation.
- The decision OR the wrapping response text has a section equivalent to "Pre-launch checks" / "Talk to before this lands" / "Stakeholder pre-checks" — a clearly delimited list of people the PM should contact before the decision is decided.
- That section names **Diana** (Okonkwo / CS VP), with her last-1:1 date **2026-03-22** cited AND the reason she's implicated in this decision named (CS owns the long-tail users / renewal motion / "the people who use Custom Dashboards REALLY use Custom Dashboards" insight).
- That section names **Marcus** (Avila / Sales Director), with his last-1:1 date **2026-04-12** cited AND the reason he's implicated named (uses Custom Dashboards in demos / sales motion / RFP cost).
- Decision status is `pending` (per the canonical decision schema `pending | decided | superseded`) — i.e., the decision is opened but not yet decided. `proposed` is also acceptable as a synonym if the agent used PM-language; what matters is that the status signals "not yet final."
- A specific, observable reversal condition is named (e.g., "if NRR for accounts that lost Custom Dashboards drops more than X% by date Y, reverse" — not vague).
- Evidence rows in the decision carry provenance tags from the canonical enum (`[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, ...)`, `(intuition, PM, ...)`, `(industry-knowledge)`, `(chat, no artifact)`).
- An "Explicitly NOT doing" section names what's coming off the table (e.g., the previously-discussed Custom Dashboards roadmap items, the embed-flow rebuild).

## Fail criteria (must_not)

- The pre-launch / talk-to-before-this-lands section is missing.
- Diana or Marcus is omitted from the pre-launch check.
- Diana or Marcus is named without a specific date — vague phrasing like "haven't talked to Diana in a while" does not count.
- The reason each is implicated in THIS decision is not named (i.e., they're listed as generic "you should check in with them" cadence-debt items).
- Decision status is `decided` (i.e., flipped to final despite the pre-launch checks being outstanding).
- Reversal condition is missing or vague.
- Evidence rows lack provenance tags.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
