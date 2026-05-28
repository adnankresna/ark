# Engineering sync — real-time alerts scoping

**Date:** 2026-04-24
**Type:** 60-min sync
**Attendees:** PM (you), Eng Lead (Diana Park), Backend Engineer (Tomás Reyes), Backend Engineer (Yuki Tanaka)
**Channel:** in-person + recorded for Yuki who joined remotely

---

## Context

PM-initiated meeting. After the Acme interview last week flagged notification overload, two things needed scoping in parallel: (1) what would a "calm mode" / weekly-digest-only product look like in code, (2) what would it cost to ship a real-time tier if we decided to. Eng team prepped a one-pager going in.

---

## Notes (PM's summary, written immediately after)

### Current state

- Notification pipeline runs as a 6-hourly cron sweep that collates events, dedupes, and emits to Slack, email, and in-app.
- Daily digest is a separate cron at 09:00 user-local that collates the previous 24 hours' high-priority items.
- Weekly digest doesn't exist as a primitive — it's just the daily digest minus the empty days, manually configured by CS for a handful of accounts (Acme being one of them).

### What a "calm mode" / weekly-only would take

- Diana: "Almost trivial. We'd promote the weekly-digest configuration to a first-class user setting, default it to ON for new accounts, and pull the existing daily / 6-hour cadences behind a toggle. Maybe 1-2 sprints including UX."
- Tomás flagged a follow-on: if weekly becomes default, we need to make sure the in-app indicator (the bell icon counter) doesn't accumulate seven days of unread badges. That's a small UI fix.

### What a real-time tier would take

- Diana walked through the architectural shift: real-time means event-driven, not cron-driven. Need an event bus (we have Kafka but it's not provisioned for this), a WebSocket fan-out layer for the in-app surface, and push-notification infra (we have FCM for mobile but the rules engine needs to live somewhere queryable in single-digit ms).
- Tomás's estimate: **6 weeks for two engineers** to MVP. Includes the event bus wiring, the WebSocket layer, the rules engine, and a kill-switch so individual customers can opt out if it goes wrong.
- Yuki flagged ops cost: real-time means we own the alerting SLO. If our cron breaks today, customers get the digest tomorrow with apologies. If our real-time alert pipeline breaks, customers miss the thing they're paying for in real time. That's a different on-call posture.
- Diana: "We can build it. The question is whether we want the operational responsibility. That's a product call, not an eng call."

### Open question raised by engineering

- Diana: "Before we scope this further, can you confirm there's actual demand? The Acme finding pointed the opposite direction — they want less, not more. Who's asking for real-time?"
- PM (you): "One inbound request via support that I haven't qualified yet. Will follow up."

### Decision from this meeting

- No decision made. Eng will write a 2-page tech doc for the real-time pipeline by 2026-05-01 so we have it as an option. PM will follow up on the inbound real-time request and run two more interviews before deciding.

---

## PM follow-up notes

- This updates the feasibility risk on the alert-cadence hypothesis. Real-time is *technically feasible* (6 weeks, two engineers) but *operationally expensive* (on-call posture changes). Both factors belong under feasibility.
- Calm-mode default is *also* technically feasible and operationally cheap. That's a separate item — the trade-off isn't symmetric.
- Diana's pushback ("who's asking for real-time?") is the right pressure. Don't scope something heavier on one inbound request and one churn signal.
