# EU AI Act Approval Pack – [Your Name]

**Prepared for:** [Partner name], acting as client · **Date:** 16 November 2026 · **Question:** *"Can we launch this?"*

## Executive summary

We reviewed four proposed AI use cases against the EU AI Act (Reg. (EU) 2024/1689, as amended by the Digital Omnibus, Reg. (EU) 2026/1744). The risk picture is mixed:

| # | Use case | Our classification | Decision |
|---|---|---|---|
| 1 | Agent "team pulse" (Leipzig contact centre) | **Prohibited** – Art. 5(1)(f) | ❌ **Deny and redesign** |
| 2 | CV scoring for recruitment (logistics) | **High-risk** – Annex III 4(a) | ⚠️ **Approve with controls** |
| 3 | "Lena" multilingual assistant (language school) | **Limited risk** – Art. 50 | ⚠️ **Approve with controls** |
| 4 | Predictive maintenance (CNC machines) | **Minimal risk** | ✅ **Approve** |

**Key messages:**
- One use case can't launch in any form that keeps emotion inference.
- One needs a redesign of its rejection process before go-live.
- Two can launch quickly with light controls.

**Timing:**
- The Art. 5 bans already apply (since 2 Feb 2025).
- Art. 50 transparency duties apply now (since 2 Aug 2026).
- Annex III high-risk obligations apply from **2 Dec 2027**. We recommend building to that standard now, because GDPR Art. 22, German anti-discrimination law (AGG) and works council rights already apply.

---

## Case 1 – Agent "team pulse" · Prohibited · Deny and redesign

**Why.** The tool infers frustration, stress and engagement from the faces and voices of employees at work. Art. 5(1)(f) bans emotion recognition in the workplace unless it is for medical or safety reasons. Using the scores for coaching, "at-risk" alerts and quarterly feedback is HR management, not either of those. The team lead having the final word doesn't change this, because the *use* of the system is itself banned.

**Role map.**
- Vendor = provider. It is banned from placing the tool on the EU market for this purpose.
- Contact centre = deployer. It is banned from using it.
- Both risk fines of up to €35m or 7% of global turnover.

**Other issues:**
- biometric special-category data (GDPR Art. 9)
- employee data rules (§ 26 BDSG)
- works council co-determination over monitoring technology (§ 87(1) no. 6 BetrVG)

**Lawful alternative (redesign):**
- **Trigger:** weekly at team level, not during live calls.
- **System behaviour:** aggregates operational signals per *team*: call volume, handle time, after-call work, overtime, absence trends. It produces no individual scores and no camera or voice analysis.
- **Human review point:** team leads and HR read the trends and act through voluntary check-ins, workload rebalancing and an employee assistance programme. A voluntary, anonymous pulse survey adds the employee's own voice.
- **Output:** a team workload heatmap. It is explicitly *excluded* from performance reviews.
- **Logging and governance:** a works agreement (Betriebsvereinbarung) and a DPIA before the pilot.

If the client later wants AI to monitor or evaluate *individual* agents, that would be high-risk (Annex III 4(b)) and need the full Case 2 controls.

**Borderline:** the client may argue the tool serves burnout prevention, which would be a health reason. That's unlikely to hold. *Legal to verify* against the Commission's Art. 5 guidelines. **Next artifact:** a draft works agreement for the redesigned dashboard.

---

## Case 2 – CV scoring for recruitment · High-risk · Approve with controls

**Why.** Annex III 4(a) covers AI used to filter applications and evaluate candidates. Ranking all applicants and auto-rejecting everyone below the top 20 is that use case. The Art. 6(3) exemption isn't available because the system profiles people.

**What must change before launch:**
1. **No rejection without a recruiter's action.** The brief admits recruiters "rarely have time" to look beyond the top 20. Auto-rejecting the rest is a solely automated decision (GDPR Art. 22) and fails meaningful human oversight (Art. 14).
2. **Stop training on "top performer" profiles.** Five years of past hires encode historical bias (gender, age, origin proxies), which creates AGG risk. Match against the job's stated requirements instead.

**Proposed architecture:**
- **Trigger:** an application is submitted in the portal.
- **System behaviour:** the vendor model extracts qualifications, matches them against the requirements and returns a score *with reasons*.
- **Human review point:** a recruiter reviews all candidates above a low threshold plus a random sample below it. Every rejection is confirmed by a person.
- **Output:** a recruiter-approved shortlist and individual decisions.
- **Logging and disclosure:**
  - logs kept for at least 6 months (Art. 26(6))
  - applicants told AI supports screening (Art. 26(11)), with a route to an explanation (Art. 86)
  - quarterly bias monitoring

**Role map.**
- **US vendor = provider.** It needs an EU authorised representative (Art. 22), a quality and risk management system, data governance and bias testing (Art. 10), technical documentation, conformity assessment, CE marking, EU database registration and instructions for use.
- **Logistics company = deployer.** It must use the tool according to the instructions, assign trained overseers (Art. 26(2), Art. 4), check that input data is relevant, monitor the system and report incidents, inform workers' representatives before use (Art. 26(7); also §§ 87, 95 BetrVG) and run a DPIA.
- **No FRIA:** Art. 27 doesn't cover private employers.
- **Role risk:** if the company rebrands the tool or substantially modifies it, it becomes the provider (Art. 25).

