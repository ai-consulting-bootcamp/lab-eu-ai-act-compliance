# Phase 2 — Apply: Classifying the Partner's Cases

Anand's four hidden client briefs were reviewed without access to his answer key. First-pass classifications were made and justified from lesson material, then refined through follow-up questioning. Both the first-pass call and the corrected reasoning are shown, since the corrections are part of demonstrating the AI Act logic accurately — a real client would expect the final memo to cite the right article and mechanism, not just land on the right label.

## Case 1 — Energy Retailer Household Scoring

**Brief summary:** Composite "customer reliability" score built from smart-meter data, social media activity, and neighborhood income/demographic indicators. Households below a threshold are automatically switched to a prepayment meter — no notice, no ability to contest, scoring logic deliberately kept opaque to prevent "gaming."

**First-pass call:** Prohibited.

**Initial reasoning (as first stated):** Described as inferring an internal state and affecting users without their knowledge, cited as falling under "Annex III."

**Correction applied:** Article 5 governs prohibited practices — Annex III is the high-risk list, not the prohibited list, and citing the wrong article would undercut credibility in front of a client. The actual mechanism is not state-inference (that pattern belongs to Case 1 in the authored set, not this case) — it is **social scoring, Article 5(1)(c)**: combining data collected in one context (social media activity, neighborhood demographics — unrelated to actual payment behavior) into a general score, then using that score to justify treatment (forced prepayment) that is disproportionate to or disconnected from the context the data came from.

**Final classification: Prohibited — Article 5(1)(c), social scoring.** The lack of notice, contestability, and transparency is a real, separate problem, but it compounds an already-prohibited practice rather than being the trigger itself.

---

## Case 2 — HR-Tech Screening Product

**Brief summary:** Scans CVs and analyzes recorded video interviews (tone, word choice, facial expression) to produce a fit score for field-technician hiring. Recruiters see a ranked list and can technically override it, but given hiring volume, are expected in practice to simply process the top-ranked names.

**First-pass call:** High-risk, Annex III.

**Initial reasoning (as first stated):** Framed the high-risk trigger as depending on whether the client intends to override human supervision.

**Correction applied:** The Annex III trigger doesn't depend on the quality of human review at all — AI used to screen, filter, or rank job applicants is explicitly named in Annex III on its own. The video-interview analysis (biometric-adjacent signals evaluating candidates) reinforces this on a second, independent basis. The human-review detail is a **separate question**: whether the required oversight control is being genuinely satisfied, not what establishes the risk tier. A recruiter told to "just process the top-ranked names" due to volume has a nominal override right that isn't practically exercised — that's a compliance gap to flag and fix, not the reason the case is high-risk in the first place.

**Final classification: High-risk — Annex III (recruitment/candidate screening).** Compliance gap identified: human oversight exists on paper but is not meaningfully exercised in practice.

---

## Case 3 — Bank Chatbot and Synthetic Voice Campaigns

**Brief summary:** A website chatbot answering account questions, plus a separate cloned "brand voice" generating synthetic audio for outbound marketing calls. Customers aren't told the chatbot is AI or that the calling voice is synthetic — marketing prefers this because a human-sounding voice tests better.

**First-pass call:** Limited risk / transparency.

**Initial reasoning (as first stated):** Correctly identified the undisclosed-AI-interaction trigger, but reasoned that the classification held because "the effects are not detrimental."

**Correction applied:** Two points refined. First, this brief actually contains **two separate Article 50 triggers**, not one: the undisclosed chatbot, and separately, the undisclosed synthetic/cloned voice used in the outbound calls (a distinct disclosure obligation for AI-generated audio content). A client fixing one would not automatically fix the other. Second, "not detrimental" isn't actually the basis for this tier — transparency obligations apply regardless of whether the interaction causes harm; that's what distinguishes this tier from prohibited/high-risk, where stakes determine the tier. The correct basis is that the case doesn't touch an Annex III domain (no employment, credit, or safety decision is involved) — not that the outcome is harmless.

**Final classification: Limited risk / transparency — Article 50, two distinct disclosure failures.** Classification is set by the nature of the interaction (AI presenting as human), not excused or triggered by outcome severity.

---

## Case 4 — Logistics Restocking AI

**Brief summary:** AI model analyzing historical sales, seasonality, and supplier lead times to generate restocking schedules and purchase order suggestions. Warehouse team reviews and approves every order before it's placed.

**First-pass call:** Minimal risk.

**Reasoning:** Ruled out each trigger rather than searching for one — no Annex III domain is touched, no individual person is evaluated or scored, no safety component is involved. This is the correct method for minimal-risk cases: systematically eliminating triggers rather than assuming safety by default.

**Refinement:** The strong human-approval step (every PO reviewed) is good operational practice, but is not what makes this minimal risk — the case would remain minimal risk even without that step, since it never approaches a regulated domain in the first place. This is the mirror image of Case 2: there, weak human review didn't remove the high-risk classification; here, strong human review doesn't create the minimal-risk classification. Risk tier and oversight quality are independent questions.

**Final classification: Minimal risk.** No AI Act-specific obligations; human approval step recommended to retain as good practice, not compliance requirement.
