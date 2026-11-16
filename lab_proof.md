# Lab proof

## Status and method

The local submission contains an AI-assisted synthetic replacement for the unavailable partner exercise. The student reports having informed the instructor. Instructor acceptance of this substitution is not evidenced here. The same assistant generated the fictional briefs, answer key, analysis, and scripted client discussion. No independent blind assessment, live discussion, real deployment, or client sign-off is claimed.

## Reviewer map

| File | Content |
|---|---|
| [client-briefs.md](client-briefs.md) | Student's four original fictional cases |
| [author-answer-key.md](author-answer-key.md) | Original case categories and rationales, now included for final review |
| [synthetic-partner-briefs.md](synthetic-partner-briefs.md) | Four replacement partner cases |
| [synthetic-partner-answer-key.md](synthetic-partner-answer-key.md) | Intended synthetic categories and rationale |
| [consulting-review.md](consulting-review.md) | Classification, architecture, roles, controls, and decision table |
| [approval-pack.pdf](approval-pack.pdf) | Final client-facing approval pack, three pages |
| [approval-pack.md](approval-pack.md) | Editable text source of the approval pack |
| [simulated-client-discussion.md](simulated-client-discussion.md) | Scripted challenges, category comparison, and closing reflection |
| [check_blind_briefs.py](check_blind_briefs.py) | Reproducible structure check |

## Workflow, input, and result

The workflow was brief creation, legal classification, architecture and role mapping, conditional launch recommendations, and a scripted debrief. The input was the four synthetic partner briefs. The output is the approval pack and review table. Legal references are listed in the pack.

Both commands were executed successfully from the repository root.

```text
python check_blind_briefs.py client-briefs.md
python check_blind_briefs.py synthetic-partner-briefs.md

Each run reported
Case A: 6 brief lines
Case B: 6 brief lines
Case C: 6 brief lines
Case D: 6 brief lines
PASS: Four neutrally titled briefs meet the line-count requirement.
```

The final PDF contains three pages. All pages were rendered and visually inspected for readable text and clipping. The classification results are A transparency, B high-risk, C prohibited, and D minimal risk. The respective decisions are Approve with controls, Approve with controls, Deny and redesign, and Approve.

## Rubric evidence

- Recognize. Each original and synthetic set contains exactly one example of each requested outcome, with answer keys.
- Apply. The review table explains the simulated consulting classifications. Independent blind inference remains untested.
- Integrate. The pack covers triggers, inputs, AI behaviour, human review, outputs, records, and provider/deployer/vendor roles.
- Verify. Decisions follow the risk logic, with a replacement for the prohibited proposal.
- Debrief. The scripted discussion compares intended and inferred categories and records changes to recommendations.

## Failure or limitation

The real partner exchange could not take place. Synthetic data allowed the analytical workflow to continue, but matching the generated key cannot validate independent classification skill. The structure-check script verifies headings and brief lengths only. No vendor evidence, implementation testing, or regulatory approval was obtained.

## Submission stage

The local analytical package is complete as a disclosed simulation. GitHub publication, pull-request submission, and course feedback are separate steps requiring the student's confirmation and the course review process.

