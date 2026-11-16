# EU AI Act Approval Pack

**Client:** Pieter (four AI proposals) · **Consultant:** Elif Yurdakul · **Question:** "Can we launch this?"

> This pack is a consulting assessment, not legal advice. Points marked ⚖️ should be confirmed by a legal team before launch.

---

## Executive summary

Of your four proposals, **one can launch as planned, two can launch once specific controls are in place, and one cannot launch in its current form.**

| # | Proposal | Category | Decision |
|---|---|---|---|
| 1 | AI voice agent for the energy hotline | Limited risk (transparency) | ✅ Approve with controls |
| 2 | Automated loan decisions | High-risk | ✅ Approve with controls |
| 3 | Agent "wellbeing" monitoring | **Prohibited** | ❌ Deny and redesign |
| 4 | Bakery production forecasting | Minimal risk | ✅ Approve |

**The biggest risks:**
- **Case 3** is banned under Art. 5(1)(f) and has been since February 2025. Fines for prohibited practices reach up to €35 million or 7% of global turnover. A lawful alternative is proposed below.
- **Case 2** is the heaviest workload. High-risk obligations require documentation, testing, human oversight and an impact assessment before launch.
- **Case 1** is easy to launch, but only if you drop the goal that customers "stop noticing it's a bot". The law requires the opposite.

---

## Case 1 · AI voice agent for the energy hotline

**Request:** a human-sounding AI voice agent answers customer calls; customers should stop noticing it's a bot.

**Category: Limited risk (transparency).** The agent talks directly to people and produces synthetic speech, which triggers Art. 50. It answers service questions and doesn't decide on credit or other Annex III areas, so it is not high-risk.

**Architecture:** customer call → speech-to-text → LLM with your FAQ and account knowledge → text-to-speech reply. Handover to a human agent on request, for complaints, or when the AI is unsure. Every call is logged.

**Roles:**
- **Provider:** the voice-AI vendor, who must mark generated audio as AI-made (Art. 50(2))
- **Deployer:** you, who must tell callers they are talking to an AI (Art. 50(1))

**Compliance implications:**
- A clear spoken disclosure at the start of every call, e.g. *"You're speaking with our AI assistant."*
- An easy route to a human
- No design aimed at making people believe they're talking to a person
- Parallel: GDPR for recordings and account data; consumer protection rules on misleading practices

**Decision: ✅ Approve with controls.** The voice agent can launch. The goal of hiding that it's a bot is denied.

---

## Case 2 · Automated loan decisions

**Request:** a model built on open-banking data approves or declines loan applications.

**Category: High-risk.** Assessing the creditworthiness of individuals is listed in Annex III point 5(b). The decision directly affects people's access to credit.

**Architecture:** application submitted → model scores the applicant from transaction and application data → **a credit officer reviews every decline and borderline case** → approve / decline / refer, with the main reasons. Each decision is logged with inputs, score, model version and reviewer.

**Roles:**
- **Provider:** you, if you build the model; otherwise the scoring vendor
- **Deployer:** you
- **Third parties:** possibly a scoring-model vendor and an open-banking data aggregator

**Compliance implications:**
- **As provider:** risk management, data governance and bias testing, technical documentation, logging, human oversight design, accuracy and robustness, conformity assessment, registration in the EU database (Arts. 9–17, 43, 49)
- **As deployer:** trained human oversight, monitoring, keeping logs, a **fundamental rights impact assessment** (Art. 27, explicitly required for credit scoring), informing applicants, and the right to an explanation (Art. 86)
- **Parallel:** GDPR Art. 22 (no fully automated decisions without safeguards); consumer credit rules
- ⚖️ Confirm the current application date for Annex III obligations (2 August 2026 under Art. 113; postponements have been discussed)

**Decision: ✅ Approve with controls.** Not as a fully automatic system: declines need human review, and launch depends on the documentation and impact assessment being complete.

---

## Case 3 · Agent "wellbeing" monitoring

**Request:** detect stress and frustration in contact-centre agents from their voice and webcam, to support wellbeing.

**Category: Prohibited.** The system infers employees' emotions from biometric signals (face, voice) at work. Art. 5(1)(f) bans emotion recognition in the workplace. The only exceptions are medical or safety reasons; "wellbeing" and coaching are neither.

**Architecture as proposed:** webcam + call audio → emotion model → stress and frustration score per agent → dashboard for team leads. **This cannot be deployed**, and showing scores only at team level would not fix it, because the emotions are still inferred from each person's biometric data.

**Roles:** Provider: the tool's vendor · Deployer: you.

**Compliance implications:** the system may not be placed on the market or used. Using it risks the highest fine tier. It would also breach GDPR (biometric data) and, in Germany, require works council co-determination.

**Decision: ❌ Deny and redesign.**

### Lawful alternative: workload-based wellbeing support
Your real goal, noticing overload before people burn out or quit, can be reached without reading anyone's emotions:

| Instead of… | Use… |
|---|---|
| Emotion scores from face and voice | **Workload signals:** call volume, back-to-back calls, average handle time, missed or shortened breaks |
| Individual "at risk" alerts | **Team-level dashboard** for planning breaks and staffing |
| Hidden measurement | **Voluntary, anonymous pulse surveys** (e.g. weekly, 3 questions) |
| AI judging people's feelings | **Team leads** using these signals to start supportive check-ins |

This is minimal risk under the AI Act. Remaining duties: GDPR (purpose limitation, data minimisation, transparency to employees) and works council involvement where one exists.

---

## Case 4 · Bakery production forecasting

**Request:** forecast how much of each product to bake, using sales data and the loyalty app.

**Category: Minimal risk.** The system predicts demand for bread, not anything about people, and isn't in any Annex III area. No specific AI Act obligations apply.

**Architecture:** daily planning run → forecast model on sales history, weather, holidays and **aggregated** loyalty-app data → recommended quantities per product and store → the store or production manager adjusts and approves. Forecast vs. actual sales are tracked.

**Roles:** Provider: the forecasting vendor or your in-house team · Deployer: you.

**Compliance implications:**
- No AI Act duties beyond AI literacy for staff (Art. 4)
- **GDPR is the real issue:** customers joined a loyalty programme, not a forecasting project. Use the data aggregated or pseudonymised, check the legal basis and purpose, update the privacy notice, and don't profile individual customers.

**Decision: ✅ Approve**, once the loyalty-data points are fixed.

---

## Next steps

| Priority | Action | Owner |
|---|---|---|
| 1 | Stop the emotion-recognition tool; scope the workload-based alternative | Client + consultant |
| 2 | Start the high-risk package for loan decisions (documentation, bias tests, impact assessment) ⚖️ | Client + legal + vendor |
| 3 | Write the call disclosure script; confirm the vendor's audio marking | Client + voice-AI vendor |
| 4 | Data protection check on the loyalty data | Client data protection officer |

**First operational artefacts the client needs:** a transparency notice for the voice agent (Case 1) and a fundamental rights impact assessment draft for loan decisions (Case 2).