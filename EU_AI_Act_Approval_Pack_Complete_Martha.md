# EU AI Act Approval Pack - Martha Olukayode

**Lab:** Classify Your Product  

## Phase 1 — Private answer key

### Case 1 - Prohibited

**Client use case — Employee Performance Insights**

A multinational customer-service company wants to improve employee productivity and reduce staff turnover. Management proposes an AI system that analyses employees' facial expressions, voice patterns and behaviour during video meetings and customer calls. The system would estimate employees' emotional states, including frustration, anxiety and enthusiasm. Managers would receive individual dashboards and use the results when planning performance reviews and staff development. Employees would be informed that the system is in use, but participation would be mandatory. Managers would make the final employment decisions.

**Why this category:** The proposed system infers emotions in the workplace for performance management, which falls within the EU AI Act's prohibition on workplace emotion inference, subject to narrow medical or safety exceptions.

### Case 2 - High-risk

**Client use case — Recruitment Shortlisting Assistant**

A regional healthcare provider receives hundreds of applications for nursing and administrative vacancies. Its HR team wants an AI system to analyse CVs, compare qualifications with job requirements and rank applicants for interview invitations. The system would use applicants' CVs, work history and the advertised job criteria. Recruiters would review the ranked list, but only the highest-scoring applicants would normally be considered. Candidates would be affected by whether they progress to an interview. The HR manager would retain authority to change the shortlist.

**Why this category:** AI used to analyse, filter or evaluate job applications in recruitment is generally a high-risk employment use under Annex III of the EU AI Act.

### Case 3 - Limited risk / transparency

**Client use case — Website Customer Support Assistant**

An online home-appliance retailer wants to provide customer support outside normal business hours. It proposes an AI chatbot that answers product questions, explains delivery options and guides customers through return procedures. The assistant would use the company's product catalogue, help-centre articles and customer questions. Customers would interact directly with the assistant on the website and could request a human support agent. The retailer wants the chat interface to resemble a normal customer-service conversation. Staff would review escalated complaints rather than every routine response.

**Why this category:** The system directly interacts with people, so the company must consider the AI Act's transparency requirement to make users aware that they are interacting with AI, unless that is obvious from the circumstances.

### Case 4 - Minimal risk

**Client use case — Internal Meeting Notes Organiser**

A small consultancy wants to reduce the time employees spend organising non-confidential internal meeting notes. It proposes an AI tool that turns staff-written notes into topic headings, action-item lists and draft follow-up summaries. Employees would paste notes into an approved internal workspace and check the output before saving or sharing it. The tool would not evaluate staff performance, make decisions about people or interact directly with customers. Its output would help employees organise information, while staff remain responsible for accuracy and any subsequent actions.

**Why this category:** This is a routine internal productivity use without an apparent prohibited practice, Annex III high-risk purpose or direct AI-interaction disclosure requirement. Other obligations, such as data protection and confidentiality, may still apply.

---

## Phase 2 — Consulting response - Review your partner as the consultant using received Client Brief

**Instructions for partner:** Review each client request without seeing its intended AI Act risk category. For each case, identify the likely classification, propose a suitable AI architecture, distinguish provider and deployer roles, identify obligations and recommend **Approve**, **Approve with controls**, or **Deny and redesign**.

### Case 1 — Employee Performance Insights

A multinational customer-service company wants to improve employee productivity and reduce staff turnover. Management proposes an AI system that analyses employees' facial expressions, voice patterns and behaviour during video meetings and customer calls. The system would estimate employees' emotional states, including frustration, anxiety and enthusiasm. Managers would receive individual dashboards and use the results when planning performance reviews and staff development. Employees would be informed that the system is in use, but participation would be mandatory. Managers would make the final employment decisions.

### Case 2 — Recruitment Shortlisting Assistant

A regional healthcare provider receives hundreds of applications for nursing and administrative vacancies. Its HR team wants an AI system to analyse CVs, compare qualifications with job requirements and rank applicants for interview invitations. The system would use applicants' CVs, work history and the advertised job criteria. Recruiters would review the ranked list, but only the highest-scoring applicants would normally be considered. Candidates would be affected by whether they progress to an interview. The HR manager would retain authority to change the shortlist.

### Case 3 — Website Customer Support Assistant

An online home-appliance retailer wants to provide customer support outside normal business hours. It proposes an AI chatbot that answers product questions, explains delivery options and guides customers through return procedures. The assistant would use the company's product catalogue, help-centre articles and customer questions. Customers would interact directly with the assistant on the website and could request a human support agent. The retailer wants the chat interface to resemble a normal customer-service conversation. Staff would review escalated complaints rather than every routine response.

