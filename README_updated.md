# LAB | Classify Your Product — EU AI Act Compliance

**Student:** Parisa Dehghani  
**Module:** Module 7 — EU AI Act  
**Lab:** Classify Your Product  
**Submission:** GitHub repository / pull request

## Overview

This repository contains my completed submission for the **EU AI Act compliance consulting lab**.

The lab work includes:

- four hidden client scenarios across the four AI Act outcomes,
- a consulting review of a partner's proposed AI systems,
- proposed AI architectures and operating models,
- provider / deployer / vendor role mapping,
- compliance controls and approval decisions, and
- a completed client-discussion debrief.

The work covers the four practical AI Act outcomes used in the lab:

- **Prohibited**
- **High-risk**
- **Limited risk / transparency**
- **Minimal risk**

## Repository Files

| File | Purpose |
|---|---|
| `EU_AI_Act_Approval_Pack_Client(Parisa)_Scenarios.md` | **Phase 1 — Recognize.** Contains my four original client scenarios, private answer key, intended AI Act categories, and reasons for each classification. |
| `EU_AI_Act_Parisa_Auditted_Louise's_Cases_Final.md` | **Phases 2 and 3 — Apply, Integrate, and Verify.** Contains my final audit of Louise Plessis's four client cases, first-pass classifications, AI architectures, provider/deployer/vendor roles, controls, consulting decisions, approval pack, lawful redesign, and legal references. |
| `final-debrief.md` | **Phase 4 — Debrief.** Contains the completed client discussion and final sign-off, comparison with the partner's intended answer key, clarifications from the discussion, changes to controls/architecture, and final reflection. |
| `EU_AI_Act_Approval_Pack_consulting(Mudit)_review.md` | **Partner consulting review.** Contains Mudit's consulting review of my four proposed AI use cases, including classifications, architecture, compliance implications, decisions, redesign guidance, and a high-risk implementation roadmap. |
| `README.md` | Repository overview, file map, workflow summary, and completion status. |

> The Phase 4 file is named exactly **`final-debrief.md`** in the repository.

## Phase 1 — Hidden Client Scenarios

I created four client scenarios with exactly one intended case in each required category:

1. **Prohibited** — AI-powered shoplifting risk detection
2. **High-risk** — AI recruitment candidate screening
3. **Limited risk / transparency** — AI customer support chatbot
4. **Minimal risk** — AI product description generator

My private answer key and client briefs are contained in:

`EU_AI_Act_Approval_Pack_Client(Parisa)_Scenarios.md`

## Phase 2 — Consulting Review of Partner Cases

I reviewed Louise Plessis's four hidden cases and made a first-pass AI Act classification for each one.

For every case, I documented:

- likely AI Act category,
- reason for the first-pass classification,
- proposed AI architecture,
- inputs and system behaviour,
- human review point,
- output / decision,
- logging or disclosure layer,
- provider / deployer / vendor roles,
- required obligations or controls, and
- final consulting decision.

The completed review is contained in:

`EU_AI_Act_Parisa_Auditted_Louise's_Cases_Final.md`

## Phase 3 — EU AI Act Approval Pack

The consulting review also contains the approval pack, including:

- executive summary,
- all four client cases,
- inferred category for each case,
- proposed architecture and role map,
- compliance implications,
- required controls,
- final decision,
- lawful redesign for the prohibited case,
- cross-case recommendations,
- borderline questions for discussion, and
- evidence / operational artifacts to request next.

## Phase 4 — Client Discussion and Final Debrief

After presenting my assessment, Luise Plessis revealed her intended classifications and we compared them with my first-pass calls.

**All four classifications matched the intended answer key.**

| Case | My classification | Client's intended category | Result |
|---|---|---|---|
| **1 — Payment support operations** | Minimal risk | Minimal risk | **Match** |
| **2 — Employee coaching platform** | High-risk | High-risk | **Match** |
| **3 — Beauty & wellness app** | Prohibited | Prohibited | **Match** |
| **4 — Reality-TV companion** | Limited risk / transparency | Limited risk / transparency | **Match** |

The discussion did not change the final risk categories or overall recommendations, but it clarified important operating boundaries and strengthened several controls.

The completed Phase 4 discussion is contained in:

`final-debrief.md`

## Final Decisions on the Reviewed Cases

| Case | Classification | Final decision |
|---|---|---|
| **1. Payment support operations** | Minimal risk | **APPROVE** |
| **2. Employee coaching platform** | High-risk | **APPROVE WITH CONTROLS** |
| **3. Beauty & wellness app** | Prohibited | **DENY AND REDESIGN** |
| **4. Reality-TV companion** | Limited risk / transparency | **APPROVE WITH CONTROLS** |

## Main Controls and Architecture Changes Confirmed During Debrief

- **Case 1:** Keep the system limited to ticket classification, priority and routing. Retain human override, logging and a strict boundary preventing use for merchant eligibility or access to financial services.
- **Case 2:** Maintain the high-risk classification and strengthen meaningful human oversight, employee information, access controls, bias/accuracy testing and logging.
- **Case 3:** Remove age, insufficient-funds signals and appearance-based vulnerability from the targeting logic. Replace them with neutral user preferences, notification limits and opt-outs, then reclassify the redesigned system.
- **Case 4:** Keep the core retrieval-and-generation architecture, but make AI disclosure, factual/theory separation, spoiler controls, approved-source retrieval, moderation and logging explicit.

## Key EU AI Act Topics Applied

This submission applies the main EU AI Act topics covered in the lab:

- Article 5 prohibited practices
- Annex III high-risk uses
- Article 50 transparency obligations
- Minimal-risk AI systems
- Provider vs. deployer responsibilities
- Third-party vendor roles
- Human oversight
- Risk management
- Data governance
- Bias and accuracy testing
- Technical documentation and logging
- Transparency and disclosure
- Lawful redesign of prohibited systems
- GDPR and other parallel compliance considerations where relevant

## Completion Status

- [x] Phase 1 — Hidden client scenarios and private answer key
- [x] Phase 2 — Partner-case classification and consulting review
- [x] Phase 3 — Approval pack with architecture, roles, controls, decisions and prohibited-case redesign
- [x] Phase 4 — Completed client discussion and final debrief
- [x] README repository map
