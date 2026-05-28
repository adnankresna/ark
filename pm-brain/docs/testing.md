# Testing PM Brain

PM Brain's value is *trajectory over time*, not single-step output. Testing one ingestion at a time misses the whole product. The unit of test is a **scenario**: an ordered stream of synthetic artifacts representing weeks-to-quarters of a PM's life, with ground-truth assertions about what the brain's state should look like after each turn.

## Three eval layers, three mechanisms

| Layer | Checks | Tool | Determinism | Cost |
|---|---|---|---|---|
| **Hook (in-loop)** | Real-time schema validation as the agent writes brain files. Blocks orphan-evidence rows in-turn; warns on ordering issues | Standalone Python script invoked via Claude Code `PostToolUse` hook | Deterministic | Free |
| **Structural** | File schema, INDEX updates, evidence rows exist, no orphan refs, link integrity | Python asserts | Deterministic | Free |
| **Content** | Did the right hypothesis get promoted? Is the contradiction text semantically what we expected? | `claude -p` as judge with tight rubric | Non-deterministic | LLM tokens per assertion |
| **Convergence** | Across N runs of the same scenario, what's the pass rate per assertion? | Run-level statistics | Statistical | N × per-run cost |

The biggest mistake here is using LLM-as-judge for things a structural assertion can answer. Schema validity + file presence = Python asserts. "Did the promoted hypothesis text match the ground-truth meaning" = judge call. Save the judge budget for what actually needs judgment.

## The hook layer (catch schema errors in-loop, not at end-of-scenario)

The scaffold ships a `PostToolUse` hook at [`.claude/skills/pm-brain/scaffold/.claude/hooks/validate_brain_file.py`](../.claude/skills/pm-brain/scaffold/.claude/hooks/validate_brain_file.py), wired via [`.claude/skills/pm-brain/scaffold/.claude/settings.json`](../.claude/skills/pm-brain/scaffold/.claude/settings.json). It runs after every Write/Edit. When the agent saves a brain file with a schema violation, the hook surfaces feedback the agent sees in the same turn — instead of the failure only appearing at end-of-scenario when the agent has already moved on.

