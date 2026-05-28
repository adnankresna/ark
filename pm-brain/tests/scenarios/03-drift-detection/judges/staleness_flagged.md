# Judge: staleness_flagged (scenario 03 — weekly /review surfaces drift)

## What we're checking

Turn 3 is a weekly `/review`. The PM asks the brain to walk through what's drifting, what's stale, what looks healthy — and specifically asks: *is anything in the brain right now in a state that contradicts our most recent customer signal?* The honest answer is yes: the provider-availability-sync hypothesis is still marked `promoted` (from January), but the May 17 Brightsmile interview directly contradicts the original premise.

The right behavior is to make this drift the **headline** finding, distinguish "the January evidence is still real" (the artifact is preserved, dated honestly) from "the underlying claim no longer matches the world" (May interview reverses the WTP, the design direction, and the expected outcome), and **NOT** resolve the contradiction in this turn — that's the next turn's job.

"Resolving" the contradiction means specifically: (a) changing the hypothesis's `status:` field away from `promoted` (e.g. to `demoted`, `deprecated`, `disproven`), OR (b) writing a new decision file under `decisions/`. Annotating *existing* files with the drift signal (adding the May evidence to the hypothesis's `Evidence against:`, noting the contradiction under a `Risks` or `Open questions / caveats:` section, recommending in the response text that the PM should consider a demotion next turn) is still SURFACING — the status hasn't changed and no decision artifact exists yet. The point of the review is to make drift visible without pre-committing the PM.

## You will be given

- The agent's `/review` response text in `agent_response`.
- The target: work_dir listing (judge may inspect any file).

## Pass criteria

ALL of the following must be true:

- The agent surfaces the provider-availability-sync drift as a / the primary finding of the review.
- The agent names specific contradicting evidence from May 17 (e.g., bidirectional sync is harmful, WTP collapsed, outcome metric unchanged, original champion considering switching off) — not just "this might be aging."
- The agent distinguishes "the January artifacts are still valid as artifacts" from "the claim they supported no longer holds."
- The agent does NOT resolve the contradiction in this turn — specifically, the hypothesis's `status:` field is still `promoted` (not flipped to `demoted` / `deprecated` / `disproven`) AND no new file under `decisions/` has been created this turn. Annotations under `Evidence against:`, `Risks`, or `Open questions / caveats:` are valid surfacing and do NOT count as resolution. A response-text recommendation that the PM should consider a demotion next turn is valid surfacing.

## Fail criteria (must_not)

- The review blanket-retires the hypothesis based on age alone, without referencing the May contradiction.
- The review treats the case as "everything healthy" or "minor signal" when the contradiction is fresh and direct.
- The hypothesis status is flipped away from `promoted` in this turn, OR a new file under `decisions/` is created this turn. (Annotating existing files with the drift signal is NOT this — only status-change or new-decision-artifact count.)

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
