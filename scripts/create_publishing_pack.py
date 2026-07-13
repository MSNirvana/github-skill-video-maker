#!/usr/bin/env python3
"""Generate strict in-platform publishing copy for a GitHub Skill video."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from platform_safety import scan_text


def date_only(value: str) -> str:
    if not value:
        return ""
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return value[:10]


def safe(value: str, fallback: str) -> str:
    value = str(value or "").strip()
    return value if value and not scan_text(value) else fallback


def safe_list(values: list[str], fallbacks: list[str]) -> list[str]:
    result = [str(item).strip() for item in values if str(item).strip() and not scan_text(str(item))]
    for fallback in fallbacks:
        if len(result) >= 3:
            break
        if fallback not in result:
            result.append(fallback)
    return result[:3]


def main() -> int:
    parser = argparse.ArgumentParser(description="Create strict in-platform copy for Douyin/WeChat Channels/Xiaohongshu.")
    parser.add_argument("--brief", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--video", default="")
    parser.add_argument("--cover", default="")
    args = parser.parse_args()

    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    repo = brief.get("repo", {}) or {}
    full_name = repo.get("full_name") or brief.get("slug", "开源 Skill")
    stars = repo.get("stars_label") or str(repo.get("stars") or "")
    captured = date_only(repo.get("captured_at") or repo.get("capture_date") or (brief.get("publishing_pack") or {}).get("source_date_note", ""))
    viral = brief.get("viral_packaging", {}) or {}
    beginner = brief.get("beginner_clarity", {}) or {}

    practical_fallback = safe(brief.get("cover_hook", ""), f"{full_name}：把 AI 工作流讲清楚")
    meme_fallback = f"别让 AI 硬着头皮乱冲：{full_name} 到底管了什么？"
    contrast_fallback = "不是模型不够强，是工作流还没说清楚"

    meme_titles = safe_list(viral.get("meme_titles", []) or [], [meme_fallback, "AI 又开始自由发挥？先看看这个流程", "一个 Skill，怎么把 AI 从临时工变成流程工？"])
    contrast_titles = safe_list(viral.get("contrast_titles", []) or [], [contrast_fallback, "看起来是工具，真正值钱的是流程", "功能很多不稀奇，边界写清楚才稀奇"])
    practical_titles = safe_list(viral.get("practical_titles", []) or [], [practical_fallback, f"{full_name} 的核心流程与边界", "把开源 Skill 放进真实 AI 工作流"])

    recommended = safe(viral.get("recommended_title", ""), meme_titles[0])
    opening = safe(viral.get("opening_line", ""), safe((brief.get("hook") or {}).get("first_3_seconds", ""), meme_titles[0]))
    plain = safe(beginner.get("plain_definition", ""), "它把一套 AI 工作方法整理成可以重复调用的流程。")
    value = safe(brief.get("why_watch", ""), "看完能判断它解决什么问题、流程怎么走，以及什么情况下不适合用。")
    boundary = safe(viral.get("boundary_clarifier", ""), "它不是结果保证，而是一套开源流程案例；具体效果取决于任务、资料和执行质量。")
    source_note = f"资料来源：公开仓库 {full_name}"
    if stars:
        source_note += f"；Star 数为制作时截图数据：{stars}"
    if captured:
        source_note += f"（{captured}）"
    source_note += "。"

    disclosure = "本视频为 AI 辅助创作，含 AI 配音和动画包装；公开数据以制作时页面截图为准，不构成官方背书。"
    cta = "收藏这条视频，关注下一期；你更想看哪个流程环节，欢迎在评论里讨论。"
    signature = safe((brief.get("creator_signature") or {}).get("closing_line", ""), "我是凸先生，专注 AI 全栈流程，我们下次再见！")

    beats = [safe(str(item), "") for item in beginner.get("so_what_beats", []) or []]
    beats = [item for item in beats if item][:3]
    while len(beats) < 3:
        beats.append(["先讲清楚它解决什么问题", "再看真实流程和证据", "最后判断适用边界"][len(beats)])

    text = f"""# Publishing Pack

## 素材信息

- Video: `{args.video or '<final mp4>'}`
- Cover: `{args.cover or '<cover png>'}`
- Source project: {full_name}
- Source/date note: {source_note}
- Distribution mode: strict_platform_safe

## 全局定位

账号定位：凸先生，专注 AI 全栈流程。

内容边界：这是开源项目/Skill 案例解析，不是官方推荐，不承诺结果，不替代专业判断。

AI 辅助声明：{disclosure}

## 抖音

标题备选：

1. {recommended}
2. {contrast_titles[0]}
3. {practical_titles[0]}

推荐标题：{recommended}

正文：

{opening}

{plain}

{value}

{boundary}

{source_note}

{disclosure}

{cta}

话题：#AI工具 #AI工作流 #开源项目 #效率工具 #凸先生

置顶评论：

普通介绍只讲功能，这期更想讲清楚流程和边界。你觉得最值得展开的是哪一步？

合规提示：仅保留收藏、关注、评论、转发等平台内动作；来源只写项目名和制作日期。

## 视频号

标题备选：

1. {contrast_titles[0]}
2. {meme_titles[0]}
3. {practical_titles[1]}

推荐标题：{contrast_titles[0]}

正文：

这期拆的是 {full_name}。

{plain}

我更关注它背后的工作流：做什么、怎么推进、证据在哪里、边界怎么判断。

{boundary}

{source_note}

{disclosure}

{signature}

话题：#AI工具 #AI工作流 #开源项目 #全栈流程

置顶评论：

如果你也在搭 AI 工作流，最容易失控的是哪一步？欢迎把问题留在评论里。

合规提示：发布内容保持平台内闭环，不提供跨平台导向信息或第三方操作指令。

## 小红书

标题备选：

1. {practical_titles[0]}
2. {meme_titles[1]}
3. {contrast_titles[1]}

推荐标题：{practical_titles[0]}

正文：

今天记录一个开源 Skill 案例：{full_name}

{plain}

我觉得最值得看的不是功能数量，而是这三件事：

- {beats[0]}
- {beats[1]}
- {beats[2]}

{boundary}

{source_note}

{disclosure}

收藏这条笔记，后面继续拆 AI 全栈流程里的真实案例。你最想看哪个环节？

话题：#AI工具 #AI工作流 #开源项目 #效率工具 #凸先生

置顶评论：

不是测评结论，也不是官方推荐；这里只讨论公开项目的流程设计和使用边界。

合规提示：仅保留平台内互动，不提供跨平台导向信息或第三方操作指令。

## 高风险检查

发布版本应保持平台内闭环：不出现跨平台导向信息、联系方式或第三方操作指令；公开来源只保留项目名、数据口径和制作日期。
"""

    findings = scan_text(text, "generated publishing pack")
    if findings:
        raise RuntimeError(f"Generated publishing pack failed platform safety scan: {findings}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(json.dumps({"output": str(output), "platform_safety": "passed"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
