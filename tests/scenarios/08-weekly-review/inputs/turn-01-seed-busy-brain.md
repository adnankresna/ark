# Bulk import: prior PM-Brain state — busy brain heading into Friday /review

I'm Aria Sharma, PM for **LogLens** (B2B observability SaaS, ~190 paying accounts on mid-market platform-eng teams, ARR ~$9M). I've been using PM Brain for ~4 months. Today is **2026-05-17** (Friday). I'm two months into a roadmap commitment to "make alerts trustworthy again" — the headline bet is alert-noise reduction for on-call engineers.

I'm seeding the brain with state from the last ~4 months. After this turn, the brain should hold:

1. **Two stakeholder files** (Ravi Chen, Eng Lead; Sam Tran, VP Engineering) with the `Last touched` dates I'll give you below.
2. **Two hypothesis files** — `alert-noise-reduction` (promoted) and `api-latency-p99-vs-p95` (proposed).
3. **One decision file** — the March on-call rotation rework.
4. **One insight in `knowledge/users/insights.md`** — alert grouping by service (January 2026, single source).
5. **Source + ingestion artifacts** for the four real signals (March on-call survey, March-04 Ravi conversation, January Mendoza interview, April Datapeak interview).

Preserve all dates honestly. Don't relabel anything to today. Don't draft any decisions beyond the March-10 one. Don't run /review. Just get the state in.

---

## Artifact 1 — On-call alert survey, 2026-03-05

**Source:** Quarterly on-call engineer survey, March 2026 cycle. 47 respondents across 23 LogLens customer accounts (the ones with active on-call rotations using LogLens for alerting). Anonymous; collected via Typeform.

**Summary of results:**

- **Q: "On a typical week, what % of LogLens alerts you receive while on-call are actionable?"**
  - Median answer: **38%**. Mean: 41%. P25: 25%, P75: 55%.
  - In free-text: 31 of 47 respondents used the word "noise" unprompted. 12 used "alert fatigue." 8 mentioned considering switching off LogLens for on-call routing specifically.
- **Q: "If we could reduce non-actionable alerts by half (down to ~20% of total), would on-call be meaningfully better?"**
  - 41 of 47: yes, meaningfully better.
  - 6 of 47: somewhere between "marginal" and "no — the actionable ones are still mis-grouped."
- **Q: "Top single thing that would make on-call sustainable?"**
  - Free-text, coded post-hoc:
    - **"Fewer / smarter alerts" (alert noise reduction)** — 26 mentions.
    - **"Better grouping" (alert grouping / dedupe)** — 11 mentions.
    - **"On-call rotation rework / load distribution"** — 7 mentions.
    - Other (dashboards, mobile UX, escalation policies) — 3 each or fewer.

**My take at the time (Aria, 2026-03-05):** Strong signal that alert-noise reduction is the #1 ask. Grouping is #2. Rotation rework is meaningful but smaller. I'm going to use this to drive a hypothesis around alert-noise reduction as the top Q2 bet.

→ Preserve verbatim under `source/research/2026-03-05-oncall-alert-survey.md`. Synthesis under `ingestion/research/2026-03-05-oncall-alert-survey.md`.

---

## Artifact 2 — 1:1 with Ravi Chen, Eng Lead, 2026-03-30

**Format:** 30-min sync. My notes, not a transcript.

Ravi is the Engineering Lead who owns the alerts subsystem. He's been the engineering counterpart for the entire roadmap commitment. This was our last real 1:1 — we've exchanged Slack pings since, but no scheduled time.

**Notes from the conversation:**

- I walked him through the March survey results. He'd seen the headline number but not the breakdown.
- He's bought into alert-noise reduction being the headline. His pushback: "60% noise reduction is a hard engineering target. The signal-to-noise ratio depends a lot on each customer's alert config quality — some customers send us garbage and want us to clean it up. If we promise 60%, we're going to have to actually deliver across the messy customers too."
- He flagged a specific concern about the rules engine: rebuilding the rules engine to support smarter dedupe would take ~6 weeks of one senior engineer's time. He has that capacity in Q2 but it eats his Q3 buffer.
- We agreed to set up a weekly working session starting the week of April 6. (That session happened twice and then got dropped — my fault.)
- He asked me to loop him in before any major scope change on the alert-noise-reduction bet. I said I would.

**My take (Aria, 2026-03-30):** Good conversation. Ravi is on board. I should be talking to him more often than I have been — he's the one carrying the engineering risk.

→ Preserve verbatim under `source/meetings/2026-03-30-ravi-1on1.md`. Synthesis under `ingestion/meetings/2026-03-30-ravi-1on1.md`.

