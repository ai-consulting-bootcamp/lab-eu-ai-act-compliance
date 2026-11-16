# EU AI Act Approval Lab | Sean Langsdorf

**Reviewer entry point · 16 November 2026**

This lab turns four fictional client requests into four launch recommendations. The consultation uses a simulated set of incoming briefs because no real partner briefs were supplied. The live swap, reveal and sign-off are still open.

## File map

| File | What it contains |
| --- | --- |
| [client_briefs.md](client_briefs.md) | Four unlabeled author briefs. Send this file alone for the blind exercise. |
| [simulated_partner_briefs.md](simulated_partner_briefs.md) | Fictional incoming briefs used for the consulting exercise. |
| [approval_pack.pdf](approval_pack.pdf) and [approval_pack.md](approval_pack.md) | Three-page client decision pack and editable source. |
| [screen_cases.py](screen_cases.py) | Offline rule-based triage for the exercise. Python standard library only. |
| [sample_input.json](sample_input.json) and [sample_output.json](sample_output.json) | One four-case run with structured input and captured evidence. |
| [incomplete_input.json](incomplete_input.json) and [incomplete_output.json](incomplete_output.json) | Failure-boundary run with a missing purpose fact. |

The author’s private answer key is held separately until the reveal. It is not needed to reproduce the evidence run and should not be committed for the blind phase.

## Reproduce the workflow

From the repository root, run:

```sh
python3 screen_cases.py sample_input.json
python3 screen_cases.py incomplete_input.json
```

The input records human-coded facts derived from the simulated briefs. The rule runner reports the matched route, supporting facts, legal hook and suggested decision. The approval pack separately specifies what must happen before launch.

| Case | Evidence returned | Final consulting decision |
| --- | --- | --- |
| A · ElbeStay | Workplace role-plays, biometric emotion inference, non-medical/non-safety purpose. | Prohibited → Deny and redesign with an observation-only human rubric. |
| B · Dockline Staffing | Recruitment, ranked applicants and a shortlist shaping the review order. | High-risk → Approve with controls, subject to oversight and launch gates. |
| C · MuseumPass | Direct conversation with visitors and generated FAQ answers. | Transparency → Approve with controls, including first-interaction disclosure and technical marking. |
| D · RegisterMatch | Internal entity matching, no direct conversation, no synthetic text and no use for hiring or emotion inference. | Minimal risk → Approve for the stated scope. |

**Observed limitation.** Removing the purpose evidence from A gives `Undetermined / Hold for legal review`. The runner deliberately does not treat a missing fact as “no medical or safety purpose.” It cannot read free text, test the accuracy of human-coded facts, apply every provision or independently validate exceptions. It is not a general AI Act classifier.

**Debrief handoff.** After reviewing real incoming briefs, compare the partner’s intended categories with the consultant’s calls. Record any disputed fact, revised decision, remaining gate and owner. Do not treat the simulated findings as a completed partner sign-off.
