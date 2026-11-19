# EU AI Act Approval Pack – Murat Çömez
## Part 2 – Client briefs for partner (Consulting response input)

> Four client requests from discovery calls. Please review each one as the consultant: what is the likely AI Act treatment, how would you design it, who is who, and can the client launch?

---

### Client A – Loss event tagging at a mid-size mortgage bank
The second-line risk team collects about 1,500 internal loss and near-miss events a year. Business units submit them as free text in German or English, often messy.
Today three analysts read each event and map it to the Basel event type and the bank's own risk taxonomy; consistency between analysts is poor and the backlog is about six weeks.
The bank wants an LLM (Azure OpenAI, EU tenant) to read each submission and suggest the event type, a root-cause tag and a two-line summary.
The analyst sees the suggestion next to the original text and accepts or changes it before it is saved to the loss database.
Descriptions sometimes include employee names, customer numbers or amounts. The data ends up in quarterly reports to the management board and the supervisor.

### Client B – Instant spending limits for a buy-now-pay-later fintech
A fintech offers "pay in 4" instalments at online checkouts in Germany and Austria and wants to grow approval rates without increasing defaults.
It plans to replace its rule engine with a machine-learning model that, in under two seconds, approves or declines the purchase and sets the customer's spending limit (0–3,000 EUR).
Signals: basket and merchant data, device and session data, past repayment behaviour, open-banking transaction data (with the customer's consent) and the external credit bureau score.
The model is bought from a specialist ML vendor; the fintech hosts it, retrains it monthly on its own data and shows it to customers under its own brand.
Declines are shown instantly with a generic message; customer service can look at a case manually only if the customer complains.

### Client C – Call quality and agent engagement in a bank contact centre
A consumer bank runs a 220-agent contact centre in Berlin and Leipzig; attrition is high and quality scores vary a lot between teams.
A telephony vendor offers a plug-in that listens to live calls and uses the agent's webcam, analysing voice tone, pitch, speaking pace, pauses and facial expressions.
It produces a weekly "wellbeing & engagement" score per agent, flagging signs of stress, frustration or disengagement, shown on team-lead dashboards.
Team leads would use the score in quarterly performance reviews and when deciding who gets preferred shifts; they can add a comment but cannot change the score.
Operations wants to start a pilot next month with two teams; HR and the works council have not been involved yet.

### Client D – 24/7 customer assistant for a home and motor insurer
A regional home and motor insurer gets thousands of calls a week asking "where is my claim?" and "am I covered for this?".
It wants a 24/7 assistant on the website and on WhatsApp, built on a large language model via API, with retrieval over policy wordings and read-only access to claim status.
Marketing wants the assistant to have a friendly persona called "Lena", with a photo, chatting in a natural, informal tone.
It cannot approve, reject or value claims; anything about payout amounts, disputes or complaints is handed to a human claims handler.
The insurer also wants it to draft personalised follow-up emails to customers, sent from the claims handler's mailbox under their name.
