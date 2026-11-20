# EU AI Act Approval Pack - Ayhan Demir

**Client question: "Can we launch this?"**

## Executive summary

Yes, all four can launch; three need controls first. No case is prohibited under Art. 5, so nothing is denied. Two are high-risk (shift coverage, hospital triage) and need conformity evidence, oversight and logs before first use. One needs an AI disclosure (support assistant). One is minimal (scheduler). Human review exists in every case, but for high-risk systems it is a required control, not a way out of the category.

| Case | Category | Decision |
| --- | --- | --- |
| 1 Retail support assistant | Limited risk / transparency (Art. 50(1)) | Approve with controls |
| 2 Professional services scheduler | Minimal risk | Approve |
| 3 Warehouse shift coverage | High-risk (Annex III pt. 4(b)) | Approve with controls |
| 4 Hospital triage | High-risk (Annex III pt. 5(d), plus MDR) | Approve with controls |

## Case 1: Retail support assistant

- **Why:** customers talk to an AI for common questions; agent-edited drafts are not an Annex III use.
- **Architecture:** customer question → LLM over product and ticket data answers or drafts → agent edits or rejects → reply → AI disclosure, human handover, chat log.
- **Roles:** provider = LLM or helpdesk vendor; deployer = retailer; vendor = yes.
- **Compliance:** disclose AI at chat start (Art. 50(1)); AI literacy (Art. 4); GDPR vendor DPA; no wrong price or warranty claims.
- **Decision: Approve with controls,** once disclosure and handover are live.

## Case 2: Professional services scheduler

- **Why:** logistics support only; no decision on jobs, tasks or access to services.
- **Architecture:** meeting or trip request → optimiser proposes times and routes → coordinator approves, employee can override → booked plan → audit log.
- **Roles:** provider = tool vendor; deployer = firm; vendor = yes.
- **Compliance:** AI literacy only. Flag GDPR on calendar data and works council rights (BetrVG §87(1) no. 6) if data could monitor staff.
- **Decision: Approve.** Keep scheduling data out of performance reviews.

## Case 3: Warehouse shift coverage

- **Why:** individual attendance drives shift allocation, which is task allocation and worker monitoring.
- **Architecture:** planning run → model forecasts gaps and proposes shift changes → supervisor approves or overrides → final schedule → log of suggestions and overrides, worker notice, contest route.
- **Roles:** provider = workforce tool vendor (company, if built in-house); deployer = logistics company.
- **Compliance:** provider: risk management, data governance, technical docs, logging, conformity assessment, CE, EU registration. Deployer (Art. 26): trained oversight, logs 6+ months, inform workers and works council, monitor incidents. GDPR DPIA; exclude sick-leave reasons.
- **Decision: Approve with controls,** after vendor conformity evidence and worker information.

## Case 4: Hospital triage

- **Why:** emergency patient triage is listed in Annex III and is likely a medical device under MDR.
- **Architecture:** patient intake → model ranks urgency and suggests referral → nurse or doctor confirms every case → triage level and referral → decision log, explanation, override reason.
- **Roles:** provider = clinical AI vendor (MDR manufacturer); deployer = hospital network.
- **Compliance:** notified body conformity assessment (MDR and AI Act), clinical evidence, bias testing; deployer Art. 26 duties, clinician training, FRIA (Art. 27) if public or public-service; GDPR Art. 9 health data and DPIA.
- **Red line:** if the ranking uses social behaviour or personal traits unrelated to medical need (e.g. lifestyle, past "non-compliance", social status) to put some patients ahead of others, it risks becoming social scoring under Art. 5(1)(c), which is prohibited. Redesign: rank on clinical urgency only, as the brief describes, and test outcomes for bias across patient groups.
- **Decision: Approve with controls,** starting with a one-site pilot after CE certificate review.

**Assumptions:** each client buys from a vendor (client = deployer; building in-house or rebranding makes it provider, Art. 25). Case 1 assumes direct customer answers; agent-only would be minimal. Legal to confirm high-risk application dates and the MDR class.

## Client discussion and sign-off

Categories match for both of us, and as clients we both agreed to the findings and adaptations.