### Case 4 — Internal Meeting Notes Organiser

A small consultancy wants to reduce the time employees spend organising non-confidential internal meeting notes. It proposes an AI tool that turns staff-written notes into topic headings, action-item lists and draft follow-up summaries. Employees would paste notes into an approved internal workspace and check the output before saving or sharing it. The tool would not evaluate staff performance, make decisions about people or interact directly with customers. Its output would help employees organise information, while staff remain responsible for accuracy and any subsequent actions.

---
# EU AI Act — Phase 2: Consulting Review from partner's Client Brief (Barsha's Client Briefs)

## Completed consulting review table

| Case | Likely category | Why this is your first-pass call | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|---|---|
| **1 – BrightLine Telecom** | **Prohibited** | AI analyses employees' voices to infer emotions and uses the results for performance reviews and bonuses. Workplace emotion recognition is generally prohibited under Article 5. | Replace emotion scoring with call-quality analysis: call/transcript → objective service-quality criteria → human review → quality feedback and audit logs. | **Provider:** VoxPulse, if supplying the system. **Deployer:** BrightLine Telecom. **Vendor:** VoxPulse (US-based). | Remove emotion inference; assess GDPR compliance; minimise personal data; provide meaningful human oversight; document and audit the redesigned system. | **Deny and redesign** |
| **2 – NextStep Academy** | **High-risk** | AI scores applicants and automatically rejects most candidates. AI used to determine access to education or vocational training can fall under Annex III. | Application and test → AdmitIQ score → meaningful human review, including potential rejections → admissions decision → logged outcome. | **Provider:** AdmitIQ vendor, subject to configuration and contractual roles. **Deployer:** NextStep Academy. | Risk management; data governance; documentation and logging; human oversight; accuracy and bias testing; GDPR safeguards; applicable high-risk conformity requirements. | **Approve with controls, after redesign** |
| **3 – Holzhaus Möbel** | **Limited risk / transparency** | An AI chatbot interacts directly with customers. Article 50 generally requires users to know they are interacting with AI. | Customer question → chatbot grounded in FAQ, catalogue and authorised order data → response → human escalation for complaints and refunds. | **Provider:** Chatbot developer/integrator, depending on arrangements. **Deployer:** Holzhaus Möbel. **Vendor:** Third-party LLM API provider. | Clearly disclose AI interaction; protect order data; implement GDPR controls; prevent misleading answers; provide human escalation. | **Approve with controls** |
| **4 – Kornfeld Bäckerei** | **Minimal risk** | AI predicts bakery demand and supports production planning; based on the described design, it does not fall within the specified high-risk use cases. | Sales, weather and event data → forecasting model → suggested baking quantities → production manager approval → production records. | **Provider:** Forecasting system developer/vendor. **Deployer:** Kornfeld Bäckerei. **Vendor:** Depends on implementation. | Basic data security; forecast monitoring; human review; reassess GDPR obligations if loyalty-app data is introduced. | **Approve** |

## Important points for the partner discussion

1. **BrightLine Telecom:** A manager making the final decision does not make prohibited workplace emotion recognition lawful. Remove the emotion-inference functionality.
2. **NextStep Academy:** Human oversight must be meaningful. Reviewing only the top 300 applicants does not adequately address the risks of automatically rejecting everyone else. Applicable high-risk requirements depend on the legal implementation timeline.
3. **Holzhaus Möbel:** Customers should know they are interacting with an AI assistant, unless that is obvious from the circumstances. The human-like presentation makes explicit disclosure particularly important.
4. **Kornfeld Bäckerei:** The forecasting tool can generally be approved, but introducing identifiable customer loyalty data later calls for a further privacy assessment.

# Phase 3: Approval pack for partner review - from Barsha

> Client question: *"Can we launch this?"* I reviewed my partner's four briefs without seeing their answer key.

### Executive summary

Of the four proposals, one cannot launch as designed, two can launch with controls, and one can launch with only light checks.

- **Case 1 (Employee Performance Insights)** infers employees' emotions from their faces and voices at work. This is a **prohibited** practice, so it is **denied**. I offer a lawful redesign below.
- **Case 2 (Recruitment Shortlisting Assistant)** ranks job applicants. This is **high-risk**, so it can launch only with human oversight, logging, documentation and candidate information in place.
- **Case 3 (Website Customer Support Assistant)** is a customer chatbot. It is **limited risk**, so it can launch if customers are clearly told they are talking to an AI.
- **Case 4 (Internal Meeting Notes Organiser)** is **minimal risk** and can launch now. GDPR and confidentiality should still be checked.

