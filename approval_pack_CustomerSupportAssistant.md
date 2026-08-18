# Approval Pack – AI Customer Support Assistant

**Client:** Confidential – Telecommunications Company  
**Project:** AI-Powered Customer Support Assistant  
**Document Version:** 1.0  
**Prepared by:** AI Consulting Team  
**Assessment Scope:** EU AI Act Compliance and Deployment Readiness Review

---

# Executive Summary

## Recommendation

**Approve with Controls.**

The proposed AI customer support assistant can be deployed, provided several governance and transparency measures are implemented before launch. Based on the information available, the solution is classified as a **Limited Risk AI system** under the EU AI Act because customers interact directly with AI while seeking support.

The primary compliance issue identified during this assessment is the absence of clear disclosure that customers are communicating with an AI assistant. Although the chatbot does not make legally binding decisions regarding customers' accounts or contracts, users should be informed that they are interacting with AI and should be able to request human assistance whenever appropriate.

The project presents a relatively low regulatory burden, and the required controls are straightforward to implement.

---

# 1. Business Context

The client operates a national telecommunications company with a high volume of customer service requests related to billing, subscription plans, invoices, roaming services, and account management.

To reduce waiting times and improve customer experience, the company proposes introducing an AI-powered virtual assistant capable of answering routine customer questions through the company website.

The assistant would use customer account information, previous conversations, and internal knowledge articles to generate responses. Complex requests would be transferred to a human customer service representative.

During the discovery meeting, the client indicated that the assistant should sound as natural as possible because customers "prefer talking to what feels like a real support agent."

---

# 2. AI Act Assessment

## Classification

**Limited Risk (Transparency Obligations)**

## Assessment Rationale

The proposed solution does not perform decisions that significantly affect customers' legal rights or access to essential services. Instead, it provides conversational support and information.

However, customers interact directly with an AI system and may reasonably believe they are communicating with a human support representative. Under Article 50 of the EU AI Act, users should be informed when they are interacting with AI unless this is obvious from the context.

Based on the current proposal, the lack of disclosure represents the primary compliance gap.

No prohibited practices or Annex III high-risk use cases have been identified.

---

# 3. Proposed Operating Model

## Business Trigger

Customer opens the online support chat.

↓

## AI Processing

The conversational AI retrieves information from:

- customer account records,
- previous support conversations,
- product documentation,
- internal knowledge base.

The model generates a response to the customer's request.

↓

## Human Decision Point

The conversation is transferred to a customer support representative when:

- the customer requests human assistance,
- confidence in the AI response is low,
- the request exceeds predefined operational limits,
- account-specific intervention is required.

↓

## Customer Output

The customer receives either:

- an AI-generated response, or
- assistance from a human support representative.

↓

## Monitoring and Logging

The company should retain:

- conversation logs,
- escalation records,
- customer satisfaction metrics,
- AI confidence scores,
- feedback from human support agents.

These records support quality assurance and continuous improvement while enabling investigation of customer complaints.

---

# 4. Roles and Responsibilities

| Function | Responsible Party |
|-----------|-------------------|
| **AI Provider** | Internal AI development team or chatbot software vendor |
| **AI Deployer** | Telecommunications company |
| **Technology Vendors** | Large Language Model provider, cloud infrastructure provider, customer service platform |

The deployer remains responsible for ensuring that customers are appropriately informed about AI interaction and that the system operates within its intended purpose.

---

# 5. Compliance Considerations

The following measures should be implemented before deployment.

### Transparency

Customers should receive a clear notification at the beginning of every conversation that they are interacting with an AI assistant.

The disclosure should be prominent, understandable, and presented before substantive interaction begins.

---

### Human Escalation

Customers should always have an accessible option to transfer the conversation to a human support representative.

Escalation should occur automatically whenever:

- confidence is low,
- repeated misunderstandings occur,
- sensitive account actions are requested.

---

### Data Protection

Because the assistant processes customer account information and conversation history, the company should ensure compliance with GDPR, including:

- lawful processing,
- data minimization,
- secure storage,
- appropriate retention periods.

---

### Operational Governance

The client should establish procedures for:

- monitoring response quality,
- reviewing inaccurate responses,
- managing model updates,
- documenting significant changes,
- responding to customer complaints involving AI-generated information.

---

# 6. Key Risks

| Risk | Potential Impact | Recommended Mitigation |
|------|------------------|------------------------|
| Customers believe they are communicating with a human | Non-compliance with AI Act transparency obligations | Clearly disclose AI interaction at the beginning of every conversation |
| Incorrect or incomplete AI responses | Customer dissatisfaction or misinformation | Human escalation pathway and continuous quality monitoring |
| Unauthorized access to customer data | Privacy and regulatory risk | GDPR compliance, access controls, encryption, security monitoring |
| Excessive reliance on AI support | Reduced service quality for complex issues | Maintain human support availability and clear escalation rules |

Overall implementation risk is assessed as **Low to Moderate**.

---

# 7. Final Recommendation

## Decision

# 🟡 APPROVE WITH CONTROLS

The proposed customer support assistant is suitable for deployment after implementing the required transparency and governance measures.

The system falls within the **Limited Risk** category under the EU AI Act. The principal compliance obligation is ensuring that customers understand they are interacting with AI. Additional operational controls—including human escalation, monitoring, and data protection—will further strengthen the solution and improve customer trust.

The consulting team recommends proceeding with implementation once these controls have been incorporated into the deployment plan.

---

# Next Steps

1. Add a clear AI disclosure at the start of every conversation.
2. Implement simple and immediate transfer to a human support representative.
3. Define confidence thresholds for automatic escalation.
4. Establish conversation monitoring and quality assurance procedures.
5. Review GDPR compliance for customer account data and conversation history.
6. Document governance responsibilities for future model updates and operational oversight.