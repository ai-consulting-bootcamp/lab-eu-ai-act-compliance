# EU AI Act Approval Pack - Barsha

---

## Part 1 - Private answer key

> Keep this part to yourself until the client discussion (Phase 4).

### Case 1 - Prohibited

BrightLine Telecom wants to score call centre agents' "wellbeing and engagement" from their voice on every call, and use the scores in performance reviews and bonus decisions. This is emotion recognition in the workplace, which Article 5 bans unless it is for medical or safety reasons.

### Case 2 - High-risk

NextStep Academy wants AI to score and filter 2,000 bootcamp applicants, and auto-reject everyone outside the top 300. This decides access to vocational training, which is an Annex III high-risk area.

### Case 3 - Limited risk / transparency

Holzhaus Möbel wants a human-like chat assistant ("Lena") to answer customer questions about delivery, returns and sizing. Under Article 50, customers must be told they are talking to an AI. The assistant makes no high-impact decisions about people.

### Case 4 - Minimal risk

Kornfeld Bäckerei wants AI to forecast tomorrow's bread sales per shop to reduce waste. It makes no decisions about people and a human approves the output, so there are no specific AI Act obligations. GDPR would need checking if loyalty app data is added later.

### Author template

| Case | Client brief for partner | Intended category | Why I chose it |
|---|---|---|---|
| 1 | BrightLine Telecom - call centre "agent wellbeing" dashboard | **Prohibited** | The system infers employees' emotions from their voice in the workplace and feeds performance reviews. Article 5 bans emotion recognition at work unless it is for medical or safety reasons. |
| 2 | NextStep Academy - bootcamp admissions scoring | **High-risk** | The AI scores and filters applicants, which decides access to vocational training. This is an Annex III education and vocational training use. |
| 3 | Holzhaus Möbel - website and WhatsApp assistant | **Limited risk / transparency** | Customers chat with an AI that feels human ("Lena"), so Article 50 requires telling them they are talking to an AI. It makes no high-impact decisions about people. |
| 4 | Kornfeld Bäckerei - bread demand forecasting | **Minimal risk** | It forecasts product sales from sales, weather and calendar data and makes no decisions about people. A human approves the output. There are no specific AI Act obligations, but adding loyalty app data would raise GDPR questions. |

---

## Part 2 - Consulting response (client briefs to share with partner)

### Case 1 - BrightLine Telecom

BrightLine Telecom runs a call centre with about 400 support agents in Leipzig and Porto. Staff turnover is high and customer satisfaction has dropped for three quarters in a row. Team leads can only listen to a tiny share of calls, so they "don't know how their people are really doing". The company wants a tool from a US startup, VoxPulse, that analyses the agent's voice on every call (tone, pitch, pace, pauses) and gives each agent a daily "wellbeing and engagement" score, such as calm, stressed, frustrated or disengaged. Team leads see a dashboard and plan to use the scores in monthly performance reviews and bonus decisions. Team leads can add comments, but the scores go into the HR file automatically. The CEO wants it live before the next bonus cycle in March.

### Case 2 - NextStep Academy

NextStep Academy is a Berlin coding bootcamp. Many of its students are career changers whose course fees are paid with job centre education vouchers. Each intake gets about 2,000 applications for 120 places, and the admissions team has only three people. The academy wants to use AdmitIQ, an off-the-shelf tool built on a large language model that the IT team would configure. It would read the application form, the motivation essay and the result of a short online logic test, then give every applicant a score from 0 to 100. The top 300 would be invited to an interview, and everyone else would get an automatic "not this time" email. Data used includes personal details, education history, employment status, the essay and the test score. The admissions team would only see the top 300, and the final decision would be made after the interviews.

### Case 3 - Holzhaus Möbel

Holzhaus Möbel is an online furniture shop selling in Germany and Austria. Customer service receives about 3,000 emails a week, mostly about delivery dates, returns and whether a sofa will fit through a door. The shop wants a chat assistant on its website and on WhatsApp, called "Lena", with a friendly photo, that answers in a warm, natural tone. It would use the FAQ pages, the product catalogue (sizes, materials) and order tracking when the customer gives an order number. It is built on a third-party language model API. Lena cannot change orders or issue refunds. Complaints and refunds over €200 are handed to a human colleague. Marketing hopes "customers won't even notice the difference".

### Case 4 - Kornfeld Bäckerei

Kornfeld Bäckerei is a family-owned bakery chain with 45 shops in Bavaria. It throws away about 18% of its bread every day, and the CEO calls cutting this waste in half "our most important AI project this year". The company wants an AI model that predicts tomorrow's sales per product per shop. The model would use past sales, weather forecasts, school holidays, public holidays and local events such as markets and football matches. Every evening at 6 pm it would send suggested baking quantities to the central bakery. The production manager would review and adjust the numbers before baking starts at 2 am. Later, the company might add purchase data from its customer loyalty app to improve accuracy.

---

