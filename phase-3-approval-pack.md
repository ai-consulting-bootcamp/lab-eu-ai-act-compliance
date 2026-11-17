# EU AI Act Approval Pack — Partner briefs

**Prepared for:** LindenDesk, HafenWerk, KiezRad and Tonwerk Supply  
**Scope:** Initial EU AI Act approval decision from the supplied briefs  
**Export target:** Three pages maximum

## Executive summary

The four proposals span the full risk spectrum. LindenDesk’s design should not launch: it infers employee emotions from facial and vocal signals in the workplace, which is a prohibited practice unless a narrow medical or safety exception applies; the brief gives no such exception. HafenWerk’s recruitment ranking is high-risk because it assists selection for employment. It can proceed only after provider evidence and deployer controls make human oversight, data quality, traceability and applicant safeguards real in operation. KiezRad’s chatbot is a limited-risk deployment whose launch depends on clear disclosure that customers are speaking with AI and on a strict boundary around transactions and escalation. Tonwerk’s internal record-grouping tool is minimal risk and can be approved with ordinary quality, security and data-governance safeguards.

The decisions are therefore: **deny and redesign** (LindenDesk), **approve with controls** (HafenWerk), **approve with controls** (KiezRad), and **approve** (Tonwerk Supply).

## Case 1 — LindenDesk: workplace coaching flags

**Inferred category:** Prohibited — Article 5(1)(f) workplace emotion recognition.

**Architecture and roles.** A weekly video recording is sent to a vendor model. The model analyses facial movements and vocal prosody, infers “frustrated”, “disengaged” or “anxious”, and names employees for a team lead’s coaching queue. The vendor is the likely provider; LindenDesk is the employer/deployer. A video host may separately process the recordings.

**Compliance assessment.** The proposed purpose—staff development—does not turn emotion recognition into a permitted use. Team-lead review and override are not enough because the prohibited inference is still made and used in the workplace. The launch decision is **Deny and redesign**. LindenDesk should stop the proposed processing, confirm retention/deletion arrangements, and obtain GDPR and worker-monitoring advice before testing any replacement.

**Lawful redesign.** Replace emotional inference with an employee-facing coaching workflow based on observable role-play criteria: policy coverage, response structure, turn-taking, and the employee’s own selected coaching goals. Produce team-level trends or voluntary individual feedback, not an emotion score or performance ranking. Keep a human coach responsible for the feedback and prohibit disciplinary use.

## Case 2 — HafenWerk: technician applicant ranking

**Inferred category:** High-risk — Article 6(2), Annex III 4(a), employment and recruitment.

**Architecture and roles.** Applications, certifications and screening answers enter a vendor ATS. The system ranks candidates and presents a top 30; a recruiter reviews and can override the ranking; HR signs the interview list. The ATS vendor is the likely provider, while HafenWerk is the employer/deployer. If HafenWerk rebrands or substantially changes the system, the provider analysis must be revisited.

**Compliance assessment and controls.** Do not operate the current “top 30 first” workflow as a de facto exclusion rule. Before go-live, require the vendor’s risk-management, data-governance, technical-documentation, logging, accuracy, robustness, cybersecurity and conformity evidence. HafenWerk must:

- assign trained human oversight with time and authority to challenge the ranking;
- validate that the input data is relevant and sufficiently representative for each technician role;
- test for disparate outcomes and prevent use of sensitive or unlawfully inferred attributes;
- review candidates outside the initial ranking rather than treating the cut-off as final;
- retain model/version, input, output, reviewer, override and incident records;
- inform affected applicants where required and provide an appropriate route to ask questions or challenge an outcome; and
- monitor drift, complaints and serious incidents after launch.

The decision is **Approve with controls**, gated on documented evidence and a tested operating procedure. A human signature alone is not sufficient if the process systematically follows the model.

## Case 3 — KiezRad: customer-support assistant

**Inferred category:** Limited risk / transparency — Article 50(1).

**Architecture and roles.** A customer opens a website chat. A hosted language model retrieves approved help-article content and generates an ordinary-language reply. Billing disputes are handed to support, while the assistant cannot access accounts, charge cards or change bookings. KiezRad is the deployer and is likely the provider of the customer-facing system if it puts it into service under its name; the hosted-model company is the GPAI model provider or technical vendor, depending on the contract and product setup.

**Compliance assessment and controls.** Because the system directly interacts with customers, the interface must clearly say that the customer is communicating with AI unless that is already obvious. The notice should appear at the start of the chat, not only in a privacy policy, and the experience must not imply that a human agent is replying. Keep the transaction boundary technically enforced, route disputes and uncertainty to a human, constrain retrieval to approved content, test prompt injection and harmful advice, and log interactions under a documented retention policy. Confirm vendor data-use, security and GDPR terms. Also ask the provider whether machine-readable marking is required for the system’s generated text under Article 50(2), and record the answer.

The decision is **Approve with controls** after the disclosure, escalation path, content controls and vendor review pass acceptance testing.

## Case 4 — Tonwerk Supply: catalog duplicate candidates

**Inferred category:** Minimal risk.

**Architecture and roles.** A nightly batch compares item names, dimensions, material and unit size, and sends candidate pairs to an internal queue. A catalog editor accepts, rejects or corrects each pair; the system never merges records and does not assess staff or customers. The model/software vendor is the likely provider; Tonwerk Supply is the deployer.

**Compliance assessment and controls.** On the supplied facts, this is not an Annex III decision system and does not trigger a specific AI Act obligation. Approve it with routine safeguards: maintain the human approval gate, measure false matches, restrict queue access, retain a change log, and review vendor security and data use. Check whether item metadata contains personal or confidential information and apply GDPR or contractual controls if it does.

The decision is **Approve**.

## Go-live conditions and escalation

LindenDesk is not approved for the proposed design. HafenWerk and KiezRad need named owners, test evidence and a signed operating procedure before launch. Tonwerk needs a catalog-quality and vendor-security check. A legal/privacy team should verify the final interpretation, particularly for employee monitoring, applicant information rights, role allocation between KiezRad and its hosted-model vendor, and any personal data in the catalog.

## Sources

- [EU AI Act — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [European Commission — transparency obligations under Article 50](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)
- [European Commission — navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act)

This pack is a lab deliverable and not legal advice.
