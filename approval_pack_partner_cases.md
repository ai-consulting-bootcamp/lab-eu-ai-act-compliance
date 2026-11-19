# EU AI Act Approval Pack – "Can we launch this?"
**Consultant:** Murat Çömez · **Client:** Max (four client cases) · **Date:** 18 Nov 2026

> First-pass consulting view, not legal advice. Final interpretation to be confirmed by the client's legal team.

## 1. Executive summary
Of the four use cases, **one cannot launch** as designed (workplace emotion recognition is prohibited), **one is high-risk** and can launch only after a full compliance programme (health scoring for insurers), **one needs transparency controls** (AI marketing images), and **one can go ahead** with good data hygiene (duplicate cleaning). GDPR is the second big constraint in cases 1 and 2, because both rely on sensitive personal data.

| Case | Inferred category | Decision | Biggest blocker |
|---|---|---|---|
| 1 Smartwatch health scores for insurers | High-risk (Annex III 5(c)) | Approve with controls | Conformity assessment + explicit consent for health data |
| 2 Supermarket emotion monitoring | Prohibited (Art. 5(1)(f)) | Deny and redesign | Emotion recognition at work is banned |
| 3 Database duplicate cleaning | Minimal risk | Approve | Wrong automatic merges (GDPR accuracy) |
| 4 AI furniture marketing | Limited risk (Art. 50) | Approve with controls | Disclosure and true-to-product images |

## 2. Case-by-case assessment

### Case 1 – Smartwatch health data for insurers
- **Client request:** Sell AI health risk scores, based on smartwatch data, to health and life insurers for premium and eligibility decisions.
- **Category and basis:** **High-risk, Annex III 5(c)** (risk assessment and pricing of natural persons for life and health insurance).
- **Architecture:** insurer request for an opted-in customer → risk score from wearable data → **underwriter review** of score, main drivers and data gaps → premium/eligibility decision with explanation to the customer → logs of inputs, score, reviewer and overrides, plus a consent register.
- **Role map:**
  - Provider: smartwatch manufacturer
  - Deployers: insurers
  - Vendor: cloud/ML platform, possibly a US analytics provider
- **Compliance implications:**
  - Provider: risk management, data governance and bias testing, technical documentation, logging, instructions for use, human oversight design, accuracy (Art. 9–15); QMS, conformity assessment, CE marking, registration.
  - Insurers: Art. 26 duties, a **FRIA (Art. 27)** before first use, and a right to explanation (Art. 86).
  - GDPR: health data needs **explicit, separate consent** (Art. 9(2)(a)); Art. 22 safeguards; a DPIA.
  - Other laws: ePrivacy/TDDDG §25 for device data, and the **Data Act** for data from connected products.
- **Decision:** **Approve with controls.** Launch the consumer health insights first; open the insurer channel only after conformity assessment, FRIA templates for insurers, and an opt-in that is not a condition for using the watch.
- **Borderline / legal to verify:** whether using lifestyle data from a consumer device to raise premiums is **social scoring (Art. 5(1)(c))**, i.e. data from an unrelated context leading to detrimental treatment. If yes, it is prohibited.
- **Next artifact:** FRIA draft for the insurer, and a consent and transparency notice.

### Case 2 – Supermarket emotion monitoring
- **Client request:** Cameras at checkouts analyse staff facial expressions and give each employee an emotion score that feeds rankings, evaluations and shift planning.
- **Category and basis:** **Prohibited, Art. 5(1)(f)**: emotion recognition in the workplace, not for medical or safety reasons.
- **Architecture (as proposed):** camera → facial emotion model → individual score → manager ranking. Not acceptable.
- **Role map:** provider: camera/AI vendor · deployer: supermarket chain.
- **Compliance implications:** banned since 2 Feb 2025, with fines up to €35m or 7% of turnover. It is also biometric data under GDPR Art. 9 and requires works council co-determination (BetrVG §87(1) Nr. 6).
- **Decision:** **Deny and redesign.**
- **Redesign option:** measure the **service, not the person**:
  - store- or shift-level queue and transaction times
  - customer feedback terminals
  - voluntary, anonymous employee pulse surveys
  - no cameras on staff and no biometric inference

  If the client later wants individual performance evaluation by AI, that is **high-risk (Annex III 4(b))** and needs the full programme.
