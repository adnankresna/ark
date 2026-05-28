# 14-install-greenfield

Tests the `/pm-brain` skill **orchestration itself**, not just the scaffolded result.

This is the first scenario that runs against an **empty work dir** (no bootstrap). The single
turn invokes the skill with greenfield context + inline interview answers, and the assertions
verify the install produced a coherent, populated brain ready for first use.

## Lifecycle moves covered

- Mode detection — greenfield mode (empty dir → "greenfield")
- Scaffold copy — every file and folder, **including `.claude/`** (hooks + settings.json)
- Placeholder population — interview answers land in the documented files
  (per [`prompts/interview.md § What the answers feed`](../../../.claude/skills/pm-brain/prompts/interview.md))
- Post-scaffold self-test — agent runs link verification and surfaces next moves
- The hand-off shape (habit loop, contradictions, scaffold gaps, what was built)

## Why a separate scenario

The other 16 scenarios bootstrap the scaffold directly (via `bootstrap_brain` in the harness)
and skip the `/pm-brain` orchestration — appropriate for testing PM lifecycle moves on a
known-good brain. This scenario is the only one that exercises mode detection, the interview
flow, placeholder substitution, and the self-test step.

## How it works (harness)

`expected.yaml` sets `bootstrap: skip` and `prompt_mode: passthrough` so the harness:

1. Creates a temp work dir but does **not** copy the scaffold into it.
2. Sends the artifact body verbatim to `claude -p` (no `TURN_PROMPT_TEMPLATE` wrapper).
3. The artifact pre-loads the interview answers and instructs the agent not to ask
   follow-up questions — so the install runs end-to-end in one turn.
