# EU AI Act Approval Pack – Nicolò

**Client question:** "Can we launch this?" · **Cases:** A–D (briefs by Friedrich) · **Date:** 16 Nov 2026

## Executive summary

Of the four proposals, one can launch as is, two can launch once specific controls are in place, and one cannot launch in its current form.

| Case | Inferred category | Decision |
|---|---|---|
| A – Funding consultancy | Minimal risk | **Approve** (fix the marketing claim) |
| B – Contact-centre outsourcer | Prohibited (Art. 5(1)(f)) | **Deny and redesign** |
| C – Hotel group | Limited risk / transparency (Art. 50) | **Approve with controls** |
| D – Vocational training provider | High-risk (Annex III 3) | **Approve with controls** |

**Timing.** The Art. 5 bans have applied since Feb 2025, and the Art. 50 transparency duties since Aug 2026. After the Digital Omnibus on AI, obligations for stand-alone high-risk (Annex III) systems apply from **2 Dec 2027**. GDPR, consumer law and anti-discrimination law apply today in every case.

---

## Case A – Funding consultancy: AI grant-matching

**Category: Minimal risk.** The tool ranks grant programmes for *companies*. It doesn't assess natural persons, isn't a listed Annex III use, and doesn't interact with the public.

**Architecture.**
- **Trigger:** a CRM client record, or a newly published funding call.
- **System:** a rules filter for hard criteria (size, sector, region, de minimis), then semantic matching of the project description against programme texts, giving a fit score with cited reasons and flagged uncertainties.
- **Human review:** the consultant checks eligibility before pitching.
- **Output:** a shortlist and deadline alerts.
- **Records:** score, model version and programme-document version are logged.

**Roles.** The consultancy is **provider and deployer** of its in-house tool. The LLM vendor is a **GPAI model provider**.

**Implications.** The AI Act sets no specific obligations, but there are parallel issues:
- "AI-verified eligibility" is misleading under unfair-competition law (UWG/UCPD). Only the funding body decides eligibility. Replace it with "AI-assisted pre-screening, final eligibility confirmed by the funding body".
- GDPR for contact persons in the CRM.
- A data-processing agreement and confidentiality terms for client project descriptions sent to the LLM.

**Decision: Approve.**

*Borderline:* if the tool is opened to SMEs as a self-service chat, Art. 50(1) disclosure applies. *Next artifact:* revised website wording and a client-data handling note.

---

## Case B – Contact-centre outsourcer: "wellbeing assistant"

**Category: Prohibited.** Voice tone and webcam images are biometric data, and inferring stress or frustration from them is emotion recognition. Doing that in the workplace is banned under Art. 5(1)(f). The only exceptions are medical or safety reasons, and the Commission's guidelines exclude general wellbeing and stress monitoring from them. "A team lead always looks first" doesn't cure the ban, and feeding the output into shifts and coaching makes it worse. The **customer-mood** module isn't banned, because callers aren't in a workplace context, but it is high-risk (Annex III 1(c)) and callers must be informed (Art. 50(3)).

**Roles.** The vendor is the **provider**; the outsourcer is the **deployer**. Under Art. 5 the vendor can't place the system on the market and the outsourcer can't use it. End-clients (telecom/insurance) are likely GDPR controllers for customer call data.

**Implications.** Fines run up to €35m or 7% of global turnover. In parallel: GDPR Art. 9 (biometric data) and works-council co-determination (BetrVG §87(1) no. 6, if in Germany).

**Decision: Deny as proposed, then redesign.**

**Lawful redesign – "workload, not mood":**
- **Trigger:** the end of each call.
- **System:** speech-to-text, then *text-only* analytics (topic, resolution, escalation, complaint language). No voice-tone or facial features.
- **Workload model:** flags *teams and queues* with a high load of difficult calls and triggers break rotation or queue rebalancing.
- **Human:** the team lead decides at team level.
- **Wellbeing:** voluntary, anonymous pulse surveys and occupational-health referrals.
- **Customer side:** transcript-based satisfaction topics replace voice mood scoring.
- **Guardrail:** no individual agent scores. Using analytics to evaluate individuals or allocate their shifts would make the system high-risk under Annex III 4(b).

