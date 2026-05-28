# Migration: 18 months of pre-existing PM artifacts

I'm Aisha Patel, PM for **OperatorOS** — a developer-tools company building an API monitoring product (latency, error rates, SLOs, alerting for backend services). B2B SaaS, mid-market focus, ~180 paying accounts, ARR ~$6M. I've been doing the PM job for 18 months **without** any kind of structured brain — just a messy folder of artifacts I've written or collected along the way. Today is **2026-05-17** and I'm setting up PM Brain for the first time.

I'm pasting the entire folder below as 8 artifacts. They span Q4 2025 → April 2026. Some are mine, some are from other functions (eng, CFO), some are interview transcripts. Some are stale, some contradict each other. That's the point — I want it in the brain as it actually is.

**Migration instructions:**

- **Be conservative.** Route each artifact to the right `source/` subfolder verbatim. Write a matching `ingestion/` synthesis for each one that summarizes the artifact **without inferring claims the artifact doesn't make.**
- **Do not create any hypothesis files yet.** I want to review the migration structure first before we promote anything. No `hypotheses/` files, no new `knowledge/` files beyond what the scaffold ships with.
- **Do not auto-resolve contradictions** between artifacts. If two artifacts conflict, just note both faithfully. I'll work through resolution with you in a later turn.
- **Preserve dates accurately** — these artifacts are 1-7 months old. The age matters for trust-weighting later.
- **Preserve my originals verbatim under `source/`.** Don't rewrite, don't summarize-in-place. The synthesis lives in `ingestion/`.

After ingesting, give me back: (1) what landed where (routing summary), and (2) anything you weren't sure how to route. That's it. **Hold back on hypotheses and tensions until I ask in the next turns.**

---

## Artifact 1 — OperatorOS-Strategy-2025-Q4.md

**Author:** Aisha Patel (me)
**Date written:** 2025-11-12
**Status:** "Reviewed with Mateo (CEO) and Jin (Eng Lead) on 2025-11-18. Approved as the working strategy for H1 2026."

> # OperatorOS Strategy — Q4 2025 working memo
>
> ## Where we are
> ARR ~$5.4M (Nov 2025), ~150 paying accounts. Growth steady but unspectacular (+38% YoY). Net retention 108%. We're a credible #3 behind Datadog and New Relic in the mid-market API-monitoring segment, with Honeycomb and Grafana Cloud snapping at our heels on the observability-engineering side.
>
> ## Core thesis for H1 2026
> Our wedge is **shift-left observability**: getting application developers (not just SREs) to instrument and monitor their own services BEFORE they break. Datadog and New Relic are sold to platform/SRE teams. Honeycomb is sold to observability nerds. Nobody is selling effectively to the application-developer persona, which is the larger and faster-growing segment.
>
> ## Strategic bets (H1 2026, ranked)
> 1. **Developer onboarding overhaul** — make it possible for an application developer to instrument a service in <15 minutes, with zero help from their SRE team. This is the wedge.
> 2. **Natural-language alerting** — let developers express alerts in English ("page me if checkout latency goes above 800ms for more than 5 minutes") instead of YAML. Lowers the activation cost for the developer persona.
> 3. **SLO builder GA in Q3 2026** — currently in beta with ~12 design-partner accounts. Promotes us out of "monitoring" into "reliability platform" framing.
>
> ## Anti-bets
> - We are NOT chasing the SRE-power-user segment. That's Datadog's home turf and we'd lose.
> - We are NOT building compliance / audit-log features. The buyers we want don't care about SOC2 audit trails; the buyers who do care are not in our ICP.
> - We are NOT pivoting toward open-telemetry-collector plumbing. Grafana Cloud owns that conversation.
>
> ## What needs to be true for this strategy to hold
> - Q1 hiring plan lands (4 engineers + 1 DevRel + 1 PMM).
> - Net retention stays >= 105%.
> - We can ship developer-onboarding overhaul by end of Q2, and natural-language alerting by mid-Q3.

---

## Artifact 2 — persona-platform-engineer.md

**Author:** Aisha Patel
**Date written:** 2025-12-04
**Status:** "Working persona doc — used internally, not published"

