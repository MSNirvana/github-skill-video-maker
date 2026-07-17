#!/usr/bin/env python3
"""Validate production-account readiness fields in a video brief."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from platform_safety import scan_brief


GENERIC_COVER_HOOKS = {"科研写作助手", "项目介绍", "skill介绍", "github项目", "开源项目"}
IP_NARRATIVE_MODES = {"ip-led-story", "hybrid-evidence", "evidence-explainer"}
IP_LED_MODES = {"ip-led-story", "hybrid-evidence"}
IP_CHARACTERS = {"black", "route", "key"}
ALL_THREE_SCENE_IDS = {"cover", "merge", "signature"}


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

    ip_narrative = brief.get("ip_narrative", {}) or {}
    narrative_mode = ip_narrative.get("mode")
    if narrative_mode not in IP_NARRATIVE_MODES:
        failures.append("ip_narrative.mode must be ip-led-story, hybrid-evidence, or evidence-explainer")
    if narrative_mode in IP_LED_MODES:
        for field in ["series_frame", "episode_type", "episode_premise", "conflict", "obstacle", "resolution_evidence"]:
            if _blank(ip_narrative.get(field)):
                failures.append(f"ip_narrative.{field} is required for {narrative_mode}")

        roles = ip_narrative.get("roles", {}) or {}
        for character in sorted(IP_CHARACTERS):
            role = roles.get(character, {}) or {}
            for field in ["working_name", "dramatic_job", "personality", "allowed_actions", "forbidden_uses"]:
                if _blank(role.get(field)):
                    failures.append(f"ip_narrative.roles.{character}.{field} is required")

        character_beats = ip_narrative.get("character_beats", []) or []
        minimum_beats = 3 if float(brief.get("duration_seconds", 90) or 90) <= 60 else 5
        if len(character_beats) < minimum_beats:
            failures.append(f"ip_narrative.character_beats should include at least {minimum_beats} meaningful beats")
        represented_characters: set[str] = set()
        for index, beat in enumerate(character_beats):
            for field in ["scene_id", "character", "intent", "line_or_reaction", "action_state", "evidence_target"]:
                if _blank(beat.get(field)):
                    failures.append(f"ip_narrative.character_beats[{index}].{field} is required")
            character = beat.get("character")
            if character not in IP_CHARACTERS:
                failures.append(f"ip_narrative.character_beats[{index}].character must be black, route, or key")
            else:
                represented_characters.add(character)
        if represented_characters != IP_CHARACTERS:
            failures.append("ip_narrative.character_beats must give black, route, and key distinct story actions")

        scene_cast = ip_narrative.get("scene_cast", []) or []
        if not scene_cast:
            failures.append("ip_narrative.scene_cast is required for IP-led production")
        for index, cast in enumerate(scene_cast):
            scene_id = cast.get("scene_id")
            lead = cast.get("lead_character")
            supports = cast.get("supporting_characters", []) or []
            if _blank(scene_id):
                failures.append(f"ip_narrative.scene_cast[{index}].scene_id is required")
            if lead not in IP_CHARACTERS:
                failures.append(f"ip_narrative.scene_cast[{index}].lead_character must be black, route, or key")
            if any(character not in IP_CHARACTERS for character in supports):
                failures.append(f"ip_narrative.scene_cast[{index}].supporting_characters contains an unknown character")
            if lead in supports or len(set(supports)) != len(supports):
                failures.append(f"ip_narrative.scene_cast[{index}] contains duplicate character assignments")
            if len(supports) > 1:
                exception_allowed = cast.get("all_three_exception") is True and scene_id in ALL_THREE_SCENE_IDS
                if not exception_allowed:
                    failures.append(
                        f"ip_narrative.scene_cast[{index}] may use more than one support only for cover, merge, or signature"
                    )

        ip_qa = ip_narrative.get("qa", {}) or {}
        for field in [
            "distinct_dramatic_jobs",
            "conflict_resolved_by_evidence",
            "meaningful_action_per_beat",
            "remove_ip_test_passed",
            "one_lead_max_one_support_per_scene",
            "characters_clear_of_subtitles_and_evidence",
        ]:
            if ip_qa.get(field) is not True:
                failures.append(f"ip_narrative.qa.{field} must be true after final script and visual review")

    script = brief.get("script_strategy", {})
    for field in ["core_angle", "viewer_doubt", "plain_answer", "account_point_of_view"]:
        if _blank(script.get(field)):
            failures.append(f"script_strategy.{field} is required")

    hkr = script.get("hkr_score", {}) or {}
    hkr_values = []
    for field in ["happy", "knowledge", "resonance"]:
        value = hkr.get(field)
        if _blank(value):
            failures.append(f"script_strategy.hkr_score.{field} is required")
            continue
        try:
            numeric = float(value)
        except (TypeError, ValueError):
            failures.append(f"script_strategy.hkr_score.{field} must be numeric")
            continue
        hkr_values.append(numeric)
        if numeric < 3:
            failures.append(f"script_strategy.hkr_score.{field} must be at least 3")
    if hkr_values and sum(1 for value in hkr_values if value >= 4) < 2:
        failures.append("script_strategy.hkr_score should score at least 4 in two dimensions")

    micro_story = script.get("micro_story", {}) or {}
    for field in ["challenge", "evidence", "process", "result", "boundary", "signature"]:
        if _blank(micro_story.get(field)):
            failures.append(f"script_strategy.micro_story.{field} is required")

    anti_fluff = script.get("anti_ai_fluff_scan", {}) or {}
    if anti_fluff.get("passed") is not True:
        failures.append("script_strategy.anti_ai_fluff_scan.passed must be true after rewriting generic/README-like narration")
    if len(script.get("escalation_beats", []) or []) < 4:
        failures.append("script_strategy.escalation_beats should include at least 4 ordered clarity/proof beats")
    script_qa = script.get("qa", {}) or {}
    for field in [
        "one_core_angle",
        "not_readme_summary",
        "beginner_can_understand_without_github",
        "claims_backed_by_evidence_or_boundary",
        "human_voice_not_ai_summary",
    ]:
        if script_qa.get(field) is not True:
            failures.append(f"script_strategy.qa.{field} must be true")

    beginner = brief.get("beginner_clarity", {})
    for field in ["plain_definition", "target_user", "pain_solved", "first_10_seconds"]:
        if _blank(beginner.get(field)):
            failures.append(f"beginner_clarity.{field} is required")
    if len(beginner.get("jargon_translations", {}) or {}) < 2:
        failures.append("beginner_clarity.jargon_translations should include at least 2 plain-language translations")
    if len(beginner.get("so_what_beats", []) or []) < 4:
        failures.append("beginner_clarity.so_what_beats should include at least 4 viewer-value beats")

    viral = brief.get("viral_packaging", {}) or {}
    if len(viral.get("meme_titles", []) or []) < 3:
        failures.append("viral_packaging.meme_titles should include at least 3 funny title candidates")
    if len(viral.get("contrast_titles", []) or []) < 3:
        failures.append("viral_packaging.contrast_titles should include at least 3 contrast/curiosity title candidates")
    if len(viral.get("practical_titles", []) or []) < 3:
        failures.append("viral_packaging.practical_titles should include at least 3 practical/search-friendly title candidates")
    for field in ["recommended_title", "opening_line", "body_voice", "factual_anchor", "boundary_clarifier"]:
        if _blank(viral.get(field)):
            failures.append(f"viral_packaging.{field} is required")
    viral_qa = viral.get("qa", {}) or {}
    for field in [
        "funny_or_surprising",
        "body_copy_keeps_same_voice",
        "playful_keywords_quoted_when_exaggerated",
        "no_false_guarantee",
        "no_fake_official_endorsement",
        "grounded_by_evidence_in_first_10_seconds",
    ]:
        if viral_qa.get(field) is not True:
            failures.append(f"viral_packaging.qa.{field} must be true")

    subtitles = brief.get("subtitle_strategy", {})
    if subtitles.get("mode") != "dual-layer":
        failures.append("subtitle_strategy.mode must be dual-layer")
    if len(subtitles.get("insight_subtitles", []) or []) < 5:
        failures.append("subtitle_strategy.insight_subtitles should include at least 5 scene-level key points")
    if len(subtitles.get("line_subtitles", []) or []) < 8:
        failures.append("subtitle_strategy.line_subtitles should include complete narration chunks, not sparse keywords")
    if _blank(subtitles.get("timing_source")):
        failures.append("subtitle_strategy.timing_source must point to the final narration audio used for subtitle timing")
    if _blank(subtitles.get("alignment_method")):
        failures.append("subtitle_strategy.alignment_method is required; do not hand-estimate line subtitle timing")
    safe_zones = subtitles.get("safe_zones", {}) or {}
    if _blank(safe_zones.get("insight_subtitle")) or _blank(safe_zones.get("line_subtitle")):
        failures.append("subtitle_strategy.safe_zones must reserve insight_subtitle and line_subtitle zones")
    subtitle_qa = subtitles.get("qa", {}) or {}
    if subtitle_qa.get("line_subtitles_aligned_to_final_audio") is not True:
        failures.append("subtitle_strategy.qa.line_subtitles_aligned_to_final_audio must be true after audio-sync verification")

    for index, item in enumerate(subtitles.get("line_subtitles", []) or []):
        if _blank(item.get("start")) or _blank(item.get("end")):
            failures.append(f"subtitle_strategy.line_subtitles[{index}] must include start and end timings from final audio")

    interaction = brief.get("interaction_style", {}) or {}
    if interaction.get("fake_human_screencast") is not False:
        failures.append("interaction_style.fake_human_screencast must be false; do not simulate human screencasts with decorative cursors or fake interaction")

    distribution = brief.get("platform_distribution_safety", {}) or {}
    if distribution.get("mode") != "strict_platform_safe":
        failures.append("platform_distribution_safety.mode must be strict_platform_safe for production-platform delivery")
    for field in [
        "external_routing_free",
        "third_party_action_free",
        "public_copy_url_free",
        "distribution_crops_verified",
    ]:
        if distribution.get(field) is not True:
            failures.append(f"platform_distribution_safety.{field} must be true after final review")
    distribution_qa = distribution.get("qa", {}) or {}
    for field in ["final_text_scan_passed", "cover_and_preview_manually_checked"]:
        if distribution_qa.get(field) is not True:
            failures.append(f"platform_distribution_safety.qa.{field} must be true")

    safety_note = brief.get("platform_safety_note", {}) or {}
    if safety_note.get("enabled"):
        if safety_note.get("text") != "AI 辅助创作":
            failures.append("platform_safety_note.text may only be AI 辅助创作 when enabled")
        if _blank(safety_note.get("placement")):
            failures.append("platform_safety_note.placement is required when the neutral AI label is enabled")

    for finding in scan_brief(brief):
        failures.append(
            f"platform public text contains {finding['risk']}: {finding['match']} ({finding['snippet']})"
        )

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
