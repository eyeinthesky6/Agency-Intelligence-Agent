#!/usr/bin/env python3
"""Tiny zero-dependency smoke test for Agency Intelligence Agent.

Checks repository contracts without evaluating model quality:
- required skills exist and contain Agent Skill frontmatter
- core JSON templates parse and use allowed verification enums
- README references the verification loop and actual renderers
- the Kazam benchmark contains a complete verification receipt trail

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
    "07-verify-and-challenge",
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

CLAIM_KINDS = {"fact", "number", "date", "comparison", "inference"}
IMPORTANCE = {"critical", "supporting"}
CONFIDENCE = {"high", "medium", "low"}
VERIFY_STATUSES = {
    "VERIFIED_PRIMARY",
    "VERIFIED_CORROBORATED",
    "PARTIAL",
    "STALE",
    "UNSUPPORTED",
    "CONTRADICTED",
}
TERMINAL_STATUSES = {
    "VERIFIED",
    "VERIFIED_WITH_CAVEATS",
    "REVIEW_REQUIRED",
    "FAILED_EVIDENCE_GATE",
}


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    check(path.exists(), f"Missing JSON file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


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
    signal = load_json(signal_path)
    for field in ("observed_at", "entity", "type", "fact", "source_url", "confidence", "impact"):
        check(field in signal, f"Signal example missing field: {field}")
    check(signal["confidence"] in CONFIDENCE, "Invalid signal confidence")

    review_path = ROOT / "templates" / "client-review.example.json"
    review = load_json(review_path)
    missing = REVIEW_REQUIRED_FIELDS - set(review)
    check(not missing, f"Client review example missing fields: {sorted(missing)}")
    check(len(review.get("recommendations", [])) <= 3, "Example has more than three recommendations")

    claims = load_json(ROOT / "templates" / "claims.example.json")
    check(claims.get("claims"), "Claims example must contain at least one claim")
    for claim in claims["claims"]:
        for field in ("id", "claim", "kind", "importance", "source_urls", "as_of", "producer_confidence"):
            check(field in claim, f"Claim example missing field: {field}")
        check(claim["kind"] in CLAIM_KINDS, f"Invalid claim kind: {claim['kind']}")
        check(claim["importance"] in IMPORTANCE, f"Invalid claim importance: {claim['importance']}")
        check(claim["producer_confidence"] in CONFIDENCE, f"Invalid producer confidence: {claim['producer_confidence']}")

    verification = load_json(ROOT / "templates" / "verification.example.json")
    check(verification.get("claims"), "Verification example must contain a checked claim")
    for claim in verification["claims"]:
        check(claim.get("status") in VERIFY_STATUSES, f"Invalid verification status: {claim.get('status')}")

    receipt = load_json(ROOT / "templates" / "receipt.example.json")
    check(receipt.get("status") in TERMINAL_STATUSES, f"Invalid receipt status: {receipt.get('status')}")

    counterfactual = ROOT / "templates" / "counterfactual.example.md"
    check(counterfactual.exists(), "Missing counterfactual template")
    counter_text = counterfactual.read_text(encoding="utf-8")
    for verdict in ("OVERTURNS", "WEAKENS", "UNCHANGED", "STRENGTHENS", "UNRESOLVED"):
        check(verdict in counter_text, f"Counterfactual template missing verdict: {verdict}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check("scripts/render_csv.py" in readme, "README missing render_csv.py")
    check("scripts/render_pptx.mjs" in readme, "README missing render_pptx.mjs")
    check("07-verify-and-challenge" in readme, "README missing verification skill")
    check("VERIFIED_WITH_CAVEATS" in readme, "README missing verification terminal states")
    check("pricing-strategy" not in readme, "README still references consulting pricing skill")
    check("campaign-brief" not in readme, "README still references removed campaign generator")

    kazam_run = ROOT / "examples" / "kazam-agency-prep" / "outputs" / "2026-08-19-verified"
    for filename in ("claims.json", "verification.json", "counterfactual.md", "final.md", "receipt.json"):
        check((kazam_run / filename).exists(), f"Kazam verification benchmark missing: {filename}")
    kazam_receipt = load_json(kazam_run / "receipt.json")
    check(kazam_receipt.get("status") in TERMINAL_STATUSES, "Kazam benchmark has invalid terminal status")
    check(kazam_receipt.get("counterfactual_challenges", 0) > 0, "Kazam benchmark did not run counterfactual challenges")

    print(f"PASS: {len(REQUIRED_SKILLS)} skills + verification contracts + Kazam audit trail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
