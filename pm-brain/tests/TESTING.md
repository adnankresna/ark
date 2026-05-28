# Testing PM Brain — detailed reference

This is the **detailed** testing doc: scenario format, harness internals, ground-truth schema, cost behavior, current coverage, gaps before publishable, and how to add a scenario.

> A note on vocabulary. A *brain* is the folder of markdown files the skill maintains for a PM. *Ingesting* something means feeding it into the brain. *Provenance* is the tag on each claim that says where it came from (documented interview, verbal claim, hunch, etc.). A *hypothesis* is a statement the brain tracks evidence for. Full definitions live in the [glossary](../docs/glossary.md).

For the 90-second version, see [`README.md` § Tests](../README.md#tests) and [`tests/README.md`](./README.md).
For the design rationale (why scenarios over per-turn unit tests, why LLM-as-judge is reserved), see [`docs/testing.md`](../docs/testing.md).

---

## Why this exists

The thing PM Brain actually delivers is **trajectory over time** — does the brain converge on the right hypotheses, surface contradictions, draft a defensible decision after weeks of accumulating evidence. Testing one ingestion at a time misses the whole product. So the unit of test is a **scenario**: an ordered stream of synthetic artifacts representing weeks-to-quarters of a PM's life, with ground-truth assertions about brain state after each turn.

A scenario passes if, across N runs, structural assertions pass 100% and content (LLM-judge) assertions pass at or above the scenario's content threshold (default 0.8). Anything less means the brain is doing the wrong thing under real PM noise — that's a bug, not a flake.

---

## Three eval layers

| Layer | What it checks | Mechanism | Determinism | Cost per call |
|---|---|---|---|---|
| **Structural** | File schema, INDEX updates, evidence rows exist, no orphan refs, link integrity | Python asserts in [`harness/checks/structural.py`](./harness/checks/structural.py) | Deterministic | Free |
| **Content** | Did the right hypothesis get promoted? Was the contradiction text semantically what we expected? | `claude -p` as judge using rubrics in [`harness/judges/`](./harness/judges/) | Non-deterministic | ~$0.02–0.05 (Sonnet) / ~$0.10–0.20 (Opus) |
| **Convergence** | Across N runs of the same scenario, what's the pass rate per assertion? | Aggregation in [`harness/run_scenario.py`](./harness/run_scenario.py) `aggregate()` | Statistical | N × per-run cost |

**Rule:** if a structural assertion can answer the question, don't reach for a judge. Judges cost money and add variance. The eval suite enforces this: judges are reserved for genuinely judgment-heavy claims ("was the contradiction surfaced explicitly vs. silently demoted"). File presence, link integrity, evidence-count deltas — all structural.

---

## Scenario format

Each scenario lives under `tests/scenarios/<NN-slug>/`:

```
tests/scenarios/01-b2b-churn/
├── README.md          # What the scenario covers + which lifecycle moves it exercises
├── inputs/            # Ordered synthetic artifacts (turn-NN-<kind>.md)
└── expected.yaml      # Ground-truth assertions per turn + final state
```

### Inputs are committed, cached, immutable

Synthetic artifacts are generated once (by hand or with an LLM), committed, and **never regenerated on the fly**. If you can't reproduce the input, you can't reproduce the failure. When you change inputs, change them deliberately and note the change in the scenario's `README.md`.

### Ground-truth schema (`expected.yaml`)

```yaml
scenario: 01-b2b-churn
description: |
  Free-text scenario summary.

pass_threshold:
  structural: 1.0   # Must pass every run
  content: 0.8     # 4 out of 5 runs minimum

turns:
  - turn: 1
    input: turn-01-interview-acme-ops.md
    structural:
      - file_exists_glob: source/interviews/*acme*.md
      - file_modified_or_created: stakeholders/acme-ops.md
      - hypothesis_count_at_least: 1
    content:
      - judge: hypothesis_proposed_not_promoted
        rubric: judges/hypothesis_proposed.md
        target_glob: hypotheses/*.md
        expected_meaning: "..."
        must_not: "..."
        # Optional: model: opus      # opt-in override; default judge model is Sonnet

final_state:
  structural:
    - all_internal_links_valid: true
    - no_orphan_evidence: true
    - no_silent_hypothesis_demotion: true
  content:
    - judge: audit_trail_navigable
      rubric: judges/audit_trail.md
      expected_meaning: "..."
```

### Structural assertion types

Implemented in [`harness/checks/structural.py`](./harness/checks/structural.py). Every assertion takes the working directory, an argument, and an optional `(files_before, files_after)` snapshot pair.

| Assertion | Purpose |
|---|---|
| `file_exists` / `file_exists_glob` | File / glob presence after the turn. Glob supports `OR` for alternatives. |
| `file_modified` / `file_modified_glob` | File was touched in this turn (mtime diff). |
| `file_modified_or_created` | File exists OR was created in this turn. |
| `hypothesis_count_at_least: N` | At least N hypothesis files exist (excluding INDEX / _SCHEMA). |
| `hypothesis_evidence_count_increased_for` | Named hypothesis gained at least one evidence-for row this turn. |
| `hypothesis_evidence_count_unchanged_for` | Named hypothesis did NOT gain evidence (used for low-signal noise turns). |
| `all_internal_links_valid` | Every relative markdown link resolves to an existing file. |
| `all_decisions_have_reversal_condition` | Every `decisions/*.md` has a non-vague reversal field. |
| `no_orphan_evidence` | Every evidence row links to a `source/` or `ingestion/` file. |
| `no_silent_hypothesis_demotion` | No hypothesis status moved to `demoted` without an evidence-against trail. |

### Content (judge) assertions

Each entry resolves a rubric markdown file under [`harness/judges/`](./harness/judges/) and passes it (plus target file content + scenario context) to `claude -p`. The judge must output exactly one `VERDICT: PASS|FAIL|UNCERTAIN — <reason>` line. UNCERTAIN counts as FAIL — aggregate pass rate across N runs handles the noise.

Default judge model is **Sonnet** (cheap, fast, follows rubrics reliably). Opt into Opus per-assertion with `model: opus` only when you've seen Sonnet flake on the same rubric across multiple runs.

---

## How the harness runs a scenario

For each run, [`harness/run_scenario.py`](./harness/run_scenario.py):

1. **Spins up a fresh scaffold** in a temp dir (or under `tests/workdir/` if `--keep-workdir` is set). Each run is isolated — no state leakage between runs.
2. **Iterates `inputs/` in filename order.** For each turn:
   - Snapshots the working dir (`files_before` mtime map).
   - Invokes `claude -p` with the turn prompt + the input artifact embedded. The skill's own CLAUDE.md takes over and decides where to write.
   - Snapshots again (`files_after`).
   - Runs the turn's structural assertions using the snapshot pair.
   - Runs the turn's content assertions (judge calls), unless `--skip-content` is set.
3. **Runs `final_state` assertions** after all turns.
4. **Writes a result JSON** to `tests/results/<date>-<scenario>-<run>.json`.

Across N runs, the harness computes per-assertion pass rate and compares against `pass_threshold`.

### CLI flags

```
python tests/harness/run_scenario.py <scenario-dir> [flags]

  --runs N                Number of runs to aggregate. Default 1.
  --max-cost N            Abort the run if cumulative cost (API-equivalent USD) exceeds N. Default 20.
  --keep-workdir          Keep the temp working dir under tests/workdir/ for inspection.
                          Without this flag, the workdir is deleted after each run.
  --stop-after-turn N     Stop after turn N (debug / iteration aid).
  --skip-content          Skip judge calls — structural assertions only (free, fast).
```

### Environment overrides

| Variable | Default | Purpose |
|---|---|---|
| `PM_BRAIN_CLAUDE_BIN` | `claude` | Path to the Claude Code CLI binary. |
| `PM_BRAIN_TURN_TIMEOUT` | `600` (seconds) | Per-turn `claude -p` timeout. |
| `PM_BRAIN_JUDGE_TIMEOUT` | `180` (seconds) | Per-judge `claude -p` timeout. |
| `PM_BRAIN_TURN_MODEL` | `sonnet` | Model used for scenario turn execution. |
| `PM_BRAIN_JUDGE_MODEL` | `sonnet` | Default model for judges (per-assertion `model:` overrides). |

---

## Cost model

The harness records the `total_cost_usd` field that `claude -p` returns in its JSON envelope. Under the Anthropic API this is real billing; **under a Claude subscription it is the API-equivalent price**, useful as a proxy for "how much quota this call consumed against my 5-hour rolling window." Either way, it's the number to optimize.

Ballpark with default Sonnet model split:

| Operation | Cost (approx., API-equivalent USD) |
|---|---|
| Per turn (`claude -p` ingesting one artifact) | $0.10–0.40 |
| Per judge call (Sonnet) | $0.02–0.05 |
| Per judge call (Opus, opt-in) | $0.10–0.20 |
| Per scenario run (10 turns + ~15 judges) | $3–5 |
| `--runs 5` of one scenario | $15–25 |
| Full suite (5 scenarios × 5 runs, when scenarios 2–5 land) | $75–125 |

`--max-cost` (default $20) aborts the run if the cumulative number exceeds the cap. Use it.

---

## What the harness does NOT do

- **Doesn't auto-grade content for free.** Every judge call is a real LLM call.
- **Doesn't share state between runs.** Each run gets a fresh scaffold. State leakage is a bug.
- **Doesn't retry on UNCERTAIN.** UNCERTAIN counts as FAIL. Aggregate pass-rate across runs handles the noise.
- **Doesn't synthesize inputs.** Inputs are committed. To add a turn, edit `inputs/` and `expected.yaml` together.
- **Doesn't push to the user's brain.** Every test runs in a fresh isolated temp dir.

---

## Assumptions the test suite makes

These are the load-bearing premises. Violate them and the suite stops measuring what it claims to measure.

1. **The skill is the unit under test, not a specific model.** The harness invokes `claude -p` with `--model sonnet` by default because Sonnet is what most PMs will run day-to-day; if the skill only works on Opus, the skill is broken.
2. **`source/` is the audit anchor.** The scenario judges and several structural assertions (`no_orphan_evidence`, `audit_trail_navigable`) assume every claim traces back to a `source/<kind>/*.md` file. The scaffold's `CLAUDE.md` instructs the agent to copy verbatim *before* synthesis. If a turn is failing `no_orphan_evidence`, check whether the agent actually populated `source/`.
3. **Hypothesis ID drift is allowed.** The scaffold schema uses `H-V1`, `H-U1`, `H-F1`, `H-B1`, `H-O1` (risk-area letter + per-area index). Older docs and some `expected.yaml` entries reference `H2`. The structural resolver in `_resolve_hypothesis` accepts literal IDs, falls back to mtime ordering, then to the single-hypothesis case. Keep new assertions slug-based when you can.
4. **One scaffold per run.** Sharing scaffolds between runs would leak state and contaminate convergence numbers. Don't do it.
5. **Synthetic data is too clean.** Real PM signal is noisier (typos, jargon, half-formed thoughts). The roadmap includes an anonymized real-data scenario for exactly this reason.
6. **`UNCERTAIN = FAIL` is the right default.** A judge that hedges is a judge that didn't decide. Tightening the rubric is the fix; "retry on UNCERTAIN" hides the rubric problem.

---

## Current coverage

### Scenarios

| Scenario | Status | Lifecycle moves exercised |
|---|---|---|
| `01-b2b-churn` | ✅ Inputs committed, expected.yaml drafted, full harness runs end-to-end. Iterating on judge thresholds. | Hypothesis proposed (single anecdote, NOT promoted), feasibility risk updated, market/product signal routing, insight evidence accumulation, low-signal noise rejection, contradiction surfacing without silent overwrite, decision drafting with reversal condition, market signal routed to viability not value, insight promoted with dissent preserved, decision quality (full evidence trail, specific reversal). |

### Structural assertion types

All 12 listed in the table above are implemented and exercised by scenario 01.

### Judges

| Rubric | Used by |
|---|---|
| `hypothesis_proposed.md` | Turn 1 |
| `risk_area_updated.md` | Turn 2 |
| `market_signal.md` | Turn 3 |
| `insight_promotion.md` | Turn 4 |
| `low_signal.md` | Turn 5 |
| `contradiction_surfaced.md` | Turn 6 |
| `decision_trigger.md` | Turn 7 |
| `risk_area_routing.md` | Turn 8 |
| `insight_promoted_with_dissent.md` | Turn 9 |
| `decision_quality.md` | Turn 10 |
| `audit_trail.md` | Final state |

---

## Gaps before "all tests pass before publishing"

The current state is one scenario with a fully wired harness. To call the suite publishable:

### Must-have before v1.0

- [ ] **Scenario 01 passes at documented thresholds across `--runs 5`** with the default Sonnet model split. Currently we have a single dry-run that confirmed the harness works end-to-end; need to confirm the assertions match what the skill actually does.
- [ ] **Fix known `expected.yaml` brittleness** — stakeholder/hypothesis filenames are too prescriptive (the skill should be allowed to pick `jamie-chen.md` instead of `acme-ops.md`, `calm-mode.md` instead of `weekly-digest.md`).
- [ ] **Resolve hypothesis-ID drift** — schema (`H-V1`), docs (`H2`), `expected.yaml` (`H2`) are inconsistent. The resolver currently absorbs the drift; long-term, the source of truth should be slug-based.

### Coverage gaps — scenarios to add before the suite is comprehensive

Listed in [`docs/testing.md § Lifecycle moves to cover`](../docs/testing.md) and the repo `CLAUDE.md`:

- [ ] **Scenario 02 — drift detection.** Old hypothesis loses support over time, weekly `/review` flags it for demotion or archival.
- [ ] **Scenario 03 — new persona emergence.** A recurring user pattern crosses the promotion threshold mid-scenario.
- [ ] **Scenario 04 — stakeholder cadence flags.** High-influence stakeholder hasn't been touched in N weeks; `/review` surfaces it.
- [ ] **Scenario 05 — maintenance sweep.** `/review` correctly compresses, archives, and preserves minority signals.
- [ ] **Scenario 06 — migration mode.** Bulk-ingest of pre-existing PM artifacts (the `mode: migration` path in `prompts/`).
- [ ] **Scenario 07 — anonymized real data.** Synthetic data is too clean; one real-shaped scenario validates the brain against noise.

### Nice-to-have

- [ ] Snapshot regression fixtures: pin a known-good final state from a passing run, diff future runs against it for structural-only fast regression checks (no judge calls needed).
- [ ] Per-rubric judge cost telemetry — surface which rubrics are eating budget so they can be tightened or moved to structural.
- [ ] CI integration once the cost shape is predictable (currently too noisy + expensive for blocking CI; viable as a nightly).

---

## Adding a scenario

1. Pick a lifecycle move not covered by existing scenarios (see the gaps list above).
2. Create `tests/scenarios/<NN-slug>/`.
3. Write `README.md` declaring what the scenario covers + which lifecycle moves it exercises. Mirror the format of [`scenarios/01-b2b-churn/README.md`](./scenarios/01-b2b-churn/README.md).
4. Generate cached synthetic inputs under `inputs/` as `turn-NN-<kind>.md`. **Commit them.** Don't regenerate on the fly.
5. Write `expected.yaml` with per-turn structural + content assertions and a `final_state` block. Lean structural; only add a judge when a structural check genuinely can't answer the question.
6. Run the harness against the scenario with `--skip-content` first to validate structural shape. Then run with judges and iterate `expected.yaml` until the scenario passes at the threshold you set.
7. Document the chosen threshold in the scenario's `README.md` with a one-line justification.

---

## Roadmap

- **v0.1 (current):** 1 scenario, full harness, structural + content layers wired, model split implemented. Iterating on assertion calibration.
- **v0.2:** Scenario 01 passes at `--runs 5`. Brittleness fixes landed.
- **v0.3:** Scenarios 02–04 (drift, persona, cadence) added.
- **v0.4:** Scenario 05 (maintenance sweep) + 06 (migration mode).
- **v1.0:** Scenario 07 (anonymized real data). Documented pass rates per scenario. Snapshot regression fixtures.
