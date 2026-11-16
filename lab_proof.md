# Classify Your Product

## Submission guide

- **This file** contains my four client briefs, my review of my partner's cases, and the confirmed change after our discussion.
- [AI System Launch Approval Pack](./AI_System_Launch_Approval_Pack.docx) contains the executive summary, architecture, roles, launch recommendations, and discussion note.

## Phase 1 · Client briefs I shared

### 1. Warehouse recruitment

A logistics company receives more applications for warehouse jobs than its team can review before interviews. It wants AI to rank applications against the basic job requirements using CVs and application form answers about experience and availability for shifts. The recruiter can open any CV but quickly checks the top applications and follows the ranking when sending invitations. Once the interview slots are full, the recruiter stops reviewing, leaving some applications unread.

### 2. Customer service coaching

A logistics company gets many calls about delivery delays. Supervisors have time to listen to only a few recordings each month and want to decide which employees to offer coaching. The AI would use employees' tone and intonation to estimate frustration. When it flags several calls from the same employee, a supervisor listens to one recording and decides whether to offer coaching.

### 3. Website customer support

A logistics company often receives the same questions in its website chat. An AI assistant in the same chat window used by staff would use the company's FAQs to answer questions about hours, pickup points, and packaging. If the customer provides an order number and the system finds a shipment, it reports the last recorded status and location. Replies are automatic. If it cannot find the shipment or the customer wants to make a complaint, a staff member reviews the question and responds.

### 4. Packaging catalogue

Suppliers use different names for similar boxes. Warehouse staff sometimes open several catalogue pages to find suitable packaging. The AI would use photos of empty boxes to suggest labels for packaging type and approximate size. A staff member reviews and can correct the labels before saving the catalogue entry. Staff use the labels to find boxes and choose the packaging for each shipment.

## Phase 2 · Consulting review of my partner's cases

| Case | Likely category | Reason | Proposed AI architecture | Provider, deployer and vendor | Obligations or controls | Decision |
|---|---|---|---|---|---|---|
| 1. Independent bookshop | Minimal risk | The assistant supports an internal buying decision. | The bookseller requests a search. The assistant checks public catalogues and publisher sites and creates a report with edition details, suggestions, and source links. The bookseller checks the report and selects titles. | The company selling the tool directly is the provider and vendor. The bookshop is the deployer. | Check references and edition details. Check accuracy and permissions before reusing third-party text in public listings. | **Approve.** |
| 2. Toy factory staff promotions | High-risk | Individual performance scores influence who is considered for promotion. Article 6(2) and Annex III, point 4(b). | The supervisor starts a quarterly review. The system scores workers using production and quality records and suggests candidates. The supervisor checks the data and chooses who to put forward to HR. The original recommendation and the supervisor's reason are recorded. | The company selling the tool directly is the provider and vendor. The factory is the deployer. | Check provider documentation, conformity assessment, and instructions. Inform affected workers and their representatives. Assign trained human oversight, monitor the system, and keep automatic logs under the factory's control for at least six months unless applicable law sets a different rule. | **Approve with controls.** Launch after checking the documentation and putting the controls in place. |
| 3. Music production company | Prohibited as proposed | The system infers emotions from musicians' faces and voices during rehearsals to support hiring and renewals. Article 5(1)(f). | In the redesign, the director requests a blank form. The assistant uses the repertoire and role requirements to draft it. The director checks the form, assesses musicians using observable criteria, makes the decisions, and records the reasons. | In the redesign, the company selling the tool directly is the provider and vendor. The production company is the deployer. | Remove emotion inference. Limit the assistant's inputs to the repertoire and role requirements. The director completes the individual assessments. | **Deny and redesign.** Offer the blank-form assistant. |
| 4. Tea Guide chatbot | Transparency (limited risk) | The chatbot speaks directly to visitors, and its name alone does not make it clear that it is AI. Article 50(1) and (5). | The chat opens with an AI notice. It uses the catalogue and supplier information to answer. If the answer needs staff review, visitors can ask for help or leave a question outside opening hours. | The company selling the configurable chat directly is the provider and vendor. The tea shop is the deployer. | Test the clear notice at chat opening. Use approved sources and test the handoff to staff, including outside opening hours. | **Approve with controls.** Launch once the notice and handoff work. |

## Phases 3 and 4 · Approval pack and client discussion

See the [approval pack](./AI_System_Launch_Approval_Pack.docx) for the launch decisions and the closing note.

**Confirmed change.** My partner agreed to replace the toy braking scenario with a staff promotion scenario. Both were assessed as high-risk. The revised scenario fits the lab's Annex III requirement because the system evaluates workers and supports promotion decisions.

**Limitation.** The architectures and launch decisions are consulting proposals. This review did not implement or test the proposed systems.

[EU AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
