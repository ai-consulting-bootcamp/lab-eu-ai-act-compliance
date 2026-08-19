# EU AI Act Approval Pack — Adam Valois

**Prepared as a consulting response to the client question: "Can we launch this?"**

Consultant: Adam Valois
Client cases reviewed: 4 (submitted by partner, Andrea)

---

## Executive Summary

This pack reviews four client use cases spanning the full range of EU AI Act risk tiers — from a **prohibited** biometric-surveillance concept through to a **minimal-risk** personal productivity tool. Two cases (Cases 2 and 3) can proceed to build with standard compliance controls. One case (Case 1) cannot be built as proposed and requires a redesign that strips out the biometric and predictive-profiling elements before any development work begins. One case (Case 4) carries effectively no AI Act obligations and can proceed immediately.

Across the four cases, the recurring compliance themes are: **human oversight** (maintained in every case where AI outputs affect people), **transparency to end users** (required wherever the system interacts directly with the public), and **data minimization** (particularly relevant to the biometric and passenger-data cases). No case in this batch can be approved without at least reviewing these three areas.

| Case | Category | Decision |
|---|---|---|
| 1 — Pub CCTV violence-risk system | Prohibited AI Practice | Do not build without redesign |
| 2 — Port authority traffic management | High-Risk | Approve with controls |
| 3 — Cruise ship excursion chatbot | Limited Risk (Transparency) | Approve with light controls |
| 4 — Travel content caption assistant | Minimal Risk | Approve — build |

---

## Case 1 — AI CCTV Camera System

### Client Problem
A pub chain wants an AI system for football match days that watches CCTV feeds and flags individual guests who are likely to become violent before any incident occurs. The system uses body language, facial expressions, movement patterns, clothing, and previous venue incident data to create a "violence risk" alert for security staff. Security guards receive the alert and may monitor, question, refuse service to, or remove the person. The people affected are ordinary customers and guests. A security guard can override the alert, but the AI warning strongly influences the decision.

### Inferred AI Act Category: **Prohibited AI Practice**

**Why this category applies:**
This proposal combines two prohibited AI use cases under the Act:
- Biometric categorization and behavior profiling
- Predictive policing and profiling of individuals

For these reasons, this cannot be built as proposed without adjustments.

### Adjustments Needed
- Remove all biometric and predictive elements from the system
- Use object detection for physical events only (e.g., a knocked-over table or broken glass)
- The system must not track faces, body language, or individual history data — it may only alert staff to a likely event at a specific location

### Proposed Architecture (post-redesign)
- Object-detection layer scanning for physical safety indicators (broken glass, overturned furniture)
- No biometric identification or facial analysis
- Alert routed to security staff by location, not by individual

### Role Map

| Role | Who | Why |
|---|---|---|
| Provider | Specialized object-detection software vendor | Provides AI that flags physical risk indicators (e.g., broken glass, upturned table) without biometric tracking |
| Deployer | AI Consulting Firm | Deploys and tests the software across pub locations, measuring safety improvement |

### Compliance Implications
- **FRIA**: Assess how cameras impact guest privacy
- **Article 52**: Deploy prominent signage at all pub entrances disclosing automated AI video analytics used for safety purposes
- **Data minimization**: Video feeds stored locally per pub; footage deleted every 24 hours unless an incident is flagged, in which case footage is retained only until the case is resolved

### Decision: **Do not build**
Unless the recommended architectural changes above are fully adopted.

---

## Case 2 — AI Traffic Management

### Client Problem
A port authority wants an AI traffic management system for a major passenger and cargo harbour. The system analyzes live vessel locations, weather, tide conditions, cargo type, passenger volume, fuel status, and berth availability to recommend which ships may enter, dock, wait, or reroute. The output is used by harbour control officers to manage vessel movements, including passenger ferries and vessels carrying hazardous materials. The AI ranking is the main basis for operational decisions during busy periods.

### Inferred AI Act Category: **High-Risk**

**Why this category applies:**
- Safety component of critical infrastructure (maritime)
- Potential for severe harm — vessels may carry hazardous materials, and a collision or accident could cause environmental disaster or loss of life

