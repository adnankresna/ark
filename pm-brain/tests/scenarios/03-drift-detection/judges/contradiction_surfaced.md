# Judge: contradiction_surfaced (scenario 03 — drift reversal)

## What we're checking

At turn 2, the same customer (Dr. Linda Park / Brightsmile Dental) who championed Provider Availability Sync in January 2026 returns with a reversed stance after using the feature for 8 weeks:

- The bidirectional sync is the bug — providers' personal calendars contain "BLOCKED — admin / lunch / case prep" that shouldn't translate to "unavailable for any patient."
- Front desk fights the sync more than they did the old manual workflow.
- Double-bookings did NOT improve (3 last month, 2 the month before — roughly unchanged).
- WTP collapsed from $50/seat (January) to $10/seat for a read-only / one-way version.
- Brightsmile is considering switching off the feature; Dentrix's read-only competitor design now looks better.

The brain's value is that it surfaces this contradiction rather than auto-resolving it. The wrong behavior is to silently demote the hypothesis, delete the original Brightsmile evidence row, or flatten the May interview into a "minor feedback note."

## You will be given

- The target file(s): all markdown files under `hypotheses/`.
- The May 17 interview content in agent_response or via the ingestion file.

## Pass criteria

ALL of the following must be true:

- The hypothesis file gains an evidence-against row (or contradictions section) citing the May 17 Brightsmile interview, with provenance tag.
- The contradiction is named explicitly — at minimum, the *kind* of contradiction (WTP reversed, bidirectional sync is harmful, outcome metric didn't move, original champion now wants to disable) is captured.
- The **original January Brightsmile evidence row is preserved**, not deleted or rewritten. The historical record of why we built the thing stays intact.
- The hypothesis was NOT silently demoted (status change with no audit trail) in this turn. Either the status stays as is and the contradiction sits in evidence-against, or the status changes with explicit reference to the new evidence.

## Fail criteria (must_not)

- The original January Brightsmile evidence row is deleted, overwritten, or rewritten to match the May stance.
- The hypothesis is auto-demoted without surfacing the conflict to the PM first (turn 2's job is to surface, not resolve).
- The May 17 interview is flattened ("minor adoption feedback") rather than recorded as a reversal.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
