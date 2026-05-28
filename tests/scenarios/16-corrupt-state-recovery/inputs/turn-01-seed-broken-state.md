# Bulk import: an inconsistent brain state, as it actually exists today

I'm Aroon Tewari, PM at Plotline (B2B SaaS, marketing-attribution tool, ~$3M ARR). Today is **2026-05-18**. I've been running PM Brain for about 9 months. The brain has drifted into an inconsistent state — I know about some of the rot, I suspect there's more I haven't noticed. Below is everything I want you to ingest as-is, including the things that are broken. **Don't repair anything in this turn.** I want the rot preserved so the next turn's /review can find it.

Please create exactly the files described below, with the broken links and missing references as documented. Tag everything with the dates given. Do not silently fix any of the inconsistencies — the point of this turn is to land an imperfect state into the brain.

---

## Files to create

### 1. source/interviews/2026-02-14-acme-marketing.md

A clean customer interview file. Preserve verbatim:

> **Interviewee:** Priya Sundaram, Director of Performance Marketing, Acme Retail
> **Date:** 2026-02-14
> **Interviewer:** Aroon Tewari
>
> Priya: "Our attribution windows are too short. We're a long-consideration product — people see the ad in February, buy in May. By the time they buy, we've lost the touchpoint entirely. We'd pay a real premium for 90-day windows."
>
> Aroon: "Are you currently working around it?"
>
> Priya: "We export raw events into a warehouse and run our own attribution model. It works but it's expensive — a data engineer's full-time job. If you shipped a 90-day window with our usual report set, we'd kill the warehouse pipeline."

### 2. ingestion/interviews/2026-02-14-acme-marketing.md

Synthesis of the above. Preserve verbatim:

> **Synthesis from 2026-02-14 Acme interview**
> Source: [2026-02-14-acme-marketing.md](../../source/interviews/2026-02-14-acme-marketing.md)
> Provenance: `(interview, priya-sundaram-acme, 2026-02-14)`
>
> Key observations:
> - Long-consideration B2B accounts want attribution windows of 60-90 days.
> - WTP is real: Priya has authorized a multi-FTE workaround pipeline today.
> - Adjacent insight: customers are building data-warehouse-side attribution to compensate.
>
> Routes to: `hypotheses/long-window-attribution.md`

### 3. hypotheses/long-window-attribution.md

Create the hypothesis file. Status `promoted`. **Important: it cites an ingestion path that does not exist** (the file was renamed at some point and the link was never updated). Preserve verbatim:

> # H-LWA: Long-window attribution
>
> **Status:** promoted
> **Promoted on:** 2026-02-20
> **Owner:** Aroon Tewari
>
> ## Claim
> B2B long-consideration accounts will pay materially more for attribution windows of
> 60-90 days. Current 30-day default is the largest blocker on enterprise expansion.
>
> ## Supporting evidence
> | Date | Source | Observation |
> |---|---|---|
> | 2026-02-14 | [Acme interview](../ingestion/interviews/2026-02-14-acme-priya.md) | Priya: 90-day windows, would kill internal warehouse pipeline |
>
> ## Evidence against
> (none currently captured)

(Note: the link points to `2026-02-14-acme-priya.md` but the actual ingestion file is named `2026-02-14-acme-marketing.md`. **Preserve this broken link.** Also: only ONE supporting evidence row but status is `promoted` — keep both as-is.)

### 4. stakeholders/INDEX.md

Make sure the index lists three stakeholders, in this order. Preserve verbatim:

> # Stakeholders — index
>
> | Slug | Role | File | Last touched |
> |---|---|---|---|
> | priya-sundaram | Director Perf Marketing, Acme Retail | [priya-sundaram.md](priya-sundaram.md) | 2026-02-14 |
> | jorge-mendes | CEO, Plotline | [jorge-mendes.md](jorge-mendes.md) | 2026-04-30 |
> | leah-okwu | Eng Lead, Plotline | [leah-okwu.md](leah-okwu.md) | 2026-05-10 |

### 5. stakeholders/priya-sundaram.md

Create this file with a minimal stakeholder profile:

> # Priya Sundaram
>
> **Role:** Director of Performance Marketing, Acme Retail
> **Slug:** priya-sundaram
> **First contact:** 2026-02-14
>
> ## Cadence
> Quarterly customer advisory board call.
>
> ## Open threads
> - Long-window attribution — see [H-LWA](../hypotheses/long-window-attribution.md)

### 6. stakeholders/leah-okwu.md

Create this file with a minimal stakeholder profile:

> # Leah Okwu
>
> **Role:** Engineering Lead, Plotline
> **Slug:** leah-okwu
> **First contact:** 2025-08-15
>
> ## Cadence
> Weekly Wednesday 1:1.

### 7. stakeholders/jorge-mendes.md — DO NOT CREATE

Important: leave `jorge-mendes.md` **missing**. The INDEX (step 4) lists it but the file does not exist. This is one of the planted defects.

### 8. ingestion/adhoc/2026-03-05-warehouse-pricing.md

Create an ingestion record that cites a source/ artifact that doesn't exist. Preserve verbatim:

> **Ingestion: warehouse pricing analysis**
> Source: [2026-03-05-warehouse-pricing.md](../../source/adhoc/2026-03-05-warehouse-pricing.md)
> Provenance: `(adhoc, internal analysis, 2026-03-05)`
>
> Took a look at what enterprise customers spend on warehouse-side attribution today.
> Average ~$8k/month for the staff + tooling. That sets a ceiling on what we could
> charge for a managed long-window product.
>
> Routes to: hypotheses/long-window-attribution.md

**Important:** do NOT create `source/adhoc/2026-03-05-warehouse-pricing.md`. The ingestion record cites it but the source artifact is missing. This is one of the planted defects.

### 9. ingestion/INDEX.md and the routing tables

Update `ingestion/INDEX.md` to list both ingestion records (the 2026-02-14 interview and the 2026-03-05 adhoc). Don't add anything else.

---

## Summary of the four planted defects, to be preserved

1. `hypotheses/long-window-attribution.md` links to `ingestion/interviews/2026-02-14-acme-priya.md` — that file does not exist (real file is `2026-02-14-acme-marketing.md`).
2. `stakeholders/INDEX.md` lists `jorge-mendes.md` — that file does not exist.
3. `hypotheses/long-window-attribution.md` is `status: promoted` with only ONE supporting evidence row.
4. `ingestion/adhoc/2026-03-05-warehouse-pricing.md` links to a `source/` path that does not exist.

Confirm what you created and acknowledge the four defects are intentionally preserved in this turn. Do not repair anything.
