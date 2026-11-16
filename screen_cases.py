"""Offline evidence triage for the simulated cases. Not a legal classifier."""
import argparse
import json


RULES = (
    ("workplace_emotion", "Prohibited", "Deny and redesign", "Art. 5(1)(f)",
     ("workplace", "biometric_emotion_inference"), ("medical_or_safety_purpose",)),
    ("recruitment_ranking", "High-risk", "Approve with controls",
     "Art. 6(2); Annex III 4(a)", ("recruitment", "candidate_ranking"), ()),
    ("direct_ai_interaction", "Limited risk / transparency", "Approve with controls",
     "Art. 50(1), (5)", ("direct_conversation",), ()),
    ("entity_deduplication", "Minimal risk", "Approve", "Art. 4 remains relevant",
     ("internal_corporate_record_matching",),
     ("workplace", "biometric_emotion_inference", "recruitment", "candidate_ranking",
      "direct_conversation", "synthetic_text")),
)
FACTS = set().union(*(set(yes + no) for _, _, _, _, yes, no in RULES)) | {"synthetic_text"}


def screen(case):
    facts = case["facts"]
    for key, fact in facts.items():
        if key not in FACTS or type(fact["value"]) is not bool or not fact["evidence"].strip():
            raise ValueError(f"Invalid or unsupported evidence for {key}")
    matches = []
    for rule, tier, decision, law, yes, no in RULES:
        required = {**dict.fromkeys(yes, True), **dict.fromkeys(no, False)}
        if all(key in facts and facts[key]["value"] is value for key, value in required.items()):
            matches.append((rule, tier, decision, law, {key: facts[key] for key in required}))
    routes = {match[0] for match in matches}
    ambiguous = (len(matches) > 1 and "workplace_emotion" not in routes)
    unresolved = (facts.get("biometric_emotion_inference", {}).get("value") is True
                  and "workplace_emotion" not in routes)
    if not matches or ambiguous or unresolved:
        return {"case": case["case"], "tier": "Undetermined",
                "decision": "Hold for legal review", "rule": None, "evidence": {},
                "reason": "No unambiguous route, or a biometric exception/context needs review."}
    rule, tier, decision, law, evidence = matches[0]
    overlay = []
    if facts.get("synthetic_text", {}).get("value") is True:
        evidence["synthetic_text"] = facts["synthetic_text"]
        overlay.append("Check Art. 50(2) marking, exceptions and transition.")
    return {"case": case["case"], "tier": tier, "decision": decision, "rule": rule,
            "legal_hook": law, "evidence": evidence, "additional_checks": overlay}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as source:
        payload = json.load(source)
    print(json.dumps([screen(case) for case in payload], ensure_ascii=False, indent=2))
