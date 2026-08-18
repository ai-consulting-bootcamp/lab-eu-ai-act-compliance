# EU AI Act Approval Pack

**Consulting review of Mudit's four proposed AI use cases**\
**Consultant:** Louise Plessis\
**Date:** 18 August 2026

## Executive summary

The portfolio spans all four practical AI Act outcomes: one minimal-risk
industrial use, one customer-facing system requiring transparency, one
high-risk employment system, and one prohibited workplace use.

My recommendation is to:

-   **Case 1:** Approve.
-   **Case 2:** Approve with controls --- add Article 50 disclosure and
    operational guardrails.
-   **Case 3:** Approve with controls after redesign --- introduce
    meaningful human oversight and high-risk controls.
-   **Case 4:** Deny and redesign --- remove workplace emotion
    recognition.

  ------------------------------------------------------------------------
  Case              Classification    Key issue          Decision
  ----------------- ----------------- ------------------ -----------------
  1\. Predictive    Minimal risk      Industrial         **Approve**
  maintenance                         maintenance; Annex 
                                      I safety-component 
                                      check              

  2\. Customer      Limited risk /    AI interaction not **Approve with
  support chatbot   transparency      currently          controls**
                                      disclosed          

  3\. Recruitment   High-risk         Employment         **Approve with
  ranking                             filtering +        controls after
                                      ineffective human  redesign**
                                      oversight          

  4\. Burnout       Prohibited        Workplace emotion  **Deny and
  detection                           recognition        redesign**
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## Case 1 --- Predictive maintenance

**Classification: Minimal risk**

A furniture manufacturer uses vibration, temperature, run-hours and
maintenance history to predict machine maintenance needs. A technician
validates every flag before a work order is issued.

### First-pass call

There is no people-facing decision and no obvious Annex III use. My
first-pass classification is therefore **minimal risk**.

### Proposed AI architecture

`Machine sensors + maintenance logs → predictive model → maintenance-risk flag → technician review → work order`

### Role map

-   **Deployer:** furniture manufacturer.
-   **Provider:** internal development team or external
    predictive-maintenance supplier, depending on who develops and
    markets the system.
-   **Third-party vendor:** potentially a predictive-maintenance/model
    provider.

### Controls and implications

No specific high-risk AI Act obligations arise from the use as
described. I would nevertheless maintain model monitoring, reliability
testing and human validation.

One point requires verification: whether the AI is a **safety component
of a regulated product covered by Annex I**. If so, Article 6(1) could
change the classification.

### Decision

**APPROVE.** Proceed subject to the Annex I/product-safety check.

------------------------------------------------------------------------

## Case 2 --- Customer support chatbot

**Classification: Limited risk / transparency**

A skincare brand deploys a chatbot for order status, returns and product
recommendations, with escalation to human support. The current design
does not tell customers upfront that they are interacting with AI.

### First-pass call

Customers interact directly with an AI system. **Article 50 transparency
requirements** therefore apply unless it is obvious to a reasonably
well-informed user that they are interacting with AI.

### Proposed AI architecture

`Customer query + order/browsing context → chatbot → answer/recommendation → escalation rules → live agent`

Add an AI disclosure at the beginning of the interaction and retain
escalation records.

### Role map

-   **Deployer:** skincare brand.
-   **Provider:** whoever develops and places the chatbot on the market
    or puts it into service under its own name/trademark.
-   **Third-party vendor:** potentially an LLM or chatbot provider.

### Controls and implications

-   Clear AI-interaction disclosure.
-   Defined escalation boundaries.
-   Quality and behaviour monitoring.
-   GDPR assessment because order history and browsing behaviour may
    constitute personal data.

Article 50 transparency obligations apply from **2 August 2026**.

### Decision

**APPROVE WITH CONTROLS.** Add the Article 50 disclosure before launch.

------------------------------------------------------------------------

## Case 3 --- Recruitment ranking and auto-rejection

**Classification: High-risk --- Annex III employment**

The bank proposes ranking applications using CVs, cover letters,
education, past employers and a video-derived "culture fit" score, then
automatically rejecting the bottom 60%. Although recruiters can
technically override the system, rejected candidates are not reviewed.

### First-pass call

AI used to analyse, filter or evaluate candidates for recruitment falls
within the AI Act's **Annex III employment category**.

The practical workflow also makes the claimed human oversight
ineffective: the bottom 60% never reach a recruiter.

### Proposed AI architecture

`CV + cover letter + justified candidate signals → ranking model → candidate score/ranking → meaningful recruiter review before rejection → shortlist/reject decision → decision and system logs`

The video-based **"culture fit"** feature should be challenged. The
client needs to define exactly what it measures, and any
emotion-inference functionality should be removed.

### Role map

-   **Deployer:** regional bank.
-   **Provider:** internal bank team if it develops/puts the system into
    service under its own name; otherwise the recruitment-system
    supplier.
-   **Third-party vendors:** potentially the underlying model provider
    and video-analysis supplier.

### Controls required before approval

-   High-risk risk-management process and documented intended purpose.
-   Appropriate data governance and bias/discrimination testing.
-   Technical documentation and record-keeping/logging.
-   Effective human oversight. An override button that is never used is
    not an adequate operating model.
