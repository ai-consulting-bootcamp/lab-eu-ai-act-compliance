# EU AI Act Approval Pack

**Prepared for:** Client discovery portfolio (4 cases)
**Prepared by:** Vit Cipher, AI Act consulting review
**Question answered:** "Can we launch this?"

## Executive summary

Across the four proposals, the risk picture spans the full spectrum: one
system must be stopped and redesigned before launch (workplace emotion
scoring), one can proceed only with real controls (CV screening), one needs
a fix to its disclosure before it's launch-ready (support chatbot), and one
is clear to ship as-is (demand forecasting). The common thread in the two
riskier cases is that both quietly repurpose a system built for one stated
purpose ("safety," "efficiency") into decisions that materially affect
people — that gap between the stated purpose and the actual use is where
each of these needs the most scrutiny before go-live.

---

## Case 1 — Workplace engagement monitoring

**System:** Camera/mic capture during shifts and stand-ups, vendor model
infers emotion/tone, produces a weekly per-employee engagement score used
by supervisors in coaching, performance, and promotion decisions.

**Category:** Prohibited (Article 5(1)(f) — AI systems that infer emotions
in the workplace, outside narrow medical/safety exceptions).

**Architecture & roles:** Vendor = provider of the emotion-recognition
model; the logistics company = deployer. No qualifying safety/medical
exception applies to a performance-management use case.

**Compliance implications:** This cannot be launched with controls — it is
banned outright as designed, and the mismatch between the stated purpose
("safety monitoring") and actual use (performance/promotion input) is an
aggravating transparency problem on its own.

**Decision: Deny as proposed.**

**Lawful redesign option:** Drop emotion/tone inference entirely. If the
underlying goal is reducing burnout-driven turnover, replace it with
self-reported, opt-in pulse surveys and objective operational signals
(overtime hours, schedule volatility, absenteeism) reviewed in aggregate —
never inferred from a worker's face or voice, and never tied to an
individual's promotion or discipline record.

---

## Case 2 — CV screening and candidate ranking

**System:** Ingests CVs and assessment results, scores and tiers candidates
("strong fit / maybe / not a fit"), auto-sends rejections to the bottom
tier, trained on 5 years of historical hiring/retention outcomes.

**Category:** High-risk (Annex III(4) — recruitment, screening, and
evaluation of candidates for employment).

**Architecture & roles:** Retailer = deployer; the model's origin (in-house
vs. purchased) determines whether the retailer or a vendor is the provider
— this must be confirmed before launch, since it changes who owns the
technical documentation and conformity obligations.

**Compliance implications:** Requires a risk management system, bias and
data-quality testing (historical hiring data can encode past discriminatory
patterns), technical documentation, logging/audit trail of every score, and
mandatory human review before any rejection is sent — currently only
"strong fit" gets human eyes, which is the biggest gap. Candidates should
also be told AI is used in screening.

**Decision: Approve with controls** — contingent on (1) human review before
every auto-rejection, (2) bias testing against historical data completed
before the six-week launch date, (3) clarified provider/deployer split with
technical documentation in hand.

---

## Case 3 — Customer support chatbot

**System:** LLM + retrieval chat widget answering order/warranty questions
and recommending accessories, escalates to a human agent, doesn't issue
refunds itself.

**Category:** Limited risk / transparency (Article 50 — natural persons
must be informed they're interacting with an AI system).

**Architecture & roles:** Retailer = deployer; underlying model vendor =
provider of the general-purpose AI component used inside the widget.

**Compliance implications:** The current small "beta support tool" label is
not adequate disclosure — it must be clear and conspicuous at the start of
the interaction, not implied by a caveat in the corner. No decision-making
authority (refunds stay human), so it does not cross into high-risk.

**Decision: Approve with controls** — contingent on replacing the current
label with an unambiguous "You're chatting with an AI assistant" notice
before first message, and preserving the human escalation path as built.

---

## Case 4 — Demand forecasting for inventory

**System:** Forecasts per-store, per-SKU daily demand from sales history,
weather, and calendar effects; suggests reorder quantities that a store
manager can accept, adjust, or override.

**Category:** Minimal risk — no specific AI Act obligations.

**Architecture & roles:** Grocery chain = deployer/provider (in-house
build). No high-risk vendor exposure identified, no Annex III area
triggered, no profiling of natural persons.

**Compliance implications:** No AI Act-specific duties apply. Flag two
adjacent items for the client's legal team: (1) confirm no customer- or
employee-level personal data is ever folded into the forecasting inputs
later, which would raise GDPR questions; (2) keep marketing claims about
the tool's accuracy factual to avoid consumer-protection exposure.

**Decision: Approve.**

---

## Legal review note

This pack reflects a first-pass classification and is not a substitute for
formal legal sign-off. Case 2's provider/deployer split and Case 1's
redesign should both be confirmed with counsel before implementation.