- **Borderline / legal to verify:** a "wellbeing" or "safety" framing does not create the medical/safety exception.
- **Next artifact:** an employee-feedback survey design and a works council information pack.

### Case 3 – Database duplicate cleaning
- **Client request:** An ML tool finds and merges duplicate records, checks new entries in real time, auto-processes high-confidence matches and sends uncertain ones to staff.
- **Category and basis:** **Minimal risk**: no Art. 5 practice, no Annex III area, no public interaction, no synthetic content.
- **Architecture:** new record or batch scan → similarity model → high-confidence match **auto-merged, reversibly**; uncertain match to a data steward → merge log (before/after, confidence, who or what).
- **Role map:** provider: tool vendor or in-house team · deployer: the company · vendor: possibly a SaaS data-quality platform.
- **Compliance implications:**
  - AI Act: Art. 4 AI literacy only.
  - GDPR: if records are customers or employees, wrong merges break **accuracy (Art. 5(1)(d))** and can expose one person's data to another; deletions must respect retention and rectification rights; the vendor needs a DPA.
- **Decision:** **Approve.**
- **Borderline / legal to verify:** if merged customer records feed decisions on access to services (e.g. credit), the downstream system may be in scope, not this tool.
- **Next artifact:** a merge and audit logging policy, with a confidence threshold and an undo procedure.

### Case 4 – AI furniture marketing
- **Client request:** Generative AI enhances product photos into styled room scenes and writes promotional text for brochures, social media and the website; marketing reviews before publication.
- **Category and basis:** **Limited risk, Art. 50.** The provider marks AI output (50(2)); the retailer discloses realistic generated images that could look authentic (50(4)).
- **Architecture:** product photo → GenAI scene and copy → **marketer checks** that the product is shown accurately and claims are true → publish with an "AI-generated image" label → asset log (prompt, model, approver).
- **Role map:** provider: GenAI tool vendor · deployer: furniture retailer.
- **Compliance implications:**
  - AI Act: Art. 50 disclosure; Art. 4 literacy.
  - Consumer protection (UCPD): images must not change the product's real colour, size or material, which would be misleading advertising.
  - Rights in reference images.
- **Decision:** **Approve with controls.**
- **Borderline / legal to verify:** pure lighting or retouching edits may fall under the "standard editing" exception to 50(2); full scene generation does not.
- **Next artifact:** a transparency label guideline and a product-accuracy checklist for the marketing team.

## 3. Stretch – mini roadmap for Case 1 (high-risk)
- **Provider (smartwatch maker) before market placement:**
  - risk management file
  - training data documentation, including bias tests across age, sex and disability
  - technical documentation and instructions for use for insurers
  - automatic logging
  - human oversight design (score drivers shown to the underwriter)
  - accuracy metrics
  - QMS
  - conformity assessment (internal control under Annex VI), EU declaration, CE marking, EU database registration
  - post-market monitoring plan
- **Deployer (insurer) before first use:**
  - **FRIA**
  - trained underwriters with authority to override
  - log retention of at least 6 months
  - customer information and an explanation process (Art. 86)
  - GDPR DPIA and Art. 22 safeguards
- **Evidence to request from the vendor:** EU declaration of conformity, registration number, instructions for use, model performance and bias test results by group, logging specification, data source and consent records, incident reporting contact.

## 4. Closing note – what changed after the client discussion?
- **Partner's intended categories vs mine:** at submission, Max had not yet confirmed his answer key in writing. The four briefs show one clear pattern per tier, and my calls (high-risk / prohibited / minimal / limited) follow that pattern. _If Max's key differs, this section will be updated in the same pull request._
- **Client response:** no challenge or redesign request received from Max at submission.
- **What I changed and why:** nothing in the classifications. After reviewing the GDPR side in the Tuesday labs, I strengthened Case 1 by adding explicit consent (Art. 9(2)(a)), the Data Act and ePrivacy, because health data from a connected device triggers all three.
