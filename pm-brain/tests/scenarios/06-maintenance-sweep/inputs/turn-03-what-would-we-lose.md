# Lossiness analysis — what would each proposed change actually erase?

For each candidate you listed in the previous turn, walk me through specifically what we'd lose if we did the change. I want concrete answers, not generic safety theater.

For each candidate, address:

1. **Signal loss.** Would we erase a distinct piece of evidence (a quote, a number, a stakeholder claim)? Or is the same signal preserved verbatim under `source/`, so the consolidation/archive is purely about reducing duplication in `ingestion/` and `knowledge/`?
2. **Link loss.** Are there other files in the brain that currently reference the candidate? If we consolidate or archive, do those links go dead — or do they need to be updated to point at the new location?
3. **Audit trail loss.** If somebody six months from now reads a downstream artifact (a decision, a hypothesis, a synthesis) and follows a link back to one of these candidates, will they still land somewhere meaningful?
4. **Specifically for the redundant churn ingestions:** if we consolidate the 3 into 1, what specifically would the consolidated record need to cite/include so that the 3 separate triangulating perspectives (Devi's CS framing, Marco's ticket pattern, my Amplitude funnel cut) are still all readable?
5. **Specifically for the weekly-email-summary hypothesis:** if we demoted it now, what would we lose vs. leave it as-is? (Honest answer is probably "nothing, because the A/B test result is already in the file" — but say so if so.)
6. **Specifically for the onboarding-funnel knowledge file:** if we archive the November version, do we lose the November funnel numbers? Or are those preserved elsewhere (e.g., in the December redesign decision record's evidence rows)?
7. **Specifically for the jordan-pm stakeholder file:** is there any active reference to Jordan in any current decision, hypothesis, or knowledge file that would go dead if the file moves?

Be specific. "No signal lost" is a valid answer where true — but you have to justify it ("the same observations are preserved verbatim under `source/...`") rather than just assert it.

If for any candidate you're not sure whether something would break, say "I don't know without checking X" rather than guessing.

Still no edits. This is still analysis.
