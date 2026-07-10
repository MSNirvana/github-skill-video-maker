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
    parser.add_argument("--style", default="evidence-explainer")
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
        "script_strategy": {
            "core_angle": "",
            "viewer_doubt": "",
            "plain_answer": "",
            "account_point_of_view": "",
            "hkr_score": {
                "happy": 0,
                "knowledge": 0,
                "resonance": 0,
            },
            "micro_story": {
                "challenge": "",
                "evidence": "",
                "process": "",
                "result": "",
                "boundary": "",
                "signature": "",
            },
            "human_voice_rules": {
                "concrete_names": [],
                "plain_benefit_before_jargon": True,
                "mild_judgment": "",
                "boundary_statement": "",
                "oral_sentence_style": True,
            },
            "anti_ai_fluff_scan": {
                "banned_patterns_checked": [
                    "随着 AI 的发展",
                    "在当今 AI 时代",
                    "今天给大家介绍",
                    "首先",
                    "其次",
                    "综上所述",
                    "值得注意的是",
                    "不难发现",
                    "赋能",
                    "生态闭环",
                    "神器",
                    "全网第一",
                ],
                "rewrites": [],
                "passed": False,
            },
            "escalation_beats": [],
            "qa": {
                "one_core_angle": False,
                "not_readme_summary": False,
                "beginner_can_understand_without_github": False,
                "claims_backed_by_evidence_or_boundary": False,
                "human_voice_not_ai_summary": False,
            },
        },
        "beginner_clarity": {
            "plain_definition": "",
            "target_user": "",
            "pain_solved": "",
            "first_10_seconds": "",
            "jargon_translations": {},
            "so_what_beats": [],
        },
        "viral_packaging": {
            "meme_titles": [],
            "contrast_titles": [],
            "practical_titles": [],
            "recommended_title": "",
            "opening_line": "",
            "factual_anchor": "",
            "boundary_clarifier": "",
            "qa": {
                "funny_or_surprising": False,
                "no_false_guarantee": False,
                "no_fake_official_endorsement": False,
                "grounded_by_evidence_in_first_10_seconds": False,
            },
        },
        "subtitle_strategy": {
            "mode": "dual-layer",
            "insight_subtitles": [],
            "line_subtitles": [],
            "timing_source": "",
            "alignment_method": "",
            "safe_zones": {
                "insight_subtitle": "mid-screen or next to evidence, never covering proof targets",
                "line_subtitle": "lower safe area above platform UI crop",
            },
            "qa": {
                "complete_line_subtitles": True,
                "line_subtitles_aligned_to_final_audio": True,
                "insight_subtitles_are_scene_conclusions": True,
                "no_overlap_with_evidence_ip_or_star": True,
            },
        },
        "interaction_style": {
            "fake_human_screencast": False,
            "cursor_policy": "omit decorative cursors; use only real recorded interaction or concrete semantic pointing",
            "preferred_visuals": ["stable screenshot crops", "readable evidence cards", "zoom", "pan", "precise highlights"],
        },
        "platform_safety_note": {
            "text": "纯干货分享，不存在站外引流",
            "placement": "upper_right_or_upper_edge",
            "style": "small, low-emphasis, readable, visually secondary",
            "avoid_zones": ["line_subtitle", "insight_subtitle", "evidence", "star_badge", "ip"],
            "qa": {
                "not_near_bottom_subtitles": True,
                "does_not_cover_key_evidence": True,
            },
        },
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
