# EU AI Act Approval Pack

## Executive Summary

The four proposals require different treatment.

Case 1 should not proceed as designed because it uses facial and vocal signals to infer employees' emotional states in the workplace and then links those inferences to account allocation and promotion decisions. The appropriate response is to remove the emotion-inference layer and redesign around objective operational and performance data.

Case 2 can proceed only as a controlled high-risk deployment. The main issue is not that AI supports admissions, but that the current threshold can prevent applicants from reaching meaningful human review.

Case 3 can proceed if transparency is built into the experience from the first interaction and the assistant remains within clearly defined service boundaries.

Case 4 can proceed. It is an operational forecasting use case with no material decision about individuals and no apparent high-risk trigger.

---

## Case 1 — Employee client-readiness scoring

**Inferred category:** Prohibited  
**Decision:** **Deny and redesign**

The system is intended to infer stress, frustration, motivation and confidence from facial and vocal signals collected during workplace video calls. Those inferred states then influence coaching, premium-account allocation and promotion opportunities.

A supervisor override does not solve the underlying problem. The issue arises before the recommendation is reviewed: the system is using AI to infer employees' emotions in the workplace for management purposes.

### Recommended redesign

Remove emotion inference entirely.

A redesigned system could support managers using objective and job-relevant information such as workload, schedule stability, quality indicators, customer outcomes, training completion and voluntary employee feedback. The AI could flag cases for review, but should not determine promotion or account allocation autonomously.

**Operating model:** operational data → AI recommendation → manager review → documented decision.

**Roles:** an external software company would normally be the provider and the customer-support company the deployer, unless the company develops, rebrands or substantially modifies the system.

**Key controls:** purpose limitation, data minimisation, meaningful human decision-making, discrimination monitoring, clear documentation and separate GDPR/employment-law review.

---

## Case 2 — Vocational programme admissions

**Inferred category:** High-risk  
**Decision:** **Approve with controls**

The AI materially influences access to vocational education, scholarships and course placement. The proposed threshold is particularly important because applicants below it would normally be excluded before an admissions officer sees them.

The system can still support admissions, but the workflow needs to change.

### Recommended architecture

Application submitted → relevant application and assessment data processed → AI generates score and supporting factors → admissions officer reviews recommendations before rejection or scholarship prioritisation → final decision and override logged.

Human review should be part of the standard process for adverse outcomes, not an exception for borderline cases.

**Roles:** admissions-system vendor as provider; academy network as deployer, subject to reassessment if the academies develop or substantially modify the system.

**Key controls:** risk management, data governance, representative-data testing, technical documentation, logging, human oversight, accuracy and robustness testing, cybersecurity, outcome monitoring, applicant information and a route for reconsideration or appeal.

A GDPR DPIA should also be assessed separately.

---

## Case 3 — Railway conversational assistant

**Inferred category:** Limited risk / transparency  
**Decision:** **Approve with controls**

The proposed use is reasonable because the assistant mainly provides information, recommends routes and prepares routine service actions. The material weakness is that the company has not decided whether passengers will know they are interacting with AI.

That should not remain an open design question.

### Recommended architecture

Passenger opens chat → clear AI disclosure → assistant accesses only necessary booking and service information → routine answer, route recommendation or request preparation → exceptional refunds and formal complaints transferred to a human agent.

The assistant should not imitate a human employee in a way that obscures its automated nature.

**Roles:** conversational-AI vendor as provider and railway company as deployer, unless the railway develops or substantially modifies the system.

**Key controls:** disclosure at the start of the interaction, easy human escalation, defined action boundaries, restricted personal-data access, response-quality testing, security, monitoring and logging of escalations and corrections.

GDPR and consumer-protection requirements remain parallel considerations.

---

## Case 4 — Grocery replenishment forecasting

**Inferred category:** Minimal risk  
**Decision:** **Approve**

This is a standard operational forecasting use case. The model predicts demand using sales, stock, weather, holidays and event data and produces replenishment recommendations. It does not evaluate people, determine access or eligibility, or make decisions about individual customers, employees or suppliers.

The existing human review is proportionate: store managers remain responsible for the order.

### Recommended architecture

Operational data → demand forecast → replenishment recommendation → store-manager review → approved order → forecast-performance monitoring.

**Roles:** forecasting vendor as provider and grocery chain as deployer. If the chain develops and operates the model under its own name, it may hold both roles.

**Key controls:** forecast-quality monitoring, clear ownership of purchasing decisions, logging of major overrides and periodic review of model performance.

No specific high-risk AI Act control framework appears necessary on the facts provided. Any future use of personal data or individual-level scoring would require reassessment.

---

## Final Recommendation

**Case 1:** do not launch as proposed. Redesign before further development.

**Case 2:** proceed only after the admissions workflow, human oversight and high-risk controls are redesigned.

**Case 3:** proceed once AI disclosure and escalation boundaries are built into the product experience.

**Case 4:** proceed with normal operational governance and performance monitoring.

The central lesson across the four cases is that the presence of AI is not the deciding factor. The regulatory outcome depends on what the system is actually doing, the context in which it is used and the effect its output has on people.