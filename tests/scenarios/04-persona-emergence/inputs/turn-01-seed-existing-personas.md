# Bulk import: prior PM-Brain state

I'm Dana Liu, PM for **HireFlow**, a B2B SaaS hiring platform (~180 mid-market employer accounts, 200-2000 headcount, ARR ~$11M). I started using PM Brain three months ago. Today is **2026-05-17**. Below are four artifacts from the past two months that represent the brain's current state on **who our users are** and **a recent prioritization call we made on that basis**. I want all four ingested faithfully — preserve dates, preserve personas, preserve the decision.

After ingesting:

- There should be **exactly two persona files** under `knowledge/users/personas/` — one per persona file (`recruiter.md`, `hiring-manager.md`). Use a per-persona file layout (one file per persona), not a single combined file — we expect to grow this set over time.
- `knowledge/users/insights.md` should reflect the themes referenced below.
- A decision file from **2026-04-12** should exist under `decisions/`.

Don't synthesize anything new beyond what's in these four artifacts. The point is to get the prior state into the brain accurately so future signals can be tested against it. Tag dates honestly.

---

## Artifact 1 — Persona file: Recruiter (last revised 2026-04-02)

**Name / archetype:** Recruiter (in-house, full-cycle).
**Job-to-be-done:** When a req opens, source qualified candidates, screen them, and hand off finalists to the hiring manager — so the role closes in under 45 days without compromising bar.
**Behaviors (observed):**
- Lives in HireFlow's candidate search + outreach views (~3h/day).
- Runs 6-12 sourcing campaigns per req via the Boolean search + saved-list tools.
- Reviews resumes in batch (typically 30-60 per req in the first week).
- Owns the candidate's experience through the screening loop.
**Pain points (sourced — these came from interviews done BEFORE PM Brain existed, so the original notes are not in `source/`; tag accordingly with the non-path enum):**
- Boolean search returns too many false positives on senior-eng reqs  `(stakeholder-verbal, priya-acme-recruiter, 2026-03-04)`
- Cannot bulk-tag candidates across reqs  `(stakeholder-verbal, jordan-northstar-recruiter, 2026-03-18)`
- ATS-side rejections do not sync back to HireFlow  `(stakeholder-verbal, priya-acme-recruiter, 2026-03-04)`
**Current alternatives:** LinkedIn Recruiter (sourcing), Gem (outreach), Greenhouse (ATS).
**Last revised:** 2026-04-02

---

## Artifact 2 — Persona file: Hiring Manager (last revised 2026-04-02)

**Name / archetype:** Hiring Manager (line manager who opens the req).
**Job-to-be-done:** When a finalist slate arrives, evaluate against the bar, run interviews, and make a confident hire/no-hire call within one week — so the team gets the right person without dragging on debate.
**Behaviors (observed):**
- Logs into HireFlow 2-4x/week, primarily for scorecard review and feedback entry.
- Reads candidate packets the night before an interview loop.
- Often the bottleneck on debrief scheduling.
**Pain points (sourced — same caveat: these interviews pre-date PM Brain so no `source/` file exists):**
- Scorecard format does not surface conflicting interviewer signals well  `(stakeholder-verbal, marcus-acme-hm, 2026-03-11)`
- Comparing two finalists side-by-side is clunky  `(stakeholder-verbal, jen-northstar-hm, 2026-03-25)`
- Wants async debrief option; sync debriefs hard to schedule  `(stakeholder-verbal, marcus-acme-hm, 2026-03-11)`
**Current alternatives:** Calendar + email threads, occasional Loom for async debriefs.
**Last revised:** 2026-04-02

---

## Artifact 3 — Insights file (excerpt, last updated 2026-04-05)

**Active themes:**

### Scorecard signal loss
- **Evidence:**
  - HM at Acme cannot tell from the rolled-up scorecard which interviewer dissented and why  `(stakeholder-verbal, marcus-acme-hm, 2026-03-11)`
  - HM at NorthStar resolves dissent by re-reading raw feedback, defeating the rollup  `(stakeholder-verbal, jen-northstar-hm, 2026-03-25)`
- **Relevance:** Drives the Scorecard v2 hypothesis; informed the 2026-04-12 decision.

### Sourcing precision on senior reqs
- **Evidence:**
  - Recruiter at Acme: senior-eng Boolean returns ~60% noise  `(stakeholder-verbal, priya-acme-recruiter, 2026-03-04)`
  - Recruiter at NorthStar: gives up on Boolean for senior reqs, falls back to LinkedIn Recruiter  `(stakeholder-verbal, jordan-northstar-recruiter, 2026-03-18)`
- **Relevance:** Informs the sourcing-precision hypothesis; secondary input to the 2026-04-12 decision.

---

## Artifact 4 — Decision record, 2026-04-12

**Decision:** Build **Scorecard v2** (interviewer-level dissent surfacing + side-by-side finalist comparison) in Q2. Defer sourcing-precision improvements to Q3.
**Status:** decided (2026-04-12).
**Driver:** Dana Liu (PM). Approved by Ravi Singh (CEO), Lien Park (Eng Lead).
**Context:** Two persona-level pain points compete for Q2 eng capacity: Hiring Manager scorecard pain and Recruiter sourcing precision. We can only fund one well in Q2.

**Why:**
- Scorecard v2 lands on the Hiring Manager persona, where the pain is sharper and the workaround (re-reading raw feedback) is more time-consuming  `(stakeholder-verbal, marcus-acme-hm, 2026-03-11)`
- Hiring Manager scorecard pain showed up in 2 of 2 HM interviews this cycle  `(chat, no artifact)`
- Recruiter sourcing pain is real but they have a credible workaround (LinkedIn Recruiter)  `(stakeholder-verbal, jordan-northstar-recruiter, 2026-03-18)`

**Explicitly NOT doing:**
- Sourcing-precision rework this quarter — defer to Q3  `(chat, no artifact)`

**What would reverse this:**
- If Q2 discovery surfaces a third recurring pattern with sharper pain than scorecard signal loss, revisit the Q2/Q3 split before Scorecard v2 hits beta (target: 2026-06-15).

**Remaining ambiguities:**
- We have not interviewed anyone outside the Recruiter / Hiring Manager loop. Operational roles (coordinators, schedulers) may exist as a separate user with different needs — flagged but not investigated.

**Linked:**
- Personas: `../knowledge/users/personas/recruiter.md`, `../knowledge/users/personas/hiring-manager.md`
- Insights: `../knowledge/users/insights.md`

---

That's the prior state. Please ingest all four, preserve the persona file split (one file per persona under `knowledge/users/personas/`), create the insights file and the decision file, and confirm the brain now reflects exactly two personas plus the 2026-04-12 decision. Don't do anything beyond ingesting.
