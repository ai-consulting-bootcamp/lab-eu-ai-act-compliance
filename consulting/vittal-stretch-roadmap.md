# Stretch — Mini Implementation Roadmap: Case 2 (CV Screening, High-Risk)

## What the provider needs before market placement

- Risk management system covering the full lifecycle of the scoring model.
- Data governance: audit the 5-year historical hiring/retention training
  data for discriminatory proxies (e.g., correlations with protected
  characteristics via zip code, school, career gaps).
- Technical documentation and instructions for use, including known
  limitations and intended scope (screening support, not final decision).
- Conformity assessment and CE marking / EU database registration as
  required for the high-risk category.
- Logging capability built in from day one (score, inputs, model version,
  timestamp) to support post-market monitoring.

## What the deployer (retailer) needs before first use

- Confirm human review is mandatory before any auto-generated rejection —
  currently the biggest gap in the proposal.
- Staff training for recruiters on how to interpret scores and when to
  override them.
- Candidate-facing notice that AI is used in the screening process.
- Internal policy for handling candidate appeals or correction requests.
- Fundamental Rights Impact Assessment (FRIA) if the retailer is a body
  governed by public law or otherwise falls under the FRIA trigger —
  confirm applicability with counsel; if not strictly required, complete
  one voluntarily given the sensitivity of employment access.

## Evidence to request from the vendor (if the model is purchased, not built in-house)

- Bias/fairness testing results and methodology used on the training data.
- Technical documentation package and instructions for use.
- Evidence of conformity assessment already completed.
- Change-management commitment: notice before any model retraining or
  material update that could shift scoring behavior.
