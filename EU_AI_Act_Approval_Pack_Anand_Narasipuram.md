# EU AI Act Approval Pack - Anand Narasipuram

---

## PART 1 — Private Answer Key

| Case | Client brief (summary) | Intended category | Why this category |
|---|---|---|---|
| 1 | Energy retailer wants an AI "reliability score" for residential customers, blending smart-meter usage, social-media sentiment, and neighborhood socioeconomic data, used to decide who gets a forced prepayment meter — score not disclosed, no human review | **Prohibited (Art. 5)** | This is social scoring: the system evaluates/classifies people based on unrelated social behavior (social media, neighborhood data) and applies the score to produce detrimental treatment (forced prepayment meters) in a context unrelated to where the data was gathered, with no transparency or human oversight. |
| 2 | HR-tech vendor builds an AI CV-screening and video-interview-analysis tool sold to utility companies to automatically shortlist/reject field technician candidates | **High-risk (Annex III — employment/recruitment)** | AI used to screen, filter, and evaluate candidates in a recruitment process falls squarely under the Annex III employment category. It affects access to employment, a fundamental interest, and can encode bias in hiring — hence high-risk with mandatory risk management, data governance, human oversight, and documentation obligations. |
| 3 | Retail bank deploys a website chatbot for customer service that can also generate marketing copy and synthetic voice snippets for outbound campaign calls | **Limited risk / transparency (Art. 50)** | The chatbot interacts directly with natural persons and the system generates synthetic voice content. Both trigger disclosure duties: users must be told they're interacting with AI, and AI-generated/synthetic audio content must be identifiable as such. No high-risk classification applies since it doesn't fall under an Annex III use case. |
| 4 | Logistics company uses an AI model to optimize warehouse shelf-restocking schedules based on historical demand and sales data | **Minimal risk** | The system operates purely on internal operational/inventory data, does not process personal data about individuals in a way that affects their rights, and doesn't fall under any Annex III category or transparency trigger. No specific AI Act obligations apply, though general GDPR and data-quality diligence still apply if any personal data is incidentally involved. |

---

## PART 2 — Consulting Response (share this with your partner)

*Categories removed. Present these as real client briefs.*

### Case 1
A regional energy retailer is exploring a new "customer reliability" model. The idea: combine smart-meter consumption patterns with publicly available social media activity and neighborhood-level income/demographic data to generate a single risk score per household. Customers who score below a threshold would automatically be switched to a prepayment meter, without being told why or being able to contest the decision beforehand. The retailer wants this rolled out quietly, without publicizing the scoring logic, to avoid customers "gaming" the system.

- **Affected parties:** Residential customers, especially in lower-income areas
- **Human review:** None planned — fully automated switch trigger
- **Data used:** Smart-meter data, social media activity, neighborhood socioeconomic indicators

### Case 2
An HR-tech startup is building a screening product aimed at utility and infrastructure companies that hire large numbers of field technicians every year. The tool scans incoming CVs and, for shortlisted candidates, analyzes recorded video interviews (tone, word choice, facial expressions) to produce a fit score. Recruiters would see a ranked candidate list and could technically override it, but in practice the client expects recruiters to just process the top-ranked names given hiring volume.

- **Affected parties:** Job applicants
- **Human review:** Technically possible, rarely exercised in practice
- **Data used:** CV text, video interview recordings (audio, facial expression, tone)

### Case 3
A retail bank wants to modernize its customer support. Plan: a website chatbot that answers account questions and, separately, a marketing team tool that generates short promotional scripts and synthetic voice clips for outbound phone campaigns, using a cloned "brand voice." Customers calling in would hear the AI voice without necessarily being told it isn't a human, since the marketing team feels a human-sounding voice performs better in tests.

- **Affected parties:** Bank customers and prospects contacted via chatbot or outbound calls
- **Human review:** Marketing team reviews scripts before campaigns go live; no review during live chatbot conversations
- **Data used:** Customer account queries (chatbot), campaign targeting data (voice calls)

### Case 4
A mid-size logistics company wants to reduce stockouts and overstocking in its warehouses. They're proposing an AI model that looks at historical sales, seasonality, and supplier lead times to automatically generate restocking schedules and purchase order suggestions for the warehouse team, who review and approve before anything is ordered.

- **Affected parties:** Internal warehouse/procurement staff (as users), no external individuals directly affected
- **Human review:** Warehouse team approves every generated purchase order
- **Data used:** Historical sales data, seasonality trends, supplier lead-time data
