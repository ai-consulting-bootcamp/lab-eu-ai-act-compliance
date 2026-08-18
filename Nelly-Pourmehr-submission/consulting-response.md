Consulting Review

Reviewer: Nelly Pourmehr Cases reviewed: partner's four hidden client briefs 


Case 1

Likely category: Prohibited

Why this is your first-pass call: The trust index scores customers on behavior unrelated to the context where it gets used (returns, delivery priority). Customers get worse treatment based on the score. No customer is told the score exists. The score is shared with a third-party logistics company, which extends the harm outside the original context. This matches the Article 5 social scoring pattern.

Proposed AI architecture:

Trigger: app usage, purchase history, optional social login data
Model behavior: scores customer "trustworthiness"
Human review point: none
Output: internal flag to store staff, score shared with logistics partner
Disclosure layer: none

Provider / deployer / vendor: Retailer is provider and deployer. Logistics partner is a downstream recipient of the score.

Required obligations or controls: None apply. The practice as designed is banned.

Decision: Deny and redesign. Redesign option: drop the trust score. Use purchase history alone for a transparent loyalty tier customers can see, that only grants rewards, never penalties.

Case 2

Likely category: High-risk

Why this is your first-pass call: CV ranking that auto-rejects 70% of applicants is recruitment and selection of natural persons. This falls under Annex III even though a human makes the final hire decision, because the human never sees the rejected candidates.

Proposed AI architecture:

Trigger: incoming CV
Model behavior: extracts skills and experience, ranks candidates, auto-filters bottom 70%
Human review point: only on the surviving 30%
Output: shortlist sent to recruiter
Logging: needed for every auto-rejected candidate

Provider / deployer / vendor: Staffing agency is deployer. The AI vendor supplying the ranking tool is provider.

Required obligations or controls: Risk management system, data governance, logging of all auto-rejections, human oversight documentation, bias testing, conformity assessment before use.

Decision: Approve with controls. Controls: recruiter spot-checks a sample of auto-rejected CVs, log retention, bias audit before go-live.

Case 3

Likely category: Limited risk / transparency

Why this is your first-pass call: The chatbot only informs and routes. It makes no binding decisions, so it does not reach high-risk. But it is built to sound human and hide that it is AI, which triggers the Article 50 disclosure duty.

Proposed AI architecture:

Trigger: customer message
Model behavior: LLM answers questions, no claim or policy authority
Human review point: complex cases routed to a live agent
Output: chat reply
Disclosure layer: needed at the start of the chat

Provider / deployer / vendor: Insurance company is deployer. The LLM API provider is provider.

Required obligations or controls: Clear AI disclosure at or before the first interaction. Keep the name and persona, but state it is an AI assistant.

Decision: Approve with controls. Add disclosure text. Remove any wording that actively implies a human.

Case 4

Likely category: Minimal risk

Why this is your first-pass call: Reordering product display using aggregate and account-level history, same price for everyone, is not profiling that affects rights or opportunities. No Annex III trigger applies.

Proposed AI architecture:

Trigger: product page load
Model behavior: reorders suggested items
Human review point: not needed
Output: display order only
Disclosure layer: not required under the AI Act

Provider / deployer / vendor: Retailer is deployer, and likely provider if built in-house.

Required obligations or controls: No AI Act obligation. Flag for legal: confirm the privacy notice covers account-level history use, separate from the analytics cookie banner.

Decision: Approve. Note to legal: confirm privacy notice language covers this use of account data.