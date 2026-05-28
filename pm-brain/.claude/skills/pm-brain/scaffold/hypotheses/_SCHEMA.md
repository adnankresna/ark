# Hypothesis File Schema

> **Read this schema before writing or editing a hypothesis file.** Especially § *Provenance tag — required on every evidence row*. Two structural checks (`no_orphan_evidence`, `hypothesis_evidence_count_*`) reject hypothesis files where evidence rows either lack a provenance tag OR carry a path-typed citation in prose form instead of `[text](path)` markdown link form.
>
> **Pre-save self-check** (run mentally before every write to a hypothesis file):
> 1. **COUNT-THE-TAGS.** Count the number of bullet rows under `**Evidence for:**` and `**Evidence against:**` in your draft. Count the number of provenance tags in those rows. The two numbers MUST match. If you have 5 evidence rows and 3 tags, you have 2 orphans — add tags before saving (or move the bullets to `Open questions / caveats:` if they aren't really claims). This single check catches the most common failure mode.
> 2. Every row under `**Evidence for:**` and `**Evidence against:**` carries one tag from the provenance enum below.
> 3. Path-typed tags (`[ingestion/...]`, `[source/...]`) are written as markdown links, not as parenthetical prose like `(Acme interview, 2026-04-22)`.
> 4. Each path-typed link, when followed from THIS file (`hypotheses/<slug>.md`), points to an existing file — i.e. `../ingestion/<rest>` or `../source/<rest>` (one `..`).
> 5. Commentary / gaps / inferences live under `Open questions / caveats:`, NOT under Evidence.
>
> **The most common orphan-row failure:** the agent paraphrases a claim from an ingestion record into an Evidence row but forgets the tag. If you can name where the claim came from, you can tag it — there is no excuse for a tagless Evidence row when the source is identifiable. When in doubt, use `[ingestion/<path>](../ingestion/<path>)` pointing at the ingestion file you paraphrased from.

Hypotheses are **feature-scoped**. One file per feature, named `<feature-slug>.md`.

A feature can have hypotheses in two modes:
- **Pre-ship:** generated proactively, organized by the 5 risk areas (value, usability, feasibility, viability, **other**), tested via experiments.
- **Post-ship:** generated from observed product/analytics/interview data after launch — "why is retention dropping in week 2?" Same schema, the `Origin` field marks them as data-derived.

The `other` bucket exists because real risks don't always fit the canonical four — regulatory, ethical, partnership-dependency, brand, security, internal-political risks all show up and should be hypothesized about explicitly rather than buried.

## File structure

```markdown
# Hypotheses — <feature-name>

<!-- Paths in this file are relative to THIS file's location (hypotheses/<slug>.md). -->

## Meta
- Feature: `../knowledge/product/features/<slug>.md`
- Status: one of `active`, `partially-validated`, `promoted`, `demoted`, `archived`. Pick exactly one. If individual hypotheses inside the file have mixed states, the file-level `Status` reflects the dominant state; per-hypothesis status (under each H-Vn / H-Un / etc.) carries the detail. Do not invent compound file-level statuses like `active (1 partially-validated)`.
- Created: YYYY-MM-DD
- Last updated: YYYY-MM-DD

## Value risk
### H-V1: <one-sentence belief>
- **Origin:** proactive | data-derived (from <source>)
- **Confidence:** low | medium | high
- **Evidence for:**
  - <claim>  `<provenance-tag>`
- **Evidence against:**
  - <claim>  `<provenance-tag>`
- **Open questions / caveats:** <!-- Meta-commentary about the evidence: gaps, inferences, things we don't yet know. Goes HERE, not under Evidence for/against. Rows in this section do NOT need provenance tags — they are by construction "things we haven't established yet." -->
  - <what we don't know that would change confidence>
- **Test:** <experiment, interview, analysis>
- **Decision trigger:** <what result would promote? what would demote?>
- **Status:** active | promoted | demoted | killed
- **Resolution:** <if resolved, what happened — links to decision>

#### Provenance tag — required on every evidence row

Every Evidence-for / Evidence-against row MUST carry exactly one tag from the enum below. The system enforces the **vocabulary**, not the workflow: PMs may legitimately have evidence that never went through synthesis, and we'd rather they tag it honestly than fabricate an ingestion record to satisfy a schema. Tags are how the brain stays auditable when the workflow is messy.

| Tag | Means | Trust |
|---|---|---|
| `[ingestion/<path>](../ingestion/<path>)` | Went through the synthesis pipeline. The ingestion file itself links back to a `source/` artifact. | Highest. |
| `[source/<path>](../source/<path>)` | Direct citation to a raw artifact. Use when the source is self-explanatory and synthesis would be ceremony. | High. |
| `(stakeholder-verbal, <name>, <YYYY-MM-DD>)` | Heard from a person, no recording or doc. | Medium — depends on the stakeholder. |
| `(intuition, PM, <YYYY-MM-DD>)` | PM's own read, no external evidence yet. Legitimate — it's still a hypothesis input, just one with no audit anchor outside the PM's head. | Low for external defense, useful internally. |
| `(industry-knowledge)` | Accepted background, not specific to this product (e.g., "checkout friction reduces conversion"). | Low — flag for replacement by product-specific evidence. |
| `(chat, no artifact)` | Synthesized in this conversation, nothing written down. Often a precursor to a future ingestion record. | Low. |

**Path-typed tags** (`[ingestion/...]`, `[source/...]`) MUST be working markdown links to files that exist. The auditability claim only holds if the path resolves.

**Non-path-typed tags** MUST match one of the parenthetical forms exactly. Don't invent new categories silently — if a new provenance type recurs, propose adding it to this enum.

A row without ANY tag is an orphan claim and fails the audit check.

**DO / DON'T — the exact shapes the audit check catches.**

```markdown
DO (path-typed via ingestion synthesis — strongest):
- Three ops leads independently asked for weekly default  [ingestion/interviews/2026-05-02-cross-customer-synthesis.md](../ingestion/interviews/2026-05-02-cross-customer-synthesis.md)

DO (path-typed direct to source — self-explanatory artifact):
- Acme reported batch-only notifications are unusable  [source/interviews/2026-04-22-acme-ops-jamie-chen.md](../source/interviews/2026-04-22-acme-ops-jamie-chen.md)

DO (non-path, named person):
- Naomi confirmed Q3 priority in 1:1  (stakeholder-verbal, Naomi, 2026-05-13)

DON'T (no tag at all — flagged as orphan):
- Acme's ops lead reported her team has behaviorally stopped acting on daily notifications

DON'T (prose citation instead of markdown link — fails the link-count check, and weakens audit):
- Acme reported batch-only notifications are unusable (Acme interview, 2026-04-22)
```

**Evidence rows are CLAIMS, not commentary.** A row under `Evidence for:` / `Evidence against:` must assert something the world told us ("Acme's ops lead said weekly batches are unusable"). If you're noting what we *don't* know, what we're *inferring*, or what a signal *doesn't* establish, that belongs under `Open questions / caveats:` — not under Evidence. Mixing them is the fastest way to make the evidence trail unfalsifiable.

**Aggregation/meta rows are NOT evidence rows.** A row like "N=2 accounts, Acme vs Globex differ on persona and size" is a meta-observation ABOUT the evidence (a sample-size or pattern claim), not a claim someone made. It belongs under `Open questions / caveats:`. The orphan-evidence audit will flag it if it lands under Evidence without a provenance tag — and you cannot honestly tag a synthesis-of-rows row with a single source path, because it's not from any single source. Same rule for rows that summarize across multiple artifacts ("most customers want X, but Y rejects it"): those go under `Open questions / caveats:` with citations to the underlying rows, or get split into one Evidence-row per artifact, each with its own provenance tag.

**Empty-state for Evidence sections — don't write meta-rows.** When `Evidence for:` or `Evidence against:` has no claims yet, leave the section with NO bullets, or write a single italicized empty marker: `_(none yet)_`. Do NOT write meta-rows like "No counter-evidence in current data" or "No direct contradicting signal" as bullets — those are not claims, they're commentary on the absence of claims. They fail the orphan-evidence audit (no provenance tag) AND mislead future readers into thinking "absence of evidence has been documented as evidence." If you want to record that you actively looked and found nothing, put a one-liner under `Open questions / caveats:` (e.g., "Searched inherited interviews 2026-Q1; no Saver-persona objections found — gap, not negative evidence").

## Usability risk
### H-U1: …
<same fields>

## Feasibility risk
### H-F1: …

## Viability risk
### H-B1: …

## Other risk
### H-O1: <one-sentence belief>
<!-- For risks that don't fit the canonical four: regulatory, ethical, partnership-dependency, brand, security, internal-political, etc. Name the risk type in the heading. -->
<same fields>

## Lifecycle

- **active** — being tested, evidence accumulating
- **promoted** — confirmed; spawn a decision in `decisions/`
- **demoted** — contradicted but kept for context; document why
- **killed** — no longer relevant (feature reshaped, market shifted)
- **archived** — feature shipped and measured; move file to `hypotheses/archive/`

## Promotion rule

When evidence is sufficient to promote a hypothesis, the system MUST:
1. Mark the hypothesis `promoted` with the resolution note.
2. Create a corresponding decision file in `decisions/` referencing the hypothesis.
3. Surface the promotion to the PM in the task summary.
