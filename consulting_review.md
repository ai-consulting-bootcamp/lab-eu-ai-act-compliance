# Consulting Review

# Case 1 – AI-Based Warehouse Restocking
A small furniture company wants an AI tool that looks at past sales numbers, season, and local weather data to predict which products to restock in each warehouse next month. The tool only produces a suggested restock list, it does not decide anything about people, it does not touch customers or employees directly. A warehouse manager reviews the suggested list every week and can change or ignore it freely before any order is placed.

**Likely category**

Minimal risk

The AI is used solely to optimize internal business operations by forecasting inventory needs. It does not make decisions about individuals or significantly affect people's rights or opportunities. A warehouse manager reviews every recommendation and can freely modify or reject it before any purchase order is placed.

**Proposed AI architecture**

- **Business trigger:** Weekly inventory planning.
- **AI behavior:** Forecasts product demand using historical sales, seasonality, and weather data to generate a recommended restocking list.
- **Human review:** Warehouse manager reviews, edits, or rejects recommendations before orders are placed.
- **Output:** Suggested restocking plan.
- **Logging/records:** Store forecasting results and manager decisions to monitor model performance and improve future predictions.

**Provider / Deployer / Vendor**

- **Provider:** AI software vendor (or internal development team if built in-house).
- **Deployer:** Furniture company.
- **Vendor:** Optional cloud AI or analytics provider.

**Required obligations or controls**

- No specific AI Act obligations for minimal-risk AI.
- Ensure compliance with GDPR if personal data is ever introduced.
- Monitor prediction quality to avoid operational losses.

**Decision**

✅ **Approve**

# Approval Pack – AI-Based Warehouse Restocking

## Executive Summary

The proposed AI system is intended to improve inventory planning by predicting future product demand using historical business data. Based on the current information, this use case falls into the **Minimal Risk** category under the EU AI Act because it supports internal operational decisions without affecting individuals' rights or opportunities. The project can proceed, provided standard business governance and applicable data protection requirements are maintained.

---

## Client Use Case

A small furniture company wants an AI tool that analyzes historical sales, seasonal trends, and local weather data to recommend which products should be restocked in each warehouse for the following month. The recommendations are reviewed weekly by a warehouse manager, who can modify or reject them before purchase orders are placed.

---

## Inferred AI Act Category

**Minimal Risk**

### Reasoning

The AI supports internal business optimization and inventory planning. It does not make decisions about customers, employees, or any other individuals whose rights or opportunities may be affected.

---

## Proposed AI Architecture

**Business trigger**

Weekly inventory planning.

**System behavior**

The AI predicts future product demand using historical sales, seasonality, and weather data.

**Human review**

Warehouse managers review every recommendation before approving purchase orders.

**Output**

Suggested warehouse restocking plan.

**Logging**

Store AI recommendations and final manager decisions to monitor forecasting performance and continuously improve the model.

---

## Roles

**Provider**

AI software vendor or internal development team.

**Deployer**

Furniture company.

**Vendor**

Optional cloud analytics provider.

---

## Compliance Implications

No specific AI Act obligations apply to this use case because it is classified as minimal risk. The company should still implement good governance practices, cybersecurity measures, and comply with GDPR if personal data is processed in future versions.

---

## Decision

## ✅ Approve

The proposed solution may be deployed as described.

-----
-----

# Case 2 – AI Customer Support Assistant
A telecom company wants to add a chat assistant to their support website. The assistant answers billing questions, helps customers change their plan, and sounds very natural, almost like a real support agent. Customers often think they are chatting with a real person. The company likes this because it feels more "human" and friendly. The assistant uses account data and past chat history to answer questions. If the issue is complex, it hands the conversation to a human agent, but the AI itself never says clearly that it is a bot.

**Likely category**

Limited risk / Transparency

Customers interact directly with an AI system, but it does not make decisions affecting their rights or obligations. The primary issue is that users are not informed they are communicating with AI, which triggers the transparency requirements of Article 50.

**Proposed AI architecture**

- **Business trigger:** Customer starts an online support conversation.
- **AI behavior:** Answers questions using account information, previous conversations, and company knowledge base.
- **Human review:** Human support agent takes over when requested or when the AI cannot resolve the issue.
- **Output:** AI-generated responses and support recommendations.
- **Disclosure/logging:** Clearly disclose that the customer is interacting with an AI assistant and log conversations for quality assurance.

**Provider / Deployer / Vendor**

- **Provider:** Chatbot software vendor or internal AI development team.
- **Deployer:** Telecom company.
- **Vendor:** Third-party LLM provider (e.g., OpenAI, Azure OpenAI).

