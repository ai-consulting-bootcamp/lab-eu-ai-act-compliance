# EU AI Act Approval Pack - Jay

---

# PART 1: PRIVATE ANSWER KEY

*(Kept hidden from partner during Phase 1-2; revealed during Phase 4 client discussion)*

## Setup / First Run

Four scenario headings below, each with a client use case fitting its target category, drafted before sharing anything with the partner (Anand).

### Case 1 - Prohibited

**Client brief for partner:** Mid-size Tier-1 automotive parts manufacturer, ~600 hourly production workers across two shifts. Plant leadership reports rising absenteeism and quality defects, suspected to be tied to worker burnout that supervisors aren't catching early. Existing workstation cameras (installed for QA footage) would gain an AI layer analyzing facial expression and posture to flag fatigue/low engagement in real time. A daily per-operator summary would go to supervisors, used both to decide who needs support that day and who gets offered overtime first. Supervisors make the final call — the AI doesn't message workers directly. Employees have been told the cameras are for standard quality-assurance monitoring, consistent with existing plant policy; no separate consent process is planned.

**Intended category (private):** Prohibited — Article 5(1)

**Why:** Workplace emotion/state recognition used to influence treatment of workers (coaching, overtime prioritization), with the real purpose disguised from employees (told it's QA monitoring only).

### Case 2 - High-risk

**Client brief for partner:** Automotive component manufacturer, ~1,200 employees across production, quality, and logistics. HR says promotion decisions rely too heavily on manager opinion and feel inconsistent — they want something more "data-driven and fair" for annual reviews. Proposed: a dashboard combining productivity, quality-error rate, and attendance with a "collaboration signal" derived from tone/responsiveness analysis of internal Slack/Teams messages, generating a quarterly composite score per employee. Managers use the score as the primary input for promotion nominations and as an early flag for termination-risk coaching. Managers write the final recommendation themselves. The chat analysis was rolled out quietly as part of an existing "workplace collaboration insights" feature bundled into the chat platform license — most employees are unaware their messages are scored for this purpose.

**Intended category (private):** High-risk — Annex III (employment: promotion/termination)

**Why:** Explicit Annex III employment-decision trigger (promotion and termination-risk recommendations); secondary GDPR/workplace-surveillance flag from the undisclosed chat-sentiment input.

### Case 3 - Limited risk / transparency

**Client brief for partner:** Tier-1 automotive supplier developing an in-cabin driver-assistance module for sale to multiple OEMs. OEMs want a differentiated safety feature ahead of upcoming drowsy-driving safety-rating requirements. Proposed: use the existing in-cabin camera to monitor eyelid closure, head position, and gaze direction, estimating real-time drowsiness/distraction and triggering an audible + dashboard alert. Processing is fully local in-vehicle, no cloud transmission, no data shared with any third party. The driver remains fully in control at all times — no human review needed in the traditional sense. The feature is described in the owner's manual under "Driver Assistance Features," with a small dashboard icon shown when actively monitoring, consistent with how other driver-assist features are typically disclosed.

**Intended category (private):** Limited risk / transparency — Article 50

**Why:** Same underlying emotion/state-detection technology as Case 1, but deployed for a genuine safety purpose rather than to influence workplace treatment — not prohibited, but still requires adequate disclosure that state-monitoring is occurring.

### Case 4 - Minimal risk

**Client brief for partner:** Metal stamping supplier producing exterior body panels and select structural components for two OEM customers. Manual visual QC on the cosmetic line is inconsistent between shifts; minor surface defects (scratches, dents, coating issues) are slipping through. Proposed: a machine-vision system at the cosmetic inspection station comparing each panel against a reference library of known good/defective panels, flagging dents, scratches, coating inconsistencies, and minor dimensional warping. Clearly defective panels route automatically to rework; clearly good panels continue without review; only borderline-confidence cases get a technician's manual check. No data about people is involved. The plant's line list also includes a smaller run of structural brackets for the same customers, but this vision system is only installed on the cosmetic panel station, not the structural line.

**Intended category (private):** Minimal risk

**Why:** Inspects physical parts, not people; no Annex III domain touched; deliberate near-miss included (plant also makes structural parts) to test whether the reviewer confirms scope rather than assuming.

---

# PART 2: CONSULTING RESPONSE

## Phase 1: Hidden Client Brief (Author Template)

| Case | Client brief for partner | Intended category (private) | Why you chose it |
|---|---|---|---|
| 1 | Emotion/fatigue-monitoring cameras on the plant floor, framed as QA, feeding a workforce risk score used for coaching and overtime decisions | Prohibited | Workplace emotion recognition used to influence worker treatment, disguised purpose |
| 2 | AI system scoring workers on productivity, quality, and chat-sentiment "collaboration," feeding promotion and termination-risk recommendations | High-risk | Explicit Annex III employment-decision trigger, plus undisclosed chat surveillance |
| 3 | In-cabin driver drowsiness/distraction monitoring (gaze, eyelid closure), disclosed via dashboard icon + owner's manual | Limited risk / transparency | Same tech as Case 1, but safety purpose — requires disclosure, not prohibited |
| 4 | Machine-vision cosmetic/dimensional defect inspection on stamped panels, structural parts explicitly out of scope | Minimal risk | Inspects parts not people; deliberate scope near-miss to test discovery rigor |

## Phase 2: Review Your Partner as the Consultant

Anand's four hidden client briefs, reviewed without access to his answer key, first-pass classified and justified from lesson material, then refined through follow-up questioning.

| Case | Likely category | Why this is your first-pass call | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|---|---|
| **1** (Energy retailer household scoring) | Prohibited — Article 5(1)(c), social scoring | Combines unrelated data (social media, neighborhood demographics) into a general reliability score, used to trigger detrimental treatment (forced prepayment) disproportionate to the data's original context; compounded by zero notice and no contestability | Meter reading cycle → composite scoring model (meter + social + demographic inputs) → automatic threshold-based meter switch → no human checkpoint, no disclosure | **Provider:** the retailer · **Deployer:** the retailer · **Vendor:** none disclosed, needs confirming if scoring model is licensed | N/A as proposed — practice itself is prohibited, not a matter of adding controls | **Deny.** Redesign required. |
| **2** (HR-tech screening product) | High-risk — Annex III, recruitment/screening | AI used to screen, filter, or rank job applicants is an explicit Annex III category; reinforced by biometric-adjacent video-interview analysis (tone, facial expression) | CV submitted → resume screening/ranking model → video-interview analysis model → composite fit score → recruiter sees ranked shortlist → override technically possible, rarely exercised given volume | **Provider:** the HR-tech startup · **Deployer:** each hiring client company · **Vendor:** none further disclosed | Conformity assessment, technical documentation, risk management system, human oversight that is genuinely exercised (not nominal), logging, bias/accuracy testing on video-analysis component, candidate disclosure | **Approve with controls** — contingent on redesigning the review workflow so override is actually exercised, plus bias testing |
| **3** (Bank chatbot + synthetic voice) | Limited risk / transparency — Article 50, two distinct triggers | Chatbot not disclosed as AI (trigger 1); cloned "brand voice" for outbound calls not disclosed as synthetic (trigger 2) — two separate Article 50 obligations, not one | Chatbot: customer query → AI response → no disclosure. Voice: script drafted → voice-cloning model generates audio → outbound call → no disclosure | **Provider:** the bank, or third-party chatbot/voice vendor if licensed (needs confirming) · **Deployer:** the bank · **Vendor:** possible voice-cloning tool, needs identifying | Clear upfront disclosure that chatbot is AI; clear disclosure at start of AI-voice calls that voice is synthetic; internal policy update since marketing's performance preference doesn't override the legal requirement | **Approve with controls** — contingent on both disclosures being implemented before launch |
| **4** (Logistics restocking AI) | Minimal risk | No Annex III domain touched, no individual person evaluated or scored, no safety component; strong human approval step is good practice but not what determines the tier | Historical sales/seasonality/lead-time data → forecasting model → generated purchase order → warehouse/procurement review and approval → order placed | **Provider:** whoever builds the forecasting model (needs confirming) · **Deployer:** the logistics company · **Vendor:** possible third-party forecasting/ERP vendor | No AI Act-specific obligations. Flag parallel issues: data governance/accuracy of forecasting inputs, standard vendor-contract terms, ordinary business-continuity risk | **Approve.** No redesign needed. |

### Self-correction notes on first-pass reasoning

Classifications were directionally correct on first pass in all four cases; two corrections were needed to the *reasoning*, not the label:

- **Case 1:** initially cited "Annex III" when the correct basis was Article 5 (prohibited practices), and the mechanism was refined from "state inference" to the more accurate "social scoring."
- **Case 2:** initially framed the high-risk trigger as depending on whether human oversight would be overridden. Corrected to recognize Annex III recruitment/screening is the trigger on its own — oversight quality is a separate compliance-gap question, not the classification trigger.

This surfaced a lesson applied consistently across the whole portfolio: **risk classification and human-oversight quality are two independent judgments.** Weak oversight doesn't change a classification (Case 2); strong oversight doesn't create a low-risk classification on its own (Case 4, below).

## Phase 3: Approval Pack

### Executive Summary

This pack reviews four proposed AI use cases submitted for launch approval. The overall risk picture is mixed: one proposal cannot proceed as designed and requires a full redesign; two proposals can move forward but only with specific controls attached before go-live; one proposal is clear to launch as-is. A recurring theme is that human oversight was described as present but not meaningfully exercised — this pack treats "human in the loop" as a control that must be functioning in practice, not just available on paper, before it counts toward compliance.

| Case | Summary | Category | Decision |
|---|---|---|---|
| 1 | Household reliability scoring → automatic prepayment switch | Prohibited | **Deny — redesign required** |
| 2 | AI candidate screening & video-interview scoring | High-risk | **Approve with controls** |
| 3 | Undisclosed AI chatbot + cloned voice outbound calls | Limited risk / transparency | **Approve with controls** |
| 4 | AI-generated warehouse restocking suggestions | Minimal risk | **Approve** |

### Case 1 — Household Reliability Scoring

**Classification: Prohibited (Article 5(1)(c) — social scoring).** The system evaluates people using data unrelated to the context it's being used against, and applies the resulting score to justify disproportionate treatment. The absence of notice or contestability compounds the problem but is not the core trigger.

**Decision: Deny as proposed.**

**Redesign path:** Base the score only on actual payment/usage signals (missed payments, tampering-suggestive consumption anomalies); drop social media and demographic inputs entirely; require human review before any meter-type change; notify the customer with a right to contest. This redesigned version would likely fall outside Article 5 entirely, though consumer-protection and utility-sector regulation may still separately apply.

### Case 2 — AI Candidate Screening Tool

**Classification: High-risk (Annex III — recruitment and selection).**

**Compliance gap identified:** Human oversight exists on paper but is not functioning as a genuine control — a reviewer expected to simply process top-ranked names is not exercising meaningful oversight.

**Required controls before launch:** Documented technical file and risk management system; bias/accuracy testing on the video/facial-expression component; a redesigned review workflow ensuring genuine human judgment is applied; candidate disclosure that AI is used; sufficient logging for audit.

**Decision: Approve with controls**, contingent on the above being implemented before go-live.

### Case 3 — Chatbot and Synthetic Voice Campaigns

**Classification: Limited risk / transparency (Article 50) — two distinct triggers.** Does not touch an Annex III domain, so does not rise to high-risk — but transparency obligations apply regardless of stakes.

**Required controls before launch:** Clear upfront disclosure that the chatbot is AI; clear disclosure at the start of outbound calls that the voice is synthetic; internal policy alignment, since marketing's preference for a human-sounding voice is a business consideration, not a basis for skipping a legal disclosure requirement.

**Decision: Approve with controls**, contingent on both disclosures being implemented before launch.

### Case 4 — Warehouse Restocking AI

**Classification: Minimal risk.** No individual person is evaluated, no Annex III domain is touched, no safety component involved. The human-approval step is good operational practice but not what determines the classification.

**Decision: Approve.** No redesign or AI Act-specific controls required.

**Parallel issues to flag (not AI Act, but worth noting):** data governance/accuracy of forecasting inputs; standard vendor due diligence if a third-party model is used; ordinary business-continuity risk if forecasts are wrong.

### Closing Note (pre-discussion)

Across this portfolio, risk category and human-oversight quality are two separate questions needing separate answers. In Case 2, weak human review didn't change the risk category — it created a compliance gap on top of an already-high-risk classification. In Case 4, strong human review didn't create the low-risk classification — it was good practice layered on top of a use case already outside AI Act scope.

## Phase 4: Client Discussion and Final Sign-off

**Comparing intended vs. inferred classifications:**

| Case (Anand's) | Anand's intended category | My inferred category | Match? |
|---|---|---|---|
| 1 | Prohibited — Art. 5(1)(c), social scoring | Prohibited — Art. 5(1)(c) | Match |
| 2 | High-risk — Annex III, recruitment/screening | High-risk — Annex III | Match |
| 3 | Limited risk / transparency — Art. 50 | Limited risk / transparency — Art. 50 | Match |
| 4 | Minimal risk | Minimal risk | Match |

| Case (mine) | My intended category | Anand's inferred category | Match? |
|---|---|---|---|
| 1 | Prohibited — Art. 5(1) | Prohibited | Match |
| 2 | High-risk — Annex III | High-risk | Match |
| 3 | Limited risk / transparency — Art. 50 | Initially High-risk; realigned after discussion | Initial mismatch, resolved live |
| 4 | Minimal risk | Minimal risk | Match |

**Client (Anand) response:** Accepted the approval pack as presented — no requested redesigns or challenges to the decisions (deny/redesign on Case 1, approve with controls on Cases 2 and 3, approve on Case 4).

**Where the hidden scenarios worked well:** All eight briefs across both authors disguised their category well enough to require genuine reasoning rather than pattern-matching, while every case still resolved correctly once properly reasoned through. The Case 1/Case 3 pairing (same emotion/state-detection technology, disguised QA purpose vs. disclosed safety purpose) was especially effective — it forced a real distinction between purpose and disclosure rather than "cameras watching people = bad."

**Where a scenario was too vague / too obvious:** The driver-monitoring brief (Case 3) was the one genuine miss on first read — Anand's first-pass call was high-risk, not limited risk/transparency, a reasonable instinct given the safety-critical framing. It surfaced the same subtlety flagged in my own reasoning on this case: a genuine safety purpose changes the *outcome* (not prohibited) but doesn't erase the *obligation* (still requires Article 50 disclosure) — and it doesn't automatically escalate to high-risk either, since the correct test is whether the Annex III list is actually touched, not whether the use case feels serious.

**Consultant's closing note — what changed after the client discussion:** The core value of this exercise wasn't discovering a wrong classification — every case ultimately landed correctly — but confirming *why* each one was correct well enough to defend it under live questioning. The one case needing real-time discussion (driver monitoring) is exactly the kind of case a real client would push back on, since "this is a safety feature" is a reasonable instinct that happens to point toward the wrong tier. Being able to explain, in the moment, why safety purpose changes the outcome but not the obligation is the actual consulting skill this exercise was testing.

## Reinforce (skipped — optional)

Not attempted due to time constraints. Noted here rather than left silent: the core deliverable (Phases 1–4) was prioritized given a limited work window; Reinforce and Stretch are explicitly framed as extensions for those who finish core tasks early.

## Stretch (skipped — optional)

Not attempted due to time constraints, for the same reason as above. If revisited, Case 2 (AI candidate screening, the strongest high-risk case) would be the natural candidate for the mini implementation roadmap, since it already has the most developed control requirements of the four cases.
