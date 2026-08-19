#!/usr/bin/env python3
"""Render a client-review JSON file into a clean CSV that opens in Excel.

Usage:
    python scripts/render_csv.py path/to/client-review.json [output.csv]

No third-party dependencies.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def flatten_review(data: dict) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(section: str, item: str, value: object = "", note: object = "", source: object = "") -> None:
        rows.append(
            {
                "section": section,
                "item": str(item or ""),
                "value": str(value or ""),
                "note": str(note or ""),
                "source": str(source or ""),
            }
        )

    add("account", "client", data.get("client", ""))
    add("account", "period", data.get("period", ""))
    add("account", "headline", data.get("headline", ""))

    for index, bullet in enumerate(data.get("executive_summary", []), start=1):
        add("executive_summary", f"summary_{index}", bullet)

    for metric in data.get("metrics", []):
        add(
            "metric",
            metric.get("name", ""),
            metric.get("current", ""),
            f"Previous: {metric.get('previous', '')}; {metric.get('note', '')}".strip("; "),
            metric.get("source", ""),
        )

    for signal in data.get("signals", []):
        add(
            "signal",
            signal.get("fact", ""),
            signal.get("impact", ""),
            signal.get("confidence", ""),
            signal.get("source", ""),
        )

    for index, learning in enumerate(data.get("learnings", []), start=1):
        add("learning", f"learning_{index}", learning)

    for index, action in enumerate(data.get("actions_completed", []), start=1):
        add("completed_action", f"action_{index}", action)

    for recommendation in data.get("recommendations", []):
        add(
            "recommendation",
            recommendation.get("action", ""),
            recommendation.get("why", ""),
            recommendation.get("priority", ""),
            recommendation.get("source", ""),
        )

    for index, decision in enumerate(data.get("decisions_needed", []), start=1):
        add("decision_needed", f"decision_{index}", decision)

    return rows


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/render_csv.py <client-review.json> [output.csv]", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".csv")

    data = json.loads(input_path.read_text(encoding="utf-8"))
    rows = flatten_review(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["section", "item", "value", "note", "source"])
        writer.writeheader()
        writer.writerows(rows)

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
