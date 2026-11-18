# EU AI Act Approval Pack — Jaime Garate Marquerie

**Lab:** Classify your product · **Client cases from:** Sandra Obregón (logistics company, four hidden briefs) · **Date:** 17 Nov 2026
**Question from the client:** "Can we launch this?"

## Executive summary
The client, a logistics company, proposed four AI uses:
- one is **prohibited** (detecting frustration in call-centre staff);
- one is **high-risk** (ranking job applications);
- one triggers **transparency** duties (parcel-tracking chatbot);
- one is **minimal risk** (labelling empty boxes).

Only the prohibited case is denied as proposed, and a lawful redesign is offered. The high-risk and transparency cases need controls before launch; the minimal-risk case can be approved after functional testing. These are consulting recommendations that depend on implementation details, not legal authorisations.

| Case | Likely category | Decision |
|---|---|---|
| 1 · Ranking job applications | High-risk | Approve with controls |
| 2 · Frustration detection in calls | Prohibited | Deny and redesign |
| 3 · Parcel-tracking chatbot | Limited risk / transparency | Approve with controls |
| 4 · Labelling empty boxes | Minimal risk | Approve (after functional tests) |

## Case 1 · Ranking job applications — High-risk
- **Why:** Annex III point 4(a), recruitment and filtering of applications (Art. 6(2)).
  - Recruiters usually read only the top-ranked applications, so the ranking decides who gets an interview.
  - An optional human review does not remove the selection purpose.
- **Architecture:** documented job criteria → CVs and forms → explainable ranking → effective human review of results, rejected cases and bias → reasoned invitations → log of version, criteria, results and reviews.
- **Roles:**
  - Provider: whoever develops it and puts it into service under its name (to confirm).
  - Deployer: the logistics company.
  - Vendor: a possible model or applicant-tracking-system (ATS) supplier (not identified).
- **Controls:**
  - the high-risk regime: risk management, data quality, documentation, logs, human oversight, accuracy, conformity assessment, registration and monitoring;
  - information to candidates;
  - GDPR safeguards on automated decisions and bias.

  No evidence of current compliance was provided.
- **Decision: Approve with controls.** No launch until the obligations and conformity are verified.

## Case 2 · Frustration detection in calls — Prohibited
- **Why:** Art. 5(1)(f) prohibits inferring the emotions of people in the workplace, except for medical or safety reasons, and none are described. A supervisor listening afterwards does not cure the practice.
- **Lawful redesign:** objective service indicators (unresolved complaints, response times, procedure quality) → supervisor's contextual review → coaching conversation. No emotional state is inferred from voice or image.
- **Roles:**
  - Deployer: the logistics company.
  - Vendor: the emotion-recognition supplier (not identified).
  - The redesign needs new owners and access rules.
- **Controls:** remove the emotion module; check the alternative for proportionality, GDPR and labour rights.
- **Decision: Deny and redesign.**

## Case 3 · Parcel-tracking chatbot — Limited risk / transparency
- **Why:**
  - Art. 50(1): a system that interacts directly with people must say it is AI unless that is obvious. Here it shares a window with human agents.
  - Art. 50(5) sets the form and timing of the notice.
- **Architecture:** notice "You are talking to an AI assistant" at the start → FAQ answers, or authenticated tracking → limited query to the shipping system → replies marked as automated → hand-off to a human agent → minimised logs and access control.
- **Roles:**
  - Provider: the chatbot developer (to confirm).
  - Deployer: the logistics company.
  - Vendors: possible LLM, hosting and tracking suppliers.
- **Controls:**
  - the AI notice, with automated replies identified;
  - access checks beyond knowing an order number (also a GDPR and security issue);
  - minimisation and retention rules;
  - monitoring of answers.
- **Decision: Approve with controls.** Individual tracking stays closed until access control and the notice are in place.

## Case 4 · Labelling empty boxes — Minimal risk
- **Why:** for this specific use there is no Art. 5 practice, no Annex III area and no Art. 6(1) safety component. Minimal risk applies to this use, not to every risk.
- **Architecture:** photo of an empty box → vision model → type and approximate size with a confidence score → mandatory human correction → internal catalogue → log of corrections and accuracy tests.
- **Roles:**
  - Provider: the vision-system developer (to confirm).
  - Deployer: the logistics company.
  - Vendor: a vision service, if any.
- **Controls:** representative samples; accuracy by box type; error handling; photo security; check that no people or personal data appear in images.
- **Decision: Approve** after reasonable functional tests. No specific AI Act obligations apply for this purpose.

## Roles across the four cases
- The logistics company is normally the **deployer**.
- The **provider** is whoever develops each system and places it on the market or puts it into service under its own name. That could be the logistics company itself.
- Model makers and cloud services are **third-party vendors**. They are not automatically the provider of the whole system.

## Client discussion and closing note
- **Discussion (17 Nov 2026):** the client (Sandra) revealed her answer key. My four inferred categories **matched** her intended categories. In writing (Slack, 17:10) she accepted the four recommendations without challenging any or asking for a redesign.
- **Closing note — what changed after the client discussion?** The classifications did not change. Before a real launch, the details I would still ask for are:
  - **Case 1:** ranking weights and how rejected candidates are handled.
  - **Case 2:** confirmation that the emotion module is removed.
  - **Case 3:** how users are authenticated before seeing a parcel's location.
  - **Case 4:** error rates by box type.

## Limits
These are recommendations for teaching scenarios, not authorisations. Sources: the client's briefs; Regulation (EU) 2024/1689, Articles 5, 6 and 50 and Annex III (consolidated text, 27 Jul 2026); GDPR. This pack is not a legal opinion, a conformity assessment or a certification.
