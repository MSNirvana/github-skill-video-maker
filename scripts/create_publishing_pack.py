#!/usr/bin/env python3
"""Generate a platform publishing pack for a finished GitHub Skill video."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def date_only(value: str) -> str:
    if not value:
        return ""
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return value[:10]


def main() -> int:
    parser = argparse.ArgumentParser(description="Create Douyin/WeChat Channels/Xiaohongshu publishing copy.")
    parser.add_argument("--brief", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--video", default="")
    parser.add_argument("--cover", default="")
    args = parser.parse_args()

    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    repo = brief.get("repo", {})
    full_name = repo.get("full_name", brief.get("slug", "GitHub Skill"))
    repo_url = repo.get("html_url", "")
    stars = repo.get("stars_label") or str(repo.get("stars") or "")
    captured = date_only(repo.get("captured_at") or (brief.get("publishing_pack") or {}).get("source_date_note", ""))
    cover_hook = brief.get("cover_hook") or brief.get("hook", {}).get("first_3_seconds") or full_name
    cta = brief.get("cta") or "关注凸先生，继续看 AI 全栈流程里的下一期 Skill。"
    why_watch = brief.get("why_watch") or "看一个开源 AI Skill 如何解决真实工作流问题。"
    signature = (brief.get("creator_signature") or {}).get("closing_line", "我是凸先生，专注 AI 全栈流程，我们下次再见！")
    disclosure = "本视频为 AI 辅助创作，含 AI 配音/动画包装；项目数据以制作时公开页面截图为准，不构成官方背书。"
    source_note = f"项目：{repo_url or full_name}。GitHub Star 数为制作时截图数据"
    if stars:
        source_note += f"：{stars}"
    if captured:
        source_note += f"（{captured}）"
    source_note += "。"

    douyin_title = f"{cover_hook}，先看这个 GitHub Skill"
    channels_title = f"{full_name}：一个 AI 写作流程案例"
    xhs_title = f"{cover_hook}｜GitHub Skill 案例"

    text = f"""# Publishing Pack

## Assets

- Video: `{args.video or '<final mp4>'}`
- Cover: `{args.cover or '<cover png>'}`
- Source: {repo_url or full_name}
- Star/date note: {source_note}

## Global Positioning

账号定位：凸先生，专注 AI 全栈流程。

内容边界：这是开源项目/Skill 案例解析，不是官方推荐，不承诺结果，不替代专业判断。

AI 辅助声明：{disclosure}

## 抖音

标题备选：

1. {douyin_title}
2. 别急着让 AI 输出，先让它守流程
3. 一个有 {stars or 'Star'} Stars 的 AI Skill，解决的不是“写”，是“管”

推荐标题：{douyin_title}

正文：

{why_watch}

它的重点不是替你完成结果，而是把任务拆成流程、记录和证据约束。

{source_note}

{disclosure}

{cta}

话题：#AI工具 #GitHub #AI工作流 #效率工具 #凸先生

置顶评论：

项目地址：{repo_url or full_name}
这不是代写/终稿工具，是流程管理和证据约束案例。下一期想看哪个 Skill？

合规提示：保留 AI 辅助说明；不要写“代写、保过、一键赚钱、绕过审核、官方推荐”等表达。

## 视频号

标题备选：

1. {channels_title}
2. AI 工具真正该补的，是流程和证据
3. 从 GitHub 项目看一个 AI 全栈流程案例

推荐标题：{channels_title}

正文：

这期拆的是 {full_name}。

我更关注它背后的工作流：先判断任务，再生成结构、记录进度、约束证据，而不是直接给一个看似完整的结果。

{source_note}

{disclosure}

{signature}

话题：#AI工具 #GitHub #AI工作流 #开源项目

置顶评论：

如果你也在搭 AI 工作流，可以先看它的流程设计。想看安装和实操，我下一期继续拆。

合规提示：避免“官方背书、保证效果、替代专业判断”等表达；外链无法直接点击时，把项目名放评论区。

## 小红书

标题备选：

1. {xhs_title}
2. AI 不要直接出结果，先给它加流程
3. 一个适合收藏的 GitHub Skill 工作流案例

推荐标题：{xhs_title}

正文：

今天记录一个 GitHub Skill 案例：{full_name}

我觉得它有价值的地方不是“更快生成”，而是：

- 先判断任务类型
- 再拆结构和进度
- 最后用证据约束输出

适合关注 AI 工作流、开源工具、自动化流程的人收藏参考。

{source_note}

{disclosure}

收藏起来，后面我继续拆 AI 全栈流程里的工具。

话题：#AI工具 #GitHub #AI工作流 #效率工具 #开源项目 #凸先生

置顶评论：

不是测评结论，也不是官方推荐；这是一个开源 Skill 的流程拆解。想看哪个项目可以留言。

合规提示：用“记录/案例/流程拆解”表达，不伪装真实使用收益，不写绝对化结论。

## High-Risk Wording Checklist

发布前删除或改写：代写论文、保过、包过、一键毕业、稳赚、一键赚钱、破解、绕过审核、规避风控、官方推荐、100%、无风险、全网第一、永久有效。
"""

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(json.dumps({"output": str(output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
