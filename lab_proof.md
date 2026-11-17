# Lab Proof

This is a lab project created for training and evaluation purposes only. It does not use any real personal, employee, customer, or business data. All examples, scenarios, and case studies are fictional and intended for compliance education, not for production, legal, regulatory, or operational decision-making.


This file confirms the completion of the EU AI Act compliance lab setup for this repository.

## Phase 1: Build the hidden client brief
Cases proposed by the LAB partner (Ayhan Demir)

### Case 1
Kleinanzeigen sellers lose buyers by replying late. Idea: an opt-in assistant in the in-app chat that answers buyer questions while the seller is offline, using the listing, the seller's past replies and price rules, in the seller's own tone. Messages appear under the seller's name with no label. Nobody reviews them live; sellers can read the thread later and switch it off.

### Case 2
Logiflex Fulfilment GmbH, a 3PL near Leipzig (~900 staff), faces a 2027 headcount cut and wants an 'objective' basis for who stays. A vendor tool would score each employee from pick rates, call handle times, voice tone on calls and webcam facial expressions in meetings, flagging stress and disengagement. The ranked list feeds the redundancy shortlist. HR makes the final call; the works council is asking questions.

### Case 3
Kessler Hausgeraete AG, a washing machine plant in Franconia, is losing margin to scrap and press-line stops. Cameras would check welds and finish, and vibration and temperature sensors would predict press failures, using images, sensor data and the MES shift log with operator IDs. A quality engineer checks flagged parts and a planner approves work orders. The plant manager asks if it could show 'which shift is weaker'.

### Case 4
Amazon EU Customer Service (hypothetical) wants a 'team contribution map' showing how each team moves CSAT, contacts per order and first contact resolution. An in-house model uses contact logs, QA scores and survey text. Phase 2: an individual score per associate to pick who moves to escalations and who enters the promotion pool. Managers approve the suggestions; in the pilot they changed under 5%.

### Cases Evaluation

| Case | Intended category | Why you chose it |
|---|---|---|
| 1 | Limited risk / transparency, with consumer-protection concerns | The assistant interacts directly with buyers, so they should be told they are interacting with AI. Unlabeled replies may mislead buyers or create false trust; consumer-protection rules may also apply. |
| 2 | Prohibited | The system infers emotions from biometric data in the workplace. This is prohibited under the AI Act except for limited medical or safety purposes, which are not described here. Its use in redundancy decisions also raises serious employment, GDPR, and labor-law concerns. |
| 3 | Minimal risk| The system supports manufacturing quality and maintenance. Comparing weld defect rates by shift is process analysis, not worker evaluation. Reassess if it becomes part of a safety-critical component or is used to score employees. |
| 4 | High-risk | Individual scoring influences worker evaluation, work allocation, and promotion decisions, which are employment-related high-risk uses. Manager approval does not remove the classification, and the low override rate warrants checking whether review is meaningful. |


## Phase 2: Review your partner as the consultant

### Practical AI Act risk assessment
| Case | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|
| 1 — Kleinanzeigen seller assistant | **Trigger:** A buyer asks a question while the seller is offline.<br>**Model:** Uses listing details, seller-approved price rules, and past replies to generate an answer in the seller’s tone.<br>**Human:** Seller opts in, can switch it off or take over; provide human handover.<br>**Output:** Buyer receives a clearly labeled AI-assisted reply.<br>**Layer:** Disclosure, conversation logs, seller controls, and a complaint route. | - **Provider:** Kleinanzeigen, if it offers the assistant under its name.<br>- **Deployer:** Sellers using it for commercial activity.<br>- **Vendor:** Underlying model supplier, if separate from Kleinanzeigen. | Clearly disclose AI interaction; do not present automated replies as personally written by the seller. Provide opt-in, override, and opt-out; protect chat data; log and review responses; consider consumer-protection requirements. | **Approve only with controls; not as currently designed without a label.** |
| 2 — Logiflex employee scoring | **Trigger:** The company prepares its redundancy shortlist.<br>**Model:** Analyzes worker metrics, call tone, and webcam expressions to infer stress or disengagement and score employees.<br>**Human:** HR reviews the ranking; the works council has raised concerns.<br>**Output:** Employee scores feeding a redundancy shortlist.<br>**Layer:** No oversight or disclosure measure makes the prohibited emotion-recognition use acceptable; remove the emotion-analysis feature. | - **Provider:** Vendor supplying the system, if it offers it under its name.<br>- **Deployer:** Logiflex.<br>- **Vendor:** External model or analytics supplier, if different from the system provider. | Do not deploy workplace emotion recognition except for the narrow medical or safety purposes allowed by the Act. Redesign without emotion inference or voice-tone and webcam analysis. Consult the works council and address GDPR and labor-law requirements. Any AI used to rank people for redundancy needs a separate high-risk employment assessment. | **Deny and redesign.** |
| 3 — Kessler weld inspection and press maintenance | **Trigger:** A camera captures a weld or sensor readings indicate a possible press fault.<br>**Model:** Detects weld defects, predicts press failures, and aggregates weld-quality trends by shift.<br>**Human:** A quality engineer checks flagged parts; a planner approves work orders.<br>**Output:** Defect alerts, maintenance predictions, and shift-level process-quality trends.<br>**Layer:** Quality and maintenance logs; minimize or pseudonymize operator IDs and do not create worker scores. | - **Provider:** External system supplier, or Kessler if it develops/offers the system under its own name.<br>- **Deployer:** Kessler, using the system in its plant.<br>- **Vendor:** External AI, camera, or integration supplier, if any. | Validate model performance; retain quality and maintenance review; limit use to process monitoring, not worker evaluation; protect operator data. Confirm whether the system is part of a safety component, which could change its AI Act classification. | **Approve with controls.** |
| 4 — Amazon customer-service contribution map | **Trigger:** Customer-service metrics are reviewed for team planning, escalation assignments, or promotion decisions.<br>**Model:** Aggregates team metrics and scores individual associates to recommend escalation assignments and promotion candidates.<br>**Human:** Managers review recommendations, but changed fewer than 5% in the pilot; review must be meaningful.<br>**Output:** Team contribution map and individual employment recommendations.<br>**Layer:** High-risk documentation, records, monitoring, and human-oversight controls. | - **Provider:** Amazon, if it develops and puts the in-house system into service.<br>- **Deployer:** Amazon EU Customer Service, using the system for employment-related recommendations.<br>- **Vendor:** External model or platform supplier, if any; role depends on how it contributes to the system. | Treat individual recommendations as high-risk employment AI. Complete applicable provider requirements, including risk management, data governance, documentation, logging, accuracy, robustness, and conformity assessment. Inform affected workers and representatives as required; test for bias; ensure meaningful human review and a way to challenge outcomes. | **Do not launch individual scoring until high-risk requirements and effective human review are in place.** |
## Phase 3: Approval pack

