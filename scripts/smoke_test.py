#!/usr/bin/env python3
"""Tiny zero-dependency smoke test for Agency Intelligence Agent.

Checks repository contracts without evaluating model quality:
- required skills exist and contain Agent Skill frontmatter
- example JSON files parse
- renderer input fields are present
- README references the actual renderer filenames

Usage:
    python scripts/smoke_test.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SKILLS = [
    "00-client-onboard",
    "01-prospect-intelligence",
    "02-competitor-watch",
    "03-meeting-prep",
    "04-growth-opportunities",
    "05-client-review",
    "06-agency-direction",
]

REVIEW_REQUIRED_FIELDS = {
    "client",
    "period",
    "headline",
    "executive_summary",
    "metrics",
    "signals",
    "actions_completed",
    "recommendations",
    "decisions_needed",
}


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    for skill in REQUIRED_SKILLS:
        path = ROOT / "skills" / skill / "SKILL.md"
        check(path.exists(), f"Missing skill: {path}")
        text = path.read_text(encoding="utf-8")
        check(text.startswith("---\n"), f"Missing YAML frontmatter: {path}")
        frontmatter = text.split("---", 2)[1]
        check("name:" in frontmatter, f"Missing skill name: {path}")
        check("description:" in frontmatter, f"Missing skill description: {path}")

    signal_path = ROOT / "templates" / "signal.example.json"
    signal = json.loads(signal_path.read_text(encoding="utf-8"))
    for field in ("observed_at", "entity", "type", "fact", "source_url", "confidence", "impact"):
        check(field in signal, f"Signal example missing field: {field}")
    check(signal["confidence"] in {"high", "medium", "low"}, "Invalid signal confidence")

    review_path = ROOT / "templates" / "client-review.example.json"
    review = json.loads(review_path.read_text(encoding="utf-8"))
    missing = REVIEW_REQUIRED_FIELDS - set(review)
    check(not missing, f"Client review example missing fields: {sorted(missing)}")
    check(len(review.get("recommendations", [])) <= 3, "Example has more than three recommendations")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("scripts/render_csv.py" in readme, "README missing render_csv.py")
    check("scripts/render_pptx.mjs" in readme, "README missing render_pptx.mjs")
    check("pricing-strategy" not in readme, "README still references consulting pricing skill")
    check("campaign-brief" not in readme, "README still references removed campaign generator")

    print(f"PASS: {len(REQUIRED_SKILLS)} agency intelligence skills + templates + renderer references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
