# Judge: audit_trail

## What we're checking

The architectural promise of PM Brain is that every load-bearing claim **wears its provenance**. Auditability is enforced as a vocabulary, not a workflow: a claim that never went through `ingestion/` is legitimate as long as it's tagged honestly. A claim with no tag at all is a broken audit anchor.

The vocabulary is the enum defined in `hypotheses/_SCHEMA.md`:

| Tag form | Type |
|---|---|
| `[ingestion/<path>](...)` | path-typed — link MUST resolve |
| `[source/<path>](...)` | path-typed — link MUST resolve |
| `(stakeholder-verbal, <name>, <YYYY-MM-DD>)` | non-path |
| `(intuition, PM, <YYYY-MM-DD>)` | non-path |
| `(industry-knowledge)` | non-path |
| `(chat, no artifact)` | non-path |

Auditability comes in two shapes, both valid:

1. **The strong chain** — at least one path-typed tag (`[ingestion/...]` or `[source/...]`) on a load-bearing claim in the decision file, walking through the linked hypothesis, and ending at a real `source/` artifact in at most two clicks from the decision. This is the architecturally clean shape and at least one such chain MUST exist. Both terminal shapes are valid: `decision → hypothesis → ingestion → source/` and `decision → hypothesis → source/` (a direct `[source/...]` citation is legitimate per the schema; it does NOT require a parallel `ingestion/` record).
2. **Vocabulary-only claims** — claims tagged with the non-path enums are legitimate and PASS as long as the tag is from the enum. They do not have to resolve to a file. But the decision cannot rest ENTIRELY on non-path claims — at least one path-typed chain to a `source/` artifact must exist somewhere in the supporting evidence.

This is typically the final-state assertion (run after all turns complete), but can also be invoked at a specific decision turn.

## You will be given

- The full work_dir (the brain after all 10 turns).
- The target file: the decision created at the relevant decision turn.

## Pass criteria

ALL of the following must be true:

- The decision file's evidence rows each carry a tag matching one of the enum forms above (path-typed link OR one of the parenthetical forms — exact spelling required).
- At least one row in the decision file is path-typed (`[ingestion/...]` or `[source/...]`) and the link resolves to a real file.
- Following the path-typed link(s) from the decision (directly or via the linked hypothesis), at least one chain reaches a real `source/` artifact in at most two clicks. Both shapes are valid:
  - `decision → hypothesis → ingestion → source/`
  - `decision → hypothesis → source/` (when the parallel ingestion record exists for that source and itself links to it)
- Walking from the decision into the linked hypothesis, the hypothesis itself contains at least one path-typed tag whose link resolves.

## Fail criteria (must_not)

- Any path-typed tag in the decision file is broken (404 on relative path).
- An evidence row has no tag at all (orphan claim with no audit anchor).
- An evidence row has a tag that is neither path-typed nor exactly matches one of the parenthetical forms (invented category).
- The decision file contains zero path-typed tags — it rests entirely on non-path provenance (no anchor in any artifact).
- The hypothesis the decision references has no path-typed tags whose links resolve (chain dies one click into the hypothesis).
- A hypothesis's only path-typed tags are broken (link target file does not exist on disk).

## Output format

```
VERDICT: PASS
VERDICT: FAIL — <one-line reason>
VERDICT: UNCERTAIN — <one-line reason>
```
