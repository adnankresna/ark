/hypothesize auto-approve-under-50

Generate hypotheses across all 5 risk areas for the auto-approve-under-$50 feature. This is pre-ship — the brain has the BrillStone interview, the roadmap entry, and Diana's stakeholder context to draw on.

Per the `/hypothesize` spec:

- Create `hypotheses/auto-approve-under-50.md`.
- Cover ALL 5 risk areas (value, usability, feasibility, viability, other). If a risk area has no signal, say "no risk identified, monitor" explicitly — silent gaps are themselves a risk.
- Every Evidence row carries a provenance tag from the canonical enum (`[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, <name>, <date>)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, `(chat, no artifact)`).
- NEW hypotheses start `active` / `low` confidence. Do NOT auto-promote any candidate.
- Each hypothesis has: belief, origin (proactive | data-derived), confidence, evidence-for, evidence-against, open questions, test plan, decision trigger.
- Update `hypotheses/INDEX.md`.

The viability risk area in particular needs Diana's fraud-risk concern wired in — that's a viability risk on this feature.

Surface back: count of hypotheses opened (grouped by risk area), the 1-2 strongest, and any risk area you flagged as gap. Do NOT draft a decision this turn.
