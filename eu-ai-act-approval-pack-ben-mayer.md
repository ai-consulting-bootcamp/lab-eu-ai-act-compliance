# EU AI Act Approval Pack - Ben Mayer

**Question from the client:** "Can we launch this?" · **Cases:** partner briefs A–D · **Date:** 26 Nov 2026 · **Not legal advice.** Items marked ⚖️ need confirmation by counsel.

## Executive summary

| Case | Use case | Risk tier | Decision |
|---|---|---|---|
| A | Rail passenger chat widget | Limited (transparency) | **Approve with controls** |
| B | Ranking job applicants | High-risk (Annex III §4(a)) | **Approve with controls** |
| C | Carton demand forecast | Minimal | **Approve** |
| D | Agent voice emotion flags | **Prohibited** (Art 5(1)(f)) | **Deny and redesign** |

Out of four proposals, one can't launch in any form: inferring employee emotions from voice is banned outright. The prohibition has applied since 2 Feb 2025, with penalties enforceable since 2 Aug 2025. One is high-risk and can launch only with provider evidence and real human oversight. Its obligations bite from **2 Dec 2027** after the Digital Omnibus (Reg. (EU) 2026/1744), but they belong in the contract now. One needs only disclosure and safe answer boundaries. One is minimal risk. **Tier depends on what the system does to people, not on the technology:** the same "AI that reads text" is minimal in Case C and high-risk in Case B.

---

## Case A - Rail passenger chat widget · Limited risk · Approve with controls

**Why:** It interacts directly with the public, so Art 50(1) requires people to be told they are talking to AI. It is not a safety component of rail operations (Annex III §2) and it doesn't decide on tickets or compensation.

**Architecture:** passenger question → retrieval from approved timetable and accessibility pages → LLM answers **only** from retrieved text, with a source link → if sources are missing or conflict, it hands over to a human ("contact staff") → weekly staff review of sampled logs.

**Roles:** Operator = **provider** (own brand) **and deployer**. LLM API company = **GPAI model provider** (must supply documentation downstream, Art 53).

**Controls:** visible AI disclosure at first message; machine-readable marking of generated text ⚖️ (Art 50(2), assistive-function exemption unclear); content freshness date on every answer; step-free route answers always link to the source page; GDPR: minimise chat logs (passengers may disclose disabilities), set retention, EU data-processing terms with the API vendor.

**Borderline view:** If the widget starts processing refunds or compensation claims, re-classify it. That's still not Annex III, but consumer law and GDPR Art 22 come in.
**Next artefact:** a transparency notice plus an answer-boundary policy (topics the bot must refuse).

---

## Case B - Applicant ranking · High-risk · Approve with controls

**Why:** Annex III §4(a) explicitly lists AI used to filter applications and evaluate candidates. Ranking is profiling, so the Art 6(3) exemption isn't available. Recruiters start at the top 20, so in practice the rank decides who gets an interview.

**Architecture:** vacancy + applications → vendor model scores CV, availability and forklift certificate against job requirements → shows **job-related reasons** per candidate → qualified candidates shown in **bands**, not a strict 1..n list, so recruiters don't anchor on the top 20 → recruiter invites and logs a reason for each override → the tool never rejects anyone.

**Roles:** Vendor = **provider**. Agency = **deployer**. If the agency rebrands or substantially modifies the tool, it becomes the provider (Art 25).

**Controls:** *Before signing:* the vendor's conformity evidence (see the stretch roadmap). *Before first use:* trained, named overseers; check that input data is relevant (no photos, age or nationality fields); tell applicants a high-risk AI system is used (Art 26(11)); GDPR DPIA. *In operation:* keep logs for 6+ months; monitor override rates and outcome gaps by group; report serious incidents; explain decisions on request (Art 86). *Germany:* works-council co-determination on selection guidelines ⚖️; AGG non-discrimination.