### Executive summary — Can we launch these?

Not all four proposals can launch as designed. Case 1 can launch only with clear AI disclosure and bounded seller-approved responses. Case 2 must be denied because workplace emotion inference is prohibited for the proposed purpose; a non-biometric, human-led redesign is possible. Case 3 is minimal risk if it stays focused on product quality and equipment maintenance, with operator data protected. Case 4 is high-risk employment AI: it is not automatically prohibited, but individual recommendations must wait until the required controls, documentation, and meaningful human oversight are in place.

### Case 1 — Kleinanzeigen seller assistant

**Inferred category:** Limited risk / transparency.

**Proposed architecture and roles:** A buyer message triggers an assistant using the listing, seller-approved price rules, and past replies to answer while the seller is offline. Kleinanzeigen is the provider if it offers the feature under its name; sellers using it are deployers; a separate model supplier is a vendor. The assistant may send within those approved boundaries, but must offer seller takeover, opt-out, and human handover.

**Compliance implications:** Tell buyers clearly that they are interacting with AI; do not imply the seller personally wrote each reply. Constrain answers to verified listing details and approved terms, log interactions, protect chat data, and provide a way to report problems. Address privacy and consumer-protection risks, including misleading claims or commitments.

**Decision:** **Approve with controls.** Do not launch the current unlabeled version.

### Case 2 — Logiflex employee scoring

**Inferred category:** Prohibited as proposed.

**Proposed architecture and roles:** The vendor system combines pick rates and call metrics with voice tone and webcam expressions to infer stress or disengagement, then ranks workers for redundancy. The system supplier is the provider; Logiflex is the deployer; any separate model supplier is also a vendor. HR receives the ranking; affected employees and the works council are directly implicated.

**Compliance implications:** Workplace emotion recognition is prohibited for this purpose; HR review does not make it permissible. The proposal also raises substantial employment, data-protection, discrimination, labor-law, and works-council concerns. Any redesigned AI that evaluates or ranks workers for employment decisions would need a separate high-risk assessment.

**Decision:** **Deny and redesign.** Remove emotion inference, voice and facial analysis, and AI-generated individual redundancy rankings. A more lawful direction is a human-led process using documented, job-relevant criteria, with works-council consultation, reasons recorded, access restricted, and a route for employees to challenge errors. If AI is retained, limit it to genuinely aggregate workforce planning that cannot evaluate or rank individuals; assess any proposed feature before use.

### Case 3 — Kessler weld inspection and press maintenance

**Inferred category:** Minimal risk, provided the system remains process-focused.

**Proposed architecture and roles:** Cameras identify weld or finish defects; vibration and temperature sensors predict press faults; MES shift logs support process trends. A quality engineer checks flagged parts and a planner approves work orders. Kessler is the deployer and is also the provider if it develops or offers the system under its own name; an external inspection, maintenance, or model supplier may be the provider or vendor depending on its role.

**Compliance implications:** Keep the purpose to quality and maintenance, not worker assessment. Validate performance, retain inspection and maintenance records, secure the data, and remove or pseudonymize operator IDs where feasible. Check whether the AI is a safety component of regulated machinery, which could change its classification. GDPR and labor-law requirements may still apply to operator-linked data; do not use shift trends to make misleading claims about individual workers.

**Decision:** **Approve with controls.** This is an approval for process monitoring, not worker scoring; reassess before any safety-critical or employment-related use.

### Case 4 — Amazon customer-service contribution map

**Inferred category:** High-risk employment AI for individual scoring and recommendations.

**Proposed architecture and roles:** The in-house model aggregates contact logs, QA scores, and survey text, then scores associates to recommend escalation assignments and promotion candidates. Amazon is the provider if it develops and puts the system into service; Amazon EU Customer Service is the deployer; an external model or platform supplier may be a vendor. Managers review recommendations, but the pilot's under-5% change rate calls the meaningfulness of that review into question.

**Compliance implications:** Before individual use, complete the applicable high-risk requirements, including risk management, data governance, technical documentation, logging, accuracy and robustness measures, monitoring, and conformity assessment. Test for bias and proxy discrimination; provide required information to affected workers and representatives; restrict access; and ensure managers can understand, challenge, and override recommendations, recording their independent reasons. Also address GDPR purpose limitation, minimization, retention, and transparency.

**Decision:** **Approve with controls.** Do not launch individual recommendations for escalation or promotion until the applicable obligations are documented, bias testing is complete, affected workers are informed, and effective human oversight is demonstrated. Team-level descriptive analytics may proceed separately only if it cannot be used to assess individuals.

## Phase 4: Client discussion and final sign-off
To be concluded