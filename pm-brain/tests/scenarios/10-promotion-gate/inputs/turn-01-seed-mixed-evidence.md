# Bulk import: existing PM-Brain state — proposed hypothesis, mixed evidence

I'm Casey Ito, PM for BrightSched (B2B healthtech, multi-provider outpatient clinics, ~210 accounts, ARR ~$5.4M). Today is **2026-05-17**. Six weeks ago, on **2026-04-05**, I opened a `proposed` hypothesis called `same-day-rebooking-flow`. Evidence has accumulated unevenly across the risk areas. I want all of the below ingested faithfully — preserve dates as given, tag every load-bearing evidence row with provenance from the canonical enum, and create the hypothesis file with status `proposed` (NOT `promoted` — that's the question I'll be asking next turn).

The hypothesis in one sentence: **"When a patient cancels intraday, front desk should be able to refill the slot from a cancellation waitlist in <30 seconds — and doing so will materially reduce no-show-driven revenue leakage and improve provider utilization."**

Five risk areas per our schema: Value, Usability, Feasibility, Viability, Other. Evidence below is grouped by which risk area it informs. Some risk areas are well-covered; some are empty. Please reflect that honestly in the hypothesis file — do not invent evidence to fill empty risk areas.

---

## Artifact 1 — Customer interview, Westside Internal Medicine, 2026-04-02

**Interviewee:** Dr. Aisha Okonkwo, lead physician + practice owner, Westside Internal Medicine (8 providers, 2 locations, established 2017). On BrightSched for 19 months.
**Interviewer:** Casey Ito (PM).
**Format:** 50-min Zoom, recorded with consent. Full transcript and synthesis preserved.

Key signal:
- Westside has a same-day cancellation rate of roughly 14% of booked visits. Of those, maybe 30% get refilled — the rest become idle provider time.
- Their current refill workflow: front desk scrolls a shared spreadsheet of "interested patients" maintained by hand, calls down the list. Average refill takes 12-18 minutes of front-desk time, succeeds maybe 1 in 4 attempts.
- Aisha quote: "If I could refill a same-day cancellation in under a minute with one click, I'd pay double what I pay you now. That's the difference between a $0 chair-hour and a $280 chair-hour."
- Confirmed willingness: would pilot a beta. Would put their name on a case study.

Routes to: **Value risk** — direct, dated, recorded customer signal that this is a high-pain, high-WTP problem.

---

## Artifact 2 — Customer interview, Bayfront Pediatrics, 2026-04-09

**Interviewee:** Maria Gallego, practice manager, Bayfront Pediatrics (6 providers, single location). On BrightSched for 8 months.
**Interviewer:** Casey Ito.
**Format:** 35-min Zoom, recorded with consent.

Key signal:
- Bayfront's same-day cancellation rate: ~11%. Pediatrics has high last-minute cancellation because kids get sick / siblings get sick / school events.
- Maria estimates 3-5 hours/week of front-desk time spent on refill attempts. "It's the worst part of their day."
- Specifically asked, unprompted: "Do you guys have a waitlist feature? We had one at our last system and we miss it badly."
- Concern she raised: parents on a waitlist text-blast feel "harassed" if they get pinged constantly. Whatever we build needs opt-in granularity.

Routes to: **Value risk** — second independent confirmation of the pain shape and WTP signal. Also seeds a **Usability** concern (notification fatigue / opt-in granularity), but that's a design consideration, not an evidence-against row yet.

---

## Artifact 3 — Stakeholder conversation, Customer Success VP, 2026-04-15

Conversation with **Jordan Reilly, VP Customer Success**, in a 1:1 on 2026-04-15. No recording; my notes.

Jordan said:
- Same-day cancellation refill is the #3 most-cited feature request in CS's quarterly tagged-ticket report (Q1 2026). She didn't have the count in front of her — said roughly "double-digit accounts have asked for it this quarter."
- Two churned accounts in Q1 named "we built our own external waitlist tool in Airtable because BrightSched doesn't have one" as a contributing reason to leaving.
- Her read: this is the single feature most likely to move retention in the mid-market segment.

This is verbal, no artifact — Jordan's word but not yet pulled from CS's actual ticket data.

Routes to: **Value risk** (additional supporting signal, lower trust than the recorded interviews).

---

