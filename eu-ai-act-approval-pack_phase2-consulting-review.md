# EU AI Act Approval Pack – Pieter Albrecht



## Summary table

| Case | Likely category | Why this is my first-pass call | Provider / deployer / vendor | Decision |
|---|---|---|---|---|
| 1 – Leipzig contact centre, "team pulse" | **Prohibited** – Art. 5(1)(f) | The tool infers emotions (frustration, stress, engagement) from biometric data (face, voice) of workers at the workplace. It isn't used for medical or safety purposes. | Vendor = provider; contact centre = deployer. The ban applies to both. | **Deny and redesign** |
| 2 – Logistics recruiting, CV scoring | **High-risk** – Annex III 4(a) | AI is used to filter applications and evaluate candidates for recruitment. | US vendor = provider (needs an EU authorised representative); logistics company = deployer | **Approve with controls**, after redesign of auto-rejection |
| 3 – Berlin language school, "Lena" | **Limited risk / transparency** – Art. 50(1), 50(2) | A chatbot and voice assistant talk directly to people and generate synthetic audio. It gives information only, with no admission, level assessment or evaluation. | Language school = provider *and* deployer of the assistant (it builds and runs it under its own name); LLM company = GPAI model provider | **Approve with controls** (disclosure is mandatory) |
| 4 – CNC predictive maintenance | **Minimal risk** | Advisory failure prediction from machine sensor data. It doesn't control the machines, isn't a safety component and doesn't make decisions about people. | Local software partner = provider (developer); manufacturer = deployer | **Approve** (flag parallel issues) |

**Timing (as of Nov 2026):** the Art. 5 bans have applied since 2 Feb 2025. Art. 50 transparency has applied since 2 Aug 2026. Under the Digital Omnibus on AI (Reg. (EU) 2026/1744), the Annex III high-risk obligations now apply from **2 Dec 2027** instead of 2 Aug 2026.

---

## Case 1 – "Team pulse" in a Leipzig contact centre → Prohibited

**First-pass reasoning.** The system reads facial expressions and tone of voice to infer emotional states of employees. That is an emotion recognition system (Art. 3(39)) used in the workplace, which Art. 5(1)(f) bans. The only exception is for medical or safety reasons. "Spotting people at risk of leaving" and feeding scores into quarterly feedback is HR performance management, not a medical or safety purpose. Saying the team lead has the final word doesn't help, because the ban covers the *use* of the system, whether or not a human reviews the output.

**Architecture as proposed (not lawful):**
- Trigger: a live call begins.
- System behaviour: webcam and audio stream → model scores frustration, stress and engagement per agent.
- Human review point: the team lead reads the dashboard and alerts.
- Output: an "at risk" alert, and scores that go into quarterly reviews.
- Logging: per-agent score history.

**Compliance implications.**
- Fines can reach €35m or 7% of worldwide turnover, for the vendor and the deployer alike.
- Parallel issues:
  - GDPR Art. 9: biometric data.
  - GDPR Art. 88 with § 26 BDSG: employee data.
  - § 87(1) no. 6 BetrVG: the works council has a co-determination right over any technical monitoring system. Launching in Q1 without it is impossible even under labour law.

**Decision: Deny as proposed. Lawful redesign:**
1. Drop all emotion inference from faces, voices or other biometric data.
2. Build an aggregate team-level workload signal instead: call volume, handle time, after-call work, overtime, absence trends per team, with no individual scores. Pair it with voluntary, anonymous pulse surveys and an employee assistance programme.
3. Keep it out of performance reviews. Using AI to monitor and evaluate *individual* workers' performance would itself be high-risk (Annex III 4(b)). If the client wants individual metrics, it needs to go through the high-risk route.
4. Agree a works agreement (Betriebsvereinbarung) with the works council before any pilot.

**Borderline / counter-argument.** The client may argue it's for burnout prevention, which is a health purpose. The Commission's Art. 5 guidelines read the medical/safety exception narrowly (for example, detecting fatigue in pilots or drivers), and general wellbeing monitoring isn't covered. **Legal should verify.**

---

## Case 2 – CV scoring for a logistics company → High-risk

**First-pass reasoning.** Annex III 4(a) explicitly lists AI used "to analyse and filter job applications, and to evaluate candidates." Ranking 300 applicants and only opening the top 20 is exactly that. The Art. 6(3) derogation isn't available because the system profiles natural persons.

**Red flags in the brief:**
- **Auto-rejection of everyone outside the top 20 with no real review.** This is a solely automated decision with significant effect (GDPR Art. 22). It also fails meaningful human oversight (Art. 14), and recruiters "rarely have time" is textbook automation bias.
- **Training on "top performer" profiles from five years of past hires.** This bakes historical bias into the model (gender, age, nationality proxies in warehouse and management roles) and creates AGG discrimination risk.

**Proposed architecture:**
- Trigger: an application is submitted through the portal.
- System behaviour: the vendor tool extracts skills and requirements, matches them only against the *job's* stated requirements (not past-hire profiles), and returns a score plus reasons.
- Human review point: a recruiter reviews every application the tool would reject, or at minimum all candidates above a low cut-off plus a random sample of the rest. No rejection email goes out without a recruiter's action.
- Output: a shortlist and a decision made by the recruiter.
- Logging and disclosure: logs kept for at least 6 months (Art. 26(6)). Applicants are told that AI supports screening (Art. 26(11)) and can get an explanation (Art. 86).

