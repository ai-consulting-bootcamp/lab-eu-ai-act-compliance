# Phase 4/5 — Debrief with Ugo Ahukannah

**Consultant's pack reviewed:** `eu-ai-act-approval-pack-ugo-ahukannah.md`
**Client (answer-key holder):** Vittal, comparing against `private/answer-key.md`

## Intended vs. inferred classification

| Case | My intended category | Ugo's inferred category | Match? |
|---|---|---|---|
| 1 — logistics burnout / emotion monitoring | Prohibited (Art 5(1)(f)) | Prohibited (Art 5, emotion recognition in the workplace) | Yes |
| 2 — retail CV screening | High-risk (Annex III(4)) | High-risk (Annex III(4), recruitment and selection) | Yes |
| 3 — electronics chat widget | Limited risk / transparency (Art 50) | Limited risk / transparency (Art 50(1)) | Yes |
| 4 — grocery demand forecasting | Minimal risk | Minimal risk | Yes |

4/4 correct on the first pass, with no answer key seen — a clean read.

## Where the hidden scenario worked well

- **Case 1** — Ugo caught the exact mechanism I'd built into the brief: the
  "for safety monitoring" framing given to employees versus the actual use
  in coaching/performance/promotion. He named that gap explicitly as covert
  deployment, which was the intended tell, not just the emotion-recognition
  fact itself.
- **Case 2** — the "recruiters mostly only open strong-fit" plus the
  undecided human-review question was meant to surface the Article 14/GDPR
  Article 22 oversight gap, and it landed — he flagged the missing human
  review at the point of detriment as the compounding fault, not just the
  Annex III trigger.
- **Case 4** — the "AI makes decisions" framing was a deliberate bait toward
  a high-risk read; Ugo correctly separated "decisions about stock units"
  from "decisions about people" rather than pattern-matching on the word
  "decision."

## Where it was too vague, or could be tightened

- **Case 3** — Ugo's read was correct, but his own note is fair: the "beta
  support tool" label was meant to be an inadequate-but-present disclosure,
  not a total absence of one. A sharper brief would make it more obvious
  that the persona (first name, photo, warm tone) is actively working
  against the label rather than just being incomplete alongside it.
- **Case 2** — I left the "does a recruiter review 'not a fit' before
  rejection" question genuinely undecided in the brief, which is realistic
  for a discovery call but meant a rigorous reviewer had to flag it as an
  open risk rather than a confirmed gap. Ugo did that correctly; a version
  of this brief for a less careful reviewer might have let that ambiguity
  slide.

## Points from Ugo's pack I'm flagging for legal verification, not treating as settled

Ugo's pack cites specific enforcement dates and a named amending regulation
(prohibitions in force since 2 February 2025; Article 50 enforceable since
2 August 2026; Annex III high-risk obligations delayed to 2 December 2027
under a "Digital Omnibus extension"; Regulation (EU) 2026/1744). These are
more granular than anything in my own materials, and I did not independently
verify them while writing my hidden briefs. Per the lab's own guidance, I'm
flagging these dates and the amending-regulation citation for counsel to
confirm before they're used in a real client conversation — the underlying
category calls (prohibited / high-risk / transparency / minimal) don't
depend on getting the dates right, but a real approval pack shouldn't ship
with unverified statutory citations.

## Client response (Vittal, as the client)

- **Case 2, 3, 4 — Accept.** The classification, architecture, and controls
  match my own reasoning, and the added Article 22/GDPR cross-reference on
  Case 2's auto-rejection flow is a genuinely useful addition I hadn't
  included — I'd fold that into the real approval pack.
- **Case 1 — Accept the classification and the redesign.** Ugo's replace-
  biometric-inference-with-aggregate-operational-signals redesign
  (overtime concentration, absence clustering, pulse surveys, reported at
  team/site level) is essentially the same lawful alternative I'd drafted
  independently — self-reported opt-in signals plus objective operational
  data, never tied to an individual's record. Independent convergence on
  the same redesign from two reviewers who didn't see each other's answer
  key is a good sign the fix is the obvious one, not an idiosyncratic
  reading.

## Closing note — what changed after the client discussion

Nothing about the classifications changed — all four were correct blind.
What the exchange added was texture I hadn't written into my own materials:
a named GDPR cross-reference on Case 2, and a sharper articulation on Case 1
that the redesign's minimal-risk status depends on staying aggregate and
advisory — if the client later asks for per-employee attrition flags, the
redesign itself crosses back into Annex III(4) high-risk. That's a
conditional I'll carry into any real version of this pack: a lawful redesign
isn't a permanent exemption, it's an exemption for the design as specified.
