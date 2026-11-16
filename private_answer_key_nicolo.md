# EU AI Act Approval Pack – Private Answer Key (Nicolò)

**Do not share with Friedrich until Phase 4.**

## Author template

| Case | Client brief for partner | Intended category | Why I chose it |
|---|---|---|---|
| 1 | Callwerk Services: a call-centre BPO reads agents' voice tone and webcam facial expressions to score mood and engagement. The score is used for coaching, account allocation and shifts. | **Prohibited** | Inferring the emotions of employees from biometric data (voice, face) in the workplace is banned under Art. 5(1)(f). The only exceptions are medical or safety reasons, and neither applies here. |
| 2 | Paylo: a BNPL fintech uses an automated model to approve pay-later and set spending limits, based on checkout, device, repayment and bank-transaction data. | **High-risk** | Evaluating the creditworthiness of natural persons is an Annex III use (point 5(b)). The fraud-detection carve-out doesn't apply, because the output is a credit approval and a limit. |
| 3 | Radhaus Brandt: an e-bike retailer runs a 24/7 phone and WhatsApp assistant with the founder's cloned voice, plus AI-generated videos of "Jonas". | **Limited risk / transparency** | Customers interact directly with an AI system, so Art. 50(1) requires them to be told. The synthetic "Jonas" audio and video are deepfakes, which Art. 50(4) requires to be disclosed. Nothing it decides falls under Annex III. |
| 4 | Nordholz Baustoffe: a materials wholesaler forecasts product demand per depot and suggests reorder quantities. Buyers approve every order. | **Minimal risk** | The tool forecasts products, not people. It's not an Art. 5 practice, not in Annex III, and it involves no chatbot or synthetic content, so the AI Act sets no specific obligations. |

---

## What I'm listening for in Friedrich's review (Phase 4)

**Case 1 – Prohibited**
- Traps: the "wellbeing tool" framing, and the "team leads can overrule it" line. Neither changes the classification, because the ban covers the practice itself, not how the output is used.
- A good answer: deny as proposed, then redesign. For example, aggregate call-quality analytics on the *content* of calls (resolution, handling time, script adherence) with no emotion inference, plus voluntary pulse surveys for wellbeing.
- Parallel issues: GDPR (employee biometric data), and works-council co-determination under BetrVG §87(1) no. 6.

**Case 2 – High-risk**
- Role nuance: the vendor is the provider of the base system. Paylo retrains the model and puts it into service under its own name, so it may become a provider itself (Art. 25, substantial modification). Friedrich should flag this.
- A good answer: approve with controls. That means a risk-management system and technical documentation from the provider, data governance and bias checks, and logging. Human oversight has to come *before* the final decline, not only on complaint. Paylo also needs a FRIA: Art. 27 explicitly covers deployers of 5(b) systems.
- Parallel issues: GDPR Art. 22 (solely automated decisions with legal or similarly significant effects), and consumer-credit rules.

**Case 3 – Limited risk / transparency**
- Trap: "customers just feel they're talking to us". That wish directly conflicts with Art. 50.
- A good answer: approve with controls. The assistant discloses at the start of every call or chat that it's AI. The synthetic Jonas videos are labelled as AI-generated. There's a clear handover to a human, and the scope stays at booking and information (no refund or credit decisions). The voice-tool vendor, as provider, carries the Art. 50(2) marking duties.
- Parallel issues: Jonas's written consent to the voice clone, GDPR for call recordings, and misleading-advertising rules (UWG).

**Case 4 – Minimal risk**
- Trap: the temp-worker sentence pulls the reviewer toward the employment area of Annex III (point 4). In my reading, an aggregate headcount forecast doesn't allocate tasks to individuals or evaluate them based on their behaviour or traits, so it isn't 4(b).
- A good answer: approve, but flag that if the tool ever starts picking *which* workers get booked, or rating them, it needs reclassifying. Parallel issues are light: GDPR only if customer-level data is used.

## Legal check needed
Get a lawyer to verify the Art. 25 provider shift for Paylo (Case 2), and whether the staffing use in Case 4 stays outside Annex III point 4.
