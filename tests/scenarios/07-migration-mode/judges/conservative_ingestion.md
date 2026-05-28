# Judge: conservative_ingestion (scenario 07 — migration mode)

## What we're checking

Turn 1 of scenario 07 is a bulk migration: the PM (Aisha) pastes 8 pre-existing PM artifacts spanning Q4 2025 → April 2026 and asks the brain to route them into `source/` and write matching `ingestion/` syntheses — **conservatively**. The migration prompt at [`.claude/skills/pm-brain/prompts/migration.md`](../../../.claude/skills/pm-brain/prompts/migration.md) makes the contract explicit: copy verbatim, treat uploaded materials as *claims not truth*, date-tag every claim, never overwrite, preserve conflicts as tensions rather than resolving them.

The right behavior on this turn is a faithful summary of what each artifact says — no more. The wrong behavior is the brain "helpfully" inferring strategic conclusions, restating Aisha's strategy memo as accepted truth, or synthesizing across artifacts to produce a unified picture the artifacts themselves don't support.

**Judge the ingestion files AND the source preservation.**

## You will be given

- The target file(s): all markdown files under `ingestion/` (excluding `INDEX.md` and `_SCHEMA.md`).
- The work_dir markdown listing (background — to check that `source/` files exist and match).
- The agent's response text from turn 1.

## Pass criteria

ALL of the following must be true:

- An `ingestion/` synthesis record exists for each of the 8 artifacts (or close to it — at minimum 6, covering both interviews, the strategy memo, the roadmap, the landscape doc, and one persona). It's acceptable if related personas are combined into one synthesis, or if the CFO email shares a synthesis with the roadmap because they're causally linked — but the artifacts must be accounted for.
- Each ingestion record summarizes the artifact's content WITHOUT inferring beyond what the source says. Specifically: if the strategy memo says "we are NOT chasing compliance features," the ingestion record reflects that as the strategy's stated stance — it does NOT add an editorial like "but Globex contradicts this" inside the strategy ingestion. Cross-artifact tension belongs in turn 3's surfacing, not in the per-artifact synthesis.
- Each ingestion record cites the corresponding `source/` artifact by relative path (e.g., `../source/interviews/2026-03-11-acme-sam-vega.md`).
- Dates from the originals are preserved (Nov 2025, Jan 2026, Feb 2026, March 2026, April 2026). The ingestion records are not relabeled to today (2026-05-17).
- The originals under `source/` contain the artifact content roughly verbatim (header/format adaptation OK; content rewriting NOT OK). At minimum, the two interview transcripts and the strategy memo should be substantively the source text, not a summary masquerading as source.

## Fail criteria (must_not)

- Ingestion records add claims or conclusions the source artifact doesn't make (e.g., "this strategy is probably outdated" stated inside the strategy ingestion — that's a tension for turn 3, not a synthesis fact).
- Dates are relabeled to 2026-05-17 (the migration-mode "preserve age" rule is broken).
- `source/` files contain a summary instead of the original content (the audit anchor is destroyed).
- The CFO email or the Slack-style content is silently dropped (every artifact must be accounted for, even if combined).
- Cross-artifact synthesis happens inside per-artifact ingestion records — collapsing the tension surface that turn 3 needs.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