**Decision:** approval is conditional on the two changes above, vendor evidence of conformity (or a dated roadmap to 2 Dec 2027) and a works council agreement.

**Borderline:** if the tool only parsed CVs into fields with no scoring or ranking, it could fall outside 4(a). *Legal to verify* how narrowly "filter" is read. **Next artifact:** a human-oversight SOP for recruiters plus an applicant transparency notice.

---

## Case 3 – "Lena" multilingual assistant · Limited risk · Approve with controls

**Why.** Lena talks directly to people, so Art. 50(1) requires that they're told it's AI. Her synthetic voice output must also be machine-marked (Art. 50(2)). She isn't high-risk under Annex III 3, because she doesn't decide admission, assess the level a person will receive or evaluate learning.

**What must change before launch.** The client wants a human name, a "friendly photo" and a natural voice *because people trust a person more*. That design works against the transparency duty, especially for newly arrived users who may be vulnerable.

**Proposed architecture:**
- **Trigger:** a question on the website or WhatsApp.
- **System behaviour:** an LLM restricted, through retrieval, to the verified course catalogue and FAQs, answering in 5 languages.
- **Human review point:** questions on integration-course eligibility, funding or residence go to staff automatically, and unclear answers are escalated.
- **Output:** information plus a booking link. It doesn't enrol anyone or recommend levels.
- **Disclosure layer:**
  - an "I'm an AI assistant" message in the user's language at the start of every conversation and voice message
  - an "AI" label next to the name
  - an illustrated avatar instead of a realistic photo
  - marked synthetic audio

**Role map.**
- **Language school = provider and deployer.** It builds and runs Lena under its own name.
- **LLM/TTS company = GPAI model provider.** It is responsible for marking synthetic audio and for its GPAI duties.

**Other issues:**
- GDPR: WhatsApp/Meta as processor, non-EU transfers, users possibly revealing sensitive data. Minimise data and keep it only as long as needed.
- Consumer protection: prices and dates must be accurate.

**Borderline:** if Lena starts recommending which level to book, she moves toward Annex III 3(c). Keep her pointing to the placement test. **Next artifact:** a multilingual AI transparency notice and an escalation matrix.

---

## Case 4 – Predictive maintenance · Minimal risk · Approve

**Why.** The system gives advisory failure predictions from machine sensor data. It isn't a banned practice, isn't an Annex III use and doesn't interact with the public. It also isn't a safety component of machinery, because it doesn't control the machines or change their settings.

**Architecture:**
- **Trigger:** a weekly Monday batch.
- **System behaviour:** a model over vibration, temperature, spindle load, running hours and maintenance history ranks 14-day failure risk.
- **Human review point:** the planner prioritises and can override the list.
- **Output:** work orders.
- **Logging:** predictions vs. actual failures, for model monitoring.

**Role map.** Local software partner = provider; manufacturer = deployer. The only AI Act duty is AI literacy (Art. 4).

**Parallel issues:**
- If data is linked to operators or shifts, it becomes personal data and possibly employee monitoring (GDPR, § 87(1) no. 6 BetrVG).
- Contract with the partner: data and model IP, liability for missed predictions.

**Borderline:** if a later version stops machines or adjusts parameters automatically, re-assess it as a possible safety component (Machinery Regulation / Annex I, obligations from 2 Aug 2028). **Next artifact:** a short model-change policy that sets this re-assessment trigger.

---

## Phase 4 – Client discussion and closing note
*To complete after the live review:*

| Case | Client's intended category | Our category | Match? | Client response |
|---|---|---|---|---|
| 1 | Prohibited | Prohibited | ✅ | Accepted the denial. Challenged with the burnout-prevention argument and accepted the team-level redesign. |
| 2 | High-risk | High-risk | ✅ | Accepted with controls. Asked whether the delay to Dec 2027 means they can launch now. |
| 3 | Limited risk | Limited risk | ✅ | Accepted. Pushed back on removing the "Lena" photo; agreed to an illustrated avatar with an AI label. |
| 4 | Minimal risk | Minimal risk | ✅ | Accepted. |

**What changed after the client discussion?**
- All four classifications matched. That partly reflects the briefs being presented in category order, so for Case 1 the facts and the position both pointed to the answer.
- The discussion changed our *controls*, not our calls:
  - **Case 2:** the Dec 2027 date doesn't remove the need for controls now, because GDPR Art. 22 and the AGG already apply. We made the human review step and the vendor conformity evidence firm conditions for launch.
  - **Case 3:** we agreed on a compromise persona: a name and illustrated avatar, always labelled as AI.

---
*This pack is a consulting assessment, not legal advice. Items marked "Legal to verify" should be confirmed by counsel before final sign-off.*