-   Accuracy, robustness and cybersecurity controls.
-   Clear instructions for recruiters.
-   Post-market monitoring appropriate to the provider/deployer role.
-   Separate GDPR assessment, including profiling/automated-decision
    implications and applicant transparency.

Under the 2026 AI Act amendment, the main Annex III high-risk
requirements apply from **2 December 2027**.

### Decision

**APPROVE WITH CONTROLS AFTER REDESIGN --- NOT AS CURRENTLY DESIGNED.**

Keep AI-assisted ranking only with a defensible feature set and
meaningful human review before consequential rejection.

------------------------------------------------------------------------

## Case 4 --- Employee engagement / burnout detection

**Classification: Prohibited**

The staffing agency proposes analysing webcam footage and voice during
shifts to infer whether call-centre employees are "disengaged" or "at
risk of burnout," with flags sent directly to managers for coaching and
shift reassignment.

### First-pass call

The core functionality infers emotional states from
biometric/behavioural signals in a workplace. **Article 5 prohibits
workplace emotion recognition**, except for narrow medical or safety
purposes.

Calling the output "coaching" or adding manager review after the
inference does not make the underlying prohibited practice lawful.

### Role map

-   **Deployer:** staffing agency.
-   **Provider:** organisation/vendor developing and marketing the
    emotion-recognition system.
-   **Third-party vendors:** potentially webcam, voice-analysis or
    foundation-model suppliers.

### Lawful redesign

Remove emotion inference entirely.

A possible alternative architecture is:

`Employee-controlled self-report/check-in + objective operational indicators → support dashboard → manager conversation`

The redesigned system should **not infer emotional state from facial
expressions or voice**.

The replacement still requires a fresh classification. If it is used to
monitor or evaluate worker performance or materially influence work
allocation, it may fall within **Annex III high-risk employment/workers'
management**, even though the Article 5 prohibition has been removed.

### Decision

**DENY AND REDESIGN.** Do not deploy the proposed webcam/voice
emotion-recognition functionality.

------------------------------------------------------------------------

# Client discussion and final sign-off

After presenting the assessment, Mudit revealed his intended
classifications and clarified how the systems would operate in practice.
The classifications aligned across all four cases. The discussion mainly
refined the conditions for approval and the redesign boundaries.

  -----------------------------------------------------------------------------
  Case              Client response /      What changed?      Final decision
                    clarification                             
  ----------------- ---------------------- ------------------ -----------------
  **1 --- Minimal   Confirmed the tool     This removes the   **Approve**
  risk**            only schedules routine main uncertainty   
                    maintenance. It is not around a possible  
                    a safety component and Annex              
                    cannot automatically   I/product-safety   
                    operate or shut down   route to high-risk 
                    machinery.             classification.    

  **2 ---           Accepted adding a      Classification     **Approve with
  Transparency**    clear AI disclosure at unchanged. The     controls**
                    the start of the chat. principal AI Act   
                    Complex requests and   gap can be         
                    complaints continue to resolved through   
                    escalate to human      the transparency   
                    agents.                control and clear  
                                           escalation         
                                           boundaries.        

  **3 ---           Confirmed that the     Classification     **Approve after
  High-risk**       bottom 60% currently   unchanged, but the redesign**
                    receive no recruiter   current            
                    review. The video      implementation is  
                    "culture fit" feature  not ready for      
                    is intended to assess  approval. Human    
                    communication/style,   oversight must be  
                    but its methodology is operational, and   
                    not yet defined.       the video feature  
                                           requires further   
                                           assessment.        

  **4 ---           Confirmed that         Original design    **Deny /
  Prohibited**      disengagement and      remains            redesign**
                    burnout are inferred   prohibited. The    
                    from facial            replacement must   
                    expressions and voice. be classified      
                    Accepted removing that again because      
                    functionality and      worker evaluation  
                    exploring self-report  or shift           
                    plus objective         allocation may     
                    workload signals.      still be           
                                           high-risk.         
  -----------------------------------------------------------------------------

## What changed after the client discussion?

My initial classifications matched the client's intended categories. The
discussion did not materially change the risk calls, but it changed the
**conditions for approval**.

For Case 1, confirming that predictive maintenance is not a safety
component removed the main classification uncertainty. For Case 2, the
compliance gap can be addressed through a straightforward Article 50
transparency control.

Case 3 highlighted that **human oversight must exist in the actual
operating process, not only technically**: an override capability has
little value if recruiters never see rejected candidates. The undefined
video-based "culture fit" score also needs further investigation before
approval.

Case 4 demonstrated that human oversight cannot make an otherwise
prohibited practice acceptable. The business objective can still be
pursued, but the architecture must remove workplace emotion recognition
entirely. The redesigned system must then be classified again.

## Final consulting takeaway

AI Act classification depends on the system's **intended purpose, the
people affected, how outputs influence decisions, and how the system
operates in practice** --- not simply on the model, industry, or
presence of a human override.

## Legal references

-   Regulation (EU) 2024/1689 (EU AI Act): Article 5, Article 6, Annex
    I, Annex III and Article 50.
-   Regulation (EU) 2026/1744: 2026 amendments, including revised
    application dates for high-risk requirements.
-   European Commission guidance on AI Act transparency obligations and
    high-risk classification.
