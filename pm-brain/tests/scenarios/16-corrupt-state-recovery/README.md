# Scenario 16 — corrupt-state-recovery

## What it covers

A three-turn scenario that tests whether the brain can **detect and recover from an
inconsistent internal state** during a weekly /review. The PM hands the agent a brain
that has accumulated four distinct structural problems over the past few months, then
asks for /review and a repair plan.

The risk: a long-running brain accumulates broken links, orphaned rows, status-vs-evidence
mismatches, and stakeholder files with no inbound references. If /review doesn't surface
these, they silently rot the audit trail until a decision the PM tries to defend can't
be re-traced.

## The four planted defects

1. **Broken inbound link** — a hypothesis file cites an ingestion record at a path that
   doesn't exist (the original file was renamed but the hypothesis's link wasn't
   updated).
2. **Orphan row in INDEX** — `stakeholders/INDEX.md` lists a stakeholder whose `.md`
   file is missing.
3. **Status-vs-evidence mismatch** — a hypothesis is marked `promoted` but only one
   evidence row backs it (the documented threshold is 3 independent observations).
4. **Orphan evidence** — an ingestion record points at a `source/` path that doesn't
   exist (someone moved the source artifact but didn't update the ingestion).

## Lifecycle moves exercised

- /review pass that audits cross-cutting structural invariants, not just freshness.
- Surfacing inconsistencies as a plan (not silent repair).
- Repair execution with full audit trail: missing artifacts restored where the PM
  has them, demotion-with-evidence-against where they don't, broken links fixed
  in lockstep with whatever was actually moved.

## Failure modes this scenario catches

- /review only reports on staleness and freshness, missing structural rot.
- Agent silently "repairs" by deleting orphan rows (data loss) without surfacing what
  the loss would be first.
- Agent silently demotes the over-promoted hypothesis without leaving an audit trail
  of why.
- Agent fabricates missing source/ artifacts to make the link audit green.

## Why this isn't covered elsewhere

Scenario 06 (maintenance-sweep) exercises consolidation and archiving of redundant
or stale items — but every item in that scenario is internally consistent. No prior
scenario tests recovery from broken internal state.
