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
    parser.add_argument(
        "--ip-narrative-mode",
        choices=["ip-led-story", "hybrid-evidence", "evidence-explainer"],
        default="ip-led-story",
        help="How strongly the recurring IP characters drive the episode story",
    )
    parser.add_argument(
        "--series-frame",
        default="AI 工具实验室",
        help="Recurring story frame, such as AI 工具实验室 or GitHub 项目面试",
    )
    parser.add_argument(
        "--episode-type",
        choices=["auto", "traffic", "depth", "brand"],
        default="auto",
        help="Episode length/editorial type; auto uses traffic up to 55s and depth otherwise",
    )
    parser.add_argument("--output-prefix", default="", help="Output filename prefix, defaults to <slug>-case")
    args = parser.parse_args()

    metadata = json.loads(Path(args.metadata).read_text(encoding="utf-8"))
    screenshots = json.loads(Path(args.screenshots).read_text(encoding="utf-8"))
    slug = slugify(metadata["full_name"])
    output_prefix = args.output_prefix or f"{slug}-case"
    episode_type = args.episode_type
    if episode_type == "auto":
        episode_type = "traffic" if args.duration <= 55 else "depth"

    scenes = [
        {"id": "cover", "goal": "Open with a function-first promise, episode conflict, Star signal, and the recurring cast.", "visual": "cover"},
        {"id": "pain", "goal": "Black Character voices the viewer doubt with minimal text.", "visual": "character conflict + project-relevant evidence"},
        {"id": "repo-proof", "goal": "Show real GitHub repo identity and Star count.", "visual": "repo + star_actions crop", "required": ["stars"]},
        {"id": "workflow", "goal": "Route Character turns the doubt into a 2-4 step test or workflow.", "visual": "route IP draws verified process line"},
        {"id": "skills", "goal": "Show the exact directory, feature, input, or configuration used by the test.", "visual": "claim-relevant screenshot"},
        {"id": "deep-dive", "goal": "Show one representative file, product state, or output artifact.", "visual": "selected evidence screenshot"},
        {"id": "compatibility", "goal": "Show supported hosts, workflow condition, or configuration boundary without public installation/download directions.", "visual": "distribution-safe evidence card"},
        {"id": "boundary", "goal": "Key Character checks the result and states limitations or expectations.", "visual": "key IP + verified boundary card"},
        {"id": "value", "goal": "Give a qualified viewer decision: who benefits and why.", "visual": "key verdict + one value sentence"},
        {"id": "signature", "goal": "Close with the creator signature and recurring cast.", "visual": "unified IP lockup"},
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
            "key": "artifact, compatibility, output, decision point",
        },
        "ip_narrative": {
            "mode": args.ip_narrative_mode,
            "series_frame": args.series_frame,
            "episode_type": episode_type,
            "episode_premise": "",
            "roles": {
                "black": {
                    "asset_role": "head",
                    "working_name": "Black Character",
                    "dramatic_job": "skeptical audience proxy who creates the conflict",
                    "personality": "quick, cheeky, evidence-seeking",
                    "allowed_actions": ["question", "point", "crossed-arms doubt", "surprise", "receive input"],
                    "forbidden_uses": ["unverified claim", "permanent corner avatar", "subtitle-area decoration"],
                },
                "route": {
                    "asset_role": "route",
                    "working_name": "Route Character",
                    "dramatic_job": "builder who turns the doubt into a visible test or workflow",
                    "personality": "practical, action-first, beginner-friendly",
                    "allowed_actions": ["carry input", "run test", "draw route", "connect steps", "show progress"],
                    "forbidden_uses": ["claim success without result evidence", "continuous idle bobbing", "subtitle-area decoration"],
                },
                "key": {
                    "asset_role": "key",
                    "working_name": "Key Character",
                    "dramatic_job": "product judge who verifies the result and states the boundary",
                    "personality": "calm, concise, mildly strict",
                    "allowed_actions": ["inspect output", "reveal artifact", "state boundary", "give verdict"],
                    "forbidden_uses": ["guaranteed-success implication", "download or install direction", "subtitle-area decoration"],
                },
            },
            "conflict": "",
            "obstacle": "",
            "resolution_evidence": "",
            "character_beats": [],
            "scene_cast": [
                {"scene_id": "cover", "lead_character": "black", "supporting_characters": ["route", "key"], "all_three_exception": True},
                {"scene_id": "pain", "lead_character": "black", "supporting_characters": []},
                {"scene_id": "repo-proof", "lead_character": "black", "supporting_characters": []},
                {"scene_id": "workflow", "lead_character": "route", "supporting_characters": []},
                {"scene_id": "skills", "lead_character": "route", "supporting_characters": []},
                {"scene_id": "deep-dive", "lead_character": "route", "supporting_characters": ["black"]},
                {"scene_id": "compatibility", "lead_character": "key", "supporting_characters": []},
                {"scene_id": "boundary", "lead_character": "key", "supporting_characters": ["black"]},
                {"scene_id": "value", "lead_character": "key", "supporting_characters": []},
                {"scene_id": "signature", "lead_character": "key", "supporting_characters": ["black", "route"], "all_three_exception": True},
            ],
            "qa": {
                "distinct_dramatic_jobs": False,
                "conflict_resolved_by_evidence": False,
                "meaningful_action_per_beat": False,
                "remove_ip_test_passed": False,
                "one_lead_max_one_support_per_scene": False,
                "characters_clear_of_subtitles_and_evidence": False,
            },
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
            "body_voice": "",
            "factual_anchor": "",
            "boundary_clarifier": "",
            "qa": {
                "funny_or_surprising": False,
                "body_copy_keeps_same_voice": False,
                "playful_keywords_quoted_when_exaggerated": False,
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
        "platform_distribution_safety": {
            "mode": "strict_platform_safe",
            "external_routing_free": False,
            "third_party_action_free": False,
            "public_copy_url_free": False,
            "distribution_crops_verified": False,
            "native_ai_label": True,
            "qa": {
                "final_text_scan_passed": False,
                "cover_and_preview_manually_checked": False,
            },
        },
        "platform_safety_note": {
            "enabled": False,
            "text": "",
            "placement": "upper_right_or_upper_edge",
            "style": "small, low-emphasis, readable, visually secondary",
            "avoid_zones": ["line_subtitle", "insight_subtitle", "evidence", "star_badge", "ip"],
            "qa": {
                "not_near_bottom_subtitles": True,
                "does_not_cover_key_evidence": True,
            },
        },
        "model_routing": {
            "controller": "current Codex conversation",
            "strong_model_tasks": [
                "repo research and factual judgment",
                "first-15-second hook and final script strategy",
                "platform-risk review",
                "screenshot/evidence selection",
                "visual QA for highlights, subtitles, IP overlap, and cover clarity",
                "nontrivial Remotion fixes",
            ],
            "low_cost_model_tasks": [
                "README summary draft",
                "title candidate draft",
                "publishing-copy first draft",
                "subtitle chunk draft",
                "visual asset list draft",
                "first-pass sensitive-word scan",
            ],
            "deterministic_tool_tasks": [
                "GitHub metadata fetch",
                "screenshot capture",
                "crop/contact-sheet generation",
                "audio conversion",
                "subtitle alignment from final audio",
                "ffprobe media checks",
                "Remotion render",
                "manifest validation",
                "final file copy",
            ],
            "external_providers": [],
            "fallback_policy": "If an external model is unavailable, too weak, or changes factual meaning, route the step back to the strongest available reasoning model and record the reason.",
            "cost_notes": "Save tokens on repeatable drafts and deterministic local work; keep account-facing judgment and final QA on a strong model.",
            "qa": {
                "no_secret_keys_in_brief": True,
                "final_facts_reviewed_by_strong_model_or_manual": False,
                "final_script_reviewed_by_strong_model": False,
                "platform_risk_reviewed_by_strong_model": False,
                "visual_quality_reviewed_by_strong_model_or_manual": False,
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
            f"{output_prefix}-script-handoff.md",
        ],
        "script_handoff": {
            "output": f"{output_prefix}-script-handoff.md",
            "editable_main_section": True,
            "timestamps_in_main_section": False,
            "source": f"{output_prefix}-narration.txt",
        },
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
