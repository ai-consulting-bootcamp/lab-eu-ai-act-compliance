# EU AI Act Approval Pack

## Executive summary: can the client launch?

Yes, but not every proposal can launch as currently designed. The travel assistant is a limited-risk customer-facing system and may launch with clear AI disclosure, human escalation and controlled source content. The bakery forecast is a minimal-risk operational tool and may launch with ordinary data, security and monitoring controls. The workplace emotion-analysis proposal must not launch: inferring employees’ emotions for performance management is a prohibited use. It should be redesigned around transparent, objective service-quality measures. The employee scheduling tool is high-risk because it supports task allocation and worker-management decisions; it may launch only after provider evidence, human-oversight, bias, logging and worker-information controls are in place.

## Case 1 — Travel agency website assistant

**Inferred category:** Limited risk / transparency.

**Architecture and operating model.** When a visitor opens the chat or asks about destinations, packages or cancellation rules, a retrieval-based assistant searches the agency’s approved catalogue. It answers with a source link and refuses unsupported questions. A low-confidence answer or request for a person is routed to a travel adviser, who validates the response. The system does not book trips or decide eligibility. The agency logs the question, source, answer, escalation and model version.

**Roles.** The travel agency is the provider if it owns or configures the assistant under its name, and it is also the deployer. No third-party AI vendor is assumed; if the agency uses a hosted model, the vendor’s provider role and contractual responsibilities must be confirmed.

**Compliance and decision.** The agency must tell visitors that they are interacting with AI at the first interaction unless this is already obvious. It should keep the catalogue current, prevent the assistant from presenting itself as human, provide an accessible human channel, and address GDPR and consumer-protection requirements for chat logs and travel claims.

**Decision: Approve with controls.**

## Case 2 — Bakery production forecast

**Inferred category:** Minimal risk.

**Architecture and operating model.** Each night, or when a manager requests a plan, a forecasting model combines historical sales by product and shop, calendar effects, weather forecasts and current stock. It proposes next-day production quantities and exceptions. A shop or production manager reviews every recommendation and edits or rejects it before production. The approved plan is the output; there is no automatic production order. The bakery records the input snapshot, forecast, model version, override, final plan and next-day variance.

**Roles.** The bakery group is the provider if it develops and puts the service into use under its name, and it is the deployer through its authorised managers. No AI vendor is assumed. A weather API may be an ordinary data supplier rather than an AI provider.

**Compliance and decision.** The use does not trigger a specific high-risk or Article 50 obligation on the stated facts. The bakery should still apply access control, data-quality checks, drift and forecast-error monitoring, backup and change management. It must reassess if the system later uses employee or customer profiles.

**Decision: Approve.**

## Case 3 — Workplace webcam and call-audio coaching

**Inferred category:** Prohibited.

**Architecture and operating model.** A coaching session or call recording is submitted to a model that analyses webcam and voice signals, infers frustration or disengagement, and produces scores for a supervisor. The supervisor may review or override the scores before coaching or shift changes, and the system records the resulting action. That human review does not make the use lawful: the stated purpose is workplace performance management, not medical or safety use.

**Roles.** The support-tool vendor is the provider because it supplies and updates the model. The customer-support centre is the deployer. A third-party vendor is involved, but the contract does not transfer responsibility for the centre’s use or make a prohibited purpose lawful.

**Compliance and decision.** The centre must not launch, procure or continue this emotion-inference purpose. It should stop the processing and delete related inputs and scores where legally permitted, document the decision, and involve its governance and privacy owners.

**Lawful redesign.** Remove emotion inference and webcam analysis. Use a transparent, human-approved quality rubric based on call content and objective service metrics, such as accuracy, resolution quality and adherence to approved procedures. Give staff clear notice, minimise data, and reassess the redesigned worker-monitoring use under employment, GDPR and applicable national rules.

**Decision: Deny and redesign.**

## Case 4 — Employee shifts and warehouse stations

**Inferred category:** High risk.

**Architecture and operating model.** A weekly scheduling run uses attendance, task times, error rates, certifications, availability and past assignments to rank feasible shifts and warehouse stations and identify coaching signals. A trained manager reviews explanations, checks constraints and bias indicators, records reasons for material overrides, and remains the decision-maker. The output is a roster and exception list; coaching suggestions are separately governed and no adverse action is automatic. Logs capture the input snapshot, model version, recommendation, explanation, human decision, affected worker, outcome and incidents. Affected workers are told when the system is used and how to ask questions or challenge a material outcome.

**Roles.** The scheduling vendor is the provider because it hosts, updates and supplies the model. The grocery distribution network is the deployer. A third-party vendor is involved. The client must obtain the vendor’s instructions, performance and bias evidence, logs, change notices and incident support; the contract does not transfer the client’s deployer duties.

**Compliance and decision.** The provider must support risk management, data governance and bias testing, technical documentation, logging, instructions for use, human oversight, accuracy, robustness, cybersecurity and conformity evidence. The deployer must assign competent and authorised oversight, verify representative inputs, monitor operation, keep records, inform affected workers, and suspend or escalate if the system presents a serious risk. The client should complete a GDPR DPIA where required, document a fundamental-rights and bias assessment, and check national employment and worker-consultation rules.

**Decision: Approve with controls.** Do not launch until the vendor evidence, oversight workflow, worker notice, logging, bias testing and escalation process are signed off.

## Overall launch decision

Launch the bakery forecast now subject to ordinary operational controls. Launch the travel assistant and employee scheduling tool only after their specified controls are implemented and evidenced. Do not launch the workplace emotion-analysis system; move forward only with the objective-metrics redesign.

## Stretch — high-risk implementation roadmap

**Selected case: employee shifts and warehouse stations.**

**Before market placement, the provider should:**

- define the intended purpose, decision boundaries and known limitations;
- complete risk management, representative-data and bias testing across roles, sites and worker groups;
- prepare technical documentation, automatic logs, instructions for use, accuracy/robustness/cybersecurity evidence and conformity documentation;
- design human-oversight tools that let managers understand, override or stop recommendations; and
- establish post-market monitoring, incident reporting and a controlled model-change process.

**Before first use, the deployer should:**

- confirm the system is registered and the vendor documentation is complete;
- run a GDPR DPIA where required and document a fundamental-rights, equality and worker-impact assessment;
- validate that attendance, task, certification and availability data are relevant and representative;
- train named managers with authority to override or stop the system, and prohibit automatic adverse action;
- notify affected workers, provide a question/challenge route, and test logging, escalation and suspension procedures.

**Evidence to request from the vendor:** intended-purpose and limitation statement; conformity documentation; technical file or summary; data sheets and bias-test results; accuracy metrics by relevant worker group; human-oversight instructions; sample logs and retention design; cybersecurity and access-control evidence; model/version change history; incident and post-market monitoring process; and contractual commitments for support, notification and audit access.

## Legal reference

- [Regulation (EU) 2024/1689, consolidated text — Articles 5, 26 and 50](https://eur-lex.europa.eu/eli/reg/2024/1689)
- [Regulation (EU) 2024/1689 — Annex III and high-risk system requirements](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R1689)
