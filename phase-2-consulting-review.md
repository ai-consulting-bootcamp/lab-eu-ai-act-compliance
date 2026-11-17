# Phase 2 — Consulting review

This is the blind-review assessment of the four briefs in [`client_briefs.md`](./client_briefs.md). The categories below are first-pass calls made from the facts in the briefs, before a client answer key is confirmed.

| Case | Likely category | Why this is the first-pass call | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|---|---|
| 1 · LindenDesk | **Prohibited** — workplace emotion recognition under Article 5(1)(f) | Facial movements and vocal prosody are analysed to infer employees’ emotions in a workplace. The stated purpose is coaching, not a medical or safety exception. | Weekly role-play recording → vendor infers “frustrated”, “disengaged” or “anxious” → named-employee flag → team-lead review/override → coaching offer. | Vendor is the likely provider of the emotion-recognition system; LindenDesk is the employer/deployer. A recording or video host may be a separate processor/vendor. | Do not put this design into service or use it. Stop the proposed processing and confirm deletion/retention handling. Redesign around non-emotional, observable coaching signals; complete GDPR and worker-monitoring review before any pilot. | **Deny and redesign** |
| 2 · HafenWerk | **High-risk** — Annex III 4(a), employment and recruitment | The system ranks applicants and influences who gets an interview. Applicants below the initial cut-off may lose access to employment opportunities without meaningful review. | Application submitted → ATS parses CV, certificates and screening answers → ranking/recommendations → recruiter reviews the full pool and records reasons/overrides → HR approves interview list → applicant communication and audit log. | ATS vendor is the likely provider; HafenWerk is the employer/deployer. If HafenWerk substantially modifies or rebrands the system, its provider obligations need legal confirmation. | Provider evidence for risk management, data governance, technical documentation, logging, accuracy, robustness, cybersecurity and conformity. Deployer controls: meaningful human oversight, representative input data, bias testing, no automatic cut-off, applicant information/contest route, monitoring and records of overrides. | **Approve with controls** |
| 3 · KiezRad | **Limited risk / transparency** — Article 50(1) | Customers directly converse with a hosted AI assistant. The fact that staff maintain the articles does not make each reply human-approved. | Customer opens chat → hosted model retrieves approved help articles → assistant drafts reply → customer is told it is AI → billing disputes are routed to support → interaction and escalation logs are retained under policy. | KiezRad is the deployer and is likely the provider of the customer-facing system if it puts the assistant into service under its name. The hosted-model company is the model provider/technical vendor. Contractual role allocation must be confirmed. | Show a clear, prominent AI disclosure at the start of the conversation and keep the boundary clear: no account lookup, payments or booking changes. Provide human escalation, approved-content controls, monitoring, retention rules, vendor/DPA review and an assessment of any Article 50(2) marking requirement for generated text. | **Approve with controls** |
| 4 · Tonwerk Supply | **Minimal risk** | The model groups similar product records for an internal maintenance queue. It does not evaluate people or make decisions about rights, employment, access or services. | Nightly catalog export → batch similarity model compares names, dimensions, material and unit size → candidate-pair queue → catalog editor accepts, rejects or corrects each pair → change log. | Model/software vendor is the likely provider; Tonwerk Supply is the deployer. The catalog editor is the human reviewer, not a separate provider. | No specific AI Act obligation is triggered on these facts. Keep the human approval gate, test false matches, restrict access, document vendor/data handling and check whether catalog fields contain personal data or confidential information. | **Approve** |

## First-pass notes

### Case 1 — LindenDesk

The human override does not cure the prohibited use: the system still infers emotions from employees’ biometric signals in the workplace. The lawful path is to remove the inference step, not to add a stronger approval workflow. A possible redesign is an employee-controlled coaching tool that uses a rubric for observable role-play behaviours—such as policy coverage, turn-taking or response structure—plus self-selected coaching topics. It should not infer emotional or mental states, produce a people ranking, or be used for performance sanctions.

### Case 2 — HafenWerk

This is not an automatic denial, but “recruiters can scroll down” is not enough human oversight when the normal process stops at the top 30. Reviewers need time, training, authority and a documented reason to depart from the system. The vendor should show that the system was designed and validated for the intended technician roles, with traceable versions and performance/bias monitoring. The final interview decision should remain a genuinely human decision rather than a rubber stamp.

### Case 3 — KiezRad

The narrow scope is a useful deployment boundary: the assistant cannot inspect accounts or take transactions, and disputes go to people. The disclosure should be visible before or at the first exchange, not hidden in a general privacy policy. The UI should not imply that a human agent is replying. Article 50 transparency is separate from GDPR, consumer-protection, security and vendor-contract obligations.

### Case 4 — Tonwerk Supply

The candidate-pair output is an internal recommendation, not an automatic merge. That human gate keeps the operational risk manageable. The team should still measure false matches and prevent the model from silently changing the catalog, because data-quality errors can create downstream purchasing or inventory problems even when the use is minimal risk under the AI Act.

## Legal anchors

- [Regulation (EU) 2024/1689, Article 5 and Article 50](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) — prohibited practices and transparency duties.
- [Regulation (EU) 2024/1689, Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) — high-risk employment and recruitment uses.
- [European Commission: transparency obligations under Article 50](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) — current guidance on direct interaction, roles and application from 2 August 2026.

This is a training exercise, not a substitute for legal advice on the final deployment, employment-law position or GDPR basis.
