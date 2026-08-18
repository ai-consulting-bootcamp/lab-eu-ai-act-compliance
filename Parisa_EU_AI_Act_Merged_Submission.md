# Audit of Louise's Four Client Cases

> **Classification summary:** Case 1 → Minimal risk · Case 2 → High-risk · Case 3 → Prohibited · Case 4 → Limited risk / transparency

| **Case**                          | **Likely category**         | **Why this is my first-pass call**                                                                                                                                                                                                                                                                                                                                                           | **Proposed AI architecture**                                                                                                                                                                                                                                           | **Provider / deployer / vendor**                                                                                                                                                           | **Required obligations or control**                                                                                                                                                                                                                                         | **Decision**              |
|-----------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| **1. Payment support operations** | Minimal risk                | The AI performs an operational support task: classifying and routing tickets. It does not determine merchants’ access to financial services, and agents can change its decisions.                                                                                                                                                                                                            | Merchant submits ticket → ticket text + operational/service-status data → AI classifies topic and suggests priority → support agent can review/override → ticket routed to team → routing and overrides logged.                                                        | Deployer: payment company. Provider: payment company if developed internally, otherwise AI software provider. Vendor: third-party model/cloud provider if used.                            | Human override; monitor routing accuracy; logging; data protection/security; ensure the system is not later used for creditworthiness or service-access decisions.                                                                                                          | **Approve**               |
| **2. Employee coaching platform** | High-risk                   | The system analyses individual employees’ workplace behaviour, progress and development and sends individual insights to managers for performance conversations. Annex III covers AI intended to monitor/evaluate workers’ performance and behaviour.                                                                                                                                        | Employee chats with AI coach → conversations + goals + activity data → AI identifies strengths/development concerns → monthly individual dashboard → manager reviews insights → manager makes final employment decisions → recommendations and manager actions logged. | Provider: coaching platform. Deployer: employer/customer using the system with employees. Vendor: underlying AI/model provider if third-party.                                             | Human oversight; risk management; data governance; testing for accuracy/bias; logging; documentation; clear limits on how insights are used; appropriate information to employees. High-risk systems also require transparency, record-keeping and human-oversight measures | **Approve with controls** |
| **3. Beauty & wellness app**      | Likely prohibited           | The system deliberately uses young age and indications of financial difficulty to decide when to apply more urgent sales pressure, while also using users’ appearance concerns. Article 5 prohibits AI that exploits vulnerabilities due to age or a specific social/economic situation where it materially distorts behaviour and causes or is reasonably likely to cause significant harm. | User uploads selfie + goals + conversations + purchase behaviour → AI identifies vulnerability/conversion signals → automatically selects timing and persuasive message → paid programme promoted → growth team only sees aggregate results.                           | Provider/deployer: beauty-app company if it designs and operates the system. Vendor: underlying model/provider if external.                                                                | Do not use age, financial vulnerability or psychological/appearance insecurities to intensify persuasion. Redesign targeting around neutral factors such as user-requested preferences and product relevance. Add clear controls against exploitative personalization.      | **Deny and redesign**     |
| **4. Reality-TV companion**       | Limited risk / transparency | Users directly interact with a generative AI assistant. The main AI Act concern is transparency rather than a consequential decision about users. Article 50 requires people interacting directly with AI to be informed that it is AI unless that is already obvious; providers of generative systems also have requirements concerning identification of AI-generated output.              | Viewer opens companion → viewing progress + question → system retrieves approved episode information → generative model produces answer/recap/theory → response shown to viewer → AI disclosure + basic interaction logs.                                              | Provider: entertainment startup. Deployer: startup if it operates the service itself; possibly streaming company if licensed to one. Vendor: underlying LLM/model provider if third-party. | Clearly disclose AI interaction; distinguish generated theories from factual episode information; control spoilers; use approved retrieval sources; maintain appropriate content safeguards and logs.                                                                       | **Approve with controls** |

# EU AI Act Approval Pack

*Consulting review of Luise's four proposed AI use cases*

## Executive Summary

The portfolio spans all four practical AI Act outcomes: one minimal-risk operational support use, one high-risk employment use, one likely prohibited vulnerability-exploitation design, and one customer-facing system requiring transparency. My recommendation is to approve Case 1, approve Case 2 only with high-risk controls and meaningful limits on manager use, deny and redesign Case 3, and approve Case 4 after Article 50 disclosure and generative-AI guardrails are in place.

