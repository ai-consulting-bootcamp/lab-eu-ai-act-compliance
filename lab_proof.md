# Lab Proof — Classify Your Product

**Module:** 7 — EU AI Act  
**Lab:** Classify Your Product (Week 7, Day 1)  
**Consultant:** Martha  
**Partner:** Barsha Mishra  
**Discussion date:** 16 November 2026  
**Status:** Four phases completed; partner acceptance and sign-off reported

## 1. What I completed

I authored four client AI use cases and exchanged scenario briefs with Barsha. Without relying on her hidden answer key, I reviewed her four proposed systems against the EU AI Act's prohibited practices, Annex III high-risk uses, Article 50 transparency requirements and minimal-risk category. For each case, I proposed an AI architecture, identified likely provider/deployer/vendor roles, recommended controls and issued a consulting decision. I then presented the recommendations and compared classifications with Barsha.

## 2. Evidence map

| Lab phase | Evidence | What the reviewer should check |
| --- | --- | --- |
| Phase 1 — Hidden client briefs | [phase1_client_scenarios.md](./phase1_client_scenarios.md) | Four client briefs and my intended category for each |
| Phase 2 — Partner review | [phase2_consulting_review.md](./phase2_consulting_review.md) | Independent risk calls, reasoning, architecture, roles, controls and decisions for Barsha's scenarios |
| Phase 3 — Approval pack | [phase3_approval_pack.md](./phase3_approval_pack.md) | Executive summary, four case assessments, launch recommendations and prohibited-case redesign |
| Phase 4 — Discussion and sign-off | [phase4_client_discussion_signoff.md](./phase4_client_discussion_signoff.md) | Comparison with Barsha's answer key, acceptance and closing reflection |
| Optional reciprocal review | [barsha_peer_review.md](./barsha_peer_review.md) | Barsha's assessment of the four scenarios I authored, if included |

## 3. Key output — consulting decisions

| Case | My inferred risk category | Recommendation | Main rationale or safeguard |
| --- | --- | --- | --- |
| **BrightLine Telecom** | **Prohibited** | **Deny and redesign** | Workplace emotion inference from employee voices for performance/bonus decisions is generally prohibited; replace it with objective call-quality analysis and reassess the redesigned tool. |
| **NextStep Academy** | **High-risk** | **Approve with controls, after redesign** | AI scoring that determines access to vocational education falls under Annex III; remove unreviewed automatic rejections, ensure meaningful human oversight and verify high-risk compliance. |
| **Holzhaus Möbel** | **Limited risk / transparency** | **Approve with controls** | Disclose clearly that customers are interacting with an AI chatbot; protect order data and provide human escalation. |
| **Kornfeld Bäckerei** | **Minimal risk** | **Approve** | Operational bakery-demand forecasting is not, on the stated facts, a prohibited or Annex III use; retain manager approval and review privacy before using identifiable loyalty data. |

**Example input:** Barsha's BrightLine Telecom client brief proposed analysing call-centre employees' voices to infer emotions and influence performance reviews and bonuses.

**Example output:** I classified this as a prohibited workplace emotion-inference use and recommended **deny and redesign**, with objective call-quality checks and trained human review instead of emotion scoring. The full reasoning and design appear in [Phase 3](./phase3_approval_pack.md).

## 4. Partner discussion and final outcome

Barsha revealed that her intended categories for BrightLine Telecom, NextStep Academy, Holzhaus Möbel and Kornfeld Bäckerei matched my independent classifications: **four out of four matched**. She accepted the recommendations and signed off. The completed discussion record is in [Phase 4](./phase4_client_discussion_signoff.md).

The acceptance is **peer-review sign-off for the lab**, not legal approval or certification of any real-world AI system. The prohibited design remains a **deny and redesign** recommendation; the high-risk and transparency cases remain conditional on implementing the stated controls.

## 5. Limitations / failure considerations

- **Brief-based assessment:** The scenarios are descriptions, not working systems. There was no production test, conformity assessment or technical audit of vendor implementations.
- **Role uncertainty:** Final provider, deployer and third-party responsibilities depend on actual contracts, branding and modifications.
- **Legal timing:** AI Act obligations and transition dates must be checked against the rules in force at any real deployment date.
- **Potential failure mode:** In the NextStep Academy scenario, a nominal human review that considers only top-ranked candidates could reproduce automated rejection and automation bias. A meaningful review process, testing, appeals and documentation are necessary before launch.

## 6. Submission notes

This lab is a **consulting classification exercise**, not a coding or model-execution lab; therefore the principal evidence is the scenario briefs, review table, approval pack and partner discussion rather than a workflow export or runtime screenshot.

**Repository check before PR:** Ensure the linked supporting files exist under these exact names. If the optional reciprocal-review file is not included, remove its row from this document and from `README.md`. Do not commit credentials or unrelated project files.
