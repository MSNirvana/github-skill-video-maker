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


def title_pack(brief: dict, full_name: str, stars: str) -> dict[str, str]:
    cover_hook = brief.get("cover_hook") or brief.get("hook", {}).get("first_3_seconds") or full_name
    plain = (brief.get("beginner_clarity") or {}).get("plain_definition", "")
    lower_context = " ".join([full_name, cover_hook, plain]).lower()

    if "agent" in lower_context or "agents" in lower_context:
        meme = "“一人公司”？一个 Skill “全家桶”全搞定！"
        contrast = "别让一个 AI 演完整家公司"
        practical = "把 AI 助手拆成一支专家团队"
        body_hook = "你可以把它理解成 AI 的“岗位表”：谁写前端，谁审代码，谁做文档，先把队伍排明白。"
        body_value = "以前是一个助手硬着头皮打全场，现在是前端、测试、安全、文档各回各工位。"
        boundary = "所谓“全家桶”，不是一键替你干完所有活，而是把常用角色、流程和安装方式打包好。"
    elif "writing" in lower_context or "writer" in lower_context or "写作" in lower_context:
        meme = "别让 AI 上来就开写，先把证据摆桌上"
        contrast = "不是写得慢，是流程太野"
        practical = "用 Skill 把写作流程先管起来"
        body_hook = "这类 Skill 更像给 AI 写作装了个“刹车片”：先看证据，再动笔。"
        body_value = "不是让 AI 一路狂飙到终稿，而是把选题、证据、结构和修改顺序摆清楚。"
        boundary = "这里不是代写终稿，而是把选题、证据、结构和修改流程管清楚。"
    elif "frontend" in lower_context or "design" in lower_context or "前端" in lower_context:
        meme = "别让 AI 把页面做成精神小伙装修"
        contrast = "不是不会写代码，是没人管设计边界"
        practical = "用 Skill 约束前端设计流程"
        body_hook = "它像给 AI 前端装了个“审美红绿灯”：哪里能放飞，哪里先刹车。"
        body_value = "重点不是让页面更花，而是把布局、组件、颜色和交付边界管住。"
        boundary = "这里不是保证一键出神图，而是把视觉规则、组件边界和交付步骤说清楚。"
    else:
        meme = f"{cover_hook}，这不比硬背提示词香？"
        contrast = "不是工具不行，是流程没人管"
        practical = f"{cover_hook}｜GitHub Skill 案例"
        body_hook = "你可以把它当成一个“流程外挂”：不是替你乱冲，而是先把步骤排好。"
        body_value = "我看的不是它名字多酷，而是它有没有真实截图、规则、命令和可落地路径。"
        boundary = "这里不是承诺一键完成所有结果，而是拆解一个开源项目的真实流程和边界。"

    star_title = f"{stars} Stars 的项目，先别急着收藏" if stars else "这个 GitHub 项目，先别急着收藏"
    return {
        "meme": meme,
        "contrast": contrast,
        "practical": practical,
        "star": star_title,
        "recommended": meme,
        "body_hook": body_hook,
        "body_value": body_value,
        "boundary": boundary,
    }


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
    titles = title_pack(brief, full_name, stars)
    source_note = f"项目：{repo_url or full_name}。GitHub Star 数为制作时截图数据"
    if stars:
        source_note += f"：{stars}"
    if captured:
        source_note += f"（{captured}）"
    source_note += "。"

    douyin_title = titles["recommended"]
    channels_title = titles["contrast"]
    xhs_title = titles["practical"]

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
2. {titles["contrast"]}
3. {titles["star"]}

推荐标题：{douyin_title}

正文：

{titles["meme"]}

{titles["body_hook"]}

{titles["body_value"]}

{titles["boundary"]}

这条视频就干一件事：不念 README，直接看它到底把 AI 工作流“管”在哪。

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
2. {titles["meme"]}
3. {titles["practical"]}

推荐标题：{channels_title}

正文：

这期拆的是 {full_name}。

{titles["body_hook"]}

{titles["boundary"]}

我更关注它背后的工作流：别让 AI 上来就冲，先把角色、步骤、证据和边界安排明白。

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
2. {titles["meme"]}
3. {titles["contrast"]}

推荐标题：{xhs_title}

正文：

今天记录一个 GitHub Skill 案例：{full_name}

{titles["body_hook"]}

{titles["boundary"]}

我觉得它有价值的地方，不是喊一句“效率起飞”，而是：

- 先判断任务类型，别让 AI 开局乱跑
- 再拆结构和进度，把活排进“工位”
- 最后用证据约束输出，少一点玄学，多一点流程

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