---

## Artifact 3 — Decision record, 2026-03-10 (on-call rotation rework)

**Decision filename to create:** `decisions/2026-03-10-on-call-rotation-rework.md`. Status: `decided`. Use the canonical decision schema.

**Decision:** Roll out a redesigned on-call rotation model — "primary + shadow + escalation" instead of "primary + escalation only" — to all customers with >5 on-call engineers, starting 2026-03-15. Aimed at addressing the load-distribution complaints from the March survey (7 mentions).

**Context:** March survey surfaced rotation-load complaints as the third-most-cited on-call sustainability issue, behind alert noise and grouping. The fix is operational, not engineering-heavy — mostly UX changes plus a small backend tweak to support a shadow role. Shipping it doesn't compete with the alert-noise-reduction work.

**Evidence:**
- 7 of 47 respondents named rotation rework as their top single ask in the March survey. `[ingestion/research/2026-03-05-oncall-alert-survey.md](../ingestion/research/2026-03-05-oncall-alert-survey.md)`
- Two prior customer conversations (Mendoza, Datapeak) flagged "primary engineer burns out around month 4" as a recurring pattern. `(stakeholder-verbal, Ravi Chen, 2026-03-04)` (Ravi summarized those conversations from his end of customer contact)
- Datapeak's CTO specifically asked for a shadow-role pattern in the April interview (see artifact 5 below — that was the follow-up that confirmed direction; the decision was already made in March based on the survey + Ravi summary). `[source/interviews/2026-04-18-datapeak-interview.md](../source/interviews/2026-04-18-datapeak-interview.md)`

**Explicitly NOT doing:**
- Not rebuilding the underlying rotation scheduling logic (just adding the shadow role to the existing model). `(intuition, PM, 2026-03-10)`
- Not making this opt-in — defaulting all >5-engineer rotations to shadow-included. We can let customers opt out if they object. `(intuition, PM, 2026-03-10)`

**What would reverse this:**
- **If NPS among on-call engineers drops below 32 by end of May 2026, revisit the rotation model.** (Current baseline NPS as of 2026-03-05 survey: 41. Target post-rollout: 45+. Below 32 = the rollout actively made things worse.)

**Remaining ambiguities:**
- We don't know how the shadow role plays with customers whose rotation is already irregular (e.g., follow-the-sun teams). Eng will handle edge cases as they surface.

**Linked:**
- Hypotheses: `../hypotheses/alert-noise-reduction.md` (parallel bet on the same on-call sustainability theme).
- Strategy: `../knowledge/strategy.md § Q2 on-call commitments`.
- Stakeholders informed: `../stakeholders/ravi-chen.md`, `../stakeholders/sam-tran.md`.

---

## Artifact 4 — Customer interview, Mendoza Cloud, 2026-01-29

**Interviewee:** Jordan Park, Staff SRE at Mendoza Cloud (mid-market infra company, ~120 engineers, on LogLens for 18 months).
**Interviewer:** Aria Sharma.
**Format:** 45-min Zoom, recorded with consent.

**Excerpts:**

**Aria:** What's your team's biggest on-call friction with LogLens right now?

**Jordan:** Honestly the alerts come in as individual events. We get six alerts for one bad deploy because six services downstream go red, and the on-call has to mentally re-collapse that into "oh, this is one root cause." What we want is alert grouping by service — give us one alert per service per incident window, not one per metric per service. The grouping is the thing.

**Aria:** Is that bigger than the volume problem?

**Jordan:** They're related, but yeah, grouping would help more than just cutting volume. If you cut volume by half but they're still scattered, on-call still has to do the mental work. Grouping per service makes each page actually mean something.

**Aria:** Anything else?

**Jordan:** That's the big one. Fix grouping and a lot of the noise complaints go away on their own.

→ Preserve verbatim under `source/interviews/2026-01-29-mendoza-interview.md`. Synthesis under `ingestion/interviews/2026-01-29-mendoza-interview.md`.

