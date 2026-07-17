#!/usr/bin/env python3
"""Check required deliverables and media properties for a generated video."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from validate_production_gate import validate_production_gate
from validate_visual_manifest import validate_manifest
from platform_safety import result_payload as platform_safety_payload
from platform_safety import scan_brief, scan_text


def ffprobe(path: Path) -> dict:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration,size:stream=index,codec_type,codec_name,width,height,r_frame_rate",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return json.loads(result.stdout)


def expected_from_required_outputs(out_dir: Path, required_outputs: list[str]) -> dict[str, Path]:
    expected: dict[str, Path] = {}
    for name in required_outputs:
        path = out_dir / name
        if name.endswith(".mp4"):
            expected["video"] = path
        elif name.endswith("-cover.png") or "cover" in name and name.endswith(".png"):
            expected["cover"] = path
        elif name.endswith("-narration.txt") or name.endswith(".txt"):
            expected["narration_text"] = path
        elif name.endswith("-narration.mp3") or name.endswith(".mp3"):
            expected["narration_audio"] = path
        elif name.endswith("-preview-sheet.jpg") or "preview" in name and name.endswith((".jpg", ".jpeg", ".png")):
            expected["preview"] = path
        elif name.endswith("-script-handoff.md"):
            expected["script_handoff"] = path
    return expected


def override_path(current: dict[str, Path], label: str, value: str) -> None:
    if value:
        current[label] = Path(value)


def main() -> int:
    parser = argparse.ArgumentParser(description="QA generated GitHub Skill video outputs.")
    parser.add_argument("--brief", required=True)
    parser.add_argument("--outputs-dir", required=True)
    parser.add_argument("--slug", default="", help="Override slug from brief")
    parser.add_argument("--video", default="", help="Explicit final MP4 path")
    parser.add_argument("--cover", default="", help="Explicit cover image path")
    parser.add_argument("--narration-text", default="", help="Explicit narration text path")
    parser.add_argument("--narration-audio", default="", help="Explicit narration audio path")
    parser.add_argument("--preview", default="", help="Explicit preview sheet path")
    parser.add_argument("--publishing-pack", default="", help="Explicit platform publishing pack Markdown path")
    parser.add_argument("--script-handoff", default="", help="Explicit editable script handoff Markdown path")
    parser.add_argument("--visual-manifest", default="", help="Optional visual manifest JSON path")
    parser.add_argument("--platform-text", action="append", default=[], help="Narration, SRT, renderer source, or other public text to scan; repeat as needed")
    parser.add_argument("--production-gate", action="store_true", help="Validate production account gate fields")
    args = parser.parse_args()

    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    slug = args.slug or brief["slug"]
    out_dir = Path(args.outputs_dir)
    expected = {
        "video": out_dir / f"{slug}-case-90s-vertical.mp4",
        "cover": out_dir / f"{slug}-case-cover.png",
        "narration_text": out_dir / f"{slug}-case-narration.txt",
        "narration_audio": out_dir / f"{slug}-case-narration.mp3",
        "preview": out_dir / f"{slug}-case-preview-sheet.jpg",
    }
    expected.update(expected_from_required_outputs(out_dir, brief.get("required_outputs", [])))
    override_path(expected, "video", args.video)
    override_path(expected, "cover", args.cover)
    override_path(expected, "narration_text", args.narration_text)
    override_path(expected, "narration_audio", args.narration_audio)
    override_path(expected, "preview", args.preview)
    publishing_pack = brief.get("publishing_pack", {})
    if publishing_pack.get("output"):
        expected["publishing_pack"] = out_dir / publishing_pack["output"]
    override_path(expected, "publishing_pack", args.publishing_pack)
    script_handoff = brief.get("script_handoff", {})
    if script_handoff.get("output"):
        expected["script_handoff"] = out_dir / script_handoff["output"]
    override_path(expected, "script_handoff", args.script_handoff)

    failures: list[str] = []
    for label, path in expected.items():
        if not path.exists() or path.stat().st_size == 0:
            failures.append(f"Missing or empty {label}: {path}")

    media = None
    if expected["video"].exists():
        try:
            media = ffprobe(expected["video"])
            streams = media.get("streams", [])
            video_stream = next((s for s in streams if s.get("codec_type") == "video"), {})
            audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), {})
            if video_stream.get("width") != 1080 or video_stream.get("height") != 1920:
                failures.append(f"Video is not 1080x1920: {video_stream.get('width')}x{video_stream.get('height')}")
            if not audio_stream:
                failures.append("Video has no audio stream")
            duration = float((media.get("format") or {}).get("duration") or 0)
            if duration < 30:
                failures.append(f"Video duration looks too short: {duration:.2f}s")
        except Exception as exc:
            failures.append(f"ffprobe failed: {exc}")

    repo = brief.get("repo", {})
    if brief.get("qa", {}).get("must_show_star_count") and ("stars" not in repo or repo.get("stars") is None):
        failures.append("Brief does not contain a GitHub Star count")

    pack_path = expected.get("publishing_pack")
    platform_safety_findings = scan_brief(brief, "brief public text")
    if pack_path and pack_path.exists():
        pack_text = pack_path.read_text(encoding="utf-8", errors="ignore")
        for required in ["抖音", "视频号", "小红书", "AI", "置顶评论"]:
            if required not in pack_text:
                failures.append(f"Publishing pack missing required section/text: {required}")
        if "High-Risk Wording Checklist" not in pack_text and "高风险" not in pack_text:
            failures.append("Publishing pack missing high-risk wording checklist")
        platform_safety_findings.extend(scan_text(pack_text, str(pack_path)))
    script_path = expected.get("script_handoff")
    if script_path and script_path.exists():
        script_text = script_path.read_text(encoding="utf-8", errors="ignore")
        if "可直接改写的正文" not in script_text:
            failures.append("Script handoff missing editable main section")
        if not script_text.strip():
            failures.append("Script handoff is empty")
    for raw_path in args.platform_text:
        platform_path = Path(raw_path)
        if not platform_path.exists():
            platform_safety_findings.append(
                {"label": str(platform_path), "risk": "missing file", "match": "", "snippet": "File does not exist"}
            )
            continue
        platform_safety_findings.extend(
            scan_text(platform_path.read_text(encoding="utf-8", errors="ignore"), str(platform_path))
        )
    for finding in platform_safety_findings:
        failures.append(
            f"Platform safety: {finding['risk']} in {finding['label']}: {finding['match']} ({finding['snippet']})"
        )

    production_gate_result = None
    if args.production_gate:
        production_gate_result = validate_production_gate(brief)
        failures.extend(production_gate_result["failures"])

    visual_manifest = args.visual_manifest or brief.get("visual_manifest", "")
    visual_manifest_result = None
    if visual_manifest:
        manifest_path = Path(visual_manifest)
        if not manifest_path.is_absolute():
            manifest_path = Path(args.brief).parent / manifest_path
        if not manifest_path.exists():
            failures.append(f"Missing visual manifest: {manifest_path}")
        else:
            visual_manifest_result = validate_manifest(json.loads(manifest_path.read_text(encoding="utf-8")))
            failures.extend(visual_manifest_result["failures"])

    result = {
        "ok": not failures,
        "slug": slug,
        "checked": {key: str(value) for key, value in expected.items()},
        "media": media,
        "production_gate": production_gate_result,
        "visual_manifest": visual_manifest_result,
        "platform_safety": platform_safety_payload(platform_safety_findings),
        "failures": failures,
        "manual_checks": [
            "Confirm subtitles are visible throughout the rendered video.",
            "Confirm highlights point to the exact target being discussed.",
            "Confirm title, opening, narration body, subtitle highlights, and publishing copy keep a funny-but-useful voice without unsupported claims.",
            "Confirm all three IP roles appear in meaningful contexts.",
            "Confirm no unrelated elements overlap screenshots, subtitles, Star badges, or IP characters.",
            "Confirm the video does not rely on fake human screencast signals such as decorative cursors, fake clicks, fake scrolling, or fake text selection.",
            "Confirm the video does not use anti-evasion copy containing `站外` or `引流`; use the platform's native AI label or the neutral label `AI 辅助创作` only when needed.",
            "Confirm cover, screenshots, narration, subtitles, and publishing copy contain no raw URL/domain, QR/contact details, third-party download/install directions, or comments/profile/private-message delivery language.",
            "Confirm public screenshot crops remove address bars, clone/download controls, package-install commands, QR codes, and unrelated outbound calls to action.",
            "Confirm platform publishing copy matches current platform policies and avoids unsafe claims.",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
