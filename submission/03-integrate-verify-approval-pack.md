# EU AI Act Approval Pack
**Prepared for:** Client Portfolio Review (4 use cases)
**Prepared by:** [Your Name]
**Date:** [Date]

## Executive Summary

This pack reviews four proposed AI use cases submitted for launch approval. The overall risk picture is mixed: one proposal cannot proceed as designed and requires a full redesign; two proposals can move forward but only with specific controls attached before go-live; one proposal is clear to launch as-is. A recurring theme across the higher-risk cases is that human oversight was described as present but not meaningfully exercised — this pack treats "human in the loop" as a control that must be functioning in practice, not just available on paper, before it counts toward compliance.

| Case | Summary | Category | Decision |
|---|---|---|---|
| 1 | Household reliability scoring → automatic prepayment switch | Prohibited | **Deny — redesign required** |
| 2 | AI candidate screening & video-interview scoring | High-risk | **Approve with controls** |
| 3 | Undisclosed AI chatbot + cloned voice outbound calls | Limited risk / transparency | **Approve with controls** |
| 4 | AI-generated warehouse restocking suggestions | Minimal risk | **Approve** |

---

## Case 1 — Household Reliability Scoring

**What's proposed:** A composite risk score per household, built from smart-meter data, social media activity, and neighborhood income/demographic indicators, used to automatically switch low-scoring customers to prepayment meters — without notice, without a contest process, and with the scoring logic deliberately kept opaque.

**Classification: Prohibited (Article 5(1)(c) — social scoring).** The system evaluates people using data unrelated to the context it's being used against — social media activity and neighborhood demographics have no direct bearing on actual payment reliability — and applies the resulting score to justify treatment (forced prepayment) that is disproportionate to, and disconnected from, how that data was generated. The complete absence of notice or contestability compounds the problem but is not the core trigger; the scoring practice itself is prohibited regardless of process.

**Architecture as proposed:** Smart-meter reading cycle → composite scoring model (meter + social + demographic inputs) → automatic threshold-based meter switch → no human checkpoint, no disclosure.

**Roles:** Retailer acts as both provider and deployer.

**Decision: Deny as proposed.**

**Redesign path:** A lawful version of this use case is achievable by narrowing the data inputs and adding process safeguards:
- Base the score only on actual payment/usage signals — missed payments, unusual consumption patterns suggesting tampering or non-payment risk
- Drop social media and demographic data entirely
- Require human review before any meter-type change is applied
- Notify the customer of the change and provide a clear path to contest it before or promptly after the switch

This redesigned version would likely fall outside Article 5 entirely, since it no longer relies on unrelated data to justify disproportionate treatment — though it should be re-reviewed once specced, as consumer-protection and utility-sector regulations may still apply separately from the AI Act.

---

## Case 2 — AI Candidate Screening Tool

**What's proposed:** An HR-tech product that screens CVs and analyzes recorded video interviews (tone, word choice, facial expression) to produce a candidate fit score, presented to recruiters as a ranked list.

**Classification: High-risk (Annex III — recruitment and selection).** AI used to screen, filter, or rank job applicants is explicitly named in Annex III; the video-interview analysis (evaluating candidates via tone and facial expression) reinforces this classification on a second, independent basis.

**Architecture as proposed:** CV submitted → resume screening/ranking model → video-interview analysis model (tone, word choice, facial expression) → composite fit score → recruiter sees ranked shortlist → recruiter can technically override, but given hiring volume, in practice top-ranked names are processed with minimal scrutiny.

**Roles:** HR-tech startup is the provider; each hiring company using the tool is the deployer.

**Compliance gap identified:** The human oversight described in this proposal exists on paper but is not functioning as a genuine control — a reviewer who is expected to simply process top-ranked names is not exercising meaningful oversight. High-risk AI Act obligations require oversight that is real, not nominal.

**Required controls before launch:**
- Documented technical file and risk management system
- Bias and accuracy testing specifically on the video/facial-expression analysis component, given known risks of bias in this type of signal
- A redesigned review workflow that ensures genuine human judgment is applied — for example, mandatory documented review of any candidate the model ranks highly but who differs meaningfully from other shortlisted candidates on demographic or background factors
- Disclosure to candidates that AI is used in the screening process
- Logging and record-keeping sufficient to support an audit

**Decision: Approve with controls**, contingent on the above being implemented and verified before go-live, not treated as a post-launch improvement.

---

## Case 3 — Chatbot and Synthetic Voice Campaigns

**What's proposed:** Two separate AI-driven customer-facing tools: a website chatbot answering account questions, and a cloned "brand voice" used to generate synthetic audio for outbound marketing calls. Neither discloses to the customer that they are interacting with AI.

**Classification: Limited risk / transparency (Article 50) — two distinct triggers.** This case does not touch an Annex III domain (no employment, credit, or safety decision is being made), so it does not rise to high-risk — but transparency obligations apply regardless of stakes, based on the nature of the interaction itself:
1. The chatbot must disclose that the customer is interacting with an AI system, unless this is already obvious from context.
2. The cloned voice used in outbound calls is synthetic audio content and separately triggers a disclosure obligation that the voice is AI-generated, not human.

These are two separate compliance gaps, and fixing one does not resolve the other.

**Roles:** The bank is the deployer for both tools; if either the chatbot or voice-cloning technology is licensed from a third party, that vendor is likely also a provider — this should be confirmed directly with the client, as it wasn't specified in the brief.

**Required controls before launch:**
- Clear, upfront disclosure at the start of any chatbot interaction that the customer is speaking with an AI
- Clear disclosure at the start of any outbound call using the synthetic voice
- Internal policy alignment — marketing's stated preference for a "more human-sounding" voice is a business consideration, not a basis for skipping a legal disclosure requirement

**Decision: Approve with controls**, contingent on both disclosures being implemented before either tool launches.

---

## Case 4 — Warehouse Restocking AI

**What's proposed:** An AI model that analyzes historical sales, seasonality, and supplier lead times to generate restocking schedules and purchase order suggestions, which the warehouse/procurement team reviews and approves before any order is placed.

**Classification: Minimal risk.** No individual person is evaluated or scored, no Annex III domain is touched, and no safety component is involved. The strong human-approval step is good operational practice, but it is not what determines the classification here — this use case would remain minimal risk even without it, since it never approaches a regulated domain in the first place.

**Architecture as proposed:** Historical sales/seasonality/lead-time data → forecasting and restocking-suggestion model → generated purchase order → warehouse/procurement review and approval → order placed.

**Roles:** Depends on whether the forecasting model is built in-house or licensed — this should be confirmed with the client, as it affects vendor due diligence even though it doesn't affect the AI Act classification.

**Decision: Approve.** No redesign or AI Act-specific controls required.

**Parallel issues to flag (not AI Act, but worth noting):** data governance and accuracy of the forecasting inputs; standard vendor due diligence if a third-party model is used; ordinary business-continuity risk if forecasts are wrong — an operational risk, not a legal one.

---

## Closing Note

Across this portfolio, the pattern worth highlighting to the client is that risk category and human-oversight quality are two separate questions that need separate answers. In Case 2, weak human review didn't change the risk category — it created a compliance gap on top of an already-established high-risk classification. In Case 4, strong human review didn't create the low-risk classification — it was simply good practice layered on top of a use case that was already outside AI Act scope. Getting this distinction right is what separates a defensible classification from a guess.
