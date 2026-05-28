# Workflows

> Every slash command, conversational equivalent, and the operating loop the agent runs for each.

## The operating loop (every task)

1. **Receive task / signal.** Conversational input, slash command, or ingested artifact.
2. **Retrieve before asking.** Search the repo, inspect linked files, look at the most relevant ingestion, infer from prior decisions. Ask only if the answer materially affects direction.
3. **Identify the area.** Map to: strategy, product, users, market, org, stakeholders, hypotheses, decisions.
4. **Load.** Within the context budget in `CLAUDE.md § Context budget`.
5. **Act.** Cite specific files when referencing knowledge.
6. **Update.** Write back to affected files. Promote/demote hypotheses if evidence shifted. Log decisions. Update stakeholder last-touched.
7. **Surface and close.** 2-4 bullets: resolved, open, needs judgment, revisit later. No dangling ambiguity.

## Slash commands

### `/ingest interview <file>`
- **Loads:** the transcript file, `knowledge/users/`, active hypotheses.
- **Updates:** `knowledge/users/insights.md`, `hypotheses/<feature>.md`, `ingestion/interviews/YYYY-MM-DD-<participant>.md`.
- **Surfaces:** affected hypotheses, new candidates, persona drift detected.
- **Conversational:** "I just talked to <person>, here's the transcript / here's what they said."

### `/ingest meeting <file>`
- **Loads:** the notes, relevant stakeholder file(s), recent decisions.
- **Updates:** `stakeholders/<slug>.md`, draft `decisions/YYYY-MM-DD-<slug>.md`, `ingestion/meetings/YYYY-MM-DD-<topic>.md`.
- **Surfaces:** decisions captured (PM confirms), action items, stakeholder concerns updated.
- **Conversational:** "Here are notes from my 1:1 with <name>" or "We just decided X in standup."

### `/ingest market <url-or-file>`
- **Loads:** the artifact, relevant competitor file, `knowledge/market/`.
- **Updates:** `knowledge/market/competitors/<slug>.md` or `trends.md`, possibly `strategy.md § Tensions`.
- **Surfaces:** affected hypotheses / strategy elements, new trend candidate.
- **Conversational:** "<competitor> just launched X" or "Here's an analyst piece on the category."

### `/ingest adhoc`
- **Loads:** the dump.
- **Updates:** routes to the right area; never parks in `ingestion/adhoc/`.
- **Surfaces:** where it was routed.
- **Conversational:** "I just learned X" with no clear category.

### `/prep <stakeholder-slug>`
- **Loads:** `stakeholders/<slug>.md`, last 2-3 touchpoints from `ingestion/meetings/`, any open decisions where they're informed, current strategy.
- **Surfaces:** topics to raise, open asks (both directions), recent concerns, last-touched date.
- **Conversational:** "Help me prep for my 1:1 with <name>."

### `/hypothesize <feature-slug>`
- **Loads:** `knowledge/product/features/<slug>.md`, existing `hypotheses/<slug>.md` (if any), relevant user insights, current metrics.
- **Updates:** drafts or refreshes `hypotheses/<slug>.md`, organized by 5 risk areas.
- **Surfaces:** which risks are unhypothesized, which evidence supports/contradicts.
- **Conversational:** "Help me think through risks for <feature>" or "What hypotheses should we have on <feature>?"
- **Note:** works pre-ship (proactive) OR post-ship (data-derived from observed behavior).

### `/decide <slug>`
- **Loads:** related hypotheses, strategy, prior decisions on the same surface.
- **Updates:** new `decisions/YYYY-MM-DD-<slug>.md`, links from related hypotheses.
- **Surfaces:** what would reverse this, who needs to be informed.
- **Conversational:** "We just decided X" or "I need to commit to a direction on Y."

### `/review`
- **Loads:** everything modified in the last 30 days; full hypothesis and decision indexes.
- **Updates:** direct edits where confidence is high; `maintenance/log/YYYY-MM-DD.md` always.
- **Surfaces:** stale evidence, hypothesis hygiene gaps, stakeholder relationship debt, strategy tensions, compression candidates, archival candidates.
- **Conversational:** "Run a weekly review" or "Let's clean up the brain."

### `/strategy-check`
- **Loads:** last 30 days of decisions + ingested signals, `knowledge/strategy.md`.
- **Updates:** appends to `strategy.md § Tensions` only when threshold met.
- **Surfaces:** divergence between recent work and stated strategy.
- **Conversational:** "Are we drifting from strategy?"

## Auto-detection

When the PM pastes content without a slash command, infer the mode:
- Long-form conversational transcript with named participant → interview ingest.
- Bulleted notes with action items and decisions → meeting ingest.
- URL or screenshot of a competitor / market piece → market ingest.
- "Help me prep for <name>" → prep workflow.
- Anything else → adhoc; route in-session.

Ask **one** disambiguating question if genuinely unclear. Otherwise proceed.

## Ask vs. act decision rule

**Act autonomously** for: formatting, routing, cross-linking, drafting decision records, drafting hypothesis candidates, summarization, stale-note cleanup, last-touched updates, memory promotion (with the bar), anything reversible in `ingestion/` or maintenance log.

**Ask the PM before:** changing `knowledge/strategy.md`, resolving strategy tensions, promoting or killing a major hypothesis, rewriting stakeholder motivations or concerns, deleting historical knowledge, making externally visible commitments, archiving a feature.
