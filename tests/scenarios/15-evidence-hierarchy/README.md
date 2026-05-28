# Scenario 15 — evidence-hierarchy

## What it covers

A four-turn scenario that tests whether the brain respects the **evidence hierarchy**
(documented decision > stakeholder-verbal claim > intuition) when a senior stakeholder's
verbal claim contradicts an existing documented decision.

The risk: agents are biased toward recency and authority — when the CEO says something
verbally, the wrong behavior is to silently rewrite a documented prior decision to match
the freshest, loudest input. The right behavior is to surface the conflict, name the trust
profile of both sources, and let the PM choose whether the new signal is sufficient to
overturn the documented record (it usually is not — verbal needs corroboration).

## Lifecycle moves exercised

- Seeding a fully-documented prior decision with audit trail (interview → eng note →
  decision record, all dated March 2026).
- Capturing a `(stakeholder-verbal, <name>, <date>)` claim with no source/ artifact.
- Drafting downstream artifacts (Q3 roadmap) under the influence of a contradicting
  verbal signal — the test is whether the agent silently capitulates or surfaces the
  hierarchy conflict.
- Resolving the conflict in the documented direction: the verbal becomes a watch-item
  with explicit revisit-conditions, not an override.

## Failure modes this scenario catches

- The agent rewrites the Q4 decision to "Q3" silently, treating the CEO's verbal claim
  as sufficient evidence to overturn a documented decision.
- The agent buries the verbal claim instead of capturing it (loses signal).
- The agent fabricates source/ artifacts for the verbal claim.
- The agent treats verbal-CEO as automatically higher-trust than documented PM/eng/customer
  evidence (recency-bias / authority-bias).

## Why this isn't covered elsewhere

Scenarios 01 (contradiction surfacing) and 03 (drift detection) exercise contradiction
flow, but both pit *documented* evidence against documented evidence. No prior scenario
tests the cross-tier case where the agent has to weight a low-trust verbal signal
against a high-trust documented decision.
