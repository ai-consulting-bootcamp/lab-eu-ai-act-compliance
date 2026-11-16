# EU AI Act Approval Pack - S. Rostovskyi
## Executive summary
Prepared 16 November 2026. Synthetic partner exercise with AI assistance. The student reports informing the instructor. Client responses are scripted, and all approvals below are consulting recommendations conditional on the stated scope and evidence.

Recommend approval with controls for the furniture assistant and lending tool, deny the proposed classroom emotion analysis and redesign it, and approve aggregate inventory forecasting. None of the companies or deployments is real. Legal and compliance owners must validate interpretation and implementation before any real launch.

## Case A - Furniture retailer assistant
A Spanish retailer commissions a branded website assistant to answer product and delivery questions using an external language-model API. Visitors' questions and approved catalogue and policy pages feed generated answers. Staff update sources and handle escalations. The assistant cannot transact, set prices, or determine credit.

Classification and decision. Limited risk / transparency. Approve with controls. Direct AI interaction and generated text engage Article 50. Product questions alone do not identify an Annex III purpose.

Architecture. Visitor question -> retrieve approved, versioned sources -> language model -> answer with source links or escalation -> staff resolution. Record source version, failures, and escalation outcomes with proportionate retention and access controls.

Roles. The retailer commissions and puts the application into service under its name, making it system provider and deployer. The API supplier provides the underlying GPAI model. An integration consultant supplies services within the agreed scope. Document these roles and reassess material changes.

Controls and evidence. Disclose AI involvement accessibly at first interaction. Assess and implement Article 50(2) machine-readable marking within its technical requirements and exceptions, including support from the API supplier. Test policy accuracy, source freshness, prompt injection, and escalation. Minimise personal data, set a lawful retention policy, and review vendor processing and transfers. Consumer-facing claims must match current terms.

Borderline and next artifact. Adding credit eligibility decisions would require reclassification. Request a tested transparency notice and escalation checklist. Legal reviews Article 50 applicability and data processing terms.


# EU AI Act Approval Pack - S. Rostovskyi
## Case B - Consumer lending recommendations
A French lender licenses a vendor-branded system to estimate repayment likelihood and recommend personal-loan limits. Verified income, debts, repayment history, and requested amounts feed the model. Officers decide applications, can override recommendations, and record reasons. Applicants' access to credit is affected.

Classification and decision. High-risk under Article 6(2) and Annex III 5(b). Approve with controls, conditional on evidence and applicable dates. This is creditworthiness assessment. The separate fraud service does not change that purpose. Officer review does not remove the model's material influence or support the narrow Article 6(3) exception.

Architecture. Application -> validate data -> vendor scoring and limit recommendation -> trained officer examines inputs, reasons, and limitations -> decision with recorded rationale and override -> customer communication and challenge route. Log model version, input provenance, output, reviewer action, and incidents.

Roles. Vendor is system provider. Lender is deployer. No GPAI dependency is established by the brief. Request the vendor component inventory. The consultant advises and integrates within scope.

Provider evidence. Obtain intended-purpose instructions, risk and data governance records, technical documentation, logging and oversight specifications, accuracy and subgroup testing, security validation, quality management, and post-market monitoring and incident procedures. The applicable conformity route for Annex III 5(b) is internal control under Annex VI. Require the declaration, CE marking, and registration when applicable.

Deployer controls. Assign trained officers with authority and time to reject a recommendation. Validate input relevance, monitor outcomes and drift, retain controlled automatic logs for at least six months unless other applicable law provides otherwise, and establish incident escalation. Provide required notices and applicable decision explanations. Complete the Article 27 FRIA for this creditworthiness use and notify the authority as required. Assess GDPR lawful basis, DPIA requirements, fairness, minimisation, and Article 22 exposure if human review becomes nominal.

Timing. For a new Annex III system, the amended high-risk requirements apply from 2 December 2027. This exercise recommends meeting the listed evidence gates before launch as a project condition. Existing GDPR duties continue to apply. Legal verifies the actual launch date, transition rules, and any significant changes.

Mini implementation roadmap. Before placement, the provider completes documentation, validation, conformity assessment, and applicable registration. Before first use, the lender completes the FRIA and privacy assessment, trains officers, tests notices and appeals, and rehearses incident handling. Procurement requests the evidence above and contractual access to logs, updates, and incident support. Launch requires documented acceptance by the lender's accountable owner. No vendor evidence has actually been supplied.


# EU AI Act Approval Pack - S. Rostovskyi
## Case C - Classroom emotion analysis
A German language school proposes vendor software that reads webcam facial movements to infer named adult students' boredom, frustration, and enthusiasm. Teachers use flags for questions and participation discussions and may dismiss them. The stated purpose is classroom management, with no medical or safety function.

Classification and decision. Prohibited under Article 5(1)(f). Deny and redesign. Teacher discretion and consent do not establish a medical or safety exception.

Architecture and roles. The rejected flow is camera -> biometric emotion inference -> named dashboard -> teacher intervention. The vendor would be provider and the school deployer. Stop procurement for that purpose. Replace it with optional self-reported lesson feedback -> teacher reads responses -> voluntary follow-up. Use a simple form without emotion inference, automated student scores, or automated consequential decisions.

Controls and evidence. Legal reviews the replacement's purpose, voluntary participation, privacy notice, access, retention, and educational obligations. Record the rejected feature and approved replacement scope. Any later student evaluation automation requires a fresh assessment. The next artifact is a redesign specification and data-flow record.

## Case D - Inventory forecasts
A Portuguese wholesaler builds a weekly product-demand model from aggregate sales, stock, lead times, and promotions. Numeric replenishment proposals go to planners, who check capacity and budget and approve orders. The stated design has no person-level scoring.

Classification and decision. Minimal risk. Approve the stated scope. No specific high-risk or Article 50 trigger is identified. General AI literacy provisions remain relevant.

Architecture and roles. Scheduled aggregate feed -> validation -> forecasting model -> planner review and adjustment -> purchase order. Record forecast version, errors, and approved quantities. The wholesaler is provider and deployer of its internal system. No external AI vendor is specified.

Controls and evidence. Back-test forecasts, cap orders through procurement controls, and support staff understanding of errors. Confirm aggregation, data rights, and access controls. Review GDPR if personal data enters the workflow and consumer or contractual claims if outputs are communicated externally. Employee performance scoring would require reclassification. The next artifact is an input-data specification and forecast evaluation record.

## What changed after the client discussion?
In the scripted debrief, all intended and inferred categories matched. A gained explicit staff escalation, B gained evidence gates and meaningful oversight, C changed to self-reported feedback, and D gained a change-review trigger. Scripted client acceptance represents no actual sign-off or independent blind assessment.

## Legal references
EU AI Act, consolidated 27 July 2026, Articles 3-6, 9-17, 26-27, 43, 47-50, 72-73, 86 and 113, Annexes III and VI.
https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng/pdf
Amending Regulation (EU) 2026/1744.
https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
GDPR, Articles 5-6, 13-15, 22, 28, 32, 35 and Chapter V.
https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
