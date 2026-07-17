#!/usr/bin/env python3
"""Create a clean, editable narration handoff from a production script."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _brief_value(brief: dict, *keys: str, default: str = "") -> str:
    value = brief
    for key in keys:
        if not isinstance(value, dict):
            return default
        value = value.get(key)
    return str(value) if value not in (None, "") else default


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a rewrite-ready script handoff Markdown file.")
    parser.add_argument("--narration-text", required=True, help="Final narration text, one spoken segment per line")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument("--brief", default="", help="Optional video brief JSON for project facts and title")
    args = parser.parse_args()

    narration_path = Path(args.narration_text)
    lines = [line.strip() for line in narration_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        raise SystemExit("narration text is empty")

    brief: dict = {}
    if args.brief:
        brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))

    project = _brief_value(brief, "repo", "full_name", default=_brief_value(brief, "slug", default="视频项目"))
    title = _brief_value(brief, "viral_packaging", "recommended_title", default="")
    capture_date = _brief_value(brief, "repo", "captured_at", default="")
    core_angle = _brief_value(brief, "script_strategy", "core_angle", default="")
    boundary = _brief_value(brief, "script_strategy", "micro_story", "boundary", default="")

    paragraphs = "\n\n".join(lines)
    numbered = "\n".join(f"{index}. {line}" for index, line in enumerate(lines, start=1))
    sections = [
        f"# {project} 视频文字稿",
        "",
        "> 这是可继续改写的旁白底稿，不含字幕时间码。改稿后请重新生成最终旁白音频，并以新音频重新对齐字幕。",
        "",
        "## 项目信息",
        "",
        f"- 项目：`{project}`",
        f"- 制作/截图日期：`{capture_date}`" if capture_date else "- 制作/截图日期：未填写",
        f"- 推荐标题：{title}" if title else "- 推荐标题：待填写",
        f"- 核心角度：{core_angle}" if core_angle else "- 核心角度：待填写",
        "",
        "## 可直接改写的正文",
        "",
        paragraphs,
        "",
        "## 原始分段",
        "",
        numbered,
        "",
        "## 改稿时保留",
        "",
        "- 先保留项目真实功能、截图证据和 Star 数，再调整语气、节奏和比喻。",
        f"- 当前边界：{boundary}" if boundary else "- 当前边界：保留项目能力边界，避免把示例输出写成结果承诺。",
        "- 改稿完成后，重新生成旁白、逐行字幕和平台发布文案，并再次执行平台安全扫描。",
        "",
    ]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(sections), encoding="utf-8")
    print(json.dumps({"output": str(output), "project": project, "line_count": len(lines)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
