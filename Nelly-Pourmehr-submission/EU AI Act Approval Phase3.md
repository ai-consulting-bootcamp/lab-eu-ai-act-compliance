# EU AI Act Approval Pack

Prepared for: Client
Prepared by: Nelly Pourmehr
Scope: review of four proposed AI use cases

## Executive Summary

We reviewed four AI use cases across retail, staffing, insurance, and e-commerce. The risk picture is mixed.

One case cannot launch as designed. It scores customers on behavior unrelated to the context and uses the score to justify worse treatment, without informing the customer. This is a prohibited practice under the AI Act.

One case is high-risk. It screens job applicants and auto-rejects most of them before a human ever sees them. This can move forward, but only with logging, oversight, and bias testing in place first.

One case needs a disclosure fix. A chatbot is built to sound human and hides that it is AI. This can launch once it tells users it is an AI assistant.

One case is low risk and can move forward as planned. We flag one privacy notice item to close before launch.

## Case 1: Loyalty App Trust Index

**Category:** Prohibited

**What was proposed:** A retail chain wants a "trust index" built from purchase history, app engagement, and social media activity. High scorers get better offers. Low scorers get stricter return scrutiny and lower delivery priority, and their score is shared with a logistics partner. Customers are never told the score exists.

**Why this is prohibited:** The AI Act bans scoring people based on behavior or traits when the score is used for treatment unrelated to where the data came from, especially without the person's knowledge. Using a shopping and app behavior score to justify stricter return scrutiny and worse delivery is exactly this pattern. Sharing the score with an outside company makes it worse.

**Architecture and roles:** Retailer is both provider and deployer. Logistics partner receives the score as a third party.

**Compliance implication:** This practice cannot be fixed with controls. It has to be redesigned.

**Decision:** Deny as proposed.

**Redesign option:** Replace the trust index with a transparent loyalty tier based on purchase history alone. Customers can see their tier. The tier only unlocks rewards, it never triggers penalties, and it is never shared outside the company.

## Case 2: CV Screening Tool

**Category:** High-risk

**What was proposed:** A staffing agency wants an AI tool that reads CVs, ranks candidates, and auto-rejects the bottom 70%. A recruiter reviews and decides on the top 30%.

**Why this is high-risk:** This is AI used in recruitment and candidate selection, which the AI Act treats as high-risk. Having a human make the final hire decision does not remove the risk, because the human never sees the 70% the AI already rejected.

**Architecture and roles:** Staffing agency is deployer. The company supplying the ranking tool is provider.

**Compliance implication:** High-risk systems can launch, but they need a risk management process, data governance, logging of every auto-rejection, human oversight documentation, and bias testing before go-live.

**Decision:** Approve with controls.

**Controls required:** Recruiter reviews a random sample of auto-rejected CVs each month. Logs kept for all rejections. Bias audit completed before launch.

## Case 3: Insurance Chatbot

**Category:** Limited risk, transparency obligation

**What was proposed:** A chatbot answers policy, claims, and premium questions on an insurer's website. It is scripted to sound human, with a human name and warm tone. It makes no binding decisions and routes complex questions to a person.

**Why this needs a disclosure fix:** The bot doesn't make high-stakes decisions, so it stays out of high-risk. But it is built to seem human, and many customers don't realize they're talking to AI. The AI Act requires that people know when they're interacting with an AI system.

**Architecture and roles:** Insurance company is deployer. The LLM provider behind the chatbot is provider.

**Compliance implication:** The fix is simple. Add a clear disclosure at the start of the conversation.

**Decision:** Approve with controls.

**Controls required:** State clearly, at first contact, that this is an AI assistant. Keep the name and tone, remove any language that actively implies a person.

## Case 4: Product Recommendation Widget

**Category:** Minimal risk

**What was proposed:** A "customers who bought this also liked" widget reorders product listings using aggregate and account-level browsing history. Price stays the same for everyone.

**Why this is minimal risk:** No rights, safety, or high-stakes decisions are affected. Reordering a product list is not the kind of use the AI Act targets.

**Architecture and roles:** Retailer is deployer, and likely provider if built in-house.

**Compliance implication:** No AI Act obligation applies. One item needs a check outside the AI Act.

**Decision:** Approve.

**Flag for legal:** Confirm the privacy notice, not just the cookie banner, covers use of account-level history for these recommendations.

## Summary Table

| Case | Category | Decision |
|---|---|---|
| 1: Loyalty trust index | Prohibited | Deny, redesign as transparent loyalty tier |
| 2: CV screening | High-risk | Approve with controls |
| 3: Insurance chatbot | Limited risk / transparency | Approve with controls |
| 4: Recommendation widget | Minimal risk | Approve |