# Lab Proof: EU AI Act Compliance (Classify Your Product)

**Pair:** Ayhan Demir and Julia, each acting as consultant for the other's cases and as client for their own.
**Result:** Both partners inferred all four of the other's categories correctly (8 of 8). Both clients accepted the recommendations.

## Files in this repository

| File | What it contains |
| --- | --- |
| [`lab_proof.md`](./lab_proof.md) | This file: evidence for each rubric step, the comparison of both answer keys, and the sign-off |
| [`EU_AI_Act_Approval_Pack_AyhanDemir.md`](./EU_AI_Act_Approval_Pack_AyhanDemir.md) | Approval pack for Julia's four cases: executive summary, category, architecture, roles, obligations, decision |
| [`EU_AI_Act_Approval_Pack_AyhanDemir.xlsx`](./EU_AI_Act_Approval_Pack_AyhanDemir.xlsx) | Working tables: my private answer key, the briefs as shared, first-pass calls, the consulting review table |
| [`Week 7 - LAB EU Act.xlsx`](./Week%207%20-%20LAB%20EU%20Act.xlsx) | Shared pair workbook: both sets of client briefs and both consultant reviews |
| [`instructions.md`](./instructions.md), [`rubric.md`](./rubric.md), [`README.md`](./README.md) | Lab brief, grading rubric, workflow |

## Rubric map

