# EU AI Act Approval Pack — Review of Ugo Ahukannah's Client Cases

**Prepared for:** Ugo Ahukannah
**Prepared by:** Vittal, AI Act consulting review
**Question answered:** "Can we launch this?"

## Executive summary

Across your four cases, the risk picture runs the full range: one system
should be denied and redesigned before launch (MobiShare's reliability
score), one is high-risk with a real human-oversight gap to close
(Nordhaven's promotion shortlisting), one needs two separate disclosures
fixed before it's launch-ready (Brightseed's assistant and synthetic
video), and one is clear to ship as-is (Lindqvist's demand forecasting).
The common thread in the two riskier cases is data or a decision built for
one purpose quietly reused for a higher-stakes one — MobiShare's driving
behaviour score gating an unrelated insurance and housing product, and
Nordhaven's promotion panel never actually seeing the candidates the model
filtered out.

---

## Case 1 — MobiShare (urban mobility)

**System:** A "member reliability score" built from ride telemetry,
cancellations, app behaviour, payment disputes, support responsiveness, and
review sentiment. The score follows the member across products and
automatically gates two unrelated offers — an insurance partnership and an
apartment-block parking subscription.

**Category:** Prohibited (Article 5(1)(c), social scoring). The score is
built in one context and used to automatically deny outcomes in unrelated
contexts — the exact fact pattern the ban targets, regardless of whether
MobiShare is a public or private actor. Even without the ban, the
insurance-pricing angle alone would independently trigger Annex III(5)(c)
as high-risk, so this fails on two separate grounds.

**Architecture & roles:** MobiShare = deployer of its own ride/app/payment
data, and provider if the model is built in-house. The insurance partner
and the apartment-block operator become downstream deployers of a score
they didn't build and can't audit — an unmanaged third-party exposure.
Gating into insurance and parking is currently fully automatic, with no
human decision point before the detriment lands.

**Compliance implications:** No control closes this gap — the cross-context
reuse itself is the prohibited element, not a process failure that
documentation or oversight can fix.

**Decision: Deny as proposed.**

**Lawful redesign option:** Keep the score, but scope it strictly to
MobiShare's own mobility risk management (e.g., deposit terms or damage
liability within MobiShare's own products). Drop the automatic feed into
the insurance offer and the parking subscription entirely; if those
partners want a risk signal, they need their own independently justified,
consented assessment — not a repurposed mobility score.

---

## Case 2 — Nordhaven Group (facilities management)

**System:** Shortlists internal candidates for regional promotion by
learning from eight years of past promotion decisions and performance
reviews, using tenure, attendance, training, team complaint counts, and
free-text manager comments. HR "sanity checks" the top 10; the panel only
ever sees the ranked list.

**Category:** High-risk (Annex III(4) — employment, promotion decisions).

**Architecture & roles:** Nordhaven = deployer; provider is Nordhaven
itself if built in-house, or the vendor if purchased — confirm before
sign-off, since it changes who owns the technical documentation. The
current design gives no one with decision authority visibility into
candidates ranked outside the top 10.

**Compliance implications:** Requires a risk-management system, bias
testing on the eight-year training set (especially the free-text comment
feature, a likely vector for subjective or regional bias), a full audit log
of rankings (not just the top 10), and disclosure to candidates that AI is
used in shortlisting. The "sanity check" as designed is not meaningful
human oversight — the panel needs the full list and underlying evidence,
not a pre-filtered top 10.

**Decision: Approve with controls** — contingent on (1) the panel receiving
the full ranked list and underlying evidence rather than a pre-filtered
top 10, and (2) bias testing on the free-text feature completed before the
next promotion cycle.

---

## Case 3 — Brightseed Nutrition (D2C supplements)

**System:** Two components — a customer-facing chat assistant with a name
and photo, styled to feel human, answering product/order/returns questions
and escalating health topics to a person; and short marketing videos using
a synthetic presenter with a cloned voice, localized into nine languages.

**Category:** Limited risk / transparency — but with two distinct Article
50 obligations, not one. The assistant needs standard AI-disclosure; the
synthetic presenter and cloned voice separately trigger the deepfake
labelling duty under Article 50(4). Neither system makes a consequential
decision about a person, so neither rises to high-risk.

**Architecture & roles:** Brightseed = deployer for both. The underlying
LLM vendor = provider of the assistant's model; the synthetic-media/voice
vendor = provider of the video-generation component — two separate
third-party vendors to track.

**Compliance implications:** The assistant's current design (name, photo,
warm tone) does not clearly disclose it's AI — this must be fixed before
launch. Every synthetic-presenter video needs a visible/audible
AI-generated label, across all nine language versions, not just the
assistant's home language.

**Decision: Approve with controls** — contingent on adding a clear
AI-disclosure to the assistant's first message and a persistent
AI-generated label on every video across all nine languages. No redesign of
the underlying systems is needed.

---

## Case 4 — Lindqvist & Sons (regional grocery wholesaler)

**System:** Forecasts demand per SKU per depot from three years of order
history, seasonality, event calendars, and weather, generating suggested
replenishment quantities that the purchasing team reviews weekly and can
change before orders go out.

**Category:** Minimal risk — no specific AI Act obligations. No individual
is assessed by the output (affected parties are purchasing staff deciding
order volumes, not subjects of an automated decision), no Annex III area is
triggered, and no personal data is involved.

**Architecture & roles:** Lindqvist = deployer/provider if built in-house.
No high-risk vendor exposure identified; if the forecasting engine is
bought in, confirm data-handling terms only — a commercial question, not an
AI Act one.

**Compliance implications:** No AI Act-specific duties apply. Worth a
light-touch note to legal if any third-party weather/event data licensing
terms restrict downstream commercial use.

**Decision: Approve.**

---

## One open question before we finalize

If Case 1 was meant to land as "high-risk" rather than "prohibited," I'd
want to talk it through — it's the *unrelated-context reuse* (driving
behaviour gating insurance and a housing-adjacent product) that pushes my
read past a garden-variety insurance risk-scoring tool. If MobiShare only
used the score to manage its own fleet risk, I'd call that high-risk,
approvable with controls. Flagging this because it's the one case where my
decision (deny and redesign) differs materially from a high-risk read
(approve with controls), and I want to confirm the fact pattern was
intentional before we compare answer keys.
