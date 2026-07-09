#!/usr/bin/env python3
"""Validate screenshot, highlight, and occlusion records for video QA."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_EVIDENCE_FIELDS = [
    "asset",
    "source_url_or_path",
    "narration_claim",
    "target_region",
    "why_this_screenshot",
]


def _is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def _box_is_too_broad(box: Any) -> bool:
    if not isinstance(box, dict):
        return False
    width = _number(box.get("width", box.get("w", 0)))
    height = _number(box.get("height", box.get("h", 0)))
    # Normalized boxes or percentage-like boxes should not swallow most of the frame.
    return (0.7 < width <= 1.0 and 0.7 < height <= 1.0) or (70 < width <= 100 and 70 < height <= 100)


def _number(value: Any) -> float:
    if isinstance(value, str):
        value = value.strip().removesuffix("%")
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    scenes = manifest.get("scenes", [])
    if not isinstance(scenes, list) or not scenes:
        failures.append("visual manifest must contain a non-empty scenes list")
        scenes = []

    for index, scene in enumerate(scenes):
        scene_id = scene.get("id") or f"scene[{index}]"
        evidence = scene.get("evidence", [])
        if not evidence:
            failures.append(f"{scene_id}: missing evidence records")
        for item_index, item in enumerate(evidence):
            label = f"{scene_id}.evidence[{item_index}]"
            for field in REQUIRED_EVIDENCE_FIELDS:
                if _is_blank(item.get(field)):
                    failures.append(f"{label}: missing {field}")
            reason = str(item.get("why_this_screenshot", "")).lower()
            if reason in {"background", "filler", "decoration", "背景", "填充", "装饰"}:
                failures.append(f"{label}: screenshot is marked as filler/decoration")
            if item.get("readable_in_vertical") is False and _is_blank(item.get("fallback_asset")):
                failures.append(f"{label}: unreadable vertical evidence needs fallback_asset")

        for highlight_index, highlight in enumerate(scene.get("highlights", [])):
            label = f"{scene_id}.highlights[{highlight_index}]"
            if _is_blank(highlight.get("target")):
                failures.append(f"{label}: missing explicit target")
            if _is_blank(highlight.get("box_or_anchor")):
                failures.append(f"{label}: missing box_or_anchor")
            if _is_blank(highlight.get("verified_frame")):
                failures.append(f"{label}: missing verified_frame")
            if _box_is_too_broad(highlight.get("box_or_anchor")) and not highlight.get("allow_broad_panel"):
                failures.append(f"{label}: broad highlight requires allow_broad_panel=true and matching narration")

        layout = scene.get("layout", {})
        if not layout:
            warnings.append(f"{scene_id}: missing layout record")
            continue
        if layout.get("overlaps_checked") is not True:
            failures.append(f"{scene_id}: layout.overlaps_checked must be true after preview inspection")
        zones = set(layout.get("reserved_zones", []))
        required_zones = {"header", "evidence", "subtitle", "ip"}
        missing = sorted(required_zones - zones)
        if missing:
            failures.append(f"{scene_id}: missing reserved zones: {', '.join(missing)}")

    return {
        "ok": not failures,
        "scene_count": len(scenes),
        "failures": failures,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a GitHub Skill video visual manifest.")
    parser.add_argument("manifest")
    args = parser.parse_args()

    path = Path(args.manifest)
    result = validate_manifest(json.loads(path.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