| **Case**                       | **Classification** | **Key issue**                                            | **Decision**           |
|--------------------------------|--------------------|----------------------------------------------------------|------------------------|
| 1. Payment support operations | Minimal risk       | Operational ticket routing; no financial-access decision | **APPROVE**            |
| 2. Employee coaching platform | High-risk          | Individual worker monitoring / evaluative insights       | **APPROVE + CONTROLS** |
| 3. Beauty & wellness app      | Likely prohibited  | Vulnerability-targeted persuasive personalization        | **DENY + REDESIGN**    |
| 4. Reality-TV companion       | Transparency       | Direct AI interaction and generated responses            | **APPROVE + CONTROLS** |

### Case 1 - Payment Support Operations

> **MINIMAL RISK**

A payment company uses AI to classify merchant support tickets, suggest operational priority and route each ticket to the correct internal team. Agents can change the category, priority or routing, and the system does not decide whether merchants can access financial products or services.

**Classification.** The use is operational triage, not an Annex III decision about a person's access to essential private services. Human agents retain full override, so the first-pass classification is minimal risk.

**Architecture.** Merchant ticket + service-status signals → classification/priority model → routing suggestion → agent review/override → internal team queue → routing and override logs.

**Roles.** Deployer = payment company. Provider = the company if it develops/puts the system into service under its own name, otherwise the support-AI supplier. A model or cloud supplier may be a third-party vendor.

**Controls.** Routing-accuracy monitoring, audit logs, access controls and GDPR/security review. Keep a clear purpose boundary so the model is not later reused for creditworthiness or merchant access decisions.

**Decision - APPROVE.** Proceed with ordinary operational and data-protection controls.

### Case 2 - Employee Coaching Platform

> **HIGH-RISK - ANNEX III EMPLOYMENT / WORKERS MANAGEMENT**

A corporate coaching platform analyses employees’ AI-coach conversations, goal completion and coaching activity to identify strengths, development areas and signs that progress may be falling behind. Managers receive monthly individual dashboards for one-to-ones and performance conversations.

**Classification.** Annex III covers AI intended to monitor or evaluate the performance and behaviour of people in work-related relationships. The dashboard produces individual evaluative insights used in performance conversations, so the first-pass call is high-risk even though managers make the final promotion or performance-plan decisions.

**Architecture.** Employee coaching interactions + goal/activity data → analysis model → individual strengths/development flags → manager dashboard → manager review and employment conversation → access, output and manager-action logs.

**Roles.** Provider = coaching-platform company if it develops/markets the system. Deployer = employer using the platform with staff. Underlying LLM, analytics or cloud providers may be third-party vendors.

**Controls.** Document intended purpose; risk management; data governance and bias/accuracy testing; technical documentation and logging; meaningful human oversight; employee information and strict limits on using coaching data for consequential HR decisions; separate GDPR/workplace-monitoring review.

**Decision - APPROVE WITH CONTROLS.** Treat as Annex III employment AI and prepare the high-risk compliance evidence. Under the 2026 AI Omnibus, the main Annex III requirements apply from 2 December 2027.

### Case 3 - Beauty & Wellness App

> **LIKELY PROHIBITED - ARTICLE 5 VULNERABILITY EXPLOITATION**

A beauty and wellness app uses selfies, appearance goals, user concerns and purchase behaviour to personalise skincare and coaching promotions. The growth design intentionally makes messages more urgent and frequent for younger users and for users who repeatedly abandon purchases because of insufficient funds, and may reuse their stated appearance concerns to encourage paid programmes.

**Why this classification.** Article 5 prohibits AI that exploits vulnerabilities due to age or a specific social/economic situation where the objective or effect is to materially distort behaviour in a way that causes or is reasonably likely to cause significant harm. Here the system deliberately uses age and financial-difficulty signals to intensify persuasive pressure. On these facts, the safest first-pass call is prohibited, subject to legal confirmation that the significant-harm threshold is met.

**Current architecture.** Selfie + appearance goals + chat concerns + purchase/insufficient-funds signals → vulnerability-aware targeting model → urgency/frequency and personalised appearance message → automatic premium-programme prompt → aggregate conversion monitoring. There is no individual human review before targeting.

**Role map.** Deployer = beauty/wellness company operating the app. Provider = the company if it develops/places the system under its own name, otherwise the personalisation supplier. LLM, vision and marketing-automation suppliers may be third-party vendors.

#### Lawful Redesign

> Remove vulnerability exploitation from the targeting logic. Use user-selected skincare preferences, explicit goals and neutral product relevance instead of age, insufficient-funds signals or inferred susceptibility. Do not intensify pressure by repeatedly surfacing appearance insecurities; cap notification frequency, provide opt-outs, and review consumer-protection and GDPR requirements.

**Important.** The redesigned system should be reclassified after the targeting features are fixed. Ordinary recommendation personalisation may be permissible, but manipulative or aggressive marketing can still create obligations under other EU consumer and data-protection rules.