## Part 3 - Approval pack: consulting review of my partner's cases

> Client question: *"Can we launch this?"* I reviewed my partner's four briefs without seeing their answer key.

### Executive summary

Of the four proposals, one cannot launch as designed, two can launch with controls, and one can launch with only light checks.

- **Case 1 (Employee Performance Insights)** infers employees' emotions from their faces and voices at work. This is a **prohibited** practice, so it is **denied**. I offer a lawful redesign below.
- **Case 2 (Recruitment Shortlisting Assistant)** ranks job applicants. This is **high-risk**, so it can launch only with human oversight, logging, documentation and candidate information in place.
- **Case 3 (Website Customer Support Assistant)** is a customer chatbot. It is **limited risk**, so it can launch if customers are clearly told they are talking to an AI.
- **Case 4 (Internal Meeting Notes Organiser)** is **minimal risk** and can launch now. GDPR and confidentiality should still be checked.

For all four cases, staff who use or oversee the AI need basic AI literacy training (Article 4), which applies to all providers and deployers.

### Consulting review table (Apply · Integrate · Verify)

| Case | Likely category | Why this is my first-pass call | Proposed AI architecture | Provider / deployer / vendor | Required obligations or controls | Decision |
|---|---|---|---|---|---|---|
| 1 | **Prohibited** | It infers employees' emotions (frustration, anxiety) from face and voice in the workplace. Article 5 bans this unless it is for medical or safety reasons. Informing staff or having a human make the final decision does not change this. | As proposed: video and call recordings → biometric emotion model → individual manager dashboard → performance reviews. Not allowed. | **Provider:** the tool's developer (vendor, or the company if built in-house). **Deployer:** the customer-service company. | Cannot be made compliant with controls. Stop the project and use the redesign below. | **Deny and redesign** |
| 2 | **High-risk** | It ranks job applicants and decides who gets an interview. Recruitment is an employment use listed in Annex III. | **Trigger:** a new vacancy closes. **System:** parses CVs and matches them to job criteria, then produces a ranked list with reasons for each score. **Human review:** a recruiter reviews the full list, including a sample below the cut-off, before invitations go out. There is no automatic rejection. **Output:** the HR manager approves the shortlist. **Logging:** scores, reasons and recruiter overrides are logged. | **Provider:** the vendor of the recruitment tool, or the healthcare provider if it builds the tool itself. **Deployer:** the healthcare provider (HR team). **Vendor:** yes, if the tool is bought. | **Provider:** risk management, data governance and bias testing, technical documentation, conformity assessment, CE marking, EU database registration. **Deployer:** use the tool as the provider's instructions say; assign trained human oversight; keep logs for at least 6 months; monitor results; inform candidates and workers' representatives; GDPR DPIA and Art. 22 safeguards. **FRIA:** needed if the provider is a public body or provides a public service. | **Approve with controls** |
| 3 | **Limited risk / transparency** | Customers chat directly with an AI that is designed to feel like a normal customer-service conversation. Under Article 50 they must be told it is an AI. It makes no high-impact decisions about people. | **Trigger:** a customer opens the chat outside business hours. **System:** an LLM answers using the product catalogue and help-centre articles only (RAG). **Disclosure:** a message at the start says "You're chatting with an AI assistant". **Human review:** a human agent is available on request, and escalated complaints are reviewed by staff. **Logging:** chat logs are kept with a defined retention period. | **Provider:** the retailer, if it builds the chatbot on an LLM API; otherwise the chatbot vendor. **Deployer:** the retailer. **Vendor:** the LLM/API provider (GPAI model provider). | Clear AI disclosure at the first interaction. An easy route to a human. Answers limited to approved sources. The bot must not make promises that go against return or warranty law (consumer protection). GDPR notice for chat data. | **Approve with controls** |
| 4 | **Minimal risk** | It is an internal productivity tool. It does not evaluate staff, make decisions about people or talk to customers, and staff check every output. | **Trigger:** an employee pastes notes. **System:** produces headings, action items and a draft summary. **Human review:** the employee edits and approves the output before saving or sharing it. **Output:** organised notes. | **Provider:** the vendor of the AI tool. **Deployer:** the consultancy. **Vendor:** yes. | No specific AI Act obligations apart from AI literacy. Flag GDPR, because notes may still name people. Check the vendor contract: data location, and no training on the consultancy's data. | **Approve** |

### Case notes and compliance implications

**Case 1 - Deny and redesign.** The ban applies however the results are used and even if staff are informed, because consent is hard to give freely at work. **Lawful alternative:** drop face and voice emotion analysis. Instead, (a) run voluntary, anonymous wellbeing pulse surveys reported only at team level; (b) use workload metrics such as call volume, handle time and overtime to spot overloaded teams; (c) if call analytics are wanted, analyse transcripts for coaching topics (for example "customer asked about refunds") without inferring anyone's emotions. Option (b) is employee monitoring, so it still needs GDPR and works council review.

