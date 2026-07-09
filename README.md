# GitHub Skill Video Maker

Create branded vertical explainer videos for GitHub repositories, Codex/Claude/Cursor/Kimi Skills, plugins, MCP tools, and open-source AI projects.

This repository is a Codex Skill. It packages a repeatable production workflow for short-form vertical videos: live GitHub research, real screenshots, Star-count proof, storyboard briefs, subtitles, animated IP roles, unified covers, QA checks, and platform-ready publishing copy for Douyin, WeChat Channels, and Xiaohongshu.

## What It Produces

- `1080x1920`, `30fps`, about `90s` vertical MP4
- Cover image using the same visual system
- Narration script and narration audio
- Preview sheet/contact sheet
- Visual manifest for screenshot and highlight verification
- Platform publishing pack with titles, captions, topics, pinned comments, AI disclosure, and compliance notes

## Skill Layout

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

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/MSNirvana/github-skill-video-maker.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/github-skill-video-maker"
```

Restart Codex or reload your skills so `github-skill-video-maker` is discovered.

## Usage

Ask Codex to use the skill on a GitHub repository:

```text
Use $github-skill-video-maker to create a 90s vertical explainer video for obra/superpowers.
Target audience: AI users.
```

The skill will guide Codex to research the repository, capture real screenshots, create a structured brief, render a video package, and generate a platform publishing pack.

## Scripted Pipeline

The bundled scripts are intentionally conservative. They create structured inputs and validation outputs; Codex still makes creative choices about script, motion, visual rhythm, and final packaging.

```bash
python3 scripts/fetch_github_metadata.py obra/superpowers \
  --output work/superpowers/metadata.json

python3 scripts/capture_github_screenshots.py obra/superpowers \
  --output-dir work/superpowers/screenshots \
  --paths README.md skills skills/test-driven-development/SKILL.md

python3 scripts/create_video_brief.py \
  --metadata work/superpowers/metadata.json \
  --screenshots work/superpowers/screenshots/screenshots-manifest.json \
  --output work/superpowers/video-brief.json \
  --output-prefix superpowers-case \
  --audience "AI users" \
  --duration 90 \
  --language zh-CN

python3 scripts/create_publishing_pack.py \
  --brief work/superpowers/video-brief.json \
  --output outputs/superpowers-case-publishing-pack.md
```

After rendering, run QA:

```bash
python3 scripts/qa_check.py \
  --brief work/superpowers/video-brief.json \
  --outputs-dir outputs \
  --production-gate
```

## Dependencies

The scripts use Python 3 standard libraries plus:

- Playwright for browser screenshot capture
- `ffprobe`/`ffmpeg` for media QA and preview sheets
- Remotion or another code-driven renderer for final video composition

Install Playwright browsers when using the screenshot script:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
```

## Publishing And Compliance

The generated publishing pack is designed to reduce common short-video publishing risk:

- Mark AI-assisted creation when relevant.
- Avoid exaggerated claims, guaranteed outcomes, academic ghostwriting, platform evasion, copyright misuse, and illegal-access language.
- Include source and capture-date notes for GitHub Star counts and other time-sensitive claims.
- Recheck official platform rules before publishing policy-sensitive content.

This repository does not provide legal advice.

## License

MIT License. See [LICENSE](LICENSE).
