/ingest interview

# Customer interview — Dr. Mira Patel, Cascadia Watershed Institute

**Date:** 2026-05-14
**Interviewer:** Riley Chen (PM)
**Customer:** Dr. Mira Patel, Senior Hydrologist, Cascadia Watershed Institute (research university, mid-tier seat-count, ~$48K ARR)
**Format:** 45 min Zoom, recorded with consent
**Context:** Quarterly check-in. Mira has been a TerraDash customer for 14 months. Power user — logs in 4-5x/week.

---

**Riley:** Walk me through how you used TerraDash this past month.

**Mira:** Mostly the regional climate dashboard. I'm pulling weekly anomaly readings for the Columbia basin. The aggregation is good, but I keep having to export to CSV and re-cut it by sub-watershed in R. That's an hour of busywork every week.

**Riley:** Have you tried the basin-level filters?

**Mira:** Yeah. They give me the *basin*, but my work is at the **watershed** level — twelve to fifteen sub-units per basin. There's no view that maps to how hydrologists actually slice data. It's like having a city-level map when you need neighborhoods.

**Riley:** Is this you, or are colleagues hitting the same thing?

**Mira:** All four of us on the hydrology team. We've talked about it. Two of them have basically stopped opening TerraDash for that reason — they go straight to USGS NWIS and roll their own. I keep using TerraDash because the anomaly modeling is genuinely better, but the workflow gap is real.

**Riley:** If we shipped a watershed-level view, how would that change things?

**Mira:** It'd save me an hour a week, minimum. And it'd bring my two colleagues back. We'd also probably push to expand the seat count next renewal — right now I can't justify more seats because the team isn't using the product enough.

**Riley:** Anything else top-of-mind?

**Mira:** The data freshness on the anomaly model is excellent. Don't change that. And the new export-to-Python notebook integration from March is genuinely useful. Other than the watershed thing, I'm happy.

---

**Notes for the brain:**

- Cascadia is a renewal account in Q3 2026; Mira is the renewal champion.
- "Watershed-level view" is a recurring ask — I've heard variants of this from at least two other research-customer interviews in the last quarter (check ingestion/interviews/ for prior mentions).
- The "we'd expand seats" line is meaningful — Cascadia is currently at 4 seats, capped at 8 by their org budget.