For all four cases, staff who use or oversee the AI need basic AI literacy training (Article 4), which applies to all providers and deployers.

### Consulting review table (Apply · Integrate · Verify)

| Case | Likely category | Why this is my first-pass call | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|---|---|
| 1 | **Prohibited** | It infers employees' emotions (frustration, anxiety) from face and voice in the workplace. Article 5 bans this unless it is for medical or safety reasons. Informing staff or having a human make the final decision does not change this. | As proposed: video and call recordings → biometric emotion model → individual manager dashboard → performance reviews. Not allowed. | **Provider:** the tool's developer (vendor, or the company if built in-house). **Deployer:** the customer-service company. | Cannot be made compliant with controls. Stop the project and use the redesign below. | **Deny and redesign** |
| 2 | **High-risk** | It ranks job applicants and decides who gets an interview. Recruitment is an employment use listed in Annex III. | **Trigger:** a new vacancy closes. **System:** parses CVs and matches them to job criteria, then produces a ranked list with reasons for each score. **Human review:** a recruiter reviews the full list, including a sample below the cut-off, before invitations go out. There is no automatic rejection. **Output:** the HR manager approves the shortlist. **Logging:** scores, reasons and recruiter overrides are logged. | **Provider:** the vendor of the recruitment tool, or the healthcare provider if it builds the tool itself. **Deployer:** the healthcare provider (HR team). **Vendor:** yes, if the tool is bought. | **Provider:** risk management, data governance and bias testing, technical documentation, conformity assessment, CE marking, EU database registration. **Deployer:** use the tool as the provider's instructions say; assign trained human oversight; keep logs for at least 6 months; monitor results; inform candidates and workers' representatives; GDPR DPIA and Art. 22 safeguards. **FRIA:** needed if the provider is a public body or provides a public service. | **Approve with controls** |
| 3 | **Limited risk / transparency** | Customers chat directly with an AI that is designed to feel like a normal customer-service conversation. Under Article 50 they must be told it is an AI. It makes no high-impact decisions about people. | **Trigger:** a customer opens the chat outside business hours. **System:** an LLM answers using the product catalogue and help-centre articles only (RAG). **Disclosure:** a message at the start says "You're chatting with an AI assistant". **Human review:** a human agent is available on request, and escalated complaints are reviewed by staff. **Logging:** chat logs are kept with a defined retention period. | **Provider:** the retailer, if it builds the chatbot on an LLM API; otherwise the chatbot vendor. **Deployer:** the retailer. **Vendor:** the LLM/API provider (GPAI model provider). | Clear AI disclosure at the first interaction. An easy route to a human. Answers limited to approved sources. The bot must not make promises that go against return or warranty law (consumer protection). GDPR notice for chat data. | **Approve with controls** |
| 4 | **Minimal risk** | It is an internal productivity tool. It does not evaluate staff, make decisions about people or talk to customers, and staff check every output. | **Trigger:** an employee pastes notes. **System:** produces headings, action items and a draft summary. **Human review:** the employee edits and approves the output before saving or sharing it. **Output:** organised notes. | **Provider:** the vendor of the AI tool. **Deployer:** the consultancy. **Vendor:** yes. | No specific AI Act obligations apart from AI literacy. Flag GDPR, because notes may still name people. Check the vendor contract: data location, and no training on the consultancy's data. | **Approve** |

### Case notes and compliance implications

**Case 1 - Deny and redesign.** The ban applies however the results are used and even if staff are informed, because consent is hard to give freely at work. **Lawful alternative:** drop face and voice emotion analysis. Instead, (a) run voluntary, anonymous wellbeing pulse surveys reported only at team level; (b) use workload metrics such as call volume, handle time and overtime to spot overloaded teams; (c) if call analytics are wanted, analyse transcripts for coaching topics (for example "customer asked about refunds") without inferring anyone's emotions. Option (b) is employee monitoring, so it still needs GDPR and works council review.

**Case 2 - Approve with controls.** The main risk is automation bias. If recruiters "normally only consider the top scores", the human review is just a formality. Controls: no automatic rejection, recruiters review a sample below the cut-off, applicants can ask for a human review, and the vendor shows bias testing for age, gender and nationality. The healthcare context makes a FRIA likely.