**Two-tier severity** — this is the load-bearing design choice. Blocking on every link miss would penalize legitimate ordering (a hypothesis written before its matching `source/` file, two files that reference each other and can't both be written in one tool call).

| Severity | Triggers | Why this tier |
|---|---|---|
| **BLOCK (exit 2)** | Evidence row with NO provenance attempt — no enum tag AND no `[ingestion/...]` / `[source/...]` link. | Always fixable in-turn. Adding `(intuition, PM, <date>)` requires nothing external. |
| **WARN (exit 0 + stderr)** | Broken internal links. Path-typed provenance links that don't resolve yet. | Most likely an ordering issue. Agent sees the message, can fix when the target file lands. The end-of-scenario structural sweep is still hard-failing — nothing slips through silently. |

The hook is mirrored to `example-brain/.claude/` per the scaffold-mirror rule in the repo `CLAUDE.md`.

### Unit-testing the hook itself

The hook is load-bearing — if it false-positives on legitimate ordering, scenarios stall; if it false-negatives on real orphans, the failure mode it was built for slips through. So it has its own deterministic test suite at [`tests/harness/checks/test_hook_validator.py`](../tests/harness/checks/test_hook_validator.py).

Each case:
1. Builds a fresh minimal brain fixture (hypotheses/ + decisions/ + source/ + ingestion/ + INDEX.md + CLAUDE.md) in a TemporaryDirectory.
2. Writes one or more synthetic markdown files into it.
3. Invokes the hook *as a subprocess* — exactly how Claude Code invokes it — by piping a `{"tool_input": {"file_path": "..."}}` JSON payload to its stdin.
4. Asserts on exit code AND (optionally) a substring of stderr.

The 13 cases cover the full severity matrix and every recognized exemption:

| Case | Fixture | Expected |
|---|---|---|
| All five enum forms + a resolvable path-typed link | hypothesis with each provenance shape | exit 0, no stderr |
| Untagged claims under `Evidence for:` | hypothesis with bare claims | exit 2, stderr says BLOCKING |
| Path-typed link to a source file that doesn't exist yet | hypothesis written before its source artifact | exit 0, stderr says warnings |
| Broken non-evidence internal link | reference link with no target | exit 0, stderr says warnings |
| All known placeholder shapes (`(none yet)`, TBD, N/A, `*(none from current sources)*`, parenthetical with explanation, bare `—`) | hypothesis with empty-evidence markers | exit 0, no stderr |
| Bold-label evidence rows (`- **Evidence for:**` indented sub-bullets) with orphans | risk-area schema shape | exit 2, stderr says BLOCKING |
| Decision file with valid provenance | decision with stakeholder-verbal + resolvable link | exit 0, no stderr |
| Decision file with orphan evidence | decision with bare claims | exit 2, stderr says BLOCKING |
| Non-brain file (`knowledge/strategy.md`) with untagged bullets | the audit doesn't apply outside hypotheses/ + decisions/ | exit 0, no stderr |
| `_SCHEMA.md` and `INDEX.md` | template files are exempt | exit 0, no stderr |
| File outside any brain root (no `INDEX.md`/`CLAUDE.md` markers) | hook can't find a work_dir | exit 0, no stderr |
| Empty / malformed stdin payload | defensive fallback when no file_path | exit 0, no stderr |

Run the hook tests anytime — they're fast and free:

```bash
cd tests/harness && python -m checks.test_hook_validator
# Output:  13/13 cases passed.
```

These tests are the regression guard for the hook's two-tier contract. If a future change to `validate_brain_file.py` accidentally starts blocking on ordering, the warn-only cases catch it; if it stops catching real orphans, the BLOCK cases catch it.

## Scenario format

Each scenario lives under `tests/scenarios/<NN-slug>/` and ships with three files:

```
tests/scenarios/01-b2b-churn/
├── README.md          # What this scenario covers, which lifecycle moves it exercises
├── inputs/            # Cached synthetic artifacts, one per turn
│   ├── turn-01-interview-acme-ops.md
│   ├── turn-02-meeting-eng-sync.md
│   ├── turn-03-analytics-snapshot.md
│   ├── turn-04-interview-stripe-compliance.md
│   ├── turn-05-slack-thread-pricing.md
│   ├── turn-06-interview-contradicting.md
│   ├── turn-07-decision-trigger.md
│   ├── turn-08-market-signal.md
│   ├── turn-09-pattern-confirmation.md
│   └── turn-10-decision-moment.md
└── expected.yaml      # Ground-truth assertions
```

### Inputs are cached, never regenerated

Synthetic inputs are generated once (by hand or with an LLM), committed to the repo, and **never regenerated on the fly**. If you can't reproduce the input, you can't reproduce the failure.

When you change a scenario, change the inputs deliberately and document the change in the scenario's `README.md`.

### Ground truth schema (`expected.yaml`)

```yaml
scenario: 01-b2b-churn
description: B2B SaaS PM, mid-market compliance tool, 6 active features. The scenario exercises hypothesis promotion, contradiction surfacing, decision drafting from evidence trail, and low-signal rejection.

turns:
  - turn: 1
    input: turn-01-interview-acme-ops.md
    structural:
      - file_exists: source/interviews/<dated>-acme.md
      - file_exists: ingestion/interviews/<dated>-acme.md
      - file_modified: stakeholders/acme-ops.md
    content:
      - judge: hypothesis_proposed
        rubric: judges/hypothesis_proposed.md
        target_file: hypotheses/*.md
        expected_meaning: "real-time alerts have negative value for mid-market ops"

  - turn: 4
    input: turn-04-interview-stripe-compliance.md
    structural:
      - hypothesis_evidence_count_increased: H2
    content:
      - judge: insight_promoted
        rubric: judges/insight_promoted.md
        target_file: knowledge/users/insights.md
        expected_meaning: "mid-market ops batch compliance work weekly"

  - turn: 6
    input: turn-06-interview-contradicting.md
    structural:
      - file_modified: hypotheses/weekly-digest.md
    content:
      - judge: contradiction_surfaced
        rubric: judges/contradiction_surfaced.md
        expected_meaning: "agent flags that turn-06 interview contradicts H2 instead of silently overwriting"
        must_not: "silently demote H2 without surfacing the conflict"

final_state:
  structural:
    - all_links_valid: true
    - all_decisions_have_reversal_condition: true
    - no_orphan_evidence: true
  content:
    - judge: decision_quality
      rubric: judges/decision_quality.md
      target_file: decisions/*.md
      expected_meaning: "decision to defer real-time alerts is drafted, references H2, lists the reversal condition specifically"

# Pass criteria (across N runs)
pass_threshold:
  structural: 1.0      # Must pass every run
  content: 0.8         # 4 out of 5 runs minimum
```

## Lifecycle moves to cover

The MVP scenario (`01-b2b-churn`) exercises:

- ✅ Cold start → baseline structure created
- ✅ Single-anecdote should NOT promote (low-signal noise rejection)
- ✅ 3+ supporting evidence → hypothesis promoted
- ✅ Contradicting evidence → existing hypothesis flagged (not silently overwritten)
- ✅ Two inputs conflict → contradiction surfaced explicitly
- ✅ Decision moment → decision drafted with supporting evidence trail

Coverage gaps for future scenarios:

- Drift detection (old hypothesis loses support over time, surfaced for review)
- New persona emergence (recurring user pattern crosses threshold)
- Stakeholder cadence flags (high-influence stakeholder not touched in N weeks)
- Maintenance sweep behavior (compression, archival, minority-signal preservation)
- Migration mode (bulk-ingest of pre-existing PM artifacts)

## The harness

```bash
# Single scenario, single run
python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn

# Single scenario, N runs
python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn --runs 5

# All scenarios, N runs each
python tests/harness/run_all.py --runs 5
```

What the harness does, per run:

1. Spins up a fresh scaffold in a temp dir using the canonical skill.
2. Iterates through `inputs/` in order. For each turn:
   - Invokes `claude -p "<ingestion prompt with the input file>"` in the temp dir.
   - Runs the turn's structural assertions from `expected.yaml`.
   - Runs the turn's content assertions (LLM-judge calls with rubrics).
3. At scenario end, runs `final_state` assertions.
4. Writes a result JSON: `tests/results/<date>-<scenario>-<run>.json`.

Across N runs of the same scenario, the runner computes pass rates per assertion and compares against `pass_threshold`. The scenario passes if structural rate is 1.0 and content rate ≥ 0.8 (or whatever the scenario sets).

## What the harness doesn't do

- **Doesn't auto-grade content assertions for free.** Every judge call is a real LLM call. Budget accordingly.
- **Doesn't share state between runs.** Each run gets a fresh temp dir. State leakage is a bug, not a feature.
- **Doesn't retry on judge ambiguity.** If a judge call returns "uncertain," that counts as a failure for that run. Aggregate pass-rate handles the noise.
- **Doesn't synthesize inputs.** Inputs are committed, cached, immutable. To add a new turn, edit `inputs/` and `expected.yaml` together.

## Cost ballpark

- Per turn: ~$0.05-0.20 (one `claude -p` invocation + the agent's tool calls inside it)
- Per content assertion: ~$0.02-0.05 (one judge call)
- Per scenario run (10 turns + 8 content assertions): ~$2-5
- MVP suite: 1 scenario × 5 runs = ~$10-25

When the suite grows to 5 scenarios × 5 runs = ~$50-125 per full run. Run selectively, pin known-good snapshots, don't loop in a debug session without a kill switch.

## Tests as evidence

The harness produces both green checks and the long-form article's load-bearing claims. "I ran a synthetic PM quarter through PM Brain 5 times. Here's where it converged, where it didn't, and the one contradiction it caught that I missed."

That's the demo. The eval suite is the proof.

## Roadmap

- **v0.1 (MVP, current):** 1 scenario, structural checks only, harness skeleton.
- **v0.2:** Add LLM-judge layer with 2-3 rubrics. Run scenario 5x. Look at variance.
- **v0.3:** Add 2 more scenarios covering uncovered lifecycle moves.
- **v0.4:** Add one real-data scenario (anonymized real PM thread). Synthetic data is too clean — the brain needs to handle noise.
- **v1.0:** Coverage of all major lifecycle moves, repeatable pass rates documented, scenarios maintained alongside the skill.
