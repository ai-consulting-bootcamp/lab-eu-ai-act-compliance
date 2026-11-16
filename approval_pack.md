# EU AI Act Approval Pack - Sean Langsdorf
**Consulting response · 16 November 2026 · Simulated partner review**

## Executive decision

Deny ElbeStay’s employee emotion scoring. Approve Dockline’s hiring tool only when the launch gates are met. Approve MuseumPass only with transparency and strict scope controls. Approve RegisterMatch for internal company-record deduplication. The examples are fictional and the decisions are recommendations, not recorded client approvals.

Timing matters. The workplace prohibition and general AI literacy duty already apply. Article 50 generally applies from 2 August 2026. The amended Annex III high-risk rules apply from 2 December 2027. For Dockline, the controls below are consulting launch gates even if the client plans an earlier rollout. Legal should check any transitional treatment under Article 111 against the system’s real placement and change history. [1, 2]

## A · ElbeStay | Prohibited | Deny and redesign

**Why.** A model infers named employees’ emotions from facial and vocal biometric signals in the workplace. Coaching is not a medical or safety purpose. Human override, notice and consent do not remove the Article 5(1)(f) prohibition. [1]

**Design and roles.** Block the proposed video/audio pipeline. The vendor would provide the emotion-scoring system and the hotel would deploy it. Replace it with a non-AI workflow. After a role-play, a manager completes a checklist of observable actions, such as whether the trainee confirmed the guest’s request. The manager agrees on a coaching step with the employee and records only the agreed action. No recordings, biometric inputs or emotion labels. ElbeStay owns the replacement workflow. There is no AI provider or model vendor in the redesign.

**Next evidence.** A written scope and removal checklist would verify that recording ingestion and scoring were never configured or have been disabled, and that no vendor retains the data. Verify with HR and privacy counsel whether the redesigned employee process needs works-council involvement.

<!-- page break -->

## B · Dockline Staffing | High-risk | Approve with controls

**Why.** Ranking applicants materially influences access to interviews under Article 6(2) and Annex III 4(a). Recruiter sign-off does not turn ranking into an Article 6(3) preparatory task. A tool that only formats CVs without scoring or influencing review order would warrant a new assessment. [1]

**Design and roles.** On vacancy close, a vendor model compares CVs and certifications to a fixed skills rubric and returns ordered candidates with source excerpts. Recruiters must independently assess everyone against the rubric before narrowing the list, can reverse the model’s ranking and can pause use. Only recruiters release invites. Restricted logs capture model version, rubric, recommendation, override and rationale. The vendor markets the finished tool under its name and is the provider. Dockline is the deployer. Changing the intended purpose or substantially modifying the tool could shift provider duties under Article 25. [1]

**Launch gates.** Provider supplies risk management, data governance, technical documentation, logging and oversight design, accuracy/robustness/security validation, conformity assessment, declaration, CE marking, applicable registration and post-market monitoring. Dockline follows instructions, assigns trained oversight, checks input relevance and representativeness where it controls inputs, informs candidates, monitors use and escalates incidents. It keeps controlled automatic logs for at least six months when Article 26 applies, subject to applicable law. Verify GDPR basis and DPIA need. An Article 27 FRIA is not triggered merely because a private staffing agency recruits for industrial clients. Recheck that if the actual deployer or service changes. [1]

## Implementation roadmap · Dockline

**Provider, before market placement.** Freeze the recruitment purpose and version. Document the validation dataset and subgroup performance, complete conformity and applicable registration, and hand over operating instructions and incident contacts.

**Deployer, before first use.** Test the complete applicant review in shadow mode without influencing real invitations. Train reviewers on overrides and escalation. Confirm notices, data retention and the stop-use process before the HR owner signs off.

**Vendor evidence to request.** Version-specific validation results, conformity documentation as applicable, the oversight and logging instructions, and proof that rankings can be overridden and disabled. Run a witnessed test with a strong candidate deliberately placed below the initial shortlist.

<!-- page break -->

## C · MuseumPass | Transparency | Approve with controls

**Why.** Real visitors talk to AI, so apply Article 50(1) and (5). The provider must also address technically feasible machine-readable marking and detectability of generated text under Article 50(2). A visual notice alone is not that technical control. These private support responses are not published to inform the public on matters of public interest under Article 50(4). [1, 2]

**Design and roles.** On opening chat, an accessible banner states “You’re chatting with an AI assistant. Contact staff for help.” The system retrieves current FAQ passages and returns a sourced, marked answer. If it lacks a source, the visitor is routed to staff. No payment, account access or refund decisions. MuseumPass commissions and puts the finished branded system into service for its own use, so it is both system provider and deployer on these facts. The hosted model company is an upstream vendor, not a substitute for MuseumPass’s system-level duties.

**Launch gates.** Test the notice before the first message, keyboard/screen-reader access, the marking mechanism and escalation. Keep minimal QA records such as article version and handoff events. Limit text retention, assess the vendor’s privacy terms and reclassify if the tool begins deciding entitlement or publishing public-interest content.

## D · RegisterMatch | Minimal risk | Approve

**Why.** Internal company-record matching scores duplicate records, not people. It does not rank candidates, assess credit, interact directly with a person conversationally or generate synthetic content. No use-specific obligation is identified here. Article 4 AI literacy still applies where relevant. [1]

**Design and roles.** A nightly import triggers a model comparing approved corporate fields. It emits IDs and scores only, with no auto-merge. An analyst verifies the register number and court before approving any merge. The log records input snapshot, scores and the analyst’s action to allow undo. The operator develops and uses the finished system in-house and is both provider and deployer. The register-data supplier is a data vendor, not the AI provider.

**Control.** Record an allowed-field schema and test for false merges. Reassess GDPR scope if sole traders or officer records enter the feed. Using the data for individual screening or credit decisions would require a new classification.

## Sign-off and client discussion

**Status.** Simulated review complete. No client or partner has approved a decision. What changed after the client discussion? Not yet assessable because the discussion has not taken place. At debrief, record intended versus inferred category, any corrected facts, the revised launch decision, and who owns each open action.

## Sources

[1] [Regulation (EU) 2024/1689, consolidated text](https://eur-lex.europa.eu/eli/reg/2024/1689) · Arts. 3–6, 9–17, 25–27, 43, 47–50, 72–73, 111, 113 and Annex III 4(a).
[2] [Regulation (EU) 2026/1744, Digital Omnibus on AI](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) · amended application dates and Article 50(2) transition for eligible pre-August 2026 systems.
