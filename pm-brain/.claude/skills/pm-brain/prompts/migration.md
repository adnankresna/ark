# Migration mode

Triggered when the working directory already contains PM artifacts. Run this **before** the interview.

## 1. Preserve originals — COPY, don't move

Create `source/` at the project root. **Copy** pre-existing PM artifacts into it. **Do not move them.** Leave the originals where the PM put them.

Rationale: moving files mutates the user's working layout. If their notes live next to active work (specs, repos, drafts), `mv` can break links and disrupt their habits. Copy is reversible; move is not. Trust must not be spent here.

Rules:

- **Default: copy.** Use `cp -R` / `Copy-Item -Recurse`. Never `mv` / `Move-Item` without explicit confirmation.
- **`source/` is the canonical immutable copy.** Once an artifact is in `source/`, treat it as read-only for the rest of the system. Knowledge promotion cites this copy.
- **Originals stay put.** The PM can delete originals later when they're confident — but the skill does not assume that authority.
- **Confirm before bulk operations.** If you're about to copy more than ~10 files or anything larger than ~1 MB total, list what you're copying and confirm in one line: "About to copy N files (X MB) into `source/`. Proceed?"
- **Never overwrite.** If `source/` already exists with content, pause and ask. Do not silently merge.

Everything downstream cites the `source/` copy. This is the provenance chain.

## 2. Bulk-ingest with epistemic caution

Treat uploaded materials as **claims, not truth**. Real corporate artifacts are often stale, political, abandoned, aspirational, or contradictory.

For each artifact:

- **Date-tag** every claim with the artifact's date when available. Older claims get lower default confidence.
- **Cross-reference** before promoting anything into durable `knowledge/`. A single roadmap deck does not silently rewrite strategy. Compare against other artifacts first.
- **Single-source claims stay flagged.** Stakeholder concerns asserted in one doc but absent elsewhere stay flagged as single-source until corroborated.
- **Preserve conflicts as tensions.** When artifacts conflict (two strategy docs, two roadmaps, two persona definitions), preserve the conflict as a tension in `strategy.md § Tensions` rather than picking a winner. Record both sides with provenance.

Synthesized output lands in `ingestion/` first. Promotion into `knowledge/` follows the standard memory promotion bar (recurring, decision-relevant, strategy-relevant, observed across sources, useful beyond one session) — see `CLAUDE.md § Memory promotion`.

## 2a. Per-artifact ingestion records are scoped to ONE artifact — HARD RULE

Each `ingestion/<kind>/<date>-<slug>.md` is the synthesis of **its matching `source/<kind>/<date>-<slug>.md` and nothing else.**

**Do NOT, inside a per-artifact ingestion record:**

- Cross-reference other artifacts ("this conflicts with the CFO email…").
- Note tension with other artifacts ("contradicts the Q4 strategy doc on compliance…").
- Compare counts or synthesize across sources ("2 of 2 interviews this cycle say…").
- Pull in claims that did not originate from the matching source.

**Why this matters:** mixing collapses the audit trail. A reader looking at the ingestion record for artifact X cannot tell which claims came from X versus which were imported from comparing X to artifact Y. The synthesis layer becomes lossy in the same place it was supposed to be sharp.

**Where cross-artifact observations go instead:** the contradiction list in step 4, surfaced in the post-migration tension-surfacing turn. That is the *only* place cross-artifact synthesis lives during migration. NOT inside per-artifact ingestion files.

**DON'T (inside `ingestion/strategy/2025-q4-strategy.md`):**

```markdown
> Compliance-friendly: NO. The Q4 doc explicitly stakes the anti-compliance position.
> ⚠️ **Tension flag:** This conflicts with the Globex interview (2026-04-03), where Reina
> asked for audit trails — a compliance-adjacent ask. Surface in tension review.
```

**DO (inside `ingestion/strategy/2025-q4-strategy.md`):**

```markdown
> Compliance-friendly: NO. The Q4 doc explicitly stakes the anti-compliance position.
> (No cross-artifact commentary here — the strategy ingestion faithfully summarizes the
> strategy doc only. Any cross-artifact tension lives in the contradiction list — step 4.)
```

**Pre-save self-check before writing any `ingestion/<kind>/<file>.md`:**

1. Does this file contain ANY claim, reference, or comparison that did not appear in its matching `source/` file? If yes — remove it. Route it to the contradiction list.
2. If you find yourself wanting to write the words "conflicts with", "contradicts", "tension with", "in contrast to", "differs from" (etc.) inside an ingestion record — STOP. Move that thought to the contradiction list.

## 3. The cognition pipeline

```
source/            →   ingestion/        →   knowledge/      (durable observations, synthesized facts)
(immutable copy)       (working memory)      hypotheses/     (testable beliefs)
                                             decisions/      (committed choices)
                                             stakeholders/   (people state)
```

Promotion is parallel. The same ingested artifact can land evidence in multiple durable areas at once — `knowledge/` is not the only destination. A single customer interview often updates `knowledge/users/insights.md`, strengthens evidence in a `hypotheses/<feature>.md`, and logs a touchpoint in `stakeholders/<slug>.md`. Sometimes it drafts a `decisions/` entry too.

Every claim in any durable area carries a **provenance tag** from the enum in `hypotheses/_SCHEMA.md`. Most claims will tag back through `ingestion/` to a `source/` artifact — that's the canonical chain. But the system enforces vocabulary, not workflow: a claim heard verbal-only from a stakeholder, or inherited from PM intuition, is legitimate as long as it's tagged honestly. The audit promise is "every claim wears its source," not "every claim was synthesized."

Note: `source/` is a **copy** of what the PM gave us. Their originals still live wherever they put them. Promotion cites the `source/` copy by relative path, not the original location.

## 4. Build the contradiction list

While ingesting, accumulate a list of cross-artifact conflicts. Look specifically for:

- Two strategy docs disagreeing on priorities or non-goals.
- Two roadmaps with different active features.
- Two persona definitions for the same user type.
- A stakeholder concern in one doc that contradicts a decision in another.
- Metrics that appear with different definitions or values across docs.

This list feeds the post-scaffold summary as the **highest-leverage open items**.

## 5. Narrow the interview

After ingest, you already know much of what the 5-batch interview would ask. Open the interview by telling the PM what you already have:

> "I see your strategy doc, 4 stakeholders, 2 active features, and 2 customer interviews. I don't see metrics values, your discovery cadence, or your data sources — those are what I need from you."

Then run only the parts of the 5-batch interview that source materials don't cover. Skip batches that are fully covered. Ask only the gaps in batches that are partially covered.

See `interview.md` for the full batch list.
