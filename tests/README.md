# tests/

Eval suite for the PM Brain skill. A *scenario* here is a short, scripted story we feed the skill (a sequence of interviews, meetings, or messages) so we can check that the resulting **brain** (the folder of markdown files the skill maintains) ends up the way it should. The check happens after every turn.

> New to PM Brain terms? The [glossary](../docs/glossary.md) covers *brain*, *ingest*, *provenance*, *hypothesis*, *decision file*, *audit trail*, and anything else that shows up in this doc and isn't obvious.

This file is the **operator-level quickstart**. For everything else (scenario format, ground-truth schema, harness internals, assumptions, full coverage / gap list, and how to add a scenario) see [`TESTING.md`](./TESTING.md). Design rationale lives in [`../docs/testing.md`](../docs/testing.md).

## Quickstart

```bash
# Single scenario, single run (cheap, fast)
python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn

# Single scenario, N runs (for convergence pass rate)
python tests/harness/run_scenario.py tests/scenarios/01-b2b-churn --runs 5

# All scenarios, N runs each
python tests/harness/run_all.py --runs 5
```

Results land in `tests/results/<date>-<scenario>-<run>.json`. The folder is gitignored by default.

## Layout

```
tests/
├── README.md                  # This file
├── scenarios/                 # Synthetic scenarios with ground truth
│   └── 01-b2b-churn/
│       ├── README.md          # What this scenario covers
│       ├── inputs/            # Cached synthetic artifacts, ordered
│       └── expected.yaml      # Ground-truth assertions
└── harness/
    ├── run_scenario.py        # Per-scenario runner
    ├── run_all.py             # Batch runner
    ├── checks/                # Structural assertion helpers
    │   └── structural.py
    └── judges/                # LLM-judge rubrics
        ├── hypothesis_promoted.md
        ├── contradiction_surfaced.md
        └── decision_quality.md
```

## What a scenario looks like

A scenario is an ordered stream of synthetic PM artifacts (we call them *turns*) plus assertions about what should be true after each turn.

Each turn under `inputs/` is a single file: an interview transcript, a meeting note, an analytics screenshot description, a Slack thread, a competitor changelog. The harness replays them in filename order, calling the skill on each one as if a real PM had just dropped it in.

`expected.yaml` declares the assertions. Two kinds:

- **Structural**: file-system checks (does this hypothesis file exist? did the decision file get updated?). Deterministic, fast, free.
- **Content**: LLM-judge calls with a tight rubric (did the brain surface the contradiction? did the synthesis tag provenance correctly?). Non-deterministic, costs money. Reserved for things a structural check can't answer.

See [`docs/testing.md § Scenario format`](../docs/testing.md#scenario-format) for the full ground-truth schema.

## Adding a scenario

1. Pick a lifecycle move not covered by existing scenarios (see the coverage gaps in `docs/testing.md`).
2. Create `tests/scenarios/<NN-slug>/`.
3. Write `README.md` declaring what the scenario covers and which lifecycle moves it exercises.
4. Generate cached synthetic inputs under `inputs/`. Name them `turn-NN-<kind>.md`. **Commit them.** Don't regenerate on the fly.
5. Write `expected.yaml` with per-turn structural + content assertions and a `final_state` block.
6. Run the harness against the scenario. Iterate on `expected.yaml` until the scenario passes at the threshold you set.

## Cost guard

The harness uses real LLM calls. Cost ballpark with the default Sonnet model split (see [`TESTING.md § Cost model`](./TESTING.md#cost-model) for the full table):

- Per turn: ~$0.10–0.40
- Per content (judge) assertion: ~$0.02–0.05 (Sonnet) / ~$0.10–0.20 (Opus, opt-in)
- Per full scenario run (10 turns + ~15 judges): ~$3–5
- `--runs 5` of one scenario: ~$15–25

Under a Claude subscription the printed cost is the **API-equivalent** price, useful as a proxy for 5-hour-window quota pressure, not real billing. Either way it's the number to optimize.

`--max-cost` (default $20) aborts the run on cumulative overrun. Use it. Don't loop the harness in a debug session without it.
