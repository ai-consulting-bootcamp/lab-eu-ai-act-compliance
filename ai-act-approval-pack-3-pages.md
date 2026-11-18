# AI Act approval pack – four launch requests

17 November 2026 · Friedrich Tschoepke
Review of four client scenarios received from Nicolò Marseu.

**Three of the four systems can launch. One cannot be built as proposed.**

| Case | Category | Decision | What it costs you |
| --- | --- | --- | --- |
| 1 Callwerk | Prohibited | Deny and redesign | Concept rebuild, works council |
| 2 Paylo | High-risk | Approve with controls | Provider obligations, FRIA, human review |
| 3 Radhaus Brandt | Limited risk | Approve with controls | Disclosure design, consent for voice clone |
| 4 Nordholz | Minimal risk | Approve | Nothing under the AI Act |

Two points carry across the portfolio. What decides the tier is **who the system judges, not how advanced it is** — Nordholz runs the most sophisticated model of the four and carries the fewest obligations. And **a human in the loop does not lower the tier**: oversight is a control inside the high-risk regime, never a defence against a prohibition.

---

## Case 1 – Callwerk: deny and redesign

**Category: prohibited.** Inferring workers' emotions from voice and facial expressions is banned under Art. 5(1)(f), in force since February 2025. The exception for medical or safety reasons covers life and health, not wellbeing monitoring, and requires limits on scope and duration that this design lacks. The team-lead override does not help: oversight is a high-risk control, not a gateway through a prohibition. Both vendor and deployer are liable, at the Act's highest penalty ceiling.

**Architecture and roles.** As proposed: not deployable. Provider would be the analytics vendor, deployer Callwerk; the prohibition covers selling and using alike.

**Redesign toward a lawful alternative.** Score what was said, not how it sounded. Call ends → transcript checked against documented quality criteria (issue resolved, correct information given, script followed) → team lead reviews samples and coaches from concrete examples → results logged, agent can object. Wellbeing is handled separately through team-level workload indicators and voluntary anonymous surveys. This works because the prohibition requires inference from **biometric** data; transcribed text is not biometric, so the redesign leaves Art. 5 entirely.

**Conditions.** No voice-tone analysis and no webcam in any component. Keep the quality score decoupled from shift and premium-account allocation — coupled, it becomes high-risk under Annex III no. 4(b). Works council first, vendor second. DPIA before go-live.

**Expected objection:** that the tool is for employee wellbeing and therefore exempt. The Commission's guidelines name general wellbeing monitoring as the example that does *not* qualify.

---

## Case 2 – Paylo: approve with controls

**Category: high-risk**, Annex III no. 5(b) — evaluating the creditworthiness of natural persons and setting their limit. The Art. 6(3) filter is unavailable because the system profiles natural persons.

**Architecture.** Shopper selects pay later → model scores checkout data, repayment history and, where connected, bank transactions → approve with a limit, or decline → every decline states its reasons and offers one-click human review, answered within a committed time → inputs, scores, overrides and outcomes logged.

**Roles.** The vendor licenses the base model, but Paylo retrains it and runs it under its own name — under Art. 25 that very likely makes Paylo the **provider** as well as deployer, carrying both obligation sets. Merchants are a sales channel, not deployers. This is the single largest cost variable and must be settled contractually first.

**Compliance implications.** Provider: risk management, data governance and bias testing, technical documentation, logging, conformity assessment, EU database registration. Deployer: human oversight, log retention, information to shoppers (Art. 26), and a fundamental rights impact assessment under Art. 27, which names credit scoring. Outside the Act: Art. 22 GDPR gives a right to human intervention on request today, and the revised Consumer Credit Directive brings pay-later within its own creditworthiness rules.

**Conditions.** Human review reachable on every decline, not only after complaint. Reasons given with the decline. Documented bias testing before go-live, with device and location signals justified or dropped. Provider role fixed in the vendor contract. High-risk duties apply from 2 December 2027; the GDPR and credit-law points bind now.

**Expected objection:** that this is fraud prevention, which is carved out. The decision being automated is whether someone can afford to repay, not whether they are who they claim to be.

---

## Case 3 – Radhaus Brandt: approve with controls

**Category: limited risk.** Two transparency duties. The assistant speaks to customers, so Art. 50(1) requires them to be told it is an AI. The videos featuring a synthetic Jonas are deepfakes under Art. 50(4) and must be labelled. No Annex III area is touched — bookings, repair status and warranty questions are ordinary commercial tasks.

**Architecture and roles.** Customer calls or messages → assistant identifies itself as an AI → answers from manuals and price lists, books appointments → refunds, complaints and unclear warranty cases escalate to staff, handover available on request → conversation logged. Videos scripted in-house, presenter generated, labelled in video and caption. Platform vendors are providers and owe the machine-readable marking (Art. 50(2)); Radhaus is deployer and owes the visible disclosure.

**Conditions.** Disclosure at the start of every call and chat, not buried in a privacy notice. Label on every generated video. Written consent from Jonas covering voice and likeness, with withdrawal and a rule for if he leaves. Warranty answers confined to documented content — an incorrect warranty statement binds the retailer whoever said it. Art. 50 transparency applies now; machine-readable marking from 2 December 2026.

**Expected objection:** that customers should simply feel they are talking to Radhaus as always. Keep the warmth and the persona name — what Art. 50 forbids is implying a human, not sounding friendly.

---

## Case 4 – Nordholz: approve

**Category: minimal risk.** The system forecasts demand per product and depot. No natural person is assessed, ranked or profiled, so no Annex III area applies; it is not a safety component, there is no interaction with people and no synthetic content.

**Architecture and roles.** Weekly run → six-week demand forecast from five years of sales history, weather, regional building-permit statistics and supplier lead times → suggested reorder quantities → the depot buyer approves or edits every order → forecasts and edits logged so accuracy can be measured. Forecasting vendor as provider, Nordholz as deployer; the staffing agency has no role in the system.

**The one point worth examining.** The temp-worker plan sits next to Annex III no. 4. It stays outside the high-risk tier because the output is a headcount for the coming week, not an assessment of individuals — the system does not select, rank, monitor or evaluate anyone. Write that boundary down; it is the thing most likely to move without anyone noticing.

**Parallel issues.** Check the licence terms of commercial weather data. Track how often buyers edit suggestions — a buyer who approves everything unexamined is a commercial risk rather than a legal one.

---

## What happens next

| Point for counsel | Case | Why it matters |
| --- | --- | --- |
| Does retraining make you the provider under Art. 25? | Paylo | Decides who carries the provider obligations |
| Scope of the revised Consumer Credit Directive for pay-later | Paylo | Binds earlier than the AI Act timeline |
| Works council and Portuguese labour law on quality scoring | Callwerk | May be stricter than the AI Act |
| Liability for warranty statements made by the assistant | Radhaus | Falls outside the AI Act entirely |

**Sequence.** Callwerk first — the prohibition has been in force since February 2025 and is the only item with no runway. Then Paylo, where GDPR and credit law bind well before the 2027 deadline. Radhaus can be built correctly from the start at almost no extra cost. Nordholz needs a one-page use boundary and nothing else.

*This is a first-pass classification from the briefs as written, for legal review — not a legal opinion.*