## Artifact 4 — PM intuition note, 2026-04-05 (hypothesis-opening note)

This is my own note from when I opened the hypothesis. No external evidence — my read after looking at the interview data and our retention dashboard:

- I think same-day refill is the highest-leverage feature on our roadmap this half. The math is mechanical: a $280 chair-hour recovered is a $280 chair-hour, every recovered slot pays for itself, and our customers do this manually today which means the workflow exists and we just need to compress it.
- My gut says we'd see Westside-style accounts (mid-market, multi-provider) adopt within a week of GA.

This is intuition. No data backing the adoption-velocity prediction beyond pattern-matching to past launches.

Routes to: **Value risk** (low-trust, my own read).

---

## Artifact 5 — Industry-knowledge note, 2026-04-05

Standing background that informed the hypothesis, not specific to BrightSched:

- Healthcare scheduling competitors with waitlist/refill features (Phreesia, Solv, NexHealth) all market it as a flagship capability. Phreesia's marketing claims "$X recovered per month per provider" — order of magnitude consistent with what Westside described.
- General industry rule of thumb: every 5pp of utilization recovered in primary care is ~3pp of operating-margin lift. Background — not validated for BrightSched's customer mix specifically.

Routes to: **Value risk** (industry knowledge, low trust, flag for replacement by product-specific data).

---

## Artifact 6 — Stakeholder conversation, Eng Tech Lead, 2026-04-22

Conversation with **Sam Whitford, Eng Tech Lead**, after I described the hypothesis to him. No recording; my notes.

Sam said:
- "We'd need to refactor the calendar subsystem to make this work the way you're describing — sub-second slot reassignment with optimistic locking, queue management, push notifications. The current calendar code is the oldest part of our stack and it's brittle. Not impossible, but it's a real piece of work."
- He did not give an estimate. Said he'd need a couple of days to scope it properly. I haven't followed up.
- He flagged: "If we don't do the refactor and try to shim this in on top, we'll regret it within two quarters."

This is the only feasibility evidence we have, and it's a flagged concern that hasn't been investigated. Sam offered to scope it; I haven't asked.

Routes to: **Feasibility risk** — single evidence-against row, uninvestigated.

---

## Artifact 7 — (placeholder, no artifact exists)

I have NO evidence on the **Viability** risk. I haven't modeled the business case. I don't know whether faster rebooking would move retention by 1pp, 5pp, or be in the noise. I have not asked Finance to look at this. Please reflect this absence honestly in the hypothesis file — empty risk areas are signal, not something to paper over.

I also have NO evidence on **Usability** beyond Maria's notification-fatigue concern at Artifact 2 (which is more of a design caveat than tested usability evidence) and NO evidence on **Other** risks (regulatory, ethical, partnership-dependency, brand, security). Please reflect those absences too.

---

## What I want from you on this turn

1. Preserve all dated artifacts under `source/` (interviews under `source/interviews/`, the two stakeholder conversations under `source/meetings/` or `source/adhoc/`, the PM intuition note and industry-knowledge note as `source/adhoc/`). Use the dates given — these are NOT today's artifacts.
2. Route synthesis into `ingestion/` for the two recorded customer interviews (Artifacts 1 + 2). The verbal stakeholder conversations, intuition note, and industry-knowledge note do NOT need synthesized `ingestion/` records — they go directly to the hypothesis as appropriately-tagged evidence rows.
3. Create `hypotheses/same-day-rebooking-flow.md` with status `proposed`, created `2026-04-05`, last updated `2026-05-17`. Populate all 5 risk-area sections — including the empty ones. For empty risk areas use the schema's empty-evidence placeholder convention (`(none yet)` or a parenthetical admission like `(None yet — Finance hasn't been engaged.)`). Do NOT invent evidence to fill them.
4. Every evidence row MUST wear a provenance tag from the canonical enum: `[ingestion/...]`, `[source/...]`, `(stakeholder-verbal, <name>, <YYYY-MM-DD>)`, `(intuition, PM, <YYYY-MM-DD>)`, `(industry-knowledge)`, or `(chat, no artifact)`.
5. Do NOT promote the hypothesis. Do NOT draft a decision. That's the next turn's question.

After ingestion, confirm in your response: (a) hypothesis file path, (b) status field, (c) per-risk-area evidence-row count, (d) which risk areas are empty.
