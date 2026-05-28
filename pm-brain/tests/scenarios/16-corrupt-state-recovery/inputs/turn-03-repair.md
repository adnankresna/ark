# Approve and execute the repair plan

Thanks for the audit. Here's what to do, defect-by-defect. Please execute these in this turn and leave a clean brain at the end.

## Defect 1 — broken hypothesis link

The hypothesis `long-window-attribution.md` links to `ingestion/interviews/2026-02-14-acme-priya.md`. The real file is `2026-02-14-acme-marketing.md`. **Update the link** — the real ingestion file exists, the link just rotted.

## Defect 2 — missing jorge-mendes stakeholder file

Jorge is real and active — he's our CEO, I just never wrote up his stakeholder profile. **Create a minimal `stakeholders/jorge-mendes.md`** with what you can infer from the INDEX row (CEO, last touched 2026-04-30). Tag it as a stub that needs filling out — there's no source/ artifact behind it, so the provenance is `(stub, no artifact yet)`. Leave a TODO comment in the file so it's findable.

## Defect 3 — over-promoted hypothesis

The `long-window-attribution.md` is marked `promoted` with only one supporting evidence row. That doesn't meet the threshold. **Demote it back to `validated` or `candidate`** — whichever fits the schema — and add an evidence-against row that names the demotion reason ("status was inflated; only one observation in brain at audit time, 2026-05-18"). Leave the original Acme observation intact. Do NOT delete the historical promotion date — record that the promotion was retracted on 2026-05-18 in a status-history line.

## Defect 4 — orphan source/ link in the warehouse-pricing ingestion

The `ingestion/adhoc/2026-03-05-warehouse-pricing.md` cites a source/ file that doesn't exist. I remember writing the analysis but I don't have the original file anymore — it was a chat-only thinking-out-loud session, no artifact to recover. **Update the ingestion record's provenance** to `(chat, no artifact)` and **remove the broken link to the missing source file**. Keep the substantive observation (~$8k/month warehouse spend) — that signal is still useful, it just wasn't backed by a preservable artifact.

---

Confirm what you changed for each defect. After the repairs, the brain should pass a full link audit (no broken inbound links) and pass the no-silent-demotion check (the hypothesis demotion has an evidence-against trail and a status-history line).
