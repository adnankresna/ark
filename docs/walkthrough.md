# A week with Ark: Adnan's first five days

Ark is easier to *see* than to describe. This is a short story about one senior product manager (Adnan) using it for a week. You'll see what he sees, what the brain catches, and what he decides.

> **First, the words we'll use.** A *brain* here is just a folder of markdown files in a git repo on your laptop. To *ingest* something means to feed it into that folder so the brain knows about it. *Provenance* is shorthand for "where this claim came from." Every important note in the brain wears a small tag saying whether it came from an interview, a Slack message, a verbal hallway exchange, or your own hunch. There is a one-page [glossary](./glossary.md) at the end if anything else gets jargon-y.

---

## Monday: sprint planning surfaces a buried conflict

**Adnan Kresna** is senior PM at a company where he sits across three functions: Product, Design, and Engineering. Monday is dense. He has a 60-minute **sprint planning** session with the engineers in the morning and a 30-minute **product priorities** meeting with Sam, Miguel, and Rafi in the afternoon. Two planning sessions, same day, different altitudes.

The team runs on Notion, Jira, Slack, and Salestrekker (for the broking pipeline). There's a daily async standup in Slack where engineers post what they shipped yesterday, what they're doing today, and what's blocking them. It works — but context is scattered across four tools and nobody cross-reads everything.

Adnan opens Claude and runs:

```
/ark
```

The skill detects there's no brain yet but real PM artifacts exist across Notion and Jira. It enters **migration mode** and walks Adnan through a short interview: company, role, current priorities, top stakeholders, what's in flight. Five batches of questions, about 10 minutes.

Then it reads through what's in Notion and Jira. Forty-five minutes later, Adnan has:

- A folder of markdown files: hypotheses being tracked, decisions on record, stakeholder profiles, knowledge files for strategy and product
- An `INDEX.md` he can use to navigate everything
- A short report from the brain saying *what it found, what it couldn't make sense of, and the questions he should answer this week*

That last part is where it gets interesting.

### The roadmap-vs-sprint disconnect

Buried in the brain's onboarding report is one line:

> **Tension surfaced.** The product roadmap in Notion (`Q2 Roadmap v2`, last updated 2026-04-08) lists *broker onboarding flow redesign* as the top Q2 initiative. But of the 34 Jira tickets completed in the last 6 sprints, 26 are infrastructure and internal tooling. Only 3 touch the onboarding funnel. The sprint work and the stated roadmap don't match.

Adnan would have eventually noticed this himself. Probably in the Wednesday progress check with Sam and Miguel, after he'd already committed sprint goals based on the roadmap. The brain noticed it on day one because it cross-checked the Notion roadmap against the Jira ticket history — two data sources humans read separately.

He has options. He can raise it in the afternoon product meeting: *are we building what we said we'd build, or has the real priority shifted?* He can check with Sam whether there was an unwritten decision to pivot toward infrastructure. The brain doesn't rewrite the roadmap. It makes the right conversation happen before the wrong work gets committed.

He writes a note in the brain's `knowledge/strategy.md`: raising with Sam in Monday afternoon product meeting.

> **Benefit, in plain words.** A PM stepping into a dense operating cadence usually takes two or three weeks before they have enough cross-functional context to spot misalignment. Adnan had a real question for the product meeting on day one. The brain caught what people smooth over when they're busy shipping.

---

## Tuesday: design review reveals a user signal Adnan almost missed

Tuesday is design cadence day. Sam, Alex, and Rafi run a 30-minute session — *what's needed next, clarify questions & constraints*. Adnan's CC'd, not leading. He listens.

During the session, Alex mentions something offhand: two brokers in user testing last week abandoned the quoting flow at the same step — the one where they need to upload compliance documents. Alex has the test recordings but nobody asked for a synthesis.

After the meeting, Adnan drops the user-testing notes into the brain:

```
/ingest broker-user-testing-may-20.md
```

The brain reads the notes and does four things:

