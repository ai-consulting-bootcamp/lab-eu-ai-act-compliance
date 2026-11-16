# Lab Proof: Classify your product (EU AI Act)

**Author:** Elif Yurdakul

## Phase 1: Hidden client briefs

Four client use cases written like discovery calls. The intended category for each case is hidden in the private answer key at the end of this file (click to reveal after the partner review).

### Case 1
We run a customer-service centre for an energy provider in Leipzig, about 180 agents across three shifts. Sick days and turnover went up a lot last year, and team leads only notice someone is struggling when they hand in their notice. A vendor showed us a "team pulse" tool: it uses the agents' webcams and call audio to read facial expressions and tone of voice, and gives each agent a live score for frustration, stress and engagement. Team leads see a dashboard and get an alert when someone looks "at risk", so they can step in with coaching. The scores would also feed into the quarterly feedback talks, but the team lead always has the final word. Our works council hasn't seen it yet. We'd like to roll it out in Q1.

### Case 2
We're a logistics company with warehouses in Germany and Poland, and we hire around 400 people a year, from forklift drivers to shift managers. Our two recruiters get up to 300 applications per role and can't read them all. We want an AI tool that reads the CVs and cover letters, compares them with the job description and our "top performer" profiles from the last five years, and gives every applicant a score. Recruiters would only open the top 20; everyone else gets an automatic "thank you, but no" email after a week. The recruiters can still pull someone up manually if they want to, though honestly they rarely have time. We'd buy the tool from a US vendor and connect it to our applicant portal.

### Case 3
We're a language school in Berlin teaching German to around 1,200 adults a year, many of them newly arrived. Our front desk spends most of the day answering the same questions: prices, course dates, which level to book, what the integration course is. We want an assistant on our website and WhatsApp that answers these questions in German, English, Arabic, Turkish and Ukrainian, any time of day. We'd call her "Lena", give her a friendly photo and a natural-sounding voice for voice messages, because people trust a person more. Lena only gives information and links to the booking page; she doesn't enrol anyone or decide levels. If a question is complicated, she passes it to our staff the next working day. It would be built on a large language model with our course catalogue and FAQs.

### Case 4
We manufacture precision parts for the automotive industry, with 60 CNC machines in two halls in Baden-Württemberg. Unplanned breakdowns stop a line for hours and cost us a lot, and our maintenance is still based on fixed intervals. We want a system that uses the machines' sensor data (vibration, temperature, spindle load, running hours) and our maintenance history to predict which machine is likely to fail in the next two weeks. Every Monday the maintenance planner gets a ranked list and decides which machines to service first; he can ignore the list. The system doesn't control the machines or change any settings. A local software partner would build it on our existing data platform.

---

## Phase 2: Consulting review of my partner's cases

*Partner:* Pieter

**Partner's client briefs (as received):**
- **Case 1:** An energy supplier wants a human-sounding AI voice agent on its phone line, and wants customers to stop noticing it's a bot.
- **Case 2:** An online lender wants to approve or decline loans with a model built on open-banking data.
- **Case 3:** A contact centre wants to detect stress and frustration in its agents from their voice and webcam, framed as "wellbeing".
- **Case 4:** A bakery chain wants to forecast how much to bake, using data that includes its loyalty app.