**Obligations:**
- **Provider (US vendor):**
  - risk management and quality management system
  - data governance and bias testing (Art. 10)
  - technical documentation
  - conformity assessment (internal control) and CE marking
  - EU database registration
  - an EU authorised representative (Art. 22)
  - instructions for use
- **Deployer (logistics company):**
  - use the tool according to the instructions for use
  - assign trained, competent overseers (Art. 26(2), Art. 4)
  - check that input data is relevant
  - monitor the system and report incidents
  - inform the works council and staff before use (Art. 26(7))
  - follow the parallel BetrVG § 95 and § 87 procedures
  - run a GDPR DPIA
- **No FRIA needed:** Art. 27 applies to public bodies, providers of public services, and credit and insurance use. A private logistics company isn't covered. A DPIA is still mandatory.
- **Role risk:** if the company rebrands the tool or substantially modifies it, it becomes the provider (Art. 25).

**Decision: Approve with controls.** The client can't launch auto-rejection as designed. It can launch after redesigning the human review step, removing the top-performer training data, getting vendor evidence of conformity (or a credible roadmap to 2 Dec 2027), and agreeing with the works council. These controls are strongly advised now even before the high-risk obligations apply, because GDPR Art. 22 and the AGG already do.

---

## Case 3 – "Lena", multilingual assistant for a Berlin language school → Limited risk / transparency

**First-pass reasoning.** Lena interacts directly with people, so Art. 50(1) requires they're informed they're dealing with AI. She also produces a synthetic voice, so Art. 50(2) requires machine-readable marking of the audio. She isn't high-risk under Annex III 3 because she doesn't decide admission, assess the level a person will receive, evaluate learning or proctor tests.

**Red flag in the brief.** A human name, a "friendly photo" and a natural voice, chosen *because people trust a person more*, are designed to make people forget it's an AI. That works against Art. 50(1). The users are often newly arrived and may be vulnerable, which raises the bar for clear disclosure.

**Proposed architecture:**
- Trigger: a user message on the website or WhatsApp.
- System behaviour: an LLM using retrieval over the course catalogue and FAQs only, answering in 5 languages, with links to booking.
- Human review point: a confidence or topic filter routes complicated questions, and anything about integration-course eligibility, funding or residence, to staff. The ticket and the staff answer are logged.
- Output: an informational answer or a hand-off.
- Disclosure layer:
  - an "I'm an AI assistant" message at the start of every conversation, in the user's language
  - an AI label next to the name
  - a clearly illustrated avatar, not a photo of a real-looking person
  - audio marked by the TTS provider

**Obligations:**
- **School (provider and deployer of the chatbot):**
  - Art. 50(1) disclosure
  - Art. 4 AI literacy for staff
  - keep answers within verified content, so the bot gives no advice on integration-course entitlement (BAMF rules)
- **GPAI / TTS vendor:** Art. 50(2) marking and its GPAI obligations.
- **Parallel issues:**
  - GDPR: WhatsApp/Meta is a processor or joint controller with transfers outside the EU. Questions may reveal residence status or other sensitive data, so minimise it and don't store chats longer than needed.
  - Consumer protection: prices and course dates must be accurate.

**Decision: Approve with controls.** Launch is fine once the disclosure layer is in place and the persona no longer passes as human.

**Borderline.** If Lena starts recommending which level to book, she drifts toward Annex III 3(c) (assessing the appropriate level of education). Keep her at "take our placement test" and link to it.

---

## Case 4 – Predictive maintenance for CNC machines → Minimal risk

**First-pass reasoning.** The system uses machine sensor data to rank failure risk for a planner who can ignore the list. It doesn't match any Art. 5 practice or Annex III area. It isn't a safety component of machinery (Annex I / Art. 6(1)) because it doesn't control or change settings. It doesn't interact with people in a way that triggers Art. 50.

**Proposed architecture:**
- Trigger: a weekly batch job every Monday.
- System behaviour: a model over vibration, temperature, spindle load, running hours and maintenance history produces a 14-day failure probability per machine.
- Human review point: the maintenance planner prioritises and can override the list.
- Output: a ranked list and work orders.
- Logging: predictions vs. actual failures, for model monitoring.

**Obligations:** none specific under the AI Act beyond Art. 4 AI literacy.

**Flag parallel issues:**
- If logs link machine data to *operators or shifts*, it becomes personal data (GDPR) and possibly employee monitoring. That triggers the works council under § 87(1) no. 6 BetrVG.
- Contract with the software partner: data ownership, IP in the model, liability for missed predictions.

**Decision: Approve.**

**Borderline.** If a later version automatically stops machines or changes parameters, re-check whether it has become a safety component. If so, it would be high-risk through the Machinery Regulation (EU) 2023/1230 / Annex I, with that obligation now from 2 Aug 2028.

---

## Notes for the debrief (Phase 5)
- The partner's briefs were presented in category order (1 = prohibited … 4 = minimal), so the position alone hinted at the answer. Suggest shuffling next time.
- Case 1 was the clearest of the four. It names "facial expressions", "tone of voice" and "stress", so the facts point straight at the category even without the label.
- Case 3 had a good trap: the persona built to seem human.