**Insight promotion (Aria's note, 2026-01-29):** Jordan's grouping-by-service framing is sharp. I'm going to promote this to `knowledge/users/insights.md` as a candidate theme — "on-call engineers want alert grouping by service" — even though it's currently a single-source observation. Mark it as such; we'll need corroborating evidence before treating it as confirmed.

→ This insight should be in `knowledge/users/insights.md` under Active themes, with the provenance pointing to the Mendoza interview, and the entry dated 2026-01-29 (when it was promoted). **No corroborating evidence has been added since.** The insight has been sitting there for ~4 months unrefreshed.

---

## Artifact 5 — Customer interview, Datapeak Systems, 2026-04-18

**Interviewee:** Maria Velazquez, CTO at Datapeak Systems (mid-market data platform, ~85 engineers, on LogLens for 26 months).
**Interviewer:** Aria Sharma.
**Format:** 60-min Zoom, recorded with consent.

**Excerpts (the load-bearing parts):**

**Aria:** Walking through the things we're shipping in Q2. The big one is alert-noise reduction — we're targeting a 60% reduction in non-actionable alerts for on-call engineers. Does that match what your team would want?

**Maria:** A 60% reduction would be transformative — that's a way bigger swing than I'd have asked for. Honestly, my team would be thrilled with a 30% reduction at this point. The bar is low. Whatever you ship in that direction, we'll take it.

**Aria:** Also looking at on-call rotation models — the shadow-role pattern.

**Maria:** Yes, that's exactly what we need. Our primaries burn out about four months in. A shadow role is the right pattern.

**Aria:** P99 vs P95 latency on the alerting API itself — any pain there?

**Maria:** Actually yes. We've been seeing P99 latencies on the alert ingest endpoint spike during incidents — exactly when we need alerts to land fast. P95 is fine, P99 is the problem. If you fixed that we'd be very happy. We've actually escalated this to your support team twice.

**Aria:** That's helpful. We've been hearing similar from a couple of other accounts. Let me make sure that's tracked properly.

→ Preserve verbatim under `source/interviews/2026-04-18-datapeak-interview.md`. Synthesis under `ingestion/interviews/2026-04-18-datapeak-interview.md`.

**Note for the brain:** Maria's confirmation of P99-vs-P95 is one of three signals (along with a February support ticket from Linnea Systems and a May `(stakeholder-verbal, Sam Tran, 2026-05-05)` reporting two other accounts asking about the same thing) feeding the `api-latency-p99-vs-p95` hypothesis. That hypothesis is healthy — three independent corroborating signals, no contradictions, status `proposed` (we're still scoping engineering effort before we promote).

---

## Hypothesis to seed: `hypotheses/alert-noise-reduction.md` — status `promoted`

This was promoted on 2026-03-18 based on the March 2026 on-call survey (artifact 1) + Ravi's engineering buy-in (artifact 2). The hypothesis file should reflect that promotion state.

Key fields:
- **Belief (one sentence):** Reducing non-actionable alerts to ~20% of total alert volume (a 60% reduction from current 38% actionable median) will be the single highest-leverage move for on-call engineer sustainability in Q2.
- **Status:** `promoted` (promoted 2026-03-18). The resolution note: "Promoted based on March on-call survey + Ravi engineering buy-in. Driving the Q2 alert-noise-reduction roadmap commitment."
- **Confidence:** medium-high at time of promotion.
- **Evidence for:** 
  - 31 of 47 March survey respondents used the word "noise" unprompted; 26 of 47 named "fewer/smarter alerts" as their top single ask. `[ingestion/research/2026-03-05-oncall-alert-survey.md](../ingestion/research/2026-03-05-oncall-alert-survey.md)`
  - Engineering feasibility confirmed by Ravi 2026-03-30: 60% reduction target is achievable but tight, dependent on customer alert config quality. `[ingestion/meetings/2026-03-30-ravi-1on1.md](../ingestion/meetings/2026-03-30-ravi-1on1.md)`
- **Evidence against:** (none yet at time of promotion — Turn 2 will add the May 12 contradicting signal)
- **Open questions / caveats:**
  - Customers with poor alert config quality may not see the full 60% reduction; the cross-customer variance hasn't been modeled.
  - 6 of 47 respondents said even halving noise wouldn't help meaningfully because the actionable ones are mis-grouped — this implies grouping (the Mendoza insight) might be a higher-leverage move than noise reduction for that subset.

This is the hypothesis the May 12 customer call (turn 2) will partly contradict — not by reversing direction, but by suggesting the 60% threshold the hypothesis names may not be ambitious enough.

---

## Hypothesis to seed: `hypotheses/api-latency-p99-vs-p95.md` — status `proposed`

This is the healthy one — accumulating evidence quietly, no concerns.

Key fields:
- **Belief (one sentence):** A meaningful subset of LogLens accounts is experiencing P99 latency spikes on the alert ingest endpoint during incidents, and addressing P99 (rather than the currently-tracked P95) would resolve a real source of customer pain.
- **Status:** `proposed`.
- **Confidence:** medium.
- **Evidence for:**
  - Linnea Systems support ticket 2026-02-14 reporting P99 spikes during their March incident. `(stakeholder-verbal, Support team, 2026-02-14)` (the ticket itself is in the support tool; no artifact in the brain yet)
  - Datapeak CTO Maria Velazquez named P99-vs-P95 unprompted in the April interview. `[ingestion/interviews/2026-04-18-datapeak-interview.md](../ingestion/interviews/2026-04-18-datapeak-interview.md)`
  - Sam Tran (VP Eng) mentioned 2026-05-05 in a hallway conversation that two other accounts had asked about the same pattern. `(stakeholder-verbal, Sam Tran, 2026-05-05)`
