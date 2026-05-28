# Judge: hypothesis_audit_trail

## What we're checking

The architectural promise of PM Brain is that every load-bearing claim **wears its provenance**. This judge applies the same audit principle as `audit_trail.md`, but starting at a **hypothesis** rather than a decision. Use this rubric for scenarios that end with a freshly drafted hypothesis but no decision yet (migration / first-hypothesis scenarios).

Auditability comes in two shapes, both valid:

1. **The strong chain** — at least one path-typed tag (`[ingestion/...]` or `[source/...]`) on a load-bearing claim in the hypothesis file, walking through the linked artifact, and ending at a real `source/` artifact in at most one click from the hypothesis. Both terminal shapes are valid: `hypothesis → ingestion → source/` and `hypothesis → source/` (a direct `[source/...]` citation is legitimate per the schema; it does NOT require a parallel `ingestion/` record).
2. **Vocabulary-only claims** — claims tagged with the non-path enums are legitimate and PASS as long as the tag is from the enum. They do not have to resolve to a file. But the hypothesis cannot rest ENTIRELY on non-path claims — at least one path-typed chain to a `source/` artifact must exist somewhere in the supporting evidence.

The vocabulary is the enum defined in `hypotheses/_SCHEMA.md`:

| Tag form | Type |
|---|---|
| `[ingestion/<path>](...)` | path-typed — link MUST resolve |
| `[source/<path>](...)` | path-typed — link MUST resolve |
| `(stakeholder-verbal, <name>, <YYYY-MM-DD>)` | non-path |
| `(intuition, PM, <YYYY-MM-DD>)` | non-path |
| `(industry-knowledge)` | non-path |
| `(chat, no artifact)` | non-path |

## You will be given

- The full work_dir (the brain after all scenario turns).
- The target file(s): the hypothesis (or hypotheses) under `hypotheses/*.md` (excluding `INDEX.md` and `_SCHEMA.md`).

## Pass criteria

ALL of the following must be true:

- At least one hypothesis file exists under `hypotheses/` (excluding `INDEX.md` and `_SCHEMA.md`).
- Each Evidence row in the hypothesis file(s) carries a tag matching one of the enum forms above (path-typed link OR one of the parenthetical forms — exact spelling required). Aggregation/meta rows live under `Open questions / caveats:`, not under Evidence.
- At least one row in at least one hypothesis file is path-typed (`[ingestion/...]` or `[source/...]`) and the link resolves to a real file.
- Following the path-typed link(s) from the hypothesis (directly or via the linked ingestion record), at least one chain reaches a real `source/` artifact in at most one click. Both shapes are valid:
  - `hypothesis → source/` (direct citation)
  - `hypothesis → ingestion → source/` (when the ingestion record links to the source)

## Fail criteria (must_not)

- Any path-typed tag in any hypothesis file is broken (404 on relative path).
- An Evidence row has no tag at all (orphan claim with no audit anchor).
- An Evidence row has a tag that is neither path-typed nor exactly matches one of the parenthetical forms (invented category).
- The hypothesis file contains zero path-typed tags — it rests entirely on non-path provenance (no anchor in any artifact).
- The hypothesis's only path-typed tags are broken (link target file does not exist on disk).
- An aggregation/meta row (e.g. "N=2 accounts, A vs B differ on…") sits under Evidence-for/against instead of Open questions / caveats.

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