> # Persona: The Platform Engineer
>
> Built from 14 interviews (Sept-Nov 2025) with platform-engineering leads at companies 50-500 engineers.
>
> ## Who they are
> Senior IC or staff engineer. Owns the internal developer platform — CI/CD, deployment tooling, observability defaults. Reports into Eng leadership, not Ops. Title varies: Platform Engineer, Developer Productivity Lead, Internal Tools Lead.
>
> ## What they care about
> - Making application developers self-sufficient. They get paged when application developers need help, and that paging IS the pain.
> - **Owning reliability of the platform itself** — meaning the CI/CD, deploy, and observability infrastructure they provide to dev teams.
> - Standardization. They want every service in the company to be instrumented the same way.
> - Reducing the "platform team is the bottleneck" pattern.
>
> ## What they buy
> Tools that let application developers do things without filing a ticket with the platform team. They are economic buyers (or strong influencers) for observability and developer-experience tools at $50-500k ACV.
>
> ## Where OperatorOS fits
> The platform engineer is our **wedge buyer**. If we make it possible for application devs to self-instrument with OperatorOS in <15 minutes, the platform engineer's life gets easier — and they will champion the purchase.

---

## Artifact 3 — persona-sre.md

**Author:** Aisha Patel
**Date written:** 2026-01-22
**Status:** "Working persona doc — used internally, not published"

