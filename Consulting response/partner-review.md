# Consulting Review: Partner Scenarios

## Executive summary

Cases 1 and 4 appear to be minimal-risk uses under the EU AI Act, with ordinary accuracy, safety, confidentiality, and data-protection concerns.

Case 2 should be rejected as proposed because the system targets patients in vulnerable situations with misleading pressure to accept expensive loans.

Case 3 is high risk because the system ranks job applicants and recommends who should be interviewed.

---

## Case 1 — Equipment quotation assistant

**Likely category:** Minimal risk under the EU AI Act.

**Why:** The system compares business documents and drafts a quotation. A qualified employee checks the technical evidence, supplier, and price before sending it. The AI does not operate equipment or make a decision about a person. The possible safety consequences still need careful attention, but they do not by themselves make this an EU AI Act high-risk use.

**Proposed AI architecture:** The system compares the customer’s requirements with supplier documents and approved company records. It drafts a proposal and links technical claims to supporting documents. A technical expert checks every claim, confirms the supplier and price, and approves the final proposal. The system stops the proposal when important evidence is missing or a discrepancy remains unresolved.

**Roles:** The software company is the provider. The equipment trading company is the deployer. Any external AI or document-processing service is a third-party vendor.

**Controls:** Use only approved and current documents. Keep links between claims and their evidence. Require expert approval before sending. Protect customer and supplier information. Check product-safety and other applicable laws separately.

**Decision:** Approve with these operational controls.

---

## Case 2 — Patient loan targeting

**Likely category:** Prohibited as described.

**Why:** The system uses patients’ urgent medical needs and limited finances to target them with more expensive loans. It also claims that patients will lose access to medicine if they do not accept quickly, even though the medicine remains available. This appears to exploit people’s vulnerability and pressure them into decisions that could cause serious harm. An employee reviewing the messages does not fix the underlying policy.

**Proposed AI architecture:** Do not use AI to target patients based on medical urgency or financial hardship, and do not send false deadlines. A redesigned system could provide the same accurate, neutral loan information to everyone who asks, show the full cost and available alternatives, and give people enough time to decide. A trained employee should be available to answer questions.

**Roles:** The software company is the provider. The pharmaceutical trading company is the deployer. Any external AI or messaging service is a third-party vendor.

**Controls:** Remove vulnerability-based targeting and false urgency. Check all information for accuracy. Make loan terms and costs clear. Give patients a real choice and a way to contact a person.

**Decision:** Deny the proposed design. Consider only the redesigned version.

---

## Case 3 — Recruitment ranking software

**Likely category:** High risk.

**Why:** The system scores and ranks job applicants and recommends who should be interviewed. The EU AI Act lists AI used to analyse or filter job applications and evaluate candidates as high risk. Human review is important, but it does not automatically change the system’s category.

**Proposed AI architecture:** The system compares each CV with documented job criteria and provides a score with reasons linked to the CV. A trained recruiter reviews the CV and the AI’s reasons, can change the ranking, and makes the final interview decision. The system must not automatically reject applicants.

**Roles:** The recruitment software company is the provider. The trading company using it is the deployer. Any external AI or recruitment-platform vendor is a third-party vendor.

**Controls:** Before use, check that the provider has completed the required high-risk system safeguards. Test for inaccurate or unfair results. Give recruiters training, time, and authority to question or override recommendations. Keep appropriate records, monitor performance, and tell applicants when the system is used to assist decisions about them.

**Decision:** Approve only after the required safeguards are demonstrated and the company has a reliable human-review process.

---

## Case 4 — Internal document filing

**Likely category:** Minimal risk under the EU AI Act.

**Why:** The system sorts documents into existing archive categories. It does not assess employees, rewrite documents, or make decisions about people. An administrator checks uncertain classifications and can correct mistakes.

**Proposed AI architecture:** The system reads document text and metadata, selects a predefined project and document type, and files the original document in the matching location. Uncertain cases go to the records administrator. The original file and its access permissions remain unchanged.

**Roles:** The software company is the provider. The trading company is the deployer. Any external storage or AI service is a third-party vendor.

**Controls:** Preserve original files and access permissions. Restrict access to authorized staff. Protect confidential information. Let the administrator correct filing mistakes and keep a record of those corrections.

**Decision:** Approve with basic accuracy, access, and data-protection controls.

---

## Closing note

The most important difference between the cases is how the AI affects people. Case 2 pressures patients in a vulnerable situation and should be rejected as proposed. Case 3 can affect people’s job opportunities, so it needs high-risk safeguards. Cases 1 and 4 mainly support business tasks, with human checks and ordinary safety or privacy controls.