### Proposed Architecture
- Live data layer: vessel tracking, weather/tidal conditions, fuel and cargo status
- Processing/validation layer to ensure quality and reliability of real-time data
- Hard-coded maritime laws, safety rules, and regulatory requirements
- Predictive scheduling via constrained machine-learning optimization
- AI generates a documented rationale for every decision and ranking
- Operator dashboard keeps a human in the loop for scheduling recommendations and real-time risk flags

### Role Map

| Role | Who | Why |
|---|---|---|
| Provider | AI Consultancy | Designs, codes, and delivers the proprietary scheduling/optimization system; trains users on the dashboard |
| Deployer | Port Authority | Deploys the software and ensures human oversight is correctly applied to critical decisions |

### Compliance Implications

**Provider obligations:**
- Risk management process to identify, estimate, and mitigate operational risks
- Data governance: training/testing data must represent weather and other major risk conditions
- Traceability: system must log events to allow tracking of algorithmic suggestions
- CE registration: conformity assessment and registration in the EU database

**Deployer obligations:**
- Human oversight: operators must be informed and retain the ability to override the system
- Monitoring: ongoing monitoring for unusual behavior or patterns, with reporting

### Decision: **Approve with controls**

---

## Case 3 — Cruise Ship Customer AI Chatbot

### Client Request Summary
A cruise company wants to launch an AI chatbot on its booking portal to help passengers choose shore excursions. Customers enter preferences, budget, mobility needs, travel style, and available time; the chatbot recommends excursions from the company's existing catalogue, or suggests a custom self-guided itinerary if no suitable option exists. The people affected are cruise passengers making travel choices. Users can opt into automatic booking. The experience is designed to feel seamless, as if chatting with a human travel advisor.

### Inferred AI Act Category: **Limited Risk (Transparency)**

**Why this category applies:**
- Article 52 transparency duty: the system interacts directly with natural persons, who have a right to know they're interacting with AI
- High-risk exclusion: leisure booking and itinerary planning do not fall under critical infrastructure

### Proposed Architecture
- User chat interface
- PII filter layer: strips and anonymizes user data related to disability or other personal identifiers
- RAG layer: LLM queries the cruise line's excursion database
- Deterministic engine: validates hard constraints (budget, time windows) without LLM involvement
- Output generation: displays only valid, constraint-checked options

### Role Map

| Role | Who | Why |
|---|---|---|
| Provider | AI Consultancy | Develops the RAG chatbot using third-party APIs (e.g., OpenAI) |
| Deployer | Cruise Company | Runs the chatbot for customers and provides staff training |

### Compliance Implications
- Explicit AI disclosure to users
- Special category data controls to protect passenger information such as mobility needs
- Financial guardrails: the AI must never automatically authorize a charge to a user's credit card — the user must give final confirmation

### Decision: **Approve with light operational controls**

---

## Case 4 — AI Travel Content Companion

### Client Request Summary
A travel content creator wants an AI assistant that reviews their own travel itinerary, notes, photos, and draft captions to suggest more engaging social media posts. The system proposes caption ideas, hashtags, posting times, and optional edits to the creator's own text. It does not automatically publish content — the creator reviews and edits every suggestion before posting. If other people appear in photos or interviews, the creator is responsible for consent and privacy checks.

### Inferred AI Act Category: **Minimal Risk**

**Why this category applies:**
- No deceptive interaction — the system engages purely with the backend user and does not generate public-facing content autonomously

### Proposed Architecture
- Text/media ingestion of travel notes
- Multimodal processing of input data
- Context engine to align content with itinerary/timeline
- LLM generates multiple text variants and suggestions
- Creator dashboard presents side-by-side edit comparisons for the user to choose from

### Role Map

| Role | Who | Why |
|---|---|---|
| Provider | AI Consultancy | Develops the solution and provides documentation |
| Deployer | End User / Creator | Uses the tool in a purely personal, non-professional capacity |

### Compliance Implications
- Human in the loop: final publishing decision belongs to the content creator, not the AI

### Decision: **Build**

---

## Summary of Decisions

| Case | Category | Decision |
|---|---|---|
| 1 — Pub CCTV violence-risk system | Prohibited AI Practice | Do not build without redesign |
| 2 — Port authority traffic management | High-Risk | Approve with controls |
| 3 — Cruise ship excursion chatbot | Limited Risk / Transparency | Approve with light operational controls |
| 4 — Travel content caption assistant | Minimal Risk | Build |