1. **Saves the original notes** under `source/research/2026-05-20-broker-user-testing.md`, untouched. Audit anchor.
2. **Writes a synthesis note** under `ingestion/research/...` pulling out the observations, tagged with Alex's name and the date.
3. **Tells Adnan what context he should know before drawing conclusions:**
   - Mark from the Broking team flagged "document upload friction" as a top-3 deal blocker in last month's pipeline review. The brain quotes him.
   - There's already a `candidate` hypothesis about document-upload drop-off. It was opened three months ago but never collected enough evidence to move forward.
   - A Slack thread from Rafi two weeks ago mentioned that the upload component uses an outdated library that doesn't support drag-and-drop on mobile. Never escalated.
4. **Adds the user-testing observation as new evidence** on the existing document-upload hypothesis. Promotes it from `candidate` to `proposed` — three independent signals now (broking pipeline, user testing, engineering flag).

Adnan reads the reply and sees not just what Alex mentioned in passing, but that same signal in the context of Mark's pipeline data and Rafi's technical flag. One design review, but the observation lands with the weight of three sources. He didn't have to remember the Slack thread or the pipeline review. The brain connected them.

He messages Sam: *"Document upload might be a bigger blocker than we scoped for. Three independent signals. Worth 10 minutes in Wednesday's progress check?"*

> **Benefit, in plain words.** Each new signal lands in the context of what the team already knew. You stop re-discovering things. You stop missing the connection between today's design review and last month's broking pipeline call.

---

## Wednesday: progress check, then a loud request from marketing

Wednesday morning is the product progress check with Sam, Miguel, and Rafi — 30 minutes of *unblock, adjust scope & tradeoffs*. Adnan walks in with the document-upload evidence pre-loaded. The conversation is productive. Sam agrees to re-scope the sprint to include a quick investigation.

That afternoon, Adnan's Slack lights up with a message from **Miguel** (who sits on both Product and Marketing):

> "Naufal just showed me the performance marketing numbers. Our landing page bounce rate spiked 15% this month. He thinks we need to rebuild the landing page this sprint. Can we pull it in?"

It's urgent-sounding, it's metric-backed, it's plausible. A less-prepared PM might start shuffling sprint priorities.

Adnan types a quick line into Claude:

```
Miguel relayed from Naufal: landing page bounce rate up 15%, wants a
landing page rebuild this sprint. Capture as stakeholder claim, flag
any conflict with what's documented.
```

The brain captures the claim with the right tag: `(stakeholder-verbal, miguel-via-naufal, 2026-05-21)`. Then it scans what's already in the brain and surfaces the documented context:

> **Relevant documented context.**
> - Sprint commitment (Monday, 2026-05-19): current sprint is committed to broker onboarding investigation + document-upload triage. No slack for a landing page rebuild.
> - Marketing cadence (weekly): Naufal owns performance marketing metrics. His Friday async hasn't landed yet — no supporting data beyond the verbal number.
> - Previous landing page bounce analysis (Notion, 2026-04-12): last month's spike was traced to a broken UTM parameter, not a design issue. Fixed in 2 days, not a rebuild.
> - Team value, "Be resourceful": *Do more with less. Find the elegant, creative solution — not just the expensive one.*

The brain doesn't argue with Miguel. It puts the documented evidence next to the verbal claim, both tagged for what they are. *One relayed verbal metric from marketing* vs. *a committed sprint, a previous false alarm, and no supporting data yet*.

Adnan replies to Miguel:

> "Got it. Let's wait for Naufal's Friday async with the full numbers. Last time bounce spiked it was a UTM issue — worth ruling that out before we scope a rebuild. If it's real, we'll prioritize it for next sprint."

He's not dismissing. He's not over-reacting. He has the documented case ready, and he's created a clear decision gate (Friday async data) instead of a knee-jerk sprint change.

> **Benefit, in plain words.** The brain keeps documented evidence and the loudest recent voice in their proper proportion. When someone makes a priority claim mid-sprint, you respond with what the team has actually learned, not vibes.

---

## Thursday: design handoff catches a scope gap

Thursday is the second design cadence: *review + ready for dev handoff*. Sam, Alex, and Rafi review what's ready to hand to engineering. Adnan's CC'd again, listening.

