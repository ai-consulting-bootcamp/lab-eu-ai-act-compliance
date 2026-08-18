# Approval Pack – AI Recruitment Screening

**Client:** Confidential – Logistics Company  
**Project:** AI-Assisted Candidate Screening and Ranking System  
**Document Version:** 1.0  
**Prepared by:** AI Consulting Team  
**Assessment Scope:** EU AI Act Compliance and Deployment Readiness Review

---

# Executive Summary

## Recommendation

**Approve with Controls.**

The proposed AI recruitment solution may be deployed, provided the organization implements the governance, documentation, and oversight measures required for **High-Risk AI systems** under the EU AI Act.

The solution supports one of the most sensitive business processes within an organization—employment decisions. Because the AI influences which candidates progress through the recruitment process, the system has the potential to significantly affect individuals' access to employment and future career opportunities.

The current proposal contains one significant weakness: although recruiters can technically review AI recommendations, they rarely challenge them in practice. This does not constitute meaningful human oversight. Before deployment, the recruitment workflow should be redesigned to ensure that AI remains a decision-support tool rather than the de facto decision-maker.

---

# 1. Business Context

The client is a mid-sized logistics company experiencing a growing volume of applications for warehouse and commercial driver positions. The current recruitment process is resource-intensive and delays hiring during periods of increased operational demand.

To improve efficiency, the company proposes implementing an AI system that evaluates resumes and short recorded video interviews before candidates reach the interview stage. The AI produces a numerical score and ranking based on work history, job-related keywords, and speech characteristics extracted from the interview recording.

Candidates scoring above a predefined threshold are invited to interview, while unsuccessful applicants receive an automated rejection email.

Recruiters have access to the AI scores but indicated that they generally accept the recommendations without modification because the system is expected to outperform manual screening.

---

# 2. AI Act Assessment

## Classification

**High-Risk AI System**

## Assessment Rationale

The proposed system is intended to support recruitment decisions by evaluating and ranking job applicants.

Employment is explicitly identified as a high-risk domain because AI outputs directly influence access to employment opportunities and may significantly affect individuals' livelihoods.

The current design also raises concerns regarding meaningful human oversight. While recruiters formally remain involved in the process, the proposed operating model suggests that AI recommendations are routinely accepted without independent assessment.

The system is therefore suitable for deployment only if appropriate governance and operational controls are implemented.

---

# 3. Proposed Operating Model

## Business Trigger

Submission of a job application.

↓

## AI Processing

The AI analyzes:

- employment history,
- qualifications,
- skills extracted from the resume,
- job-related keywords,
- structured information from the application,
- selected characteristics from recorded video interviews.

The model produces a candidate suitability score and ranked shortlist.

↓

## Human Review

Recruitment specialists review:

- AI scores,
- supporting application materials,
- interview recordings where appropriate,

before making any progression or rejection decision.

Human reviewers should have both the authority and the responsibility to override AI recommendations whenever appropriate.

↓

## Recruitment Decision

Candidates are either:

- invited to interview,
- placed on hold,
- rejected following documented recruiter review.

↓

## Monitoring and Logging

The recruitment platform should retain:

- AI recommendations,
- recruiter decisions,
- documented overrides,
- model performance metrics,
- audit logs,
- system version history.

These records support accountability, auditing, and continuous performance monitoring.

---

# 4. Roles and Responsibilities

| Function | Responsible Party |
|-----------|-------------------|
| **AI Provider** | Recruitment software vendor or internal AI development team |
| **AI Deployer** | Logistics company |
| **Technology Vendors** | Large Language Model provider, cloud infrastructure provider, recruitment platform provider |

The deployer remains responsible for ensuring that the AI system is used within its intended purpose and that human oversight remains meaningful throughout the recruitment process.

---

# 5. Compliance Considerations

Before deployment, the following measures should be implemented.

### Human Oversight

Recruiters should actively evaluate AI recommendations rather than routinely accepting system rankings.

The organization should establish documented review procedures demonstrating that hiring decisions remain under human control.

---

### Risk Management

The provider should implement a structured risk management process covering:

- model limitations,
- foreseeable misuse,
- operational risks,
- mitigation measures,
- ongoing monitoring.

---

### Data Governance

Training and operational datasets should be reviewed to reduce the risk of bias, incomplete information, or unintended discrimination.

The company should periodically evaluate recruitment outcomes for fairness and consistency across candidate groups.

---

### Technical Documentation

Documentation should include:

- intended purpose,
- model limitations,
- evaluation methodology,
- system architecture,
- performance metrics,
- update history.

---

### Logging and Monitoring

The deployment should maintain comprehensive audit trails documenting:

- AI recommendations,
- recruiter decisions,
- overrides,
- system performance,
- significant incidents.

---

### GDPR

The company should review:

- lawful basis for processing applicant data,
- retention periods,
- transparency notices,
- candidate rights,
- security of recruitment information.

---

# 6. Key Risks

| Risk | Potential Impact | Recommended Mitigation |
|------|------------------|------------------------|
| Recruiters rely exclusively on AI rankings | Reduced human oversight and regulatory non-compliance | Require documented independent review before every hiring decision |
| Bias in training or operational data | Discriminatory recruitment outcomes | Regular fairness testing and dataset review |
| Insufficient documentation | Regulatory and audit challenges | Maintain complete technical and governance documentation |
| Model performance deteriorates over time | Reduced recruitment quality | Continuous monitoring and scheduled model evaluation |
| Improper handling of applicant data | GDPR and reputational risk | Strong access controls, encryption, and data governance |

Overall implementation risk is assessed as **Moderate**, provided governance measures are fully implemented.

---

# 7. Final Recommendation

## Decision

# 🟡 APPROVE WITH CONTROLS

The proposed recruitment solution may proceed, but only after implementing the governance framework required for High-Risk AI systems.

The consulting team recommends redesigning the recruitment workflow so that recruiters actively assess each recommendation rather than routinely relying on AI rankings. Human judgement should remain the primary decision-making mechanism, with AI serving as a structured decision-support tool.

Provided these controls are implemented, the solution offers a balanced approach to improving recruitment efficiency while maintaining compliance with the EU AI Act and supporting fair hiring practices.

---

# Next Steps

1. Redesign the recruitment workflow to establish meaningful human oversight.
2. Define responsibilities for provider and deployer under the AI governance framework.
3. Prepare technical documentation and model documentation before deployment.
4. Establish procedures for bias testing, performance monitoring, and periodic model review.
5. Develop audit logging and incident management procedures.
6. Review GDPR compliance, applicant transparency notices, and data retention policies.
7. Conduct a readiness assessment before moving the system into production.