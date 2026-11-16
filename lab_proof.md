# Lab Proof – Classify Your Product (EU AI Act Approval Pack)

**Student:** Nicolò · **Partner:** Friedrich · **Module:** Week 7 – EU AI Act · **Date:** 16 Nov 2026

This file is the entry point for the reviewer. Every deliverable is linked below.

## File map

| File | What it contains | Lab phase |
|---|---|---|
| [client_briefs_for_partner.md](client_briefs_for_partner.md) | My four hidden client briefs, with no category labels (the "Consulting response" version shared with Friedrich) | Phase 1 |
| [private_answer_key_nicolo.md](private_answer_key_nicolo.md) | My private answer key: intended category and reasoning per case, plus what I expected the reviewer to catch | Phase 1 |
| [phase2_consulting_review.md](phase2_consulting_review.md) | My consulting review of Friedrich's four briefs: category, architecture, roles, obligations, decision | Phase 2 |
| [phase3_approval_pack.md](phase3_approval_pack.md) | Approval pack (≤ 3 pages) answering "Can we launch this?" for Friedrich's four cases | Phase 3 + Reinforce |
| [stretch_roadmap_case_d.md](stretch_roadmap_case_d.md) | Half-page implementation roadmap for the strongest high-risk case | Stretch |
| `lab_proof.md` (this file) | Workflow, one worked run, evidence, Phase 4 debrief, limitation | Submission |

## 1. Workflow

1. **Build:** wrote four hidden briefs (one per outcome: prohibited, high-risk, transparency, minimal) and a separate private answer key.
2. **Swap:** exchanged briefs with Friedrich. Answer keys stayed hidden.
3. **Review:** classified each of Friedrich's cases from the facts alone, then designed the architecture (trigger, system behaviour, human review point, output, records) and the role map (provider / deployer / vendor).
4. **Decide:** applied the lab's decision rules (prohibited means deny and redesign; high-risk means approve only with controls; transparency means approve with disclosures; minimal means approve and flag parallel law).
5. **Verify:** checked the two uncertain legal points against current sources before finalising (see Evidence).
6. **Sign-off:** presented the pack to Friedrich as client, compared it with his answer key, and recorded the outcome (Phase 4).

## 2. One run: input → output (Case D)

**Input (Friedrich's brief, summarised):** a private training provider runs publicly funded reskilling courses and has three times as many applicants as places. It wants a system that scores aptitude tests and motivation letters and outputs a ranked admission list. Staff "normally confirm the top 20" with about two minutes per applicant. The client calls it "just a pre-sorting aid". The tool comes from an EdTech vendor, and the client will retrain it on its own data and run it under its own brand.

**Reasoning steps:**
- **Area:** admission to vocational training, which falls under Annex III 3(a) (plus 3(b) for test evaluation).
- **Exemption test:** the Art. 6(3) "preparatory task" exemption fails. The ranking materially shapes the outcome, and the system profiles natural persons.
- **Oversight test:** two minutes per file with default confirmation is automation bias, not effective human oversight.
- **Role test:** retraining plus own branding makes the client a provider under Art. 25(1).

**Output:** **High-risk → Approve with controls.** Conditions: a redesigned human-review band, a bias audit of the historical admission data, applicant transparency and an appeal route, and full provider documentation. Full detail is in [phase3_approval_pack.md](phase3_approval_pack.md#case-d--vocational-training-provider-admission-ranking).

## 3. Evidence

I checked two points against current sources rather than relying on prior knowledge:

- **High-risk timeline:** the Digital Omnibus on AI, adopted June 2026, moved obligations for stand-alone Annex III systems to **2 Dec 2027**. The transparency obligations were not delayed. This changed the timing advice for Case D. Sources: [Lease Europe](https://www.leaseurope.org/new-application-dates-high-risk-ai-system-rules), [National Law Review](https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force).
- **The "medical reasons" exception (Case B):** the Commission's guidelines on prohibited practices treat workplace wellbeing and stress monitoring as outside the exception. This confirmed the prohibited call despite the client's "wellbeing" framing. Sources: [MobiHealthNews](https://www.mobihealthnews.com/news/eu-issues-guidelines-banned-ai-practices), [Lewis Silkin](https://www.lewissilkin.com/en/insights/2025/02/17/understanding-the-eu-ai-acts-prohibited-practices-key-workplace-and-advertising-102k011).

## 4. Final output

- **Approval pack:** [phase3_approval_pack.md](phase3_approval_pack.md)
- **Decisions:** A Approve · B Deny and redesign · C Approve with controls · D Approve with controls

## 5. Phase 4 – Client discussion and sign-off

| Case | Friedrich's intended category | My inferred category | Match |
|---|---|---|---|
| A – Funding consultancy | Minimal risk | Minimal risk | ✅ |
| B – Contact-centre outsourcer | Prohibited | Prohibited (plus a high-risk/transparency customer-mood module) | ✅ |
| C – Hotel group | Limited risk / transparency | Limited risk / transparency | ✅ |
| D – Vocational training provider | High-risk | High-risk | ✅ |

**Client response:** Friedrich, as client, accepted all four recommendations. He did not challenge any of them or ask for a redesign.

**Where the hidden scenarios worked:**
- **D was the best-hidden case.** "Just a pre-sorting aid" and the human confirmation step were credible reasons to argue it out of high-risk.
- **A's trap was well placed.** The real issue was the "AI-verified eligibility" marketing claim, not the AI Act.

**Where they were too easy:**
- **B gave its category away.** Webcam and voice-based stress detection on employees is close to a textbook prohibited example.
- **C signalled its category through marketing's wishes.** "Sound like a real receptionist" plus a synthetic employee pointed straight at Art. 50.

**Closing note – what changed after the client discussion?** Nothing. All four classifications matched the answer key and all four decisions were accepted, so the pack stands as submitted. The one point we agreed to keep flagged for legal review is the boundary of the Case B redesign (text-based analytics as an alternative to biometric emotion recognition).

## 6. Failure / limitation

- **One case doesn't fit one category.** Case B contains two AI uses with different treatment: the agent module is prohibited, while the customer-mood module is high-risk under Annex III 1(c) and also carries a transparency duty under Art. 50(3). The lab's "one category per case" structure couldn't capture that, so I classified the case by its most severe element and flagged the second module separately.
- **The redesign rests on non-binding guidance.** The redesign for Case B relies on the Commission's reading that inferring emotion from text (not biometric data) falls outside the Art. 3(39) definition. That guidance isn't binding, so a legal team would need to confirm it before build.
