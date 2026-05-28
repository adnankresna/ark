# Bulk import: documented Q4 SSO decision from March 2026

I'm Maya Lindgren, PM at Trellis Studio (B2B SaaS, design-collaboration tool, ~$6M ARR, 1,200 paying teams). Today is **2026-05-18**. Below are three artifacts from **March 2026** that established our documented Q3/Q4 priority call on enterprise SSO. Please ingest faithfully, preserving March 2026 dates — the point is to anchor this decision in the brain so future contradicting signals can be evaluated against it on equal footing.

After ingest, the active hypothesis should be `enterprise-sso-q4` with status `validated` (the decision was made on the strength of this evidence), and there should be a real decision file dated 2026-03-26.

Don't synthesize anything new beyond what's in these three artifacts. Tag everything with March 2026 dates.

---

## Artifact 1 — Customer interview, Quartzline Labs, 2026-03-09

**Interviewee:** Dana Okafor, Head of IT Operations, Quartzline Labs (a 280-seat biotech R&D firm, Trellis customer since 2024, on the $30/seat Team plan).
**Interviewer:** Maya Lindgren (PM)
**Format:** 35-min Zoom, recorded with consent.

**Maya:** Walk me through your SSO situation today.

**Dana:** We provision Trellis through Okta for our 280 designers and PMs. It works for the most part — SCIM keeps things in sync. The friction is that we can't enforce SSO-only login. People who set up accounts before we rolled out SSO can still log in with email + password, and we have no way to force them onto Okta. Our compliance auditor flagged this in our SOC 2 prep last month.

**Maya:** How urgent is closing that gap?

**Dana:** Honestly, it's a compliance hygiene thing, not an outage. We have manual workarounds — we audit weekly and force resets on the holdouts. It's annoying but not blocking. If you shipped enforced-SSO at the end of the year, that'd be fine. If you shipped it tomorrow, I'd celebrate, but I'm not going to threaten to leave over it.

**Maya:** Any timeline that would actually move the needle?

**Dana:** Q4 would be great. Q3 would be a bonus. Beyond Q4 I'd start asking my account manager pointed questions. We're not at "evaluate competitors" yet — Trellis is too embedded in the design workflow.

**Maya:** Would you pay more for enforced SSO as part of an Enterprise tier?

**Dana:** We're already discussing Enterprise. If enforced SSO is gated behind it, I won't fight that internally. We'd pay the upgrade — call it another $15-20/seat. The compliance team would sign off.

---

## Artifact 2 — Engineering scoping note, 2026-03-17

**Author:** Henrik Vasquez, Eng Lead, Platform
**Re:** Enforced SSO / SCIM hardening — scoping for Q3 vs Q4

Spent two days looking at the SSO enforcement work end-to-end. Summary:

- **Enforced-SSO toggle (org-level):** ~3 weeks. Straightforward — gate the password-login endpoint behind a per-org flag, force-migrate password users through a one-time SSO bind on next login. Tested pattern, we already have the org-level flag infrastructure.
- **SCIM hardening:** ~2 weeks. Today's SCIM implementation drifts on edge cases (deactivated-then-rehired users, group nesting). Tightening this is independent work but pairs naturally with the enforcement story.
- **Audit log expansion:** ~3 weeks. SOC 2 auditors want immutable audit logs for auth events. We have logs; they're not immutable. This is a real chunk of work.
- **Identity-provider expansion:** Today we support Okta + Google. Adding Azure AD is ~4 weeks; adding Ping is ~3 weeks. Roughly half our enterprise pipeline is on Azure AD.

Total: **~8 weeks Q3-scoped (enforcement + SCIM hardening + Azure AD)** or **~14 weeks if we also do audit logs + Ping**.

The harder question is sequencing. Q3 is already committed to the realtime-cursors GA work (4 engs, 11 weeks) and the export-API rebuild (2 engs, 8 weeks). We don't have spare capacity for an 8-week SSO push in Q3 without pulling someone off realtime-cursors. **My recommendation: Q4.** We finish realtime-cursors clean, then take Q4 for the full Enterprise hardening pass (SSO + SCIM + audit + Azure AD + Ping). That's a 14-week Q4 with the whole platform team — coherent and shippable as an "Enterprise tier" launch.

---

## Artifact 3 — Decision record, 2026-03-26

**Decision:** Defer enforced-SSO + Enterprise hardening to **Q4 2026**. Q3 stays focused on realtime-cursors GA and the export-API rebuild.
**Driver:** Maya Lindgren (PM). Approved by Naveen Acharya (CEO), Henrik Vasquez (Eng Lead).
**Status:** decided (2026-03-26).

**Why:**
- Documented customer signal (Quartzline interview, 2026-03-09): Q4 is acceptable; competitive risk is low; customer is willing to pay for Enterprise tier inclusion.
- Eng feasibility & sequencing (Henrik's note, 2026-03-17): Q3 is fully booked; doing SSO in Q3 means pulling from realtime-cursors, which has higher revenue impact.
- CS quarterly review (2026-02-28): SSO appears as a "watch item" in 3 of 47 enterprise-pipeline accounts but is a hard blocker in zero. Realtime-cursors appears as a hard blocker in 7.
- Sales pipeline (Q1 close-loss review): zero deals lost in Q1 with "missing enforced SSO" as the cited reason. Two deals lost over "realtime collaboration latency."

**What we'd ship in Q4:**
- Enforced SSO + SCIM hardening + audit log expansion + Azure AD support + Ping support, packaged as the "Enterprise tier launch."
- Pricing: Enterprise tier at +$15-20/seat over Team (Dana's WTP signal).

**Reversal conditions** (what would move this earlier than Q4):
- Three or more confirmed lost or stalled deals in any single quarter cite "missing enforced SSO" as the primary blocker, with documented sales-call notes. (Note: must be primary blocker, not a wish-list line item.)
- A SOC 2 or SOX customer issues a formal cure-period notice over auth posture.
- Realtime-cursors GA slips its Q3 milestone by more than 4 weeks, freeing platform engineering capacity earlier than expected.

**Explicitly NOT doing in Q3:**
- Any SSO work, including "small" hardening tickets. Q3 platform capacity is fully booked.
- Repricing the Enterprise tier; we hold the +$15-20/seat target until launch.

---

That's the March state. Please ingest all three faithfully, preserve them under `source/` with March 2026 dates, create the `enterprise-sso-q4` hypothesis file (status `validated`), create the `2026-03-26` decision file, and confirm `decisions/INDEX.md` lists the new row. Don't do anything beyond ingesting and routing.
