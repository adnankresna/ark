# PM Brain — System Evolution

> This document governs the evolution of the PM Brain itself.
>
> It is intentionally separate from product knowledge. The PM Brain manages two different things:
>
> 1. Product/company knowledge
> 2. The architecture and behavior of the knowledge system itself
>
> Do not mix them.
>
> `knowledge/` contains durable PM knowledge.
>
> `docs/system-evolution.md` contains operational guidance for keeping the PM Brain useful over time.

---

# Core principle

The PM Brain should become:
- more compressed,
- more operational,
- more decision-relevant,
- easier to retrieve from,
- and more epistemically trustworthy

over time.

If the system instead becomes:
- larger,
- slower,
- noisier,
- more ceremonial,
- or harder to navigate,

then the architecture is degrading.

The primary enemy is not missing information.

The primary enemy is entropy.

---

# Architectural philosophy

The PM Brain is not:
- a documentation vault,
- a knowledge dump,
- a Notion replacement,
- a wiki,
- or an archive of everything.

It is:
- a retrieval system,
- a synthesis system,
- a decision-support system,
- and an operational memory layer.

The system exists to improve:
- judgment,
- continuity,
- strategic consistency,
- and learning velocity.

Not to maximize stored information.

---

# Expected failure modes

These are not theoretical.

They are the most likely ways the system degrades over time.

## 1. Knowledge bloat

Symptoms:
- Too many files
- Overly long files
- Repeated concepts across areas
- Narrative-heavy summaries
- Large context loads for simple tasks

Failure pattern:
The system slowly becomes impossible to load efficiently, causing retrieval quality to collapse.

Corrective action:
- Compress aggressively
- Merge duplicates
- Prefer references over repetition
- Archive aggressively after extracting durable lessons
- Prefer operational summaries over exhaustive prose

---

## 2. Over-promotion from ingestion → knowledge

Symptoms:
- One-off interview comments becoming durable insights
- Weak stakeholder opinions becoming strategy tensions
- Temporary market noise becoming persistent knowledge

Failure pattern:
The system starts treating fresh signals as durable truth.

Corrective action:
- Re-apply the promotion threshold
- Require recurrence before promotion
- Preserve uncertainty explicitly
- Move weak signals back into ingestion

---

## 3. Hypothesis theater

Symptoms:
- Hypotheses written but never referenced
- Empty risk categories filled performatively
- Excessive hypothesis generation
- No decisions linked to promoted hypotheses

Failure pattern:
The system simulates rigor instead of improving decisions.

Corrective action:
- Reduce hypothesis count
- Keep only decision-relevant hypotheses active
- Archive stale hypotheses aggressively
- Audit whether hypotheses changed real decisions

---

## 4. Tension graveyards

Symptoms:
- Strategy tensions accumulate endlessly
- The same contradiction appears repeatedly
- Tensions are surfaced but never resolved
- The PM stops reading the section

Failure pattern:
The contradiction layer becomes intellectual landfill.

Corrective action:
- Merge recurring tensions
- Resolve obsolete tensions deliberately
- Escalate only recurring, high-confidence tensions
- Preserve ambiguity selectively, not universally

---

## 5. Retrieval breadth explosion

Symptoms:
- The agent loads too many files per task
- Recursive directory scans become common
- Context windows fill with historical material
- Simple tasks trigger broad retrieval

Failure pattern:
The agent loses prioritization discipline.

Corrective action:
- Reinforce targeted retrieval
- Prefer INDEX routing before file loading
- Load the minimum viable context
- Compress historical synthesis further

---

## 6. Canonical ownership drift

Symptoms:
- Metrics diverge across files
- Stakeholder concerns appear in multiple places
- Roadmap state differs by area
- Contradictory summaries emerge

Failure pattern:
The system forks its own truth layer.

Corrective action:
- Reassert canonical ownership
- Replace duplicated state with references
- Surface drift explicitly instead of silently overwriting

---