**Case 2 - Approve with controls.** The main risk is automation bias. If recruiters "normally only consider the top scores", the human review is just a formality. Controls: no automatic rejection, recruiters review a sample below the cut-off, applicants can ask for a human review, and the vendor shows bias testing for age, gender and nationality. The healthcare context makes a FRIA likely.

**Case 3 - Approve with controls.** Making the chat "resemble a normal conversation" is acceptable, but hiding the fact that it is an AI is not. The disclosure must be clear from the first message. Keep the bot to approved sources so it does not invent delivery or return terms.

**Case 4 - Approve.** AI is used, but nothing significant is decided about people. The parallel issues are GDPR and confidentiality, not the AI Act.

### Where a legal team should verify

- Whether the healthcare provider in Case 2 counts as a public body or a provider of public services (this decides whether a FRIA is needed).
- The current application dates for high-risk obligations, because the EU has proposed postponing some Annex III deadlines.
- In Case 1, whether any part of the system could fall under the medical or safety exception (unlikely as described).

---

## Part 4 - Debrief

### Round 1 - My review of Martha's cases vs Martha's answer key

| Case | Martha's intended category | My category | Match? | What worked / what was vague |
|---|---|---|---|---|
| 1 - Employee Performance Insights | Prohibited | Prohibited | ✅ | Clear and realistic. The brief says the system "estimates emotional states", which made the category easy to spot. A real client would more likely describe it as "engagement insights", so the brief was slightly too obvious. The detail "employees are informed but participation is mandatory" was a good trap, because informing staff does not lift the ban. |
| 2 - Recruitment Shortlisting Assistant | High-risk | High-risk | ✅ | Worked well. "Only the highest-scoring applicants would normally be considered" was a realistic, slightly messy detail that pointed to automation bias. It is vague whether the tool is bought from a vendor or built in-house, and whether the provider counts as a public body (FRIA question). |
| 3 - Website Customer Support Assistant | Limited risk / transparency | Limited risk / transparency | ✅ | Worked well. "Resemble a normal customer-service conversation" was the key hint for the AI disclosure duty. It is vague which LLM or vendor powers the bot, which affects who the provider is. |
| 4 - Internal Meeting Notes Organiser | Minimal risk | Minimal risk | ✅ | Too obvious. The brief says the tool "would not evaluate staff performance, make decisions about people or interact directly with customers", which almost states the category. It could have been messier, for example by saying notes sometimes mention clients. |

**Result:** 4 out of 4 matched. Martha's answer key and my review used the same AI Act logic: Article 5 for Case 1, Annex III employment for Case 2, Article 50 for Case 3, and no specific obligations for Case 4, with data protection flagged.

**Client response (Martha):** Martha accepted all four recommendations.

### Round 2 - Martha's review of my cases vs my answer key

| Case | My intended category | Martha's category | Match? | What worked / what was vague in my brief |
|---|---|---|---|---|
| 1 - BrightLine Telecom | Prohibited | Prohibited (Deny and redesign) | ✅ | Calling it "wellbeing and engagement" did not hide the emotion inference, which is realistic, because a consultant should see through the label. Martha's redesign (objective call-quality checks, no emotion inference) is close to mine. |
| 2 - NextStep Academy | High-risk | High-risk (Approve with controls, not as designed) | ✅ | The automatic "not this time" email for 1,700 applicants was the key detail. Martha made approval conditional on removing automatic rejection. That is stricter than "approve with controls" and fits the case well. |
| 3 - Holzhaus Möbel | Limited risk / transparency | Transparency obligations (Approve with controls) | ✅ | "Customers won't even notice the difference" worked as a trap. My brief did not say how customers prove their identity before order tracking. Martha flagged authentication, which I had not thought about. |
| 4 - Kornfeld Bäckerei | Minimal risk | Minimal risk (Approve) | ✅ | Calling it the CEO's "most important AI project" made it sound high-stakes without being high-risk, which worked well. Martha also spotted the later loyalty app data as a GDPR issue, as I intended. |

**Result:** 4 out of 4 matched.

**My response as the client:** I accept Martha's recommendations for all four cases, including the stricter condition for NextStep (no automatic rejections before launch).

### What changed after the client discussion?

Both answer keys matched 4 out of 4, so my categories and decisions stay the same. The discussion made my recommendations sharper in three places:
- For Case 2 (recruitment), Martha's review of my NextStep case showed that when an AI rejects people automatically, "approve with controls" should mean "do not launch until a human reviews rejections". I would apply the same firm condition to the healthcare recruitment tool.
- For Case 4, a "minimal risk" call still needs a data protection check, and Martha flagged the same thing.
- For Case 3, the disclosure duty applies "unless it is obvious" the user is talking to an AI. Because the client wants the chat to feel like a normal conversation, it is not obvious, so disclosure stays a firm condition.

The open points to confirm with the client are whether the Case 2 recruitment tool is bought from a vendor (provider role) and whether the healthcare provider counts as a public body (FRIA).