**Case 3 - Approve with controls.** Making the chat "resemble a normal conversation" is acceptable, but hiding the fact that it is an AI is not. The disclosure must be clear from the first message. Keep the bot to approved sources so it does not invent delivery or return terms.

**Case 4 - Approve.** AI is used, but nothing significant is decided about people. The parallel issues are GDPR and confidentiality, not the AI Act.

### Where a legal team should verify

- Whether the healthcare provider in Case 2 counts as a public body or a provider of public services (this decides whether a FRIA is needed).
- The current application dates for high-risk obligations, because the EU has proposed postponing some Annex III deadlines.
- In Case 1, whether any part of the system could fall under the medical or safety exception (unlikely as described).

# Phase 4: Client Discussion and Final Sign-off
 

## 1. Consultant presents the approval pack

Martha presented the four-case EU AI Act assessment, including the proposed AI architectures, role allocation, compliance controls and launch recommendations.

| Case | Client | Martha's inferred category | Consulting recommendation |
|---|---|---|---|
| 1 | BrightLine Telecom | Prohibited | **Deny and redesign.** Remove workplace emotion inference from voice analysis. Consider objective call-quality and workload metrics with appropriate privacy and employment safeguards. |
| 2 | NextStep Academy | High-risk | **Approve with controls, conditional on redesign and applicable compliance requirements.** Eliminate unreviewed automatic rejections; implement meaningful human oversight, bias testing, documentation and logging. |
| 3 | Holzhaus Möbel | Limited risk / transparency | **Approve with controls.** Clearly identify the chatbot as AI, safeguard customer/order information and provide human escalation. |
| 4 | Kornfeld Bäckerei | Minimal risk | **Approve.** Retain human review of production forecasts and reassess GDPR implications before adding identifiable loyalty-app data. |

## 2. Partner reveals the private answer key

During the discussion, Barsha confirmed that her intended categories were the same as Martha's classifications for all four scenarios.

| Case | Martha's classification | Barsha's intended classification | Match? |
|---|---|---|---|
| BrightLine Telecom | Prohibited | Prohibited | **Yes** |
| NextStep Academy | High-risk | High-risk | **Yes** |
| Holzhaus Möbel | Limited risk / transparency | Limited risk / transparency | **Yes** |
| Kornfeld Bäckerei | Minimal risk | Minimal risk | **Yes** |

**Result:** 4 of 4 classifications matched (100% agreement).

## 3. Client discussion and response

Barsha accepted Martha's recommendations for all four scenarios and confirmed sign-off. No additional challenge or redesign request was raised during the discussion.

The parties agreed on the following central implications:

- **BrightLine Telecom:** The proposed workplace emotion-inference functionality must not launch. Any alternative based on objective call metrics or anonymous staff surveys still requires appropriate data protection and employment-law assessment.
- **NextStep Academy:** AI-supported admissions may require high-risk controls. Human review must be meaningful rather than a formality; automatic rejection without appropriate oversight is not an acceptable launch design.
- **Holzhaus Möbel:** Customers should be clearly informed that they are interacting with an AI assistant, with suitable data safeguards and access to human support.
- **Kornfeld Bäckerei:** Demand forecasting can proceed under the described use case, with human review and attention to GDPR if personal loyalty-app data is added later.

**Client decision:** Accepted recommendations.  
**Requested changes during discussion:** None.  
**Sign-off:** Confirmed by Barsha, as reported during the lab discussion.

## 4. Final consulting decisions and sign-off

| Client | Final consulting decision | Partner response |
|---|---|---|
| BrightLine Telecom | Deny and redesign | Accepted |
| NextStep Academy | Approve with controls, subject to redesign and compliance checks | Accepted |
| Holzhaus Möbel | Approve with controls | Accepted |
| Kornfeld Bäckerei | Approve | Accepted |

**Consultant:** Martha — signed off  
**Partner / Client:** Barsha — accepted and signed off  
**Phase 4 status:** Complete

*These are consulting recommendations for the lab, not legal authorisation, conformity certification or confirmation that any system is ready for deployment. Applicable requirements and timelines should be verified before a real launch.*

## 5. Closing note — What changed after the client discussion?

The discussion confirmed that Martha and Barsha independently reached the same EU AI Act classifications for all four cases. Barsha accepted the proposed decisions and safeguards, so the recommendations did not need to change. The review reinforced the importance of distinguishing prohibited workplace emotion inference from permissible analytics, ensuring meaningful human oversight in admissions, providing AI chatbot transparency, and maintaining appropriate privacy controls even for minimal-risk forecasting systems.
