# Customer interview — Sam Chen, MidCo, 2026-05-06

I just got off a discovery call. Please ingest. Source under `source/interviews/`, synthesis under `ingestion/interviews/`, and update insights/observations as appropriate. Don't force this person into either of our existing personas if she doesn't fit — I want the signal preserved as-is so we can look at it again next week.

**Interviewee:** Sam Chen, Hiring Operations Coordinator at MidCo (~600 headcount, B2B fintech).
**Interviewer:** Dana Liu (PM).
**Format:** 35-min Zoom, recorded with consent. MidCo has been on HireFlow for ~9 months.

---

**Dana:** Walk me through a normal day for you. What does your work actually look like?

**Sam:** Calendars. So many calendars. I'm not a recruiter — I don't source candidates and I don't write the JDs. I'm not a hiring manager — I'm not making the hire/no-hire call. I sit between them. When a recruiter says "we want to interview these four people next week," that lands on me. I have to find a panel of three or four interviewers per candidate, get them on the calendar, send the prep materials, send the candidate the Zoom link and the parking instructions and the dietary thing if it's on-site, follow up with the panel afterwards to remind them to submit scorecards, and re-schedule when someone drops.

**Dana:** How many candidates a week are you scheduling for?

**Sam:** Right now? About 25-30 active loops at any time, spread across maybe 14 open reqs. So I'm doing 50-80 individual interview blocks per week.

**Dana:** What does HireFlow do for you in that workflow?

**Sam:** Honestly, not much. I live in Google Calendar and Slack. HireFlow is where the candidate record sits, so I open it to check who the recruiter assigned, what stage they're in, and which interviewers got assigned. But the scheduling itself happens outside HireFlow. We use GoodTime for the actual calendar work — it's not great either, but at least it tries.

**Dana:** What would good look like for you?

**Sam:** A few things. First, when a recruiter moves a candidate to "schedule onsite," HireFlow should kick off the loop creation in the scheduling tool, with the right interviewer panel pre-suggested based on the req's interviewer pool. Right now the recruiter Slacks me, I open HireFlow to look up the panel, I copy names into GoodTime, I send invites manually. Second — interviewers don't keep their HireFlow availability up to date because they never go into HireFlow. Their Google Calendar is the truth. I need that to be the source of truth for scheduling, not a separate availability that the recruiter set six weeks ago.

**Dana:** Who else at MidCo does what you do?

**Sam:** There are two of us. I cover engineering and product reqs, Theo covers GTM and ops. We don't report to the recruiting lead — we report to the COO's chief of staff. It's an ops function, not a recruiting function.

**Dana:** When you talk to peers at other companies — same role at other places — does it look similar?

**Sam:** Yeah, mostly. Sometimes it's a junior recruiter who's been ratholed into scheduling, which is bad for them and bad for the company because they want to do real recruiting. Sometimes it's an EA who got handed it. The companies that take it seriously — 500 people and up — make it a real role. I think at 200 you have one of us, by 600 you have two or three, by 2000 you have a team of six.

**Dana:** What about the hire/no-hire decisions — do you ever weigh in?

**Sam:** No. That's not my job and I don't want it to be. I want the scheduling to work and the prep materials to be on time. If the candidate ghosts or the panel falls apart, that's on me. If we hire the wrong person, that's not on me.

**Dana:** Last thing — if HireFlow were dramatically better for you, would MidCo pay more for it?

**Sam:** Talk to the COO's chief of staff, not me. I'd advocate internally though. We currently pay for HireFlow, GoodTime, Gem, Greenhouse — there's room to consolidate if HireFlow actually did the scheduling layer.

---

**My internal note for ingestion:** I want to be careful here. Sam's role doesn't fit Recruiter (she doesn't source, doesn't screen, doesn't own candidate experience) and doesn't fit Hiring Manager (she's not making the hire/no-hire call and she's not a line manager). She explicitly says "I'm not a recruiter and I'm not a hiring manager." When ingesting, please **don't try to file her under either existing persona** — tag the signal honestly. If she fits a third pattern we haven't named, route to observations or insights and flag it; don't create a new persona file from a single interview. I want to see if this recurs.

When you tag claims from this interview in any synthesis, use the canonical provenance tags — `[source/interviews/...]` is fine for direct citation; if you write an `ingestion/` synthesis file, link from there.
