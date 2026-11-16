# EU AI Act Approval Pack - S. Rostovskyi

## Private answer key

This author key is included for final reviewer access. The partner stage was replaced by the disclosed synthetic exercise.

### Case 1 - Prohibited

**Blind-review brief:** Case D

- An Italian outsourced contact centre wants coaching staff to spend less time listening through long recordings of billing calls.
- It wants to license a vendor-branded tool that analyses the agent's voice using pitch variation, cadence, and other acoustic features.
- The tool estimates whether the employee felt irritated or anxious and flags those calls in a dashboard after each shift.
- The proposal covers individual employees on the billing desk, and supervisors would see the flags alongside each employee's name.
- A supervisor listens to flagged calls and chooses whether to schedule a coaching session. Supervisors can dismiss any flag.
- Management wants to use the results for routine coaching and service consistency. The tool has no medical or safety purpose.

**Rationale.** The system uses biometric voice features to infer employees' emotions in the workplace for routine coaching, which triggers the Article 5(1)(f) prohibition and falls outside its medical and safety exceptions.

### Case 2 - High-risk

**Blind-review brief:** Case B

- A German staffing agency struggles to review applications quickly enough before warehouse clients fill their seasonal shifts.
- It wants to license a vendor-branded tool that gives recruiters a ranked list of applicants for each vacancy.
- The tool reads CVs, availability forms, and job requirements, including shift availability and any required forklift certificate.
- Recruiters typically start with the first 20 names, so an applicant's position affects whether they get an interview before all slots are filled.
- Recruiters can open the full list, change the order, and decide whom to invite. The tool never sends rejections itself.
- The agency expects recruiters to see the job-related reasons behind each rank and record an override when they disagree.

**Rationale.** The system ranks applicants for recruitment and materially influences who receives an interview, bringing it within Article 6(2) and Annex III, point 4(a), despite the recruiter's override.

### Case 3 - Limited risk / transparency

**Blind-review brief:** Case A

- A regional rail operator in Belgium gets a surge of support requests when weekend engineering works change the timetable.
- It wants a website widget where visitors can type questions about replacement buses, station access, and where to get help.
- The widget retrieves approved timetable and accessibility pages, then generates a short answer and links to the relevant source.
- Visitors are passengers planning a trip, including travellers who rely on step-free routes or have limited time to change trains.
- Customer service staff maintain the source pages and take over when information is missing or conflicting. They do not review every answer before it appears.
- The operator wants to launch the widget under its own brand using an external language-model API. Ticket changes and compensation decisions stay with staff.

**Rationale.** Direct interaction with passengers and generated answers bring the branded assistant within Article 50(1), (2), and (5), subject to the relevant exceptions, and the described purpose has no high-risk trigger.

### Case 4 - Minimal risk

**Blind-review brief:** Case C

- A Dutch parcel depot sometimes runs out of standard cartons late in the week, even though it has storage space for more.
- Its operations team wants an internal tool that forecasts next week's demand for each carton size and proposes reorder quantities.
- The team would fit a forecasting model to weekly depot-level shipment totals by carton size, lead times, promotion dates, and holiday calendars.
- The output is a numeric purchase proposal for the inventory planner. Customers may see fewer packing delays if stock is available.
- The planner checks warehouse capacity, can change any quantity, and submits orders through the existing procurement system.
- The depot would build and use the tool internally. The input feed contains product and depot totals without shipment-level records or customer identifiers.

**Rationale.** Internal forecasting of carton demand produces numeric proposals from aggregate data and triggers no prohibited practice, high-risk category, or Article 50 duty, while Article 4 AI literacy still applies.

## Sources

- [EU AI Act, consolidated text of 27 July 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02024R1689-20260727)
- [Digital Omnibus on AI, Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026R1744)
- [European Commission guidelines on Article 50 transparency obligations](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems)

