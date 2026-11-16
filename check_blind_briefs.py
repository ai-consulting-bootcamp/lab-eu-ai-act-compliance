"""Check the structure and heading labels of the blind-review handout."""

import argparse
from pathlib import Path
import re
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("briefs", type=Path)
    args = parser.parse_args()

    document = args.briefs.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", document, flags=re.MULTILINE)
    bodies = re.split(r"^## .+$", document, flags=re.MULTILINE)[1:]
    expected_headings = ["Case A", "Case B", "Case C", "Case D"]
    errors = []
    print(f"Input: {args.briefs.as_posix()}")

    if headings != expected_headings:
        errors.append("Expected four neutral case headings in order from A to D.")

    for heading, body in zip(headings, bodies):
        lines = [line.strip() for line in body.splitlines() if line.strip()]
        bullets = sum(line.startswith("- ") for line in lines)
        print(f"{heading}: {bullets} brief lines")
        if bullets != len(lines) or not 5 <= bullets <= 7:
            errors.append(f"{heading} must have five to seven bullet lines.")

    if errors:
        print("FAIL: " + " ".join(errors))
        return 1

    print("PASS: Four neutrally titled briefs meet the line-count requirement.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

