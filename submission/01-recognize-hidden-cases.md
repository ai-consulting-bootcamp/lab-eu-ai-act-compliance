# Phase 1 — Recognize: Hidden Client Cases

Four manufacturing/automotive-grounded client scenarios were authored, one per AI Act outcome. Each was written to read as a realistic, slightly messy client discovery brief, with the category label removed before sharing with the partner (Anand).

## Author Table (Private — Intended Categories)

| Case | Client brief (sent to partner) | Intended category | Why |
|---|---|---|---|
| 1 | Emotion/fatigue-monitoring cameras on the plant floor, framed as QA, feeding a workforce risk score used for coaching and overtime decisions | **Prohibited — Article 5(1)** | Workplace emotion/state recognition used to influence treatment of workers, disguised purpose (told it's QA, not this) |
| 2 | AI system scoring workers on productivity, quality, and chat-sentiment "collaboration," feeding promotion and termination-risk recommendations | **High-risk — Annex III (employment: promotion/termination)** | Explicit Annex III employment-decision trigger; secondary GDPR/surveillance flag from chat-sentiment input |
| 3 | In-cabin driver drowsiness/distraction monitoring (gaze, eyelid closure), disclosed via dashboard icon + owner's manual | **Limited risk / transparency — Article 50** | Same emotion/state-detection technology as Case 1, but safety purpose (not prohibited) — still requires adequate disclosure |
| 4 | Machine-vision cosmetic/dimensional defect inspection on stamped panels, structural parts explicitly out of scope | **Minimal risk** | Inspects parts, not people; no Annex III domain; deliberate near-miss (plant also makes structural parts) to test scope-checking |

## Hidden Briefs Sent to Anand (No Labels)

### Case 1
Client: Mid-size Tier-1 automotive parts manufacturer, ~600 hourly production workers across two shifts. Plant leadership reports rising absenteeism and quality defects, suspected to be tied to worker burnout that supervisors aren't catching early. Existing workstation cameras (installed for QA footage) would gain an AI layer analyzing facial expression and posture to flag fatigue/low engagement in real time. A daily per-operator summary would go to supervisors, used both to decide who needs support that day and who gets offered overtime first. Supervisors make the final call — the AI doesn't message workers directly. Employees have been told the cameras are for standard quality-assurance monitoring, consistent with existing plant policy; no separate consent process is planned.

### Case 2
Client: Automotive component manufacturer, ~1,200 employees across production, quality, and logistics. HR says promotion decisions rely too heavily on manager opinion and feel inconsistent — they want something more "data-driven and fair" for annual reviews. Proposed: a dashboard combining productivity, quality-error rate, and attendance with a "collaboration signal" derived from tone/responsiveness analysis of internal Slack/Teams messages, generating a quarterly composite score per employee. Managers use the score as the primary input for promotion nominations and as an early flag for termination-risk coaching. Managers write the final recommendation themselves. The chat analysis was rolled out quietly as part of an existing "workplace collaboration insights" feature bundled into the chat platform license — most employees are unaware their messages are scored for this purpose.

### Case 3
Client: Tier-1 automotive supplier developing an in-cabin driver-assistance module for sale to multiple OEMs. OEMs want a differentiated safety feature ahead of upcoming drowsy-driving safety-rating requirements. Proposed: use the existing in-cabin camera to monitor eyelid closure, head position, and gaze direction, estimating real-time drowsiness/distraction and triggering an audible + dashboard alert. Processing is fully local in-vehicle, no cloud transmission, no data shared with any third party. The driver remains fully in control at all times — no human review needed in the traditional sense. The feature is described in the owner's manual under "Driver Assistance Features," with a small dashboard icon shown when actively monitoring, consistent with how other driver-assist features are typically disclosed.

### Case 4
Client: Metal stamping supplier producing exterior body panels and select structural components for two OEM customers. Manual visual QC on the cosmetic line is inconsistent between shifts; minor surface defects (scratches, dents, coating issues) are slipping through. Proposed: a machine-vision system at the cosmetic inspection station comparing each panel against a reference library of known good/defective panels, flagging dents, scratches, coating inconsistencies, and minor dimensional warping. Clearly defective panels route automatically to rework; clearly good panels continue without review; only borderline-confidence cases get a technician's manual check. No data about people is involved. The plant's line list also includes a smaller run of structural brackets for the same customers, but this vision system is only installed on the cosmetic panel station, not the structural line.