During the review, Rafi flags that the broker onboarding flow redesign (the Q2 roadmap item from Monday's tension) has three Figma screens approved but no spec for the error states. Alex says he deprioritized error states because "nobody asked for them."

This is the kind of gap that normally surfaces in QA, two weeks later, as a bug. Adnan captures it:

```
Rafi flagged: broker onboarding redesign has 3 approved screens but no
error-state specs. Alex deprioritized them. Capture as a scope gap on
the onboarding hypothesis, flag for next sprint planning.
```

The brain records the observation (`(meeting-note, rafi, 2026-05-22)`) and attaches it to the broker-onboarding hypothesis under a *scope gaps* section. It also surfaces a connection:

> **Related.** The document-upload hypothesis (promoted to `proposed` Tuesday) shares the same flow. If error states aren't specced for the parent flow, the upload step will inherit the same gap. Two hypotheses, one spec debt.

Adnan forwards the brain's note to Sam with a one-liner: *"Two birds, one spec. Worth getting Alex to cover error states for both before Monday."*

> **Benefit, in plain words.** Cross-functional input from design reviews, engineering standups, and broking pipeline calls all land where they're findable later — not buried in meeting notes nobody re-reads.

---

## Friday: `/review`, then the weekly async

It's Friday. Adnan runs:

```
/review
```

The weekly maintenance sweep. The brain reads the whole folder and produces one page covering what changed this week, what's drifting, and what to take into next week. For Adnan, it reads:

> **This week**
> - **Roadmap-vs-sprint disconnect** (Monday): raised with Sam in product meeting. Decision: infrastructure work was an unwritten pivot. Sam agreed to update the Notion roadmap to reflect reality. Status: waiting on Sam to update.
> - **Document-upload hypothesis** moved from `candidate` to `proposed` after cross-referencing user testing (Alex), broking pipeline (Mark), and engineering flag (Rafi). Three independent signals. Next step: scoped investigation in current sprint.
> - **Landing page bounce** (Miguel/Naufal, Wednesday): captured as verbal claim. Waiting for Naufal's Friday async with supporting data. Previous spike was a UTM issue, not a design problem.
> - **Error-state scope gap** (Rafi, Thursday): two hypotheses share the same spec debt. Alex tasked with covering both before Monday.
>
> **Drifting**
> - The `broker-retention-flow` hypothesis hasn't had new evidence in 38 days. It's still listed as a Q3 candidate but nobody from Broking has sourced new data since Mark's last pipeline review. Worth asking Christine in the next fortnightly.
> - Denise's Friday partner async hasn't mentioned the API integration request from two months ago. Either it resolved or it dropped. Worth one question.
>
> **For Monday**
> 1. Open sprint planning with the document-upload investigation scope. Engineering needs a clear ask.
> 2. Check if Sam updated the roadmap. If not, the disconnect persists into next week's planning.
> 3. Review Naufal's Friday data on bounce rate. If it's real, scope a lightweight fix for next sprint — check whether it's another UTM issue before committing to a rebuild.

Adnan reads this in five minutes. His Monday is pre-loaded.

He walks into the next week with the conversations he needs to have, the evidence to support each one, and no surprise gaps. The brain didn't make any of these decisions for him. It made the week's signal *legible*.

> **Benefit, in plain words.** The Friday sweep is the forcing function. It's the moment the brain pays you back for the small captures you made all week. Skip it for a month and the system rots; do it weekly and the next week starts with momentum.

---

## What Adnan got, in five lines

- **Monday:** a roadmap-vs-reality question raised before the wrong sprint got committed
- **Tuesday:** a passing design comment that connected to two other signals he didn't remember
- **Wednesday:** documented evidence ready when an urgent-sounding request arrived mid-sprint
- **Thursday:** a spec gap caught before it became a QA bug two weeks later
- **Friday:** a one-page summary that made Monday's sprint planning easy

None of this is automation. None of it is the brain making decisions Adnan should be making. It's the brain doing the small, boring, easy-to-forget work of cross-referencing what you already know — across Product, Design, Engineering, Broking, and Marketing cadences that each generate signal in different tools. The judgment work stays with Adnan. The connective tissue is what the brain handles.

## Want to try it?

- [Install](../README.md#install) takes about three minutes
- [How it works](./how-it-works.md): the technical version, with files and folder structure
- [Architecture](./architecture.md): the design choices and why they're what they are
- [Glossary](./glossary.md): every term used in Ark, in one place
