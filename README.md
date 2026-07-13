# GitHub Skill Video Maker

[中文说明](README.zh-CN.md)

Create branded vertical explainer videos for GitHub repositories, Codex/Claude/Cursor/Kimi Skills, plugins, MCP tools, and open-source AI projects.

This repository is a Codex Skill. It packages a repeatable production workflow for short-form vertical videos: live GitHub research, real screenshots, Star-count proof, storyboard briefs, subtitles, animated IP roles, unified covers, evidence-based visual packaging, QA checks, and platform-ready publishing copy for Douyin, WeChat Channels, and Xiaohongshu.

## What It Produces

- `1080x1920`, `30fps`, about `90s` vertical MP4
- Cover image using the same visual system
- Optional image2 key art for covers, first frames, chapter posters, and branded end cards
- Narration script and narration audio
- Meme-style, contrast-style, and practical title candidates, with narration/body copy that keeps the same funny-but-useful voice
- Strict in-platform distribution: public video/copy omits URLs, QR/contact details, third-party action directions, and comment/profile/private-message delivery language
- Preview sheet/contact sheet
- Visual manifest for screenshot and highlight verification
- Image2 key-art manifest records prompts, intended use, text verification, and evidence boundaries
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
│   ├── image2-key-art.md
│   ├── platform-publishing-pack.md
│   ├── platform-risk-guardrails.md
│   ├── production-checklist.md
│   └── video-brief-schema.md
└── scripts/
    ├── capture_github_screenshots.py
    ├── create_publishing_pack.py
    ├── create_video_brief.py
    ├── fetch_github_metadata.py
    ├── qa_check.py
    ├── validate_platform_safety.py
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

The skill does not fake human screencasts. Decorative cursors, fake clicks, fake scrolling, and fake text selection should be omitted unless they come from real recorded interaction or serve a concrete evidence-pointing purpose.

Titles, narration, body copy, and subtitles should be funny or surprising enough to earn attention, but they must be grounded by real evidence such as screenshots, Star counts, files, commands, or workflow artifacts. Use quoted playful phrases such as `“全家桶”` or `“一人公司”` when the phrase is entertainment framing rather than a literal guarantee.

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

python3 scripts/validate_platform_safety.py \
  --brief work/superpowers/video-brief.json \
  --text outputs/superpowers-case-narration.txt \
  --text outputs/superpowers-case-subtitles.srt \
  --text outputs/superpowers-case-publishing-pack.md
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
- Keep source URLs in internal metadata. Public video, cover, captions, and pinned comments use project identity and dated evidence without outbound addresses or acquisition instructions.
- Crop public screenshots to remove address bars, QR/contact details, clone/download controls, package-install commands, and unrelated outbound calls to action.
- Keep CTAs inside the platform: save, follow, comment on the topic, forward, or watch the next episode.
- Recheck official platform rules before publishing policy-sensitive content.

This repository does not provide legal advice.

## License

MIT License. See [LICENSE](LICENSE).
