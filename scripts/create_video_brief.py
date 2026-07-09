#!/usr/bin/env python3
"""Create a structured video brief and storyboard from metadata/screenshots."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.lower().replace("/", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create video brief JSON.")
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--screenshots", required=True, help="screenshots-manifest.json")
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--audience", default="AI users and builders")
    parser.add_argument("--duration", type=int, default=90)
    parser.add_argument("--language", default="zh-CN")
    parser.add_argument("--style", default="case-walkthrough")
    parser.add_argument("--output-prefix", default="", help="Output filename prefix, defaults to <slug>-case")
    args = parser.parse_args()

    metadata = json.loads(Path(args.metadata).read_text(encoding="utf-8"))
    screenshots = json.loads(Path(args.screenshots).read_text(encoding="utf-8"))
    slug = slugify(metadata["full_name"])
    output_prefix = args.output_prefix or f"{slug}-case"

    scenes = [
        {"id": "cover", "goal": "Open with project name, promise, Star signal, and all IP characters.", "visual": "cover"},
        {"id": "pain", "goal": "State the user pain with minimal text.", "visual": "repo screenshot as background evidence"},
        {"id": "repo-proof", "goal": "Show real GitHub repo and Star count.", "visual": "repo + star_actions crop", "required": ["stars"]},
        {"id": "workflow", "goal": "Explain the core flow.", "visual": "route IP draws process line"},
        {"id": "skills", "goal": "Show skills directory or important Skill files.", "visual": "skills screenshot"},
        {"id": "deep-dive", "goal": "Show one representative file or capability.", "visual": "selected file screenshot"},
        {"id": "install", "goal": "Show supported platform/install evidence.", "visual": "README/plugin config screenshot"},
        {"id": "boundary", "goal": "State limitations and expectations.", "visual": "head IP + short tags"},
        {"id": "value", "goal": "Close with one value sentence.", "visual": "unified IP lockup"},
    ]

    brief = {
        "schema_version": 1,
        "slug": slug,
        "repo": metadata,
        "screenshots": screenshots.get("captures", {}),
        "audience": args.audience,
        "duration_seconds": args.duration,
        "language": args.language,
        "style": args.style,
        "theme": {
            "background": "white/light",
            "primary": "red laser infinity eye",
            "secondary": "blue for structure",
            "accent": "orange for energy/unlock",
        },
        "ip_roles": {
            "head": "pain, warning, conclusion",
            "route": "workflow, connection, platform support",
            "key": "install, access, unlock",
        },
        "hook": {
            "first_3_seconds": "",
            "pain": "",
            "contradiction": "",
            "viewer_reason_to_continue": "",
        },
        "why_watch": "",
        "real_case_flow": {
            "input": "",
            "skill_action": "",
            "output_artifacts": [],
            "value": "",
        },
        "proof_moment": "",
        "cover_hook": "",
        "cta": "",
        "creator_signature": {
            "speaker": "凸先生",
            "account_focus": "AI 全栈流程",
            "closing_line": "我是凸先生，专注 AI 全栈流程，我们下次再见！",
        },
        "retention_beats": [],
        "evidence_cards": [],
        "sound_design": [],
        "production_score": {
            "hook": 0,
            "clarity": 0,
            "proof": 0,
            "visual_rhythm": 0,
            "cta": 0,
        },
        "required_outputs": [
            f"{output_prefix}-90s-vertical.mp4",
            f"{output_prefix}-cover.png",
            f"{output_prefix}-narration.txt",
            f"{output_prefix}-narration.mp3",
            f"{output_prefix}-preview-sheet.jpg",
        ],
        "publishing_pack": {
            "output": f"{output_prefix}-publishing-pack.md",
            "platforms": ["douyin", "wechat_channels", "xiaohongshu"],
            "ai_disclosure_required": True,
            "source_date_note": metadata.get("captured_at", ""),
            "risk_terms": [
                "代写论文",
                "保过",
                "包过",
                "稳赚",
                "一键赚钱",
                "破解",
                "绕过审核",
                "官方推荐",
                "100%",
                "无风险",
            ],
        },
        "storyboard": scenes,
        "qa": {
            "must_show_star_count": True,
            "must_include_subtitles": True,
            "must_include_all_three_ip_roles": True,
            "must_export_cover": True,
            "must_verify_highlights": True,
        },
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(output), "slug": slug, "stars_label": metadata.get("stars_label")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
