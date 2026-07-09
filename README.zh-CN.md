# GitHub Skill Video Maker

把 GitHub 项目、Codex/Claude/Cursor/Kimi Skill、插件、MCP 工具和开源 AI 项目，制作成适合短视频平台发布的竖屏讲解视频。

[English README](README.md)

这是一个 Codex Skill。它不是一个完整的视频 SaaS，也不是随机素材拼接工具，而是一套可复用的视频生产流程：先研究真实 GitHub 项目，再抓取真实截图，生成结构化 brief，制作低文字密度的案例讲解视频，并输出封面、字幕、预览图、QA 结果和平台发布文案。

## 它能产出什么

- `1080x1920`、`30fps`、约 `90s` 的竖屏 MP4
- 与视频统一风格的封面图
- 旁白文案和旁白音频
- 关键帧预览图/contact sheet
- 视觉 manifest，用来记录截图来源、红框目标、遮挡检查
- 抖音、视频号、小红书发布包：标题、正文、话题、置顶评论、AI 辅助声明和合规避坑

## 适合什么场景

- 给一个 GitHub 开源项目做短视频介绍
- 给一个 Codex/Claude/Cursor/Kimi Skill 做案例讲解
- 给插件、MCP 工具、AI 工作流做“真实流程”演示
- 需要统一封面、统一 IP 视觉、字幕、发布文案和 QA 检查的生产账号

## Skill 目录结构

```text
github-skill-video-maker/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── ip/
├── references/
│   ├── platform-publishing-pack.md
│   ├── production-checklist.md
│   └── video-brief-schema.md
└── scripts/
    ├── capture_github_screenshots.py
    ├── create_publishing_pack.py
    ├── create_video_brief.py
    ├── fetch_github_metadata.py
    ├── qa_check.py
    ├── validate_production_gate.py
    └── validate_visual_manifest.py
```

## 安装

把仓库克隆到 Codex 的 skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/MSNirvana/github-skill-video-maker.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/github-skill-video-maker"
```

然后重启 Codex，或重新加载 skills，让 `github-skill-video-maker` 被发现。

## 使用方式

在 Codex 里直接要求使用这个 Skill：

```text
Use $github-skill-video-maker to create a 90s vertical explainer video for obra/superpowers.
Target audience: AI users.
```

也可以用中文描述：

```text
用 $github-skill-video-maker 给 Norman-bury/research-writing-skill 做一个 90 秒竖屏介绍视频。
目标观众是正在使用 AI 的人群。
要求有真实 GitHub 截图、Star 数、字幕、统一封面、三个 IP 角色和抖音/视频号/小红书发布文案。
```

Codex 会按照 Skill 的流程去研究仓库、抓截图、生成 brief、制作视频包，并输出发布包。

## 推荐生产流程

这些脚本负责把信息结构化，最终视频的脚本、动效、节奏和包装仍由 Codex 根据项目来完成。

### 1. 抓取 GitHub 元数据

```bash
python3 scripts/fetch_github_metadata.py obra/superpowers \
  --output work/superpowers/metadata.json
```

如果 GitHub API 被限流，脚本会尝试使用 GitHub HTML 作为 fallback。生产时建议配置 `GITHUB_TOKEN`。

### 2. 抓取真实截图

```bash
python3 scripts/capture_github_screenshots.py obra/superpowers \
  --output-dir work/superpowers/screenshots \
  --paths README.md skills skills/test-driven-development/SKILL.md
```

Skill 要求截图必须服务于旁白，不允许使用无关截图、随机素材或乱画红框。

### 3. 生成视频 brief

```bash
python3 scripts/create_video_brief.py \
  --metadata work/superpowers/metadata.json \
  --screenshots work/superpowers/screenshots/screenshots-manifest.json \
  --output work/superpowers/video-brief.json \
  --output-prefix superpowers-case \
  --audience "AI users" \
  --duration 90 \
  --language zh-CN
```

brief 是后续脚本、旁白、截图、字幕、封面、QA 和发布包的统一源头。

### 4. 生成平台发布包

```bash
python3 scripts/create_publishing_pack.py \
  --brief work/superpowers/video-brief.json \
  --output outputs/superpowers-case-publishing-pack.md
```

发布包会覆盖抖音、视频号、小红书，包括标题备选、正文、话题、置顶评论、AI 辅助声明、来源说明和风险词提醒。

### 5. 最终 QA

```bash
python3 scripts/qa_check.py \
  --brief work/superpowers/video-brief.json \
  --outputs-dir outputs \
  --production-gate
```

QA 会检查视频、封面、旁白、预览图、发布包、production gate 和 visual manifest。它不能替代人工审片，但能把很多低级问题挡在交付前。

## 质量要求

这个 Skill 默认按生产账号标准约束视频：

- 必须展示真实 GitHub Star 数
- 必须有统一封面
- 必须有中文字幕
- 必须有真实或代表性的使用流程
- 红框、箭头、激光标记必须指向正在讲的具体目标
- 三个 IP 角色必须参与讲解，而不是装饰贴图
- 结尾必须有创作者签名，例如：`我是凸先生，专注 AI 全栈流程，我们下次再见！`
- 必须输出抖音、视频号、小红书发布文案和合规提示

## 依赖

脚本主要使用 Python 3 标准库，另外需要：

- Playwright：用于浏览器截图
- `ffmpeg` / `ffprobe`：用于媒体检查和预览图
- Remotion 或其他代码化视频渲染工具：用于最终视频合成

安装 Playwright：

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
```

## 发布与合规

平台发布包的目标不是“规避平台”，而是减少常见发布风险：

- AI 配音、AI 动画、声音克隆或合成角色，应按平台要求做 AI 辅助声明
- 不写夸大承诺、保证收益、学术代写、绕过审核、侵权搬运、破解等高风险表达
- GitHub Star 数、截图、功能状态等会变化的信息，应注明制作/截图时间
- 医疗、法律、金融、教育、资质、安全等敏感领域，需要写清边界，不替代专业判断

平台规则会变。发布前请重新确认抖音、视频号、小红书以及当地监管要求。

本仓库不提供法律意见。

## 开源协议

MIT License。详见 [LICENSE](LICENSE)。