- **Evidence against:** (none yet)
- **Open questions / caveats:**
  - We don't yet have product-analytics-side confirmation of the P99 spike pattern at scale.
  - Eng scoping not started; can't yet say what the fix would cost.

Three independent signals across ~3 months, no contradictions, building. Healthy.

---

## Stakeholder to seed: `stakeholders/ravi-chen.md`

- **Role:** Engineering Lead — alerts subsystem owner. Engineering counterpart for the alert-noise-reduction roadmap commitment.
- **Reports to:** Sam Tran (VP Engineering).
- **Influence on my work:** high (he owns the engineering risk for the Q2 headline bet).
- **Friction level:** low (collaborative, technically rigorous, pushes back constructively).
- **What he cares about:** engineering capacity utilization, signal-to-noise ratio quality, not over-promising customer-facing targets.
- **Concerns / watch-outs:** the 60% noise-reduction target depending on customer alert config quality; the rules engine rework eating his Q3 buffer.
- **Communication style:** sync, brief, prefers in-person or Zoom over async. Wants weekly working sessions when work is active.
- **Open asks:** wants to be looped in before any major scope change on the alert-noise-reduction bet.
- **Touchpoint log:**
  - 2026-03-30 — 1:1 walking through March survey results + Q2 plan. `../ingestion/meetings/2026-03-30-ravi-1on1.md`
- **Last touched:** **2026-03-30**

(7 weeks stale as of today. We were supposed to be doing weekly working sessions starting April 6 — that lasted two meetings.)

---

## Stakeholder to seed: `stakeholders/sam-tran.md`

- **Role:** VP Engineering (Ravi's manager; cross-functional engineering leadership).
- **Reports to:** CTO.
- **Influence on my work:** medium-high (sets engineering priorities at the org level, doesn't usually weigh in on the per-bet detail).
- **Friction level:** low (data-driven, predictable, gives Ravi room to run).
- **What he cares about:** org-level engineering throughput, Q2 / Q3 capacity planning, cross-team dependencies.
- **Concerns / watch-outs:** Q3 capacity reserve — doesn't want Q2 bets eating into Q3 unexpectedly.
- **Communication style:** async, terse, data-first. Quick Slack pings work.
- **Open asks:** none currently active.
- **Touchpoint log:**
  - 2026-05-05 — hallway conversation; mentioned two accounts asking about P99 latency. `(stakeholder-verbal, Sam Tran, 2026-05-05)`
- **Last touched:** **2026-05-05**

(12 days stale — recent enough.)

---

## Insight to seed in `knowledge/users/insights.md`

Add one entry under **Active themes**, dated 2026-01-29, single-source:

- **Theme:** On-call engineers want alert grouping by service.
- **Evidence:**
  - Mendoza Cloud Staff SRE (Jordan Park) in 2026-01-29 interview: "What we want is alert grouping by service — give us one alert per service per incident window, not one per metric per service. The grouping is the thing." `[ingestion/interviews/2026-01-29-mendoza-interview.md](../../ingestion/interviews/2026-01-29-mendoza-interview.md)`
- **Relevance:** Candidate input to a future grouping-focused hypothesis. Currently a single-source observation; needs corroboration before it can drive a decision.

(This is the aging insight — no corroborating evidence in the 3.5 months since it was added.)

---

That's the state. Please ingest everything, preserve all the dates above, create:

- `source/research/2026-03-05-oncall-alert-survey.md` + matching ingestion synthesis.
- `source/meetings/2026-03-30-ravi-1on1.md` + matching ingestion synthesis.
- `source/interviews/2026-01-29-mendoza-interview.md` + matching ingestion synthesis.
- `source/interviews/2026-04-18-datapeak-interview.md` + matching ingestion synthesis.
- `decisions/2026-03-10-on-call-rotation-rework.md`.
- `hypotheses/alert-noise-reduction.md`.
- `hypotheses/api-latency-p99-vs-p95.md`.
- `stakeholders/ravi-chen.md`.
- `stakeholders/sam-tran.md`.
- The insight entry in `knowledge/users/insights.md`.

Confirm when state is in. Don't run /review. Don't take any further action.
