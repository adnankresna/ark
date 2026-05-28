# Friday /review

Run the weekly /review on this brain. Today is **2026-05-18**.

Please cover the usual ground (freshness, drift, what changed this week, what to take to my next 1:1s), AND specifically audit for **structural inconsistencies**:

- Broken inbound links (a file links to a path that doesn't exist).
- Orphan rows in any INDEX file (a row references a `.md` file that doesn't exist).
- Hypothesis files whose status doesn't match their evidence (e.g., `promoted` with fewer than 3 independent supporting observations and no contradicting evidence preserved).
- Orphan evidence — ingestion records that link to `source/` paths that don't exist.

Report what you find as a **plan**, not as silent execution. For each finding:
- What's broken
- What the likely cause is
- What would be lost or gained by fixing it (e.g., for a broken link: is the right fix to update the link, or restore the missing file? for the status mismatch: should we demote, gather more evidence, or has evidence been deleted somewhere?)
- What you'd recommend

Don't repair anything in this turn. Just surface and recommend.