**Required obligations or controls**

- Clearly inform users that they are interacting with AI.
- Ensure customers can easily reach a human agent.
- Comply with GDPR regarding customer account data and conversation history.

**Decision**

🟡 **Approve with controls**

# Approval Pack – AI Customer Support Assistant

## Executive Summary

The proposed AI assistant is designed to answer customer service questions and reduce workload for human support agents. The system primarily triggers **transparency obligations** under the EU AI Act because customers interact directly with AI. The project may proceed provided appropriate disclosures and governance measures are implemented.

---

## Client Use Case

A telecom company wants to introduce an AI assistant on its support website that answers billing questions, explains available plans, and assists customers with routine requests. The assistant can transfer conversations to human support staff when necessary but currently does not clearly inform customers that they are communicating with AI.

---

## Inferred AI Act Category

**Limited Risk / Transparency**

### Reasoning

Customers interact directly with an AI system. The assistant provides information rather than making legally significant decisions, making transparency the primary regulatory requirement.

---

## Proposed AI Architecture

**Business trigger**

Customer initiates an online support chat.

**System behavior**

The AI retrieves relevant company information and customer account data to generate responses.

**Human review**

Complex conversations are transferred to a human support representative.

**Output**

AI-generated customer support responses.

**Disclosure**

Customers should be informed that they are interacting with an AI assistant.

**Logging**

Conversation logs should be maintained for quality assurance and service improvement.

---

## Roles

**Provider**

Chatbot software provider or internal AI development team.

**Deployer**

Telecommunications company.

**Vendor**

Third-party LLM provider.

---

## Compliance Implications

The company should:

- clearly disclose AI interaction,
- allow customers to contact a human representative,
- comply with GDPR when processing customer data,
- monitor chatbot performance.

---

## Decision

## 🟡 Approve with Controls

Deployment is appropriate once transparency and customer communication requirements have been implemented.

-----
-----

# Case 3 – AI Checkout Behavior Analysis
A large online clothing store wants to add a small camera to the checkout page on their website, using the customer's own webcam. The AI watches the customer's face during checkout and tries to detect stress, confusion, or hesitation. When it detects hesitation, the system automatically shows urgent messages like "Only 2 left!" or "Price goes up in 5 minutes!" to push the person to finish the purchase fast. The store believes this will lower cart abandonment. Customers are not told the camera is analyzing their face or mood. No human checks or approves these messages before they are shown, everything runs automatically in real time.

**Likely category**

Prohibited

The system analyzes customers' facial expressions to infer emotional or mental states and immediately uses those inferences to influence purchasing behavior through targeted pressure tactics. This combines emotion inference with manipulative commercial practices and lacks transparency or meaningful human oversight.

**Proposed AI architecture**

- **Business trigger:** Customer reaches the online checkout.
- **AI behavior:** Processes webcam images to estimate behavioral indicators and automatically selects urgency messages.
- **Human review:** None; messages are generated automatically in real time.
- **Output:** Personalized urgency prompts during checkout.
- **Logging:** Interaction logs could be stored, but this does not resolve the legal issue.

**Provider / Deployer / Vendor**

- **Provider:** AI marketing analytics vendor.
- **Deployer:** Online clothing retailer.
- **Vendor:** Computer vision and AI inference service.

**Required obligations or controls**

- The proposed use should **not** be deployed.
- Redesign the solution to remove emotion or behavioral inference from webcam analysis.
- If personalization is desired, use lawful contextual information such as shopping cart contents, purchase history, or browsing behavior instead of biometric analysis.
- Ensure compliance with GDPR for any customer data processing.

**Decision**

❌ **Deny and redesign**

# Approval Pack – AI Checkout Behavior Analysis

## Executive Summary

The proposed system analyzes customers through their webcams during online checkout and adapts marketing messages based on inferred behavioral signals. This proposal falls within the **Prohibited** category of the EU AI Act and should not be deployed as designed. A lawful alternative is recommended.

---

## Client Use Case

An online clothing retailer wants to reduce shopping cart abandonment by analyzing customers' facial expressions during checkout. The AI automatically displays urgency messages whenever it predicts hesitation or uncertainty. The entire process runs automatically without human review.

---

## Inferred AI Act Category

**Prohibited**

### Reasoning

The system infers emotional or behavioral states from customers' biometric data and immediately uses those inferences to manipulate purchasing behavior. This creates significant concerns under the prohibited AI practices established by the AI Act.

---

## Proposed AI Architecture