| Case | Likely category | Why this is my first-pass call | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|---|---|
| 1 · Energy voice agent | **Limited risk / transparency** | The system talks directly to customers and generates synthetic speech, which triggers Art. 50. It gives service information and doesn't decide on credit, benefits or access to essential services, so it isn't Annex III. The client's wish that customers "stop noticing it's a bot" conflicts directly with the disclosure duty. | Trigger: customer calls the service line<br>System behaviour: speech-to-text → LLM with FAQ/account knowledge → text-to-speech reply<br>Human review: handover to a human agent on request, for complaints, or when the AI is unsure<br>Output: spoken answers, routing, ticket<br>Logging/disclosure: spoken AI disclosure at the start of every call; machine-readable marking of generated audio; call logs | Provider: voice-AI vendor (marking of synthetic audio, Art. 50(2))<br>Deployer: the energy supplier (informing callers, Art. 50(1))<br>Vendor: the same voice-AI company, possibly also an LLM provider underneath | Clear disclosure at the start of each call ("You are speaking with an AI assistant"); generated audio marked as synthetic; easy route to a human; no design meant to make people believe it's human. Parallel: GDPR for call recordings and account data; consumer protection (no misleading practices). | **Approve with controls.** The goal of hiding that it's a bot must be dropped; that part is denied. |
| 2 · Online lender | **High-risk** | Deciding whether individuals get a loan is creditworthiness assessment, listed in Annex III point 5(b). The model makes approve/decline decisions that directly affect people's access to credit. | Trigger: loan application submitted<br>System behaviour: model scores the applicant from open-banking transaction data and application data<br>Human review: a credit officer reviews every decline and borderline case before the decision is sent<br>Output: approve / decline / refer, with the main reasons<br>Logging/disclosure: every decision logged with inputs, score, model version and reviewer; explanation available to the applicant | Provider: the lender if it builds the model itself, otherwise the model vendor<br>Deployer: the lender<br>Vendor: possibly a scoring-model vendor and the open-banking data aggregator | Provider: risk management, data governance and bias testing, technical documentation, logging, human oversight design, accuracy and robustness, conformity assessment, registration in the EU database (Arts. 9–17, 43, 49).<br>Deployer: use as instructed, trained human oversight, monitoring, keeping logs, **fundamental rights impact assessment** (Art. 27, required for credit scoring), informing applicants, right to explanation (Art. 86).<br>Parallel: GDPR Art. 22 (no fully automated decisions without safeguards), consumer credit rules. | **Approve with controls.** Not as a fully automatic decline system: declines need human review, and launch depends on the documentation and FRIA being in place. |
| 3 · Contact-centre "wellbeing" | **Prohibited** | The system infers employees' emotions (stress, frustration) from their voice and face. Emotion recognition in the workplace is banned under Art. 5(1)(f). The "wellbeing" framing doesn't make it a medical or safety use, so the exception doesn't apply. | As proposed: webcam + call audio → emotion model → stress/frustration scores per agent → dashboard for team leads.<br>**Redesign (lawful alternative):** workload signals only (call volume, average handle time, back-to-back calls, missed breaks), shown at team level, plus voluntary anonymous pulse surveys; team leads plan breaks and check-ins. No biometric data, no emotion inference. | Provider: the vendor of the emotion tool<br>Deployer: the contact centre<br>Vendor: same vendor; for the redesign, the existing workforce-management system | As proposed: may not be used (prohibition applies since 2 Feb 2025).<br>Redesign: GDPR (employee data, purpose limitation, data minimisation), works council involvement where it exists, transparency to employees about what is measured. | **Deny and redesign.** Replace emotion recognition with workload-based signals and voluntary surveys. |
| 4 · Bakery forecasting | **Minimal risk** | It predicts how much to bake from sales patterns. It doesn't make decisions about people and isn't in any Annex III area, so no specific AI Act obligations apply. The open question is the loyalty-app data. | Trigger: daily or weekly planning run<br>System behaviour: forecast model on sales history, weather, holidays and aggregated loyalty-app purchase data<br>Human review: the store or production manager adjusts and approves the baking plan<br>Output: recommended quantities per product and store<br>Logging/disclosure: forecast vs. actual sales tracked to monitor accuracy | Provider: forecasting-software vendor or in-house team<br>Deployer: the bakery chain<br>Vendor: possibly a forecasting SaaS vendor | No specific AI Act duties (AI literacy for staff under Art. 4 still applies).<br>Parallel: **GDPR**: use loyalty data aggregated or pseudonymised, check legal basis and purpose limitation (customers agreed to a loyalty programme, not necessarily to forecasting), update the privacy notice, no individual profiling. | **Approve**, with the GDPR points on loyalty data fixed first. |

*Decision options:* Approve · Approve with controls · Deny and redesign

---

## Phase 3: Approval pack

The approval pack (3 pages max) is in [approval_pack.md](approval_pack.md).

---

## Phase 4: Client discussion and sign-off

| Case | Intended category (Pieter) | My category | Match? | Client response (accept / challenge / redesign) |
|---|---|---|---|---|
| 1 · Energy voice agent | Limited risk / transparency (Art. 50) | Limited risk / transparency | ✅ | [accept / challenge / redesign] |
| 2 · Online lender | High-risk (Annex III 5(b)) | High-risk | ✅ | [accept / challenge / redesign] |
| 3 · Contact-centre "wellbeing" | Prohibited (Art. 5(1)(f)) | Prohibited | ✅ | [accept / challenge / redesign] |
| 4 · Bakery forecasting | Minimal risk (+ GDPR) | Minimal risk | ✅ | [accept / challenge / redesign] |

**Result:** 4 of 4 categories match. Each case also contained the trap Pieter intended, and the review caught it: the "customers should stop noticing it's a bot" wish in case 1, the "wellbeing" framing in case 3, and the loyalty-app data in case 4.

**What changed after the client discussion?**
[Fill in after talking with Pieter. Points to raise:]
- Case 1: does the client accept dropping the "hide that it's a bot" goal? If not, the decision becomes deny and redesign for that feature.
- Case 2: is the lender building the model itself (provider + deployer) or buying it (deployer only)? This changes who carries the provider obligations.
- Case 3: is the workload-based alternative enough for the client's real goal (reducing burnout and turnover)?
- Case 4: is loyalty-app data needed at all, or do aggregated sales give similar accuracy?

