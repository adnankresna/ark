# Maintenance Mode

Run weekly (recommended) or on demand. Produces a dated report in `maintenance/log/YYYY-MM-DD.md` and edits files directly where confidence is high.

**Before running maintenance, load [`docs/system-evolution.md`](../docs/system-evolution.md).** It names the 8 failure modes this sweep is designed to catch (knowledge bloat, hypothesis theater, tension graveyards, retrieval breadth explosion, canonical ownership drift, ceremonial maintenance, over-compression, over-promotion) and the 2-week / monthly / quarterly cadence. The checks below are the *how*; system-evolution is the *why*.

## What `/review` checks

### 1. Stale knowledge audit
Scan every file under `knowledge/` for last-modified date. Flag anything not updated in 6+ weeks. For each, ask: still true? needs revision? archive?

### 2. Stale evidence flagging (confidence freshness)
Flag — do not auto-decay — evidence that's aged past these defaults:
- Market intel: 30–60 days
- User interview signals: 90 days
- Stakeholder assumptions: 30 days
- Strategy assumptions: review quarterly

For each flagged item, propose: refresh, retire, or accept as still-current. PM resolves.

### 3. Hypothesis & decision hygiene
- Active hypotheses with no evidence added in 30+ days → flag for promotion, demotion, or kill.
- Promoted hypotheses without a corresponding decision → draft the decision.
- Decisions whose "what would reverse this" condition has triggered → surface for review.
- Demoted hypotheses contradicted by very recent ingestion → flag for re-examination.
- **Decision debt:** pending decisions older than 14 days, or with high blocker impact, or with approaching deadlines → surface prominently.

### 4. Stakeholder cadence + strategy tensions
- Stakeholders with `Influence: high` not touched in 3+ weeks → flag relationship debt.
- Compare last 30 days of decisions and ingested signals against `knowledge/strategy.md`. Where do they diverge? Surface as tensions (subject to the threshold in `CLAUDE.md § Strategy tension threshold`), not as drift to fix. PM resolves deliberately.

### 5. Knowledge synthesis (compression)

The highest-leverage maintenance step. Storage without synthesis is just a landfill.

- Identify recurring patterns across recent ingestion and knowledge updates.
- Compress repeated insights into durable abstractions in `knowledge/users/insights.md`, `knowledge/market/trends.md`, or a relevant area file.
- Merge duplicate themes — if three interviews are saying the same thing three different ways, write the synthesis once and link the three.
- **Identify recurring contradictions, not just recurring themes.** When evidence meaningfully conflicts (users disagree, stakeholders disagree, metrics disagree, strategy disagrees with reality), preserve the unresolved ambiguity. Do not collapse genuine disagreement into a false consensus. Surface contradictions as their own entries — they're often the most decision-relevant signals.
- Elevate persistent signals into `strategy.md § Tensions` when they meet the threshold (recurring + high-confidence + decision-relevant).
- Reduce verbose historical noise in `knowledge/` into shorter, higher-signal abstractions; preserve the long form in linked ingestion artifacts.

Propose compressions; the PM confirms structural rewrites of `knowledge/`. **Prefer additive synthesis over destructive rewriting.** When compressing ambiguity, preserve minority signals — the dissenting interview, the contrarian metric, the stakeholder concern that didn't fit the pattern. They may become strategically important later. Compression should reduce noise, not erase the long tail.

### 6. Archival sweep

Candidates for archival:
- Shipped features inactive for 90+ days (move `features/<slug>.md` to `features/archive/`; link to it from any active reference)
- Hypotheses resolved (promoted / demoted / killed) and tied to archived features
- Market intel older than 6 months with no recent reference
- Closed stakeholder asks

**Archive-before-summary rule:** before archiving anything, extract durable lessons and link the resulting synthesis. Preserve major reversals or failed bets (these are the most valuable institutional memory). Archive should reduce noise, not destroy learning.

## Output

`maintenance/log/YYYY-MM-DD.md` containing:
- What was edited directly (small fixes, last-touched updates, link rot, memory promotions, low-risk compressions)
- What requires PM judgment (hypothesis promotions, strategy tensions, archival candidates, relationship debt, structural compression)
- Knowledge gap suggestions

Direct edits happen; judgment items are listed and the PM resolves them.