**Decision - DENY AND REDESIGN.** Do not deploy the vulnerability-targeting design as proposed.

### Case 4 - Reality-TV Companion

> **LIMITED RISK / TRANSPARENCY**

A streaming startup offers an AI companion that chats with viewers about contestants, relationships and events from episodes already watched. It retrieves approved episode information and generates recaps, answers and theories tailored to the viewer’s progress. It does not make decisions about users or control access to content or services.

**Why this classification.** The main AI Act issue is transparency: users interact directly with an AI assistant, and some responses are generated rather than retrieved. Article 50 requires appropriate disclosure for direct human-AI interaction and provider-side measures that make AI-generated content identifiable where applicable.

**Recommended architecture.** Viewer progress + question → approved-source retrieval → generative model → answer/recap/theory → spoiler and safety checks → viewer. Add a clear AI disclosure at first interaction, generated-content marking where required, and interaction/moderation logs. Routine responses may be automated; flagged content can be escalated to a human moderator.

**Role map.** Provider/deployer = streaming startup if it develops and operates the companion under its own name. The underlying LLM, retrieval platform or moderation service may be third-party vendors.

**Controls.** Clear AI disclosure; avoid presenting generated theories as verified facts; spoiler controls tied to episode progress; approved-source/RAG quality checks; hallucination and moderation monitoring; privacy review for viewing-history data. Article 50 transparency obligations apply from 2 August 2026.

**Decision - APPROVE WITH CONTROLS.** Launch after the transparency and safe-generation controls are implemented.

## Approval Conditions & Next Steps

The key consulting principle across these cases is to classify the intended use, data and affected people rather than the industry label or the presence of AI alone. Human review helps manage risk, but it does not make a prohibited design lawful; for high-risk employment AI, the oversight must be meaningful and connected to the actual decision workflow.

### Cross-Case Recommendations

- Case 1 - Launch with reliability, security and logging controls, while keeping the model strictly separated from merchant eligibility or credit decisions.
- Case 2 - Define the coaching system's intended purpose, restrict manager use, establish meaningful human oversight and prepare Annex III high-risk compliance evidence.
- Case 3 - Stop vulnerability-based targeting. Redesign personalisation around neutral user preferences and product relevance, with notification limits and clear opt-outs.
- Case 4 - Add Article 50 AI disclosure, approved-source retrieval, spoiler controls, generated-content identification where required and ongoing quality monitoring.

### Borderline Questions for the Client Discussion

**Case 1:** Can ticket priority or routing ever change a merchant's access to payment services, or is it strictly an internal support workflow?

**Case 2:** How often do managers rely on the individual dashboard in promotion, performance-plan, role-allocation or termination discussions? Could the coaching insights be separated from formal HR evaluation?

**Case 3:** How is “younger” defined, are minors included, what exactly does the insufficient-funds signal represent, and what psychological or financial harms are reasonably foreseeable from the urgency strategy?

**Case 4:** Is the AI nature already obvious in the interface, how is the disclosure shown at first interaction, and what provider-side marking or detection method is used for generated content?

### Evidence / Artifacts I Would Request Next

- Case 1: ticket taxonomy, routing/priority rules, accuracy metrics, data-flow map and override/audit-log sample.
- Case 2: intended-purpose statement, model/technical documentation, data description, bias and accuracy tests, logging design, human-oversight procedure and workplace/GDPR assessment.
- Case 3: targeting feature specification, age/financial-signal logic, harm assessment, notification policy and redesigned data-flow showing removal of vulnerability exploitation.
- Case 4: AI disclosure copy, approved-source list/RAG design, moderation/escalation policy, spoiler controls and Article 50 generated-content marking approach.

### Final Sign-Off

| **Case 1**  | **Case 2**             | **Case 3**          | **Case 4**             |
|-------------|------------------------|---------------------|------------------------|
| **APPROVE** | **APPROVE + CONTROLS** | **DENY + REDESIGN** | **APPROVE + CONTROLS** |

### What Changed After the Client Discussion?

To complete after debrief: compare Luise's intended answer key with these classifications, note any facts clarified during discussion, and record whether the recommendation, controls or architecture changed.

### Legal References

Regulation (EU) 2024/1689 (EU AI Act): Article 5; Article 6; Annex III; Article 50.

Regulation (EU) 2026/1744 (Digital Omnibus on AI): revised application dates, including 2 December 2027 for Annex III high-risk requirements.

European Commission, Guidelines on transparency obligations for providers and deployers of AI systems under Article 50 (July 2026).

European Commission / AI Act Service Desk, Annex III employment and workers-management classification materials; Article 5 prohibited-practices guidance.