**Borderline view:** The vendor may argue that "the recruiter decides". That doesn't matter: Annex III attaches to the intended purpose, and the human review only counts if it is real (GDPR Art 22).
**Next artefact:** a human-oversight procedure with override logging, plus a vendor due-diligence checklist.

---

## Case C - Carton forecast · Minimal risk · Approve

**Why:** It's internal, uses aggregate data, involves no people, and isn't a listed use. A planner makes every order decision.

**Architecture:** weekly run → forecasting model on carton-size totals, lead times, promotions and holidays → reorder proposal → planner edits and submits via the existing procurement system → forecast vs. actual tracked.

**Roles:** Depot = **provider and deployer** (in-house build). No vendor.

**Controls:** none specific under the AI Act beyond Art 4 AI literacy. Parallel: confirm the data feed stays aggregate (any customer or shipment-level data brings in GDPR); don't make external accuracy claims.

**Borderline view:** A simple statistical forecast may fall outside the Art 3(1) definition of "AI system" altogether ⚖️. Either way, the answer is "approve".

---

## Case D - Agent voice emotion flags · Prohibited · Deny and redesign

**Why:** Art 5(1)(f) bans inferring the emotions of people **in the workplace** from **biometric data**. Pitch, cadence and acoustic features are voice biometrics, and "irritated or anxious" are emotions. The only exceptions are medical or safety purposes, which the brief excludes. A supervisor who can dismiss flags doesn't fix it, because the inference itself is the banned practice. Exposure: fines up to €35m or 7% of global turnover, for **the deployer as well as the vendor**.

**Lawful redesign: "call-quality coaching queue"**
- **Inputs:** call transcript and call metadata only. No acoustic or emotion features.
- **Behaviour:** flag **calls**, not people, using objective signals: unusual duration, holds and transfers, repeat contacts within 7 days, refund or escalation outcomes, missed mandatory disclosures (script check).
- **Human point:** supervisor reviews the flagged call; agents can nominate their own calls for coaching; team-level trends are shown by default.
- **Roles:** vendor = provider; contact centre = deployer. Contract warranty that emotion and voice-biometric features are **disabled**.

**Redesign risk check:** if these flags feed **individual performance evaluation** or discipline, the redesign becomes high-risk under Annex III §4(b), which adds Art 26 duties including informing workers before use (Art 26(7)). Italy also requires a union agreement or labour-inspectorate authorisation for remote monitoring of workers (Workers' Statute Art 4) ⚖️. **Recommended scope:** coaching only, with no use in ratings, so the client can approve the redesign with controls.

**Borderline view:** Inferring emotion from the **transcript** text isn't covered by 5(1)(f), which requires biometric data. It is still emotion inference about employees, though, so I advise against it.

---

## What the client needs next

| Case | Next step | Owner |
|---|---|---|
| A | Disclosure banner, answer boundaries, log-retention policy, then launch | Operator digital team |
| B | Vendor evidence pack, DPIA, oversight SOP, works-council agreement, then pilot | Agency + vendor |
| C | Launch; confirm data feed is aggregate | Depot ops |
| D | Terminate the emotion pilot; scope the redesign; union agreement | Contact centre + vendor |

## What changed after the client discussion?

The client confirmed all four tiers (4/4 match with the answer key). The controls got more specific:
- **A:** Art 50(2) output marking changes from "verify with legal" to a firm launch requirement, and the AI disclosure must appear at the first interaction, clear and accessible (Art 50(5)).
- **B:** "Bands instead of a ranked list" is softened to *ranking inside visible bands*, plus a metric that checks whether recruiters approve the top 20 at a much higher rate than people further down.
- **D:** the client's alternative of analysing emotion in the *customer's* voice was rejected. It avoids Art 5(1)(f) but is high-risk (Annex III §1(c)) and needs Art 50(3) notices. The client signed off on the coaching-only metadata redesign.

Full comparison: [`debrief-and-client-discussion.md`](./debrief-and-client-discussion.md).