| Rubric step | Evidence | Where |
| --- | --- | --- |
| 1. Recognize | Four hidden cases, exactly one per outcome, with a private answer key | [Section 1](#1-recognize-my-four-hidden-client-cases) |
| 2. Apply | A first-pass category for each of Julia's briefs, justified from the facts | [Section 2](#2-apply-first-pass-calls-on-julias-briefs) |
| 3. Integrate | Architecture, human review point, provider, deployer and vendor for every case | [Section 3](#3-integrate-architecture-and-role-map), approval pack |
| 4. Verify | A decision for every case, checked against the required decision rules | [Section 4](#4-verify-decisions), approval pack |
| 5. Debrief | Intended and inferred categories compared in both directions, adaptations agreed, sign-off | [Section 5](#5-debrief-intended-vs-inferred) |
| Learning objective | Compliant recommendations: controls for high-risk and transparency cases, a lawful redesign for the prohibited case | Sections 4 and 5, approval pack |

## 1. Recognize: my four hidden client cases

### Private answer key (not shared with Julia)

| Case | Shared as | Intended category | Why I chose it |
| --- | --- | --- | --- |
| 1 Prohibited | B (Logiflex) | Prohibited, Art. 5(1)(f) | It infers employees' emotions (stress, frustration) from voice and face at work, which is banned outside medical or safety reasons. HR sign-off and the productivity data do not fix that. |
| 2 High-risk | D (Amazon EU CS) | High-risk, Annex III pt. 4(b) | Phase 2 scores individual associates to allocate tasks and select for promotion, which is evaluating workers for employment decisions. The team-level framing is a decoy. |
| 3 Limited risk / transparency | A (Kleinanzeigen) | Limited risk, Art. 50(1) | An AI chats with buyers who think they are talking to the seller, so it must disclose that it is AI. It makes no decision in an Annex III area. |
| 4 Minimal risk | C (Kessler) | Minimal risk | Quality inspection and predictive maintenance on parts and machines is not Annex III and not a safety component. The operator IDs and the "weaker shift" question are decoys: flag GDPR, and note it turns high-risk if used to evaluate workers. |

### Briefs as shared with Julia (labels removed, order shuffled)

- **A.** Kleinanzeigen sellers lose buyers by replying late. Idea: an opt-in assistant in the in-app chat that answers buyer questions while the seller is offline, using the listing, the seller's past replies and price rules, in the seller's own tone. Messages appear under the seller's name with no label. Nobody reviews them live; sellers can read the thread later and switch it off.
- **B.** Logiflex Fulfilment GmbH, a 3PL near Leipzig (~900 staff), faces a 2027 headcount cut and wants an "objective" basis for who stays. A vendor tool would score each employee from pick rates, call handle times, voice tone on calls and webcam facial expressions in meetings, flagging stress and disengagement. The ranked list feeds the redundancy shortlist. HR makes the final call; the works council is asking questions.
- **C.** Kessler Hausgeraete AG, a washing machine plant in Franconia, is losing margin to scrap and press-line stops. Cameras would check welds and finish, and vibration and temperature sensors would predict press failures, using images, sensor data and the MES shift log with operator IDs. A quality engineer checks flagged parts and a planner approves work orders. The plant manager asks if it could show "which shift is weaker".
- **D.** Amazon EU Customer Service (hypothetical) wants a "team contribution map" showing how each team moves CSAT, contacts per order and first contact resolution. An in-house model uses contact logs, QA scores and survey text. Phase 2: an individual score per associate to pick who moves to escalations and who enters the promotion pool. Managers approve the suggestions; in the pilot they changed under 5%.

## 2. Apply: first-pass calls on Julia's briefs

| Case | Julia's brief (short) | My first-pass call | Why |
| --- | --- | --- | --- |
| 1 | Electronics retailer: an AI support assistant answers common questions and drafts replies from product and ticket data; agents edit or reject before sending | Limited risk / transparency | Customers talk to an AI for common questions, so it must disclose that (Art. 50(1)). Agent-edited drafts are not Annex III. |
| 2 | Professional services firm: an AI scheduler recommends travel plans and meeting times; coordinators approve and employees can override | Minimal risk | Logistics support only: no decision on hiring, task allocation, performance or access to services. |
| 3 | Warehouse company: AI predicts staffing gaps and suggests shift changes from attendance, workload and weather; supervisors review before schedules are final | High-risk | Individual attendance drives shift allocation, which is task allocation and worker monitoring (Annex III pt. 4(b)). Supervisor review does not remove the category. |
| 4 | Hospital network: AI triage ranks patient urgency and suggests referrals from symptoms, history, labs and notes; nurses and doctors review everything | High-risk | Emergency patient triage is listed in Annex III pt. 5(d) and is likely a medical device under MDR. Clinician review is a required control, not an exemption. |

## 3. Integrate: architecture and role map

Each architecture has a trigger, AI behaviour, a human review point, an output and a record layer. The full versions are in the [approval pack](./EU_AI_Act_Approval_Pack_AyhanDemir.md).

| Case | Trigger and AI behaviour | Human in the loop | Record / disclosure layer | Provider | Deployer | Third-party vendor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 Retail support | Customer question; an LLM over product and ticket data answers or drafts | Agent edits or rejects drafts | AI notice at chat start, handover to a human, chat log | LLM or helpdesk vendor | Retailer | Yes (SaaS assistant) |
| 2 Scheduler | Meeting or trip request; an optimiser proposes times and routes | Coordinator approves, employee can override | Audit log | Scheduling tool vendor | Firm | Yes |
| 3 Warehouse shifts | Planning run; the model forecasts gaps and proposes shift changes | Supervisor approves or overrides each change | Log of suggestions and overrides, worker notice, route to contest a change | Workforce tool vendor (the company, if built in-house) | Logistics company | Likely |
| 4 Hospital triage | Patient intake; the model ranks urgency and suggests a referral | Nurse or doctor confirms every case | Decision log, explanation shown to clinician, override reason | Clinical AI vendor (MDR manufacturer) | Hospital network | Yes: CE certificate and notified body report requested |

Assumption: each client buys from a vendor, which makes the client the deployer. Building in-house or rebranding the system makes the client the provider (Art. 25).

## 4. Verify: decisions

| Case | Category | Decision | Decision rule applied | Condition before launch |
| --- | --- | --- | --- | --- |
| 1 Retail support | Limited risk / transparency | Approve with controls | Transparency: approval depends on disclosure and safe boundaries | AI disclosure and human handover are live; AI literacy (Art. 4); vendor DPA; no wrong price or warranty claims |
| 2 Scheduler | Minimal risk | Approve | Minimal: approve, flag parallel issues | GDPR on calendar data; works council rights (BetrVG §87(1) no. 6); scheduling data kept out of performance reviews |
| 3 Warehouse shifts | High-risk | Approve with controls | High-risk: no automatic denial; approval depends on controls, oversight and documentation | Vendor conformity evidence (CE, EU registration); trained oversight; logs kept 6+ months; workers and works council informed; DPIA; sick-leave reasons excluded |
| 4 Hospital triage | High-risk | Approve with controls | Same high-risk rule | Notified body conformity assessment (MDR and AI Act); clinical evidence and bias testing; FRIA if public; DPIA; one-site pilot after CE certificate review |

**Prohibited rule:** none of Julia's four cases is prohibited, so the pack contains no Deny decision. The pack still sets a red line for Case 4. If the triage ranking starts using social behaviour or personal traits unrelated to medical need, it risks becoming social scoring under Art. 5(1)(c). The lawful redesign is already written: rank on clinical urgency only and test outcomes for bias across patient groups.

The prohibited path was tested on my own Case B (Logiflex). Julia denied it and proposed a redesign; see Section 5.

## 5. Debrief: intended vs inferred

### My cases, reviewed by Julia

| Case (shared as) | My intended category | Julia's inferred category | Match | Julia's decision |
| --- | --- | --- | --- | --- |
| Logiflex (B) | Prohibited, Art. 5(1)(f) | Prohibited | ✅ | Deny and redesign |
| Amazon EU CS (D) | High-risk, Annex III pt. 4(b) | High-risk | ✅ | Approve only with strong safeguards |
| Kleinanzeigen (A) | Limited risk / transparency | Limited risk / transparency | ✅ | Approve only with controls |
| Kessler (C) | Minimal risk | Minimal risk | ✅ | Approve with controls |

### Julia's cases, reviewed by me

| Case | Julia's intended category | My inferred category | Match | My decision |
| --- | --- | --- | --- | --- |
| 1 Retail support | Limited risk / transparency | Limited risk / transparency | ✅ | Approve with controls |
| 2 Scheduler | Minimal risk | Minimal risk | ✅ | Approve |
| 3 Warehouse shifts | High-risk | High-risk | ✅ | Approve with controls |
| 4 Hospital triage | High-risk | High-risk | ✅ | Approve with controls |

### What worked and where the scenarios were thin

- **The decoys worked without misleading the reviewer.** HR sign-off did not stop Julia calling Logiflex prohibited. The team-level framing did not hide the individual scoring at Amazon. The operator IDs and "weaker shift" question did not push Kessler into high-risk; Julia treated them as a data-minimisation issue instead.
- **The categories matched but the reasoning differed in places:**
  - *Kessler:* Julia chose Approve with controls for a minimal case, because of the operator IDs. That is stricter than the minimal default, but it follows the rule to flag parallel issues. She also asked to confirm the system is not a safety component, since that would change the classification.
  - *Kleinanzeigen:* Julia named Kleinanzeigen as provider and the sellers as deployers. That role split is sharper than my answer key needed.
  - *Logiflex:* Julia added that a redesigned redundancy ranking without emotion inference still needs a high-risk employment assessment. The redesign moves the case from prohibited to high-risk, not to free use.
- **Borderline in Julia's set:** retail support is limited risk only because customers get direct answers. An agent-only version would be minimal. This assumption is stated in the approval pack.
- **Gap in Julia's set:** it has two high-risk cases and no prohibited case, so the Deny and redesign rule could not be applied to her briefs. The Case 4 red line covers that logic in advance.

### What changed after the client discussion?

No category changed in either direction. As clients, we both accepted the adaptations each consultant proposed:

- **Ayhan as client** accepted Julia's recommendations:
  - Kleinanzeigen: label AI replies and add a human handover.
  - Logiflex: remove emotion inference and voice and webcam analysis, consult the works council, and assess any remaining ranking as high-risk.
  - Kessler: pseudonymise operator IDs and keep analysis at process and shift level, with no worker scores.
  - Amazon: make manager review meaningful (the pilot changed under 5% of suggestions), test for bias, and give workers a way to challenge outcomes.
- **Julia as client** accepted my recommendations:
  - Retail support: AI disclosure and handover before launch.
  - Scheduler: keep scheduling data out of performance reviews.
  - Warehouse shifts: vendor conformity evidence and informing workers before first use.
  - Hospital triage: a one-site pilot after CE review, with ranking on clinical urgency only.

Categories match for both of us, and as clients we both agreed to the findings and adaptations.
