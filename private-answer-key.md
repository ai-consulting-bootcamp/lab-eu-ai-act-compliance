# EU AI Act Approval Pack - Ben Mayer

## Private answer key

Hidden from the partner until the client discussion. The partner gets only the unlabelled, shuffled briefs in [`client-briefs-for-partner.md`](./client-briefs-for-partner.md).

### Case 1 - Prohibited

**Blind-review brief:** Case X, fashion chain entrance cameras with a "cultural profile" segment.
**Why:** This is biometric categorisation: it uses facial features to infer race/ethnic origin or religious beliefs (head coverings used as a proxy for faith), and Art 5(1)(g) bans that outright. Age and gender alone wouldn't be banned, and that is the trap.

### Case 2 - High-risk

**Blind-review brief:** Case Z, business school auto-scores essays and interviews; the top and bottom bands get automatic offers or waitlisting.
**Why:** AI that determines admission to education is a listed high-risk use under Annex III §3(a)-(b). The automatically decided bands make human oversight the key weakness.

### Case 3 - Limited risk / transparency

**Blind-review brief:** Case Y, a tourism campaign with an AI-generated presenter and AI-altered footage of real places.
**Why:** Synthetic video of a realistic person and real places that could pass as authentic is a deepfake. The provider must mark it machine-readably (Art 50(2)) and the deployer must disclose it as AI-generated (Art 50(4)).

### Case 4 - Minimal risk

**Blind-review brief:** Case W, publisher auto-tags its internal photo archive and archivists approve the tags.
**Why:** It's internal content tagging with human acceptance, makes no decisions about people and isn't a listed use. Only the Art 4 AI-literacy duty applies, plus parallel GDPR and contract points.

## Author template

| Case | Client brief for partner | Intended category | Why I chose it |
|---|---|---|---|
| 1 | X - fashion chain "cultural profile" cameras | Prohibited | Art 5(1)(g): infers ethnicity or religion from biometrics |
| 2 | Z - business school admission scoring | High-risk | Annex III §3: decides access to education |
| 3 | Y - AI-generated tourism presenter | Limited / transparency | Art 50(2) and 50(4): deepfake marking and disclosure |
| 4 | W - photo-archive tagging | Minimal | No listed use, no decisions about people |

## Deliberate traps

- **X:** faces aren't stored or identified. This tempts a reviewer to say "anonymous, so fine", but Art 5(1)(g) bans *inferring* sensitive traits, not identifying people.
- **Z:** a human can override anything, but in practice only the middle band gets read. This tests whether the reviewer spots that the oversight is nominal.
- **Y:** the marketing team approves every clip, but human approval does **not** remove the deepfake disclosure duty. "Sunnier, emptier beaches" is a hook for a parallel consumer-protection issue (misleading advertising).
- **W:** the photos contain people. The reviewer should flag GDPR for identifiable people without moving the case up an AI Act tier.