*Borderline:* the redesign relies on text-based inference falling outside the Art. 3(39) emotion-recognition definition. **Legal should verify this** before build. *Next artifact:* a DPIA and a draft works-council agreement.

---

## Case C – Hotel group: booking voice assistant and synthetic presenter

**Category: Limited risk / transparency.** Callers interact directly with an AI system, so Art. 50(1) applies. A synthetic presenter resembling a real employee is a deepfake, so Art. 50(4) applies. Taking reservations isn't an Annex III area.

**Architecture.**
- **Trigger:** an inbound call.
- **System:** speech-to-text, then an LLM grounded on the FAQs, connected to the booking API (availability, create reservation). Reservation history is looked up only after the caller is verified.
- **Disclosure:** in the opening line ("I'm Lena, the hotel's AI assistant").
- **Human handover:** for complex requests, complaints, or on request at any time.
- **Output:** a booking and a confirmation email.
- **Records:** transcripts with defined retention, and a reservation audit trail.
- **Video:** generated with the vendor's tool, labelled "AI-generated", with the employee's written consent.

**Roles.** The voice-AI vendor and the video-generation vendor are **providers** (the video vendor carries Art. 50(2) marking). The hotel group is the **deployer**. It becomes the provider if it builds the assistant itself on an LLM API.

**Implications.**
- Marketing's "sound like a real receptionist, with a name" is fine for tone and persona. It isn't fine as a pretence of being human: the assistant must disclose that it's AI and answer truthfully if asked.
- Parallel issues: GDPR (call recording, use of history), PCI DSS (no card data taken by voice), the employee's revocable consent to their likeness, and UCPD for ad claims.

**Decision: Approve with controls**, conditional on the disclosure script, video labelling and the escalation route.

*Borderline:* if the assistant starts pricing dynamically per caller profile, review again under consumer law. *Next artifact:* the transparency notice and call script.

---

## Case D – Vocational training provider: admission ranking

**Category: High-risk.** The system determines access and admission to vocational training (Annex III 3(a)) and evaluates aptitude-test results (3(b)). Calling it "just a pre-sorting aid" doesn't trigger the Art. 6(3) exemption. A ranked list that is "normally confirmed" materially shapes the outcome, and the system profiles natural persons, which keeps it high-risk in any case.

**Architecture.**
- **Trigger:** the application window closes.
- **System:** scores the aptitude test and extracts education and experience from CVs, producing a **per-criterion scorecard with reasons** rather than one opaque rank. Motivation letters are scored by humans against a rubric.
- **Human review:** two assessors decide the borderline band, plus random samples from the top and bottom, with realistic time per file. The admissions committee signs off.
- **Records:** inputs, model version, score, final decision and override reason.
- **Disclosure:** applicants are told AI is used, and there's an appeal route.

**Roles.** The EdTech vendor is the original **provider**. Retraining the model and running it under the client's own brand makes the client a **provider** under Art. 25(1), as well as the **deployer**. The vendor must hand over documentation and support compliance (Art. 25(2)).

**Implications.**
- **As provider:** risk management, data governance (including a bias audit of past admission decisions), technical documentation, logging, human-oversight design, accuracy testing, a quality-management system, conformity assessment, CE marking and EU database registration (Art. 9–17, 43, 49).
- **As deployer:** competent oversight staff, log retention, applicant information, and likely a fundamental-rights impact assessment (FRIA, Art. 27), because this is a publicly funded service.
- **Today:** GDPR Art. 22 (automated decisions) and the AGG apply already.
- **Main gap:** two minutes per applicant is automation bias, not oversight.

**Decision: Approve with controls.** It can't go live as proposed. It can go live once the human-review design, the bias audit and applicant transparency are in place. I'd recommend building to the full Annex III standard now rather than waiting for Dec 2027.

*Borderline:* if the client drops its own branding and uses the vendor model unchanged, it stays a deployer only, which is much lighter. *Legal should verify* whether this counts as a "public service" for the FRIA. *Next artifact:* a FRIA draft and a data-governance/bias-audit plan.
