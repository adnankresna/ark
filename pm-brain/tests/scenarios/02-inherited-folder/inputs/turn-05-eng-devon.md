# Meeting — Devon Park (lead eng), Tally backend

**Date:** 2026-05-12
**Duration:** 60 minutes
**Attendees:** Maya, Devon
**Type:** intro / feasibility recheck

---

## Context

Devon wrote the eng feasibility note in March that's in the inherited folder (social = 6 weeks, shared budgets = 10 weeks, AI insights = 3 weeks). That note is now ~7 weeks old. I wanted to sit with him and see what holds, what's changed, and what he'd actually advise.

---

## Notes from the conversation

### On the March feasibility numbers

Devon stood by them with two caveats:

- **Shared budgets**: he now thinks 10 weeks was optimistic. He's spent more time looking at the user/account data model since Q1 and the migration path is messier than he'd realized. New estimate: 12-14 weeks, and he'd want a 2-week spike before committing.
- **AI insights**: still ~3 weeks for v1. Inference cost is the part that's gotten worse — model pricing has shifted and a naive implementation at our MAU would be expensive. He wants a pricing model defined before they build it.
- **Friend leaderboards**: same as before, ~6 weeks. Devon volunteered: "I will say, since you joined we've had zero new asks for this from CS or sales. Alex wanted it. I'm not sure who else does."

### On the strategy-vs-roadmap tension

I asked him directly: did he know about the Q4 draft Alex had?

> "I knew Alex was thinking that way. He talked to me about it twice. I told him both times that the eng cost of 'all three at once' was unrealistic. He never showed me the draft. I never saw it until the brain pulled it out of his folder yesterday."

I asked which of the three he'd advise, if forced to pick one. His answer:

> "Shared budgets. It's the biggest scope, but it's also the one with the clearest pull from CS. The other two are pushes — leadership wanting them or competitive pressure wanting them. Shared budgets has actual customers asking. And it's the one Monarch is winning on. If we don't do it we keep losing the couples segment to them."

### On the broader retention question

Devon's view: the retention drop isn't a feature problem, it's a positioning problem. "We've been adding things that the Achiever segment likes, in an app where the Achiever segment is a quarter of users and a smaller fraction of revenue. We should either commit to Achievers or stop building for them."

I asked him to stay out of strategy for now and just help me get the engineering story straight. He laughed and said "fair, I'll stick to dates."

---

## Maya's takeaways

- Eng feasibility note from March needs updating: shared budgets is now 12-14 weeks + spike, not 10. AI insights still 3 weeks but pricing-blocked. Leaderboards unchanged but Devon flagged absence of demand signal.
- Devon independently named the same Saver/Achiever tension Jordan's personas doc pointed at, and the same couples-budgeting signal the CS monthly pointed at. That's two independent reads of "Achievers are over-weighted, couples are under-served." Not three independent yet, but moving that way.
- He's an eng lead, not a PM. I should not weight his strategy opinion as much as his feasibility opinion. Worth capturing both, but tagged differently.
- Action: update the feasibility risk on the shared-budgets and AI-insights items.
