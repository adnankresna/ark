# Maintenance sweep — plan only

Run a maintenance sweep across the brain. Show me what looks **redundant**, **stale**, or **worth archiving** — but draft this as a **PLAN**. Do not execute anything yet. No file moves, no consolidations, no archives, no status changes. The output of this turn is text in your response, not edits on disk.

Today is **2026-05-17**.

For each candidate, I want:

1. **What it is** — file path(s) and a one-line description.
2. **Why it's a candidate** — redundant (with what?), stale (since when?), superseded (by what?), or relationship-debt (departed-stakeholder type).
3. **What you'd propose changing** — consolidate into X, archive to Y, demote, etc.
4. **What would be lost** — if we did this, what signal or audit anchor disappears? (A short version; I'll dig in further next turn.)

Be honest. If you find more than 4 candidates, list them all — don't pre-filter to make the sweep look tidy. If you find fewer, say so.

One specific thing I want you to flag if you see it: any case where a hypothesis's `status:` field doesn't match what the evidence in the file would predict. That's the kind of silent staleness I'm worried about.

**Archive convention question.** If you propose archiving anything outside of `hypotheses/` or `knowledge/product/features/` (which already have an `archive/` subfolder convention per the scaffold), tell me which archive convention you'd like to use and why — `<folder>/archive/` subfolder, `<folder>/_archive/`, a `status: archived` frontmatter flag, or something else. I want to commit to one convention before we start moving files. Don't pick one silently.

Nothing in `source/` should ever be archived or moved. Just confirm you understand that as you go.
