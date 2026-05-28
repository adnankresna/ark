# Analytics snapshot — mid-market churn, QoQ

**Date:** 2026-04-26
**Source:** PM's note after pulling the weekly retention dashboard
**Format:** a digest the PM wrote for themselves, not a deck

---

## What the data shows

- **Mid-market churn rate:** Q1 2026 closed at 6.1%. Q2 trailing 4 weeks is tracking 10.3%. Up 4.2 percentage points QoQ.
- Enterprise churn flat (1.2% → 1.4%, within noise).
- SMB churn flat (12% → 11.8%).
- The QoQ jump is concentrated entirely in the mid-market segment.

## Exit-survey reasons (free text, top categories, n=18 for Q2 to date)

| Category | Count | % |
|---|---|---|
| Notification overload / "too many alerts" | 5 | 28% |
| Pricing / budget cut | 4 | 22% |
| Acquired by larger company on different tool | 3 | 17% |
| Onboarding never completed | 2 | 11% |
| Other / unclear | 4 | 22% |

Notification overload is the top free-text reason. This matches the Acme finding. But the sample is small (5 of 18) and the survey response rate on churn is around 40%, so the real distribution could be different.

## Cohort behavior

Pulled a quick cohort: 6 mid-market accounts that churned in the last 30 days, vs 6 comparable mid-market accounts that renewed in the same period.

- **Churned cohort:** notification engagement (clicks + reactions on emails/Slack/in-app) high in months 1-3, then drops to near-zero by month 6. They didn't unsubscribe; they just stopped acting on alerts.
- **Renewed cohort:** similar curve but the drop-off is gentler, and they still have nonzero engagement at month 6.

The pattern is suggestive but **the dataset is tiny (n=12)** and confounded — these are the same accounts I'd qualitatively expect to behave this way based on Customer Success notes. Don't draw causal conclusions from this.

## What I'm doing about it

- Tagging this as a watch item, not a confirmed pattern.
- The Acme interview last week (one source) + this analytics signal (one source) is not enough to confirm notification overload as *the* driver of mid-market churn.
- Next step: 2-3 more mid-market interviews this week, plus a pull on the 6 churned accounts' notification volumes (did they actually get more notifications than the renewed cohort, or did they just disengage from the same volume?).

## What I am NOT doing

- Not opening a new hypothesis on this signal alone. The Acme interview already opened one on notification volume / value risk; this is a second data point that's consistent but circumstantial.
- Not flagging this to leadership as "we have a churn problem caused by notifications." That would be jumping ahead of the evidence.
- Not adjusting the product strategy this week. Strategy adjustments need at least three independent signals.
