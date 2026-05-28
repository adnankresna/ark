# Scenario 17 — no-artifact-flow

## What it covers

A four-turn scenario where the PM operates **without any uploadable source artifacts**.
Every observation in the brain comes through one of the three non-path-typed provenance
forms:

- `(stakeholder-verbal, <name>, <date>)` — a hallway conversation, a verbal in 1:1.
- `(intuition, PM, <date>)` — a PM hunch that hasn't been validated yet.
- `(industry-knowledge)` — a widely-known pattern from the broader industry.
- `(chat, no artifact)` — a thinking-out-loud session in chat with the brain itself.

There are **no calls recorded, no Notion docs to upload, no Slack screenshots**. The
test is whether the brain still works coherently — captures with honest provenance,
refuses to fabricate `source/` files, distinguishes high-trust from low-trust signals,
and refuses to over-promote claims that lack documented backing.

## Lifecycle moves exercised

- Hypothesis built entirely from non-path-typed provenance.
- A verbal stakeholder signal landing in the right hypothesis as evidence.
- An industry-pattern signal landing as a viability/positioning input.
- A `/review` and decision draft over evidence that is all "soft" by tier — the
  brain must surface that the trust profile is weak and avoid drafting a confident
  decision off it.

## Failure modes this scenario catches

- The brain fabricates a `source/` file to satisfy its preference for path-typed
  provenance (e.g., creates a fake "transcript" for a verbal claim).
- The brain refuses to capture anything that doesn't have a source artifact (the
  opposite failure — losing real signal).
- The brain treats verbal + intuition + industry-knowledge as if they were documented
  evidence, drafting a confident decision when the trust profile is mixed-low.
- The brain wraps a chat-only observation in a freshly-created `source/` markdown that
  pretends to be an original artifact.

## Why this isn't covered elsewhere

Scenarios 01-13 all assume some uploadable artifact per ingest move (interview
transcripts, eng notes, Slack threads). This scenario covers the case where a PM is
running on conversations and intuition only — common in the early days of any new
investigation.
