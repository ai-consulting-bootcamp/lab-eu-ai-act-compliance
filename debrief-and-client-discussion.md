# Debrief and client discussion

> **Simulation disclosure.** My partner (S. Rostovskyi) was not available for the live session. The **briefs and answer key are the partner's real work** ([repo](https://github.com/s-rostovskyi/lab-eu-ai-act-compliance)). I wrote my review before opening their answer key. The **client discussion below was simulated with an AI assistant** playing the client, raising the challenges the partner's briefs invite. The partner has not yet reviewed my briefs; that review is still pending.

## 1. Intended vs. inferred

| Partner case | Partner's intended category | My inferred category | Match | Notes |
|---|---|---|---|---|
| A - Rail chat widget | Limited (Art 50(1), (2), (5)) | Limited (Art 50(1), 50(2) flagged for legal check) | ✅ | Partner treats 50(2) marking as applying outright. I hedged. 50(5) (disclosure at first interaction, clear and accessible) I covered in substance but didn't cite. |
| B - Applicant ranking | High-risk (Art 6(2), Annex III §4(a)) | High-risk (Annex III §4(a)) | ✅ | Same reasoning: the top-20 habit means the rank matters despite the override. |
| C - Carton forecast | Minimal (Art 4 still applies) | Minimal (Art 4 still applies) | ✅ | I also raised the Art 3(1) "is it even AI?" question. |
| D - Agent voice emotion | Prohibited (Art 5(1)(f)) | Prohibited (Art 5(1)(f)) | ✅ | Same. |

**Score: 4/4.**

## 2. How well the hidden scenarios worked

- **Worked well:** **A** is a good test. "Rail" makes you think of critical infrastructure (Annex III §2), and you have to notice it isn't a safety component. **B** has a realistic trap: on paper the human can override, but in practice the first 20 names decide.
- **Too revealing:** **D** ("the tool has no medical or safety purpose") and **C** ("without shipment-level records or customer identifiers") answer the legal exception questions for you. Real clients rarely volunteer that. A messier version would leave it out and make the consultant ask.
- **Self-critique of my own briefs, fixed before sharing:** after seeing the partner's briefs, I applied the same test to mine. My first drafts had the same problems:
  - They were numbered in template order (1 = prohibited … 4 = minimal), so the tiers could be read off the numbers. I relabelled them W–Z and shuffled the order.
  - The fashion-chain case named "ethnic heritage" and "religiously observant" outright. It now says "cultural profile from facial features and clothing", so the reviewer has to work out that it is a sensitive-trait inference.
  - The photo-archive case said "never used to make decisions about individuals" and "not asked to recognise who they are", which answered the legal questions for the reader. I removed both lines.
  - Case Y's "sunnier weather and fewer people" stays, as a deliberate parallel-issue hook (misleading advertising), not a tier clue.

## 3. Simulated client discussion

| Case | Client response | Challenge raised | Consultant answer | Outcome |
|---|---|---|---|---|
| A | **Challenge** | "We just embed someone else's API. Isn't the vendor the provider?" | No. The vendor provides the *GPAI model*. The operator builds the *AI system* and puts it into service under its own brand, so the operator is the provider and owns the Art 50 duties. | Accepted. Added Art 50(2) output marking as a **firm** requirement, not just a "verify" item, in line with the partner's key. |
| B | **Challenge** | "Recruiters want a ranked list. Bands will slow them down." | Keep the ranking *inside* each band, but show the band break visually. Track whether recruiters approve the top 20 at a much higher rate than people further down. If they do, oversight isn't working, and that is the deployer's problem under Art 26. | Accepted with that compromise. |
| C | **Accept** | - | - | Approved as written. |
| D | **Asks for one redesign** | "Can we keep the acoustic analysis but only on the **customer's** voice?" | That avoids 5(1)(f), because customers aren't in a workplace relationship with the centre. But emotion recognition of customers is **high-risk** (Annex III §1(c)), needs an Art 50(3) notice to every caller, and voice data used this way raises GDPR special-category questions. It would cost more and coach less than the metadata redesign. | Client chooses the **metadata/transcript redesign**, limited to coaching (no ratings), so it avoids Annex III §4(b). |

## 4. What changed after the client discussion?

1. **Case A:** Art 50(2) machine-readable marking of generated answers changed from "verify with legal" to a firm launch requirement. I also cite Art 50(5) explicitly: disclosure at the first interaction, clear and accessible, which matters for passengers with disabilities.
2. **Case B:** The "bands instead of a ranked list" control is softened to ranking inside bands, plus a monitoring metric for anchoring on the top 20. The legal outcome doesn't change; the control is just easier to put into practice.
3. **Case D:** The customer-voice variant was evaluated and rejected as worse on both risk and value. The client signs off on the coaching-only metadata redesign, with a written commitment not to use it for performance ratings. Using it for ratings would push the system into high-risk.
4. **No category changed.** The tiers held, and the discussion only made the controls more specific. That's the main lesson: getting the classification right is the easy part, and most of the consulting value is in designing controls the client will actually use.
