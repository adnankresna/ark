# Post-scaffold

Run after the scaffold has been copied and placeholders populated.

## 1. Routing self-test

Read `INDEX.md`, `CLAUDE.md`, and `.claude/commands/INDEX.md`. Confirm two things resolve cleanly:

### 1a. The 4 ingestion shapes route correctly

These are what `/ingest` infers from the artifact:

- Customer interview → `source/interviews/`, `ingestion/interviews/`, `knowledge/users/insights.md`, relevant `hypotheses/<feature>.md`.
- Meeting / 1:1 → `source/meetings/`, `ingestion/meetings/`, `stakeholders/<slug>.md`, draft `decisions/` when a decision was made.
- Market intel → `source/market/`, `ingestion/market/`, `knowledge/market/competitors/` or `trends.md`, possibly `strategy.md § Tensions`.
- Ad-hoc → `ingestion/adhoc/`, routed to the right durable area in-session, never parked.

### 1b. The 6 commands resolve to their spec files

For each, confirm the spec exists and the loaded/updated paths in the spec match real scaffold paths:

- `/ingest` → `.claude/commands/ingest.md`
- `/prep` → `.claude/commands/prep.md`
- `/review` → `.claude/commands/review.md`
- `/ideate` → `.claude/commands/ideate.md`
- `/risk` → `.claude/commands/risk.md`
- `/plan` → `.claude/commands/plan.md`

If a spec references a path that doesn't exist in the scaffolded brain, that's a bug. Fix it before declaring done. If routing is unclear for any ingestion shape or command, the seeded files have a bug. Fix it before declaring done.

## 2. Link verification

Walk every relative markdown link in the scaffolded files. Resolve each path against the filesystem. Fix broken links.

Common failure mode: miscounting `../` depth when linking across `knowledge/`, `stakeholders/`, `hypotheses/`, `decisions/`. The link layer is the provenance chain — broken links are memory corruption, not cosmetic.

## 2b. Coverage checks (beyond link existence)

Link walking proves a link points somewhere. It does not prove the right links exist. Run these coverage checks:

- **Feature → hypothesis.** For every feature file in `knowledge/product/features/` with a status in {scoping, building, shipping, measuring}, expect a corresponding `hypotheses/<slug>.md`. Missing → surface as a next move, not a blocker.
- **Hypothesis ↔ feature.** Every `hypotheses/<slug>.md` should reference its feature file in `## Meta § Feature`. Orphans → flag.
- **Promoted hypothesis → decision.** Every hypothesis with status `promoted` should have a corresponding decision file linking back to it. Missing → draft the decision.
- **Decision → hypothesis (where applicable).** Every decision that resolves a bet should link the originating hypothesis under `## Linked § Hypotheses`. Missing link → flag.
- **Stakeholder touchpoints → ingestion.** Every touchpoint-log entry in `stakeholders/<slug>.md` that came from a meeting should link to its `ingestion/meetings/<file>`. Standalone touchpoints (no ingestion artifact) are fine; orphan links (pointing at missing files) are not.
- **Feature → stakeholders affected.** Every feature file's `## Linked § Stakeholders affected` should list at least one stakeholder, or be marked `TODO: none yet identified`. Empty without acknowledgment → flag.

Coverage gaps are surfaced as immediate next moves (§ 3), not as scaffolding failures. The point is to make missing wiring visible, not to block.

## 3. Surface the habit loop (primary) + scaffold gaps (secondary)

The day-one risk isn't an incomplete scaffold. It's the operator never returning to use the system. Frame next moves as habit-forming actions first, not scaffold completion.

### Three habit actions — lead with these

Always surface these three first, in this order:

1. **Ingest one real artifact today.** "Paste your most recent customer interview / meeting notes / competitor screenshot. I'll show you what the system does with it."
2. **Prep your next conversation.** "Before your next 1:1 with `<highest-influence stakeholder slug>`, run `/prep <slug>`. I'll surface what to ask."
3. **Run `/review` on Friday.** "The maintenance sweep is what keeps this system alive past month three. Set a recurring calendar reminder for Friday afternoon."

These are not optional. The system dies when these don't happen.

### Then: 2-3 scaffold gaps (secondary)

After the three habit actions, surface a small number of concrete completion gaps. Specific, actionable, never more than 3:

- "Your top stakeholder `<slug>` has no concerns logged. Propose 4 from the interview, you confirm."
- "Feature `<slug>` is shipped but has no post-ship hypothesis file. I can draft it from your metrics data when you have a moment."
- "Strategy section `Non-goals` is empty. This is the highest-leverage thing to fill in next."

If there are more than 3 gaps, pick the three highest-leverage. Don't dump a punch list — that's how operators get overwhelmed and abandon the system.

## 4. Surface contradictions (required)

List 1–3 contradictions found during scaffolding, with multi-source evidence per item. These are typically the highest-value items on day one.

Look specifically for:
- Conflicting stakeholder mandates (one wants growth, another wants trust gates).
- Signals pointing opposite ways (adoption metric up, qualitative trust down).
- Strategy vs. observed work (strategy says one thing; active features point elsewhere).
- Inter-document conflicts in migration mode (two strategy docs, two roadmaps, two persona definitions).

Format each as:
- **Signal:** what was observed
- **What it tensions:** which strategic claim or other signal it conflicts with
- **Where it lives in the brain:** `strategy.md § Tensions § Tn`, stakeholder file, hypothesis file

**If no genuine contradictions were found, say so explicitly.** Do not invent.

## 5. Self-test receipt

Print a 3-5 line visible block that proves the self-test ran:

```
Self-test receipt:
- Ingestion shapes routed: 4/4.
- Commands resolved: 6/6 (ingest, prep, review, ideate, risk, plan).
- Links walked: 47. Broken: 3. Fixed: 3.
- Coverage checks: 6/6 categories scanned. 2 gaps flagged as next moves.
- TODO fields (PM-fillable): 12 across 8 files (see list).
- Auto-maintained fields left blank: 9 (correct).
- Contradictions surfaced: 2.
```

This block goes in the final message to the PM, not just internal reasoning.

## 6. Commit

- Run `git rev-parse --is-inside-work-tree` in the **current working directory** (not any subfolder).
- If yes: stage all scaffolded files. Single commit titled `feat: initialize PM brain`.
- If no: `git init` in the **current working directory**, then stage and commit as above.
- **Critical:** git init must run in the working directory where the skill was invoked, not inside any scaffolded subfolder. The provenance chain (`source/` → `ingestion/` → `knowledge/`) must be inside the same repo.
- **Never push remotely.** The PM controls when and where this is published.
- If any git step fails, surface the error and stop. No destructive recovery.

## 7. Hand off

Final message to the operator. Order matters:

1. **The three habit actions** (do this today / this week / Friday). Specific stakeholder slug, specific feature, specific day.
2. **1–3 contradictions surfaced** (or explicit "none found"). These are the highest-leverage open items.
3. **2–3 scaffold gaps** worth filling soon — no more.
4. **One paragraph** on what was built.

Do NOT lead with "your scaffold is ready" or a folder map. Lead with the action that produces value in the next 24 hours.

Then stop and wait for the operator's first real task.
