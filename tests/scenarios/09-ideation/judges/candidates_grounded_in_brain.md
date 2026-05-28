# Judge: candidates_grounded_in_brain (scenario 09 — ideation)

## What we're checking

Turn 3 asks the brain to propose 1-2 candidate hypotheses that the existing evidence in the brain would support but that haven't been framed yet. The PM was explicit: "Don't make stuff up. Only candidates motivated by artifacts already in the brain. Every claim in the proposed candidate must cite an existing brain artifact."

The right behavior is for each proposed candidate to be traceable to **specific existing artifacts**: the three customer interviews (Northstar 2026-01-22, Brillstone 2026-02-18, Pacific Greens 2026-04-09), the insights entry on Friday-batch processing, the Brex competitor note, the CS monthly receipt-matching ranking, the roadmap open question, or some combination thereof. Each supporting claim should wear a path-typed citation (`[ingestion/...]`, `[source/...]`, `[knowledge/...]`) pointing to a real file in the brain.

The wrong behavior is to propose candidates whose supporting evidence is invented, paraphrased without citation, or sourced primarily from `(industry-knowledge)` / training data without brain-citations alongside.

## You will be given

- The agent's response text from turn 3 (`agent_response`).
- The list of files in the working directory at the time of turn 3 (so the judge can verify cited paths exist).

## Pass criteria

ALL of the following must be true:

- The agent proposes 1-2 candidate hypotheses (not zero, not 5+).
- Each proposed candidate cites **at least two specific artifacts** that exist in the brain. Citations must be path-typed (`[ingestion/...]`, `[source/...]`, `[knowledge/...]`) and resolve to real files seeded in turn 1.
- For the receipt-matching candidate (the strongest one), the cited evidence should plausibly include some combination of: the three interviews, the CS monthly, the Brex competitor note, the Friday-batch insights entry, the roadmap open question. (The judge does NOT need to see ALL of these — but at least two distinct artifact citations per candidate.)
- No claim within a proposed candidate is sourced ONLY from `(industry-knowledge)` or `(intuition)` without brain-citations alongside. If `(industry-knowledge)` appears, it should be supplementary, not load-bearing.

## Fail criteria (must_not)

- Candidates cite no brain artifacts and read like generic-best-practice ideas.
- Candidates cite paths that don't exist in the working directory (fabricated citations).
- The receipt-matching candidate is not proposed at all (the evidence for it is the most concentrated in the brain — missing it is a serious miss, though the judge should accept the candidate framed under a different name like "smart match" or "fuzzy receipt reconciliation").
- The proposed candidates rest on training-data industry knowledge ("Brex has this so we should too") without referencing the specific brain artifacts that motivate the bet.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