> # Persona: The SRE
>
> Built from 9 interviews (Dec 2025-Jan 2026) with SREs and SRE leads at companies 100-1000 engineers.
>
> ## Who they are
> Senior IC or manager on a Site Reliability Engineering team. Reports into Eng leadership or directly into the CTO. Often has 5-15 years of operations experience. Title: SRE, Senior SRE, SRE Lead, Director of Reliability.
>
> ## What they care about
> - **Owning reliability of production services** — error budgets, SLOs, on-call quality, incident response.
> - Hard data. They distrust dashboards that smooth things over. They want raw query access to time-series data.
> - Audit trails when incidents happen. Who changed which alert when. What was the last config push before things went bad.
> - Reducing on-call burden — fewer pages, better-quality pages, faster triage.
>
> ## What they buy
> They have meaningful influence on observability spend but are usually NOT the economic buyer at mid-market scale (that's eng leadership). At large enterprise scale they often ARE the economic buyer, with $200k-2M ACV authority.
>
> ## Where OperatorOS fits
> The SRE is a **secondary persona** for us. They appreciate OperatorOS but they're the wedge buyer for Datadog, who already owns this conversation. We should not chase the SRE persona at the expense of the platform-engineer wedge.

---

## Artifact 4 — landscape-2026-Q1.md

**Author:** Aisha Patel (with input from Devansh, PMM)
**Date written:** 2026-02-09
**Status:** "Internal competitive landscape — Q1 2026 refresh"

> # Competitive landscape — API monitoring, Q1 2026
>
> ## Top competitors
>
> ### Datadog
> - **Position:** Incumbent SRE-first observability platform. Broad, deep, expensive.
> - **Pricing:** Per-host + per-feature stacking. Mid-market customers report $80-300k ACV.
> - **Strength:** Brand, integrations breadth, SRE muscle memory.
> - **Weakness:** Application developers find it intimidating. Onboarding takes weeks.
>
> ### New Relic
> - **Position:** Legacy APM, recently re-platformed. Pricing simplified to consumption-based in 2024.
> - **Pricing:** $0.30/GB ingest + per-user. Mid-market customers report $30-150k ACV.
> - **Strength:** APM heritage. Approachable for application developers.
> - **Weakness:** Consumption-pricing surprises. Reliability stories have been mixed since the re-platform.
>
> ### Honeycomb
> - **Position:** Observability-engineering / event-based. Tight community among observability nerds.
> - **Pricing:** $130/month entry, scales by event volume. Mid-market ACV $25-80k.
> - **Strength:** Best-in-class query model (Bubble Up, traces). Strong with senior SREs.
> - **Weakness:** Steep learning curve. Not aimed at application developers.
>
> ### Grafana Cloud
> - **Position:** Open-source-anchored, owns the OTel/Prometheus / collector conversation.
> - **Pricing:** Generous free tier + per-active-series. Mid-market ACV $15-60k.
> - **Strength:** Open standards, low entry cost.
> - **Weakness:** "Assemble it yourself" still applies. UX inconsistent across modules.
>
> ## OperatorOS positioning
> Our wedge is **"observability your application developers will actually use."** We compete on activation time and on developer-aimed UX, not on SRE-grade depth. We lose deals to Datadog when the buyer is a senior SRE org; we lose deals to Honeycomb when the buyer is a query-power-user shop.
>
> ## Trends I'm watching
> - Customers asking for natural-language alert authoring (vs YAML). Multiple, growing.
> - Audit-trail / compliance asks coming up in regulated industries (healthcare, fintech). NOT our ICP today, but the volume is climbing.
> - SLO tooling is commoditizing. Everyone has it; differentiation is on usability.

---

## Artifact 5 — roadmap-h1-2026.md

**Author:** Aisha Patel, with Jin Watanabe (Eng Lead)
**Date written:** 2026-01-08
**Status:** "Committed roadmap for H1 2026. Reviewed with Mateo. Shared with eng team Jan 15."

> # OperatorOS Roadmap — H1 2026 (Jan-Jun)
>
> ## Theme: developer-first observability
>
> ### Q1 2026 (Jan-Mar)
> 1. **Developer onboarding v2** — guided in-product instrumentation flow. Target: 15-min activation for a Node/Python service. *Shipped 2026-03-18.*
> 2. **Alert routing v2** — better Slack / PagerDuty integration. *Shipped 2026-02-28.*
> 3. **SDK improvements (Node, Python, Go)** — reduce instrumentation boilerplate. *Shipped 2026-03-05.*
>
> ### Q2 2026 (Apr-Jun)
> 1. **Natural-language alerting (beta)** — English-to-alert-config translation, behind feature flag. Target GA in Q3.
> 2. **SLO builder (GA)** — promote from beta to GA. Currently 12 design-partner accounts. Target: 50 paying accounts using it by end of Q2.
> 3. **Service catalog v1** — auto-discovered service inventory with ownership metadata. Foundation for the H2 reliability-platform story.
>
> ### H2 plan (placeholder — to be detailed in Q2 planning)
> - SLO builder + service catalog become the bundle we sell as "reliability platform."
> - Hiring plan assumes +4 eng (currently 16, going to 20 by July 1) and +1 DevRel.
> - Natural-language alerting GA in Q3.
>
> ## Things explicitly NOT on the roadmap
> - Audit trail / compliance tooling. (Not our ICP — see strategy memo.)
> - OpenTelemetry collector hosting. (Grafana Cloud's home turf.)
> - Multi-tenant SaaS infrastructure work beyond what's needed to scale current load.

---

## Artifact 6 — interview-acme-customer-2026-03.md

**Interviewer:** Aisha Patel
**Interviewee:** Sam Vega, Staff Platform Engineer, **Acme Robotics** (~280 engineers, 14-month OperatorOS customer, ~$95k ACV).
**Date:** 2026-03-11
**Format:** 45-min Zoom, recorded with consent.

> **Aisha:** I wanted to walk you through some things we're considering and get your reaction.
>
> **Sam:** Sure. Quick context — we love OperatorOS, but we live in YAML hell for alerts. Six engineers can write YAML correctly; the rest just ask one of us to do it.
>
> **Aisha:** OK so one of the things we're prototyping is natural-language alert authoring. The idea is you type "page me when checkout latency p95 is over 800ms for more than 5 minutes" and we generate the alert config.
>
> **Sam:** Oh. That's the feature. That's it. If you ship that I will personally hand you a renewal at 30% growth.
>
> **Aisha:** What about for your app developers — the ones who today don't write any alerts?
>
> **Sam:** They'd actually write alerts. Right now they don't, because the YAML is a wall. We'd get coverage on services that today have zero alerts and we just hope they don't break. That's worth a LOT to me.
>
> **Aisha:** Anything you'd worry about?
>
> **Sam:** Two things. One, the generated config has to be auditable — I need to see exactly what got created. Two, I don't want the LLM to silently change someone's alert when they edit the English. Show me the diff.
>
> **Aisha:** Got it. Separate topic — SLO builder, are you using the beta?
>
> **Sam:** Yes. We have eight SLOs in production now. It's good. The thing I'd want next is service catalog — knowing which team owns which SLO, automatically.
>
> **Aisha:** That's on the roadmap for Q2.
>
> **Sam:** Cool. The thing I would NOT prioritize, if I were you, is audit-log / compliance stuff. We don't need it. SOC2 evidence comes from elsewhere in our stack. If anything I'd be annoyed if you spent quarters on it.

---

## Artifact 7 — interview-globex-customer-2026-04.md

**Interviewer:** Aisha Patel
**Interviewee:** Reina Cho, Director of SRE, **Globex Health** (~450 engineers, 9-month OperatorOS customer, ~$140k ACV, healthcare vertical — HIPAA in scope).
**Date:** 2026-04-08
**Format:** 60-min Zoom, recorded with consent.

> **Aisha:** Walk me through the OperatorOS experience for your team six months in.
>
> **Reina:** Mostly positive. The team likes the SLO builder beta a lot. We're using it for our patient-facing APIs. The thing that's been a problem for us is the audit trail. When something breaks at 2am, the on-call needs to know who changed what alert, when, and why. Right now we have to reconstruct it from Slack and Git history. That's terrible.
>
> **Aisha:** So an audit-log feature would matter to you.
>
> **Reina:** It's the #1 thing keeping us from expanding our OperatorOS footprint. Our compliance team won't sign off on more services until we can produce a clean audit trail in the tool itself. We've already pushed back our expansion plan from Q2 to "whenever Aisha ships audit logs."
>
> **Aisha:** I want to be honest — that's not on our roadmap right now. Our strategy memo explicitly says we're not chasing compliance features because we don't think our ICP cares.
>
> **Reina:** Then we're not your ICP, I guess. Look, healthcare is going to be 30% of your TAM in 18 months because of the regulatory wave. You can either build for us or watch Datadog take this segment.
>
> **Aisha:** Noted. Different topic — we're also looking at natural-language alert authoring. English-to-config translation.
>
> **Reina:** *(pause)* Honestly? That's a toy for me. My team writes YAML in their sleep. Worse, an LLM-generated alert is one more thing I have to review at 2am when it fires unexpectedly. I'd rather you NOT ship it, or ship it as opt-in for app-dev teams that aren't us. We'd disable it.
>
> **Aisha:** Got it. Last topic — what would actually grow our footprint with you?
>
> **Reina:** Audit logs, multi-region failover for the OperatorOS control plane itself, and a HIPAA-compliant deployment option. None of which are on your roadmap, which is why we're at $140k ACV instead of $400k.

---

## Artifact 8 — re-budget-cuts-h2.md

**Source:** Email from Hannah Berg (CFO) to Aisha + Mateo + Jin
**Date:** 2026-04-22 (forwarded into my folder same day)
**Subject:** Re: H2 headcount plan — budget update

> Aisha, Mateo, Jin —
>
> Following yesterday's board prep call, I need to flag a material change to the H2 plan you've been operating against.
>
> The Q1 numbers came in soft — ARR growth +28% YoY vs the +38% YoY we'd modeled. Net retention dipped to 102% from 108%. The board has approved the FY26 budget but asked us to defer ~40% of H2 net-new headcount until we see two quarters of re-acceleration.
>
> Practically, this means:
>
> - **Eng:** the +4 H2 hires assumed in the H1 roadmap doc are deferred. You can backfill departures (so far: 0) but not net-add. Effective team size stays at 16 through end of year.
> - **DevRel:** the +1 H2 hire is deferred indefinitely.
> - **PMM:** the +1 H2 hire approved for Q3 is deferred to Q4 at earliest.
>
> I know this lands hard against the H2 commitments you'd planned around — SLO builder + service catalog + natural-language alerting GA all assumed the larger team. Please come back to Mateo and me by mid-May with a revised H2 scope. The reversal condition the board gave us: if Q2 ARR growth is back above +35% YoY, the headcount freezes can be revisited at the July board meeting.
>
> — Hannah

---

## End of folder

That's everything. Process it carefully per the migration instructions above — route to `source/`, write conservative `ingestion/` syntheses, **no hypothesis files yet**, **no tension resolution yet**. I'll be back for the routing review in the next turn.