**Failure or limitation I hit:**
- **The briefs were not hidden.** Pieter's file named the category and article for each case ("Art. 50", "Annex III 5(b)", "banned under Art. 5(1)(f)"). My first-pass classification was therefore not blind, and the 4/4 match does not prove I would have found the categories from the facts alone. A fairer test would use unlabelled briefs.
- **The briefs were very short** (one or two sentences). They lacked details I needed for the architecture, such as who builds the lending model and whether the voice agent can change contracts, so I had to make assumptions and flag them.
- **Pieter's case 3 is almost identical to my case 1** (contact centre, voice and webcam, "wellbeing"). It shows how typical this trap is, but it also means our exchange tested one category less than it could have.

---

## Reinforce

**One borderline argument per case:**
| Case | Borderline argument | Where legal should verify ⚖️ |
|---|---|---| s
| 1 | If the agent could change tariffs, arrange payment plans or decide disconnections, it would make decisions about essential services, not just answer questions. | Scope of actions the agent may take |
| 2 | Fraud detection is excluded from Annex III 5(b); if part of the model only detects fraud, that part may be outside high-risk. | Split between credit scoring and fraud detection |
| 3 | The exception for medical or safety reasons (e.g. fatigue detection for safety-critical work) does not cover coaching or performance, but a client may argue it. | Whether any safety purpose exists |
| 4 | If forecasts were used to set staff schedules or judge individual employees, it could move toward employment (Annex III 4). | Whether outputs are used for staff decisions |

**Next operational artefacts the client needs:** a transparency notice and call script for the voice agent (case 1), and a FRIA draft for the loan model (case 2).

---

## Stretch: implementation roadmap for the high-risk case (Case 2, loan decisions)

**Provider before market placement:** risk management process covering wrong declines and bias (Art. 9) · data governance with bias testing across age, gender and nationality groups (Art. 10) · technical documentation in Annex IV format (Art. 11) · automatic logging of every decision (Art. 12) · instructions for use for credit officers (Art. 13) · human oversight built in: no decline without officer review (Art. 14) · accuracy and robustness testing (Art. 15) · quality management system (Art. 17) · conformity assessment, EU declaration and CE marking, registration in the EU database (Arts. 43, 47–49) · post-market monitoring plan (Art. 72).

**Deployer before first use:** fundamental rights impact assessment (Art. 27) · trained credit officers with authority to override (Art. 26) · keep logs for at least six months · inform applicants that AI is used and offer an explanation of decisions (Art. 86) · GDPR Art. 22 safeguards.

**Evidence to request from the vendor (if the model is bought):** technical documentation and instructions for use · EU declaration of conformity and registration number · bias and accuracy test results on comparable populations · data sources used for training (including open-banking data handling) · logging capabilities and how overrides are recorded.

---

## File map
| File | Contents |
|---|---|
| `lab_proof.md` | Entry point: my four hidden briefs, review of Pieter's cases, sign-off, reinforce, stretch, my answer key |
| `approval_pack.md` | Phase 3: approval pack for Pieter's four cases (3 pages max) |

---

## Private answer key

<details>
<summary><b>Spoiler: click to reveal only after the partner has classified all four cases</b></summary>

| Case | Client brief | Intended category | Why I chose it |
|---|---|---|---|
| 1 | Customer-service centre, "team pulse" via webcam and voice | **Prohibited** | The system infers employees' emotions (frustration, stress, engagement) from face and voice in the workplace; Art. 5(1)(f) bans emotion recognition at work, and "wellbeing" is not the medical or safety exception. |
| 2 | Logistics company, AI ranks applicants, recruiters see only the top 20 | **High-risk** | Filtering and ranking job applicants is an Annex III point 4(a) employment use, and in practice the ranking decides who a human ever looks at. |
| 3 | Language school assistant "Lena" with a human-like voice | **Limited risk / transparency** | It interacts directly with people and gives information only (no decisions about access or grading), so the main duty is Art. 50(1): people must know they are talking to an AI. |
| 4 | Manufacturer forecasting machine maintenance | **Minimal risk** | It predicts machine wear from sensor data; it does not decide about people, is not a safety component, and a planner makes the final call, so no specific AI Act obligations apply. |

**Borderline notes (for the debrief):**
- **Case 1:** the "wellbeing" framing may tempt a reviewer toward the medical/safety exception. It doesn't apply: the purpose is performance and coaching.
- **Case 2:** "a human reviews the shortlist" may tempt a reviewer to say "not high-risk". Human review doesn't change the Annex III category, only how the obligations are met.
- **Case 3:** the human-like voice and persona are the transparency trigger. If Lena ever placed students into levels that decide course access, it could move toward Annex III education.
- **Case 4:** if the forecasts were used to judge individual technicians' performance, it would move into employment territory.

</details>