**Business trigger**

Customer reaches the checkout page.

**System behavior**

The AI analyzes webcam images to infer behavioral indicators and automatically selects personalized urgency messages.

**Human review**

None.

**Output**

Personalized real-time marketing messages.

**Logging**

Interaction logs may be stored, although logging does not resolve the legal issues associated with the proposed design.

---

## Roles

**Provider**

AI marketing software vendor.

**Deployer**

Online clothing retailer.

**Vendor**

Computer vision and AI inference provider.

---

## Compliance Implications

The proposed implementation should not be deployed because it relies on biometric analysis to infer customer behavior and uses those inferences to influence purchasing decisions.

---

## Decision

## ❌ Deny and Redesign

### Recommended Lawful Alternative

Replace webcam analysis with personalization based on lawful business information such as:

- shopping cart contents,
- browsing history,
- previous purchases,
- voluntarily provided customer preferences.

This achieves personalized recommendations without relying on biometric or behavioral inference.

-----
-----


# Case 4 – AI Recruitment Screening
A mid-size logistics company gets many job applications for warehouse and driver roles. They want an AI tool that reads resumes and short video interviews, then gives each candidate a score and a rank. Only candidates above a certain score move to a human interview, the rest get an automatic rejection email. The AI looks at work history, keywords in the resume, and tone of voice in the video. HR staff can technically see the score, but in practice they trust the ranking and rarely change it.

**Likely category**

High-risk

The AI evaluates and ranks job applicants and determines which candidates progress in the recruitment process. Employment is one of the high-risk areas under Annex III because AI decisions can significantly affect individuals' career opportunities. Human oversight exists only formally, since HR rarely challenges the AI ranking.

**Proposed AI architecture**

- **Business trigger:** New job applications are submitted.
- **AI behavior:** Analyzes resumes and video interviews to score and rank candidates.
- **Human review:** HR reviews recommendations before invitations or rejections are sent, with genuine authority to override AI recommendations.
- **Output:** Candidate ranking and hiring recommendations.
- **Logging:** Maintain decision logs, audit trails, model documentation, and reasons for overrides.

**Provider / Deployer / Vendor**

- **Provider:** Recruitment AI software vendor.
- **Deployer:** Logistics company.
- **Vendor:** Third-party AI platform and possibly an external LLM provider.

**Required obligations or controls**

- Establish meaningful human oversight rather than automatic acceptance of AI rankings.
- Maintain technical documentation and audit logs.
- Perform risk management and testing for bias, fairness, and accuracy.
- Ensure data governance and GDPR compliance.
- Train HR staff on appropriate use and limitations of the system.

**Decision**

🟡 **Approve with controls**

# Approval Pack – AI Recruitment Screening

## Executive Summary

The proposed AI recruitment system supports candidate evaluation and ranking during hiring. Employment decisions are classified as **High-Risk AI** under the EU AI Act because they can significantly affect individuals' career opportunities. The project should only proceed after appropriate governance, documentation, and oversight mechanisms have been established.

---

## Client Use Case

A logistics company wants to use AI to evaluate resumes and video interviews for warehouse and driver positions. The AI produces candidate scores and rankings, and applicants below a predefined threshold receive automatic rejection emails. HR staff can review the rankings but rarely override the recommendations.

---

## Inferred AI Act Category

**High-Risk**

### Reasoning

The AI influences recruitment decisions and therefore affects access to employment, placing it within the high-risk category under the AI Act.

---

## Proposed AI Architecture

**Business trigger**

Submission of a job application.

**System behavior**

The AI evaluates resumes and video interviews to generate candidate rankings.

**Human review**

Recruiters review recommendations before interview invitations or rejection decisions are finalized. Human reviewers must have genuine authority to override AI recommendations.

**Output**

Candidate scores, rankings, and hiring recommendations.

**Logging**

Maintain complete audit trails, model documentation, performance records, and documentation of human overrides.

---

## Roles

**Provider**

Recruitment AI software vendor.

**Deployer**

Logistics company.

**Vendor**

Third-party AI platform and language model provider.

---

## Compliance Implications

Before deployment, the company should implement:

- risk management,
- data governance,
- technical documentation,
- meaningful human oversight,
- audit logging,
- bias and performance testing,
- GDPR compliance,
- staff training.

Current practice, where HR rarely questions AI recommendations, should be changed to ensure genuine human oversight.

---

## Decision

## 🟡 Approve with Controls

Deployment is appropriate only after implementing the required high-risk AI governance framework and ensuring meaningful human oversight throughout the recruitment process.