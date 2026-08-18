# EU AI Act — Partner Review

## Partner
Paola

## Review approach

This review was completed without access to Paola's private answer key. The classifications below are based only on the four client briefs shared in the `partner-share` branch.

---

## Case 1 — Employee client-readiness scoring

**Likely category:**  
Prohibited.

**Why this is my first-pass call:**  
The system attempts to infer employees' stress, frustration, motivation and confidence from facial movements, vocal patterns, speaking pace and pauses during workplace video check-ins. The EU AI Act prohibits AI systems used to infer emotions in the workplace, except where the use is intended for medical or safety reasons. The fact that supervisors can override the resulting recommendations does not remove the prohibited underlying use.

**Proposed AI architecture:**  
The proposed emotion-inference layer should not be deployed. A lawful redesign could use non-biometric operational information such as workload, schedule stability, quality metrics, voluntary employee feedback and documented performance information. The system could identify possible coaching or workload-review needs, but a manager should assess the context before any account allocation or promotion decision.

**Provider / deployer / third-party vendor:**  
If an external vendor supplies the system under its own name, the vendor is the provider and the customer-support company is the deployer. If the company develops, rebrands or substantially modifies the system, provider responsibilities may shift to the company.

**Required obligations or controls:**  
Remove emotion inference from facial and vocal signals. Restrict any redesigned system to relevant workplace information, apply data minimisation and clear purpose limitation, document the permitted use, provide meaningful human review and monitor for discriminatory effects. GDPR and employment-law implications should also be reviewed.

**Consulting decision:**  
**Deny and redesign.**

---

## Case 2 — Vocational programme admissions

**Likely category:**  
High-risk.

**Why this is my first-pass call:**  
The system ranks applicants for vocational education and determines admission shortlists, scholarship priority and recommended course level. The output materially affects access to education and vocational training, and applications below the threshold would normally be excluded before human review.

**Proposed AI architecture:**  
Application submitted → relevant application, education and assessment data analysed → system generates a recommendation and supporting factors → trained admissions officer reviews both positive and adverse recommendations before exclusion or scholarship prioritisation → final decision and any override are recorded.

**Provider / deployer / third-party vendor:**  
If supplied by an external admissions-software company, that vendor is the provider and the academy network is the deployer. If the academies develop or substantially modify the system, their role would need to be reassessed.

**Required obligations or controls:**  
Risk management, appropriate data governance, technical documentation, logging, clear instructions for use, effective human oversight, accuracy, robustness and cybersecurity controls. The deployer should monitor outcomes, establish an appeal or reconsideration process and assess GDPR requirements, including whether a DPIA is required.

**Consulting decision:**  
**Approve with controls.**

---

## Case 3 — Railway conversational assistant

**Likely category:**  
Limited risk / transparency.

**Why this is my first-pass call:**  
The assistant interacts directly with passengers through the website and WhatsApp and deliberately communicates in a human-like conversational style. The company has not yet decided whether users will be told that “Mila” is an automated system. This makes the transparency requirement central to the deployment.

**Proposed AI architecture:**  
Passenger starts a conversation → clear AI disclosure → assistant accesses only the necessary schedule, ticket, refund and booking information → provides information or prepares a routine request → exceptional refunds and formal complaints are escalated to a human → interaction, escalation and correction events are logged where appropriate.

**Provider / deployer / third-party vendor:**  
If a third-party conversational-AI platform supplies the system, the vendor is the provider and the railway company is the deployer. If the railway company develops or rebrands the system, the role allocation would need to be reassessed.

**Required obligations or controls:**  
Clearly disclose at the start of the interaction that Mila is an AI system, maintain accessible human escalation, restrict autonomous actions to approved low-impact tasks, minimise personal-data access, test response accuracy and monitor incorrect routing or refund information. GDPR and consumer-protection requirements should also be considered.

**Consulting decision:**  
**Approve with controls.**

---

## Case 4 — Grocery replenishment forecasting

**Likely category:**  
Minimal risk.

**Why this is my first-pass call:**  
The system forecasts inventory requirements using operational information such as sales, stock, weather, holidays and local events. It does not evaluate individuals, determine eligibility or make decisions about customers, employees or suppliers. Managers also review its recommendations before orders are placed.

**Proposed AI architecture:**  
Daily planning cycle → historical sales, stock levels, weather, holidays and local-event data ingested → demand forecast and replenishment recommendation generated → store manager reviews and adjusts recommendation → approved order is placed → forecast accuracy and overrides are logged for monitoring.

**Provider / deployer / third-party vendor:**  
If an external forecasting platform is used, the vendor is the provider and the grocery chain is the deployer. If the chain develops the forecasting system internally and places it into service under its own name, it may act as provider as well as deployer.

**Required obligations or controls:**  
No specific high-risk AI Act regime appears to apply on the facts provided. The company should still monitor forecast accuracy, maintain clear human accountability for purchasing decisions and document the operational boundaries of the system. Any personal-data use introduced later would require a separate GDPR assessment.

**Consulting decision:**  
**Approve.**

---

# Debrief

## Intended vs inferred classifications

| Case | Partner intended category | My inferred category | Match? |
|---|---|---|---|
| 1 | To be revealed by Paola | Prohibited | Pending |
| 2 | To be revealed by Paola | High-risk | Pending |
| 3 | To be revealed by Paola | Limited risk / transparency | Pending |
| 4 | To be revealed by Paola | Minimal risk | Pending |

## Client discussion on Gretel's cases

I accept Paola's recommendations for Cases 1, 2 and 3.

For my Case 4, I accept Paola's distinction but would retain the original minimal-risk classification at the system-use level. The review-summary system does not make consequential decisions about individuals or fall within an Annex III high-risk use case. However, I accept that the provider may separately have Article 50 obligations relating to AI-generated output. I would therefore add that provider-level obligation without treating the use case itself as high-risk.

## What changed after the client discussion?

The main change was how I would describe Case 4. I initially treated minimal risk mainly as the absence of a specific high-risk AI Act regime. The discussion showed that risk classification and role-specific obligations should be considered separately. A system can remain outside the high-risk categories while a provider may still have transparency or marking obligations for AI-generated output.

For the other cases, the discussion did not change the core classification, but it reinforced the importance of separating the legal classification from the architecture and operating controls proposed for deployment.