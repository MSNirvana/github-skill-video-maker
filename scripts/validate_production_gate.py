#!/usr/bin/env python3
"""Validate production-account readiness fields in a video brief."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


GENERIC_COVER_HOOKS = {"科研写作助手", "项目介绍", "skill介绍", "github项目", "开源项目"}


def _blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def validate_production_gate(brief: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []

    hook = brief.get("hook", {})
    for field in ["first_3_seconds", "pain", "viewer_reason_to_continue"]:
        if _blank(hook.get(field)):
            failures.append(f"hook.{field} is required")
    if _blank(brief.get("why_watch")):
        failures.append("why_watch is required")

    case = brief.get("real_case_flow", {})
    for field in ["input", "skill_action", "output_artifacts", "value"]:
        if _blank(case.get(field)):
            failures.append(f"real_case_flow.{field} is required")

    for field in ["proof_moment", "cover_hook", "cta"]:
        if _blank(brief.get(field)):
            failures.append(f"{field} is required")
    if str(brief.get("cover_hook", "")).strip().lower() in GENERIC_COVER_HOOKS:
        warnings.append("cover_hook looks generic; prefer a concrete curiosity hook")

    signature = brief.get("creator_signature", {})
    for field in ["speaker", "account_focus", "closing_line"]:
        if _blank(signature.get(field)):
            failures.append(f"creator_signature.{field} is required")

    if len(brief.get("retention_beats", [])) < 5:
        failures.append("retention_beats should include at least 5 beats")
    if len(brief.get("evidence_cards", [])) < 3:
        failures.append("evidence_cards should include at least 3 readable proof assets")
    if len(brief.get("sound_design", [])) < 5:
        warnings.append("sound_design should include at least 5 planned moments")

    score = brief.get("production_score", {})
    if score:
        numeric_scores = [float(value or 0) for value in score.values()]
        if any(value < 7 for value in numeric_scores):
            failures.append("production_score items must be at least 7")
        if sum(numeric_scores) / max(1, len(numeric_scores)) < 8:
            failures.append("production_score average must be at least 8")

    return {
        "ok": not failures,
        "failures": failures,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate production-account video brief fields.")
    parser.add_argument("brief")
    args = parser.parse_args()
    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    result = validate_production_gate(brief)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