## 7. Maintenance becoming ceremonial

Symptoms:
- Maintenance reports become long but low-signal
- No decisions emerge from reviews
- Same stale items appear repeatedly
- PM stops reading outputs

Failure pattern:
The maintenance loop optimizes for activity instead of cognition.

Corrective action:
- Compress outputs aggressively
- Focus on decision-relevant tensions
- Reduce maintenance verbosity
- Eliminate low-value checks

---

## 8. Over-compression

Symptoms:
- Minority signals disappear
- Important contradictions vanish
- Nuance collapses into generic synthesis
- Everything starts sounding strategically aligned

Failure pattern:
The system becomes coherent but wrong.

Corrective action:
- Preserve meaningful dissent
- Preserve contradictory evidence when strategically relevant
- Retain provenance for high-leverage claims
- Prefer unresolved ambiguity over false consensus

---

# Signals the system is degrading

The PM Brain is likely degrading if:

- The agent regularly loads large portions of the repo
- Retrieval feels slower or less precise
- Maintenance reports are ignored
- TODO counts continuously grow
- Feature files stop being updated
- Decisions stop being logged
- Strategy tensions accumulate without resolution
- Files become narrative-heavy instead of operational
- Stakeholder files stop reflecting real relationships
- The PM no longer trusts the knowledge layer
- The same questions are repeatedly asked despite prior ingestion
- The PM starts bypassing the system entirely

These are architectural warning signs.

Treat them seriously.

---

# Refinement cadence

The PM Brain should evolve continuously.

The architecture is not fixed.

## Every 2 weeks

Review:
- Retrieval efficiency
- File usefulness
- Duplicate abstractions
- Context load size
- Hypothesis usefulness
- Maintenance signal quality
- Whether the system still improves decisions

Suggested actions:
- Remove low-signal structure
- Merge duplicate concepts
- Compress repetitive synthesis
- Simplify routing
- Delete unused workflows
- Tighten retrieval rules

Key question:

> Is the system improving thinking, or merely documenting thinking?

---

## Monthly

Review:
- Canonical ownership integrity
- Strategy tension quality
- Stakeholder freshness
- Decision hygiene
- Knowledge promotion quality

Suggested actions:
- Resolve stale tensions
- Archive dead features
- Re-evaluate recurring assumptions
- Audit whether durable knowledge still reflects reality

---

## Quarterly

Review the architecture itself.

Questions:
- Are current abstractions still useful?
- Are some folders unnecessary?
- Is the retrieval model still efficient?
- Are hypotheses creating value or ceremony?
- Should certain schemas be simplified or removed?
- Is maintenance overhead justified?
- Is the system still lightweight enough to survive long-term?

The system should become simpler over time where possible.

Not more elaborate.

---

# Evolution rules

## Prefer subtraction over addition

Adding structure is easy.

Removing structure while preserving cognition is harder.

Prefer:
- deleting dead abstractions,
- merging concepts,
- simplifying schemas,
- compressing workflows,

over adding more process.

---

## Preserve operational usefulness

Every file, workflow, and schema should justify its retrieval cost.

If something is rarely used and not strategically important, simplify or remove it.

The system exists to support decisions under constraints.

Not to model reality perfectly.

---

## Preserve epistemic humility

The system is not reality.

It is a compressed operational representation of reality.

Durable knowledge can be:
- incomplete,
- stale,
- politically distorted,
- strategically outdated,
- or overfit to recent evidence.

The PM Brain should continuously question its own assumptions.

---

## Optimize for survivability

The best PM Brain is not the most sophisticated one.

It is the one that:
- still works after 6 months,
- is still trusted,
- is still maintained,
- and still improves decisions under real operational pressure.

Long-term survivability matters more than theoretical elegance.

---

# Final principle

A PM Brain that cannot prune itself eventually collapses under its own accumulated structure.

Compression, synthesis, deletion, and selective forgetting are not maintenance details.

They are core cognitive functions.
