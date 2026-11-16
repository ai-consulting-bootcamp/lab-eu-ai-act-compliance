# Lab proof

**Lab:** Classify your product  
**Status:** Author briefs complete. Partner review and client debrief pending.

## Workflow and evidence

- **Code:** [check_blind_briefs.py](check_blind_briefs.py)
- **Input and current output:** [client-briefs.md](client-briefs.md), the four fictional client requests written for the blind exchange.
- **Run from the repository root:** `python check_blind_briefs.py client-briefs.md`

```text
Input: client-briefs.md
Case A: 6 brief lines
Case B: 6 brief lines
Case C: 6 brief lines
Case D: 6 brief lines
PASS: Four neutrally titled briefs meet the line-count requirement.
```

The run exited with code 0. A separate content review confirmed that each brief describes the client, business need, proposed AI behaviour, input data, affected people, and human review or override. The lab author holds the answer key separately for the debrief.

**Limitation.** The script checks headings and line counts. A passing run cannot establish whether each brief contains enough evidence to classify it or whether the legal reasoning is sound. The partner exchange and first-pass consulting review provide that evidence.

## Remaining lab outputs

1. Exchange label-free briefs and record a first-pass classification of all four partner cases before their key is revealed.
2. Build the review table and a client-facing approval pack of at most three pages. Cover architecture, provider and deployer roles, any vendor, obligations, launch decisions, and a lawful redesign for any prohibited proposal.
3. Compare the inferred and intended categories after the live discussion. Record the client's response, any change to the recommendation, and the final decision.

