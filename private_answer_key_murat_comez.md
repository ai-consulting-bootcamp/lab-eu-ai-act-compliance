# EU AI Act Approval Pack – Murat Çömez
## Part 1 – Private answer key (do NOT share with partner)

> The partner version (`client_briefs_for_partner.md`) uses **Client A–D in shuffled order** so the position of a case gives no hint. Mapping below.

| Case | Partner label | Client brief (short) | Intended category | Why I chose it (one sentence) |
|---|---|---|---|---|
| Case 1 – Prohibited | **Client C** | Bank contact centre: vendor plug-in reads agents' voice + webcam for "stress / frustration / disengagement" and feeds a score into performance reviews and shift planning | **Prohibited – Art. 5(1)(f)** | It infers the emotions of natural persons in the workplace from biometric data (voice, face) and is not used for medical or safety reasons. |
| Case 2 – High-risk | **Client B** | BNPL fintech: ML model sets each customer's spending limit and approves/declines at checkout | **High-risk – Annex III, point 5(b)** | It evaluates the creditworthiness of natural persons / establishes their credit score, and it is not a fraud-detection use. |
| Case 3 – Limited risk / transparency | **Client D** | Home & motor insurer: 24/7 GenAI assistant "Lena" on website + WhatsApp for claim status and coverage questions, hands off decisions to humans | **Limited risk – Art. 50(1) (+ 50(2) for the generated content)** | It interacts directly with people, so they must be told they are talking to an AI; it does not decide claims or price life/health insurance, so it stays out of Annex III. |
| Case 4 – Minimal risk | **Client A** | Bank risk function: LLM suggests Basel event type, root-cause tag and summary for internal loss events; analyst accepts or edits | **Minimal risk – no specific AI Act obligations** | It is internal decision support on operational events, not on people, and a human makes every final entry; only Art. 4 AI literacy and parallel laws (GDPR, DORA, MaRisk) apply. |

---

### Case 1 – Prohibited (Client C)
- **Trigger:** emotion recognition (Art. 3(39)) using biometric data (voice prosody, facial expression) of **employees**.
- **Art. 5(1)(f):** prohibited to place on the market / put into service / use AI to infer emotions of a natural person in the areas of **workplace** and education, except for medical or safety reasons. Applies since **2 Feb 2025**.
- "Wellbeing" framing does not make it a medical/safety use; the output goes into performance reviews and shift allocation.
- **Borderline argument the partner may raise:** "It only analyses the call, not the person" → still prohibited, because the emotion is inferred about the agent. Analysing **customer** sentiment from text transcripts (no biometrics) would not be Art. 5(1)(f).
- **Expected decision:** Deny and redesign → e.g. text-based call quality scoring on transcripts (script adherence, resolution, compliance phrases), no biometric inference, aggregated at team level, not used for individual sanctions. Note: if used for individual evaluation, that redesign could fall into **Annex III point 4(b)** (monitoring/evaluating performance of workers) → high-risk. Works council (BetrVG §87(1) Nr. 6) + GDPR/§26 BDSG also needed.

### Case 2 – High-risk (Client B)
- **Trigger:** Annex III 5(b) – creditworthiness / credit score of natural persons. Exception only for fraud detection, which this is not.
- **Roles:** external ML vendor = **provider**; fintech = **deployer**. Borderline: fintech fine-tunes and runs it under its own brand → could become provider under **Art. 25(1)** (substantial modification / own name).
- **Obligations:** provider – Art. 9–15 (risk management, data governance, technical documentation, logging, transparency to deployers, human oversight design, accuracy/robustness), conformity assessment, CE marking, EU database registration, QMS. Deployer – Art. 26 (use per instructions, competent human oversight, monitor, keep logs ≥ 6 months, inform affected persons) + **Art. 27 FRIA** (explicitly required for deployers using Annex III 5(b)) + Art. 86 right to explanation.
- **Parallel:** GDPR Art. 22 (fully automated declines), SCHUFA judgment (CJEU C-634/21), Consumer Credit Directive (CCD2) creditworthiness rules, BaFin model risk expectations.
- **Expected decision:** Approve with controls (human review route for declines and borderline limits, logging, FRIA before go-live, vendor evidence pack).
- **Timing note for legal team:** Annex III obligations were set to apply from 2 Aug 2026; verify current date given the Digital Omnibus proposal to postpone high-risk obligations.

### Case 3 – Limited risk / transparency (Client D)
- **Trigger:** AI system intended to interact directly with natural persons → **Art. 50(1)**: inform people they are interacting with AI (unless obvious). GenAI text → **Art. 50(2)** machine-readable marking is a **provider** duty (model/system provider).
- Not Annex III: Annex III 5(c) covers risk assessment and pricing for **life and health** insurance only; this is home/motor and the bot does not decide claims.
- **Persona risk:** a human name + photo ("Lena") makes non-disclosure more likely to mislead → disclosure must be clear at the first interaction, on every channel.
- **Borderline:** follow-up emails "sent under the claims handler's name" → not strictly an Art. 50(4) public-interest text, but sending AI text as if a human wrote it is a consumer-protection / trust issue; recommend disclosure or human approval before sending.
- **Expected decision:** Approve with controls (disclosure banner + first message, no claim decisions, hand-off rules, logging, accuracy testing on policy wordings).

### Case 4 – Minimal risk (Client A)
- AI involved, but no Art. 5 practice, no Annex III area (not employment evaluation, not credit, not access to services), no direct interaction with the public, no deepfakes.
- **Still applies:** Art. 4 AI literacy (since 2 Feb 2025); voluntary codes of conduct (Art. 95).
- **Parallel issues to flag:** GDPR (employee names / customer numbers in free text → pseudonymise before prompt, DPA with Microsoft, EU data residency), DORA (ICT third-party risk register, the LLM is an ICT service), MaRisk AT 9 outsourcing assessment, regulatory reporting accuracy (loss data goes to the board and supervisor → model validation, sample checks).
- **Borderline:** if the tool started rating **which employee** caused a loss and fed HR decisions → moves towards Annex III 4(b).
- **Expected decision:** Approve (with good-practice controls, not AI Act obligations).
