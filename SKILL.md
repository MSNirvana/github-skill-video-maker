---
name: github-skill-video-maker
description: Create branded vertical explainer videos for GitHub repositories, Codex/Claude/Cursor/Kimi Skills, plugins, MCP tools, and open-source AI projects using a scriptable production pipeline. Use when the user asks to make or revise a video that introduces a GitHub project or Skill, especially when requirements include real screenshots, GitHub Star counts, structured video briefs/storyboards, subtitles, animated IP characters, unified covers, Remotion packaging, Doubao narration, QA checks, social-video style case walkthroughs, or platform-ready publishing copy for Douyin/WeChat Channels/Xiaohongshu.
---

# GitHub Skill Video Maker

## Output Standard

Create a polished vertical explainer video that feels like a real case walkthrough, not a text-heavy slide deck.

Default output:

- `1080x1920`, `30fps`, about `90s`, H.264 MP4 with AAC audio
- A separate cover image using the same visual system
- Narration script and generated narration audio
- Preview sheet of key frames
- A platform publishing pack for Douyin, WeChat Channels, and Xiaohongshu
- All user-facing deliverables saved in the thread `outputs/` directory

## Required Workflow

1. Research the source.
   - Use the GitHub repository, README, docs, release notes, plugin manifests, and important Skill files.
   - Verify unstable facts from the live web, especially GitHub Star count, current repo state, supported platforms, and install commands.
   - Record the source URL and the capture date in working notes or metadata when practical.

2. Capture real screenshots.
   - Include the GitHub repo page with the visible Star count.
   - Capture pages that are actually discussed: README sections, skills directory, selected `SKILL.md`, plugin config, install docs, or real command output.
   - Do not use unrelated screenshots, stock video, or arbitrary background footage.
   - For every screenshot or crop that reaches the final edit, record `scene_id`, `source_url_or_path`, `narration_claim`, `target_region`, and `why_this_screenshot` in a visual manifest.
   - If the key text or UI target is unreadable in vertical video, create a tighter crop or redraw it as a readable evidence card; do not keep the unreadable screenshot as filler.

3. Write a low-text case script.
   - Use this structure unless the user gives a better one: pain point -> project identity -> real workflow -> key capabilities -> install/support -> boundary -> value.
   - Avoid on-screen paragraphs. On-screen text should be short labels or emphasis words.
   - Use narration for explanation, visuals for evidence.
   - For Skill videos, include at least one real or representative usage flow: user prompt/input -> Skill routing/action -> generated or expected artifacts -> value. Do not rely only on repo browsing.
   - Before rendering, define a production gate in the brief: `hook`, `why_watch`, `real_case_flow`, `proof_moment`, `cover_hook`, `cta`, and `creator_signature`.
   - The final 3-6 seconds must include a recognizable creator signature: who is speaking, what the account focuses on, and a closing line. For this user's series, default to: `我是凸先生，专注 AI 全栈流程，我们下次再见！`
   - Do not proceed to final render if the script has no strong first-3-second hook, no real case flow, no proof moment, no CTA, or no creator signature.

4. Build the video.
   - Use Remotion or an equivalent code-driven renderer for predictable motion.
   - Use screenshots as the primary visual material.
   - Use zoom, pan, crop, spotlight masks, callout arrows, and red boxes only on exact areas being discussed.
   - Never “randomly circle” UI. If the highlighted area is not semantically correct, remove or reposition it.
   - Bind every red box, underline, arrow, or laser mark to an explicit target: text phrase, UI control, file path, command, Star count, or generated artifact. Broad panel highlights are allowed only when the narration names the whole panel.
   - Verify highlights against exported frames or a preview sheet, not only against the source screenshot.
   - Reserve stable zones for header/title, evidence screenshots, subtitles, IP characters, Star badges, and callouts. Do not let decorative or unrelated elements overlap evidence, subtitles, or each other.

5. Add subtitles.
   - Every final video must include readable Chinese subtitles, synchronized by scene or narration chunks.
   - Keep subtitle lines short enough to read on mobile.
   - Place subtitles in a consistent lower safe area and avoid covering core screenshots or IP characters.

6. Integrate the IP.
   - Use all three bundled IP roles when the video is long enough:
     - `head`: insight, pain point, warning, conclusion
     - `route`: workflow, connection, process, platform support
     - `key`: install, access, unlock, API/key concepts
   - Animate IP characters with motion-design techniques: entrance, bobbing, tilt, glow pulse, route drawing, unlock ring, or pointing/callout behavior.
   - IP must participate in the explanation, not sit as decoration.

7. Create a unified cover.
   - Same IP theme, same colors, same title treatment, same repo/Star signal.
   - Cover should work as the first-frame visual language for a series.
   - Export it as a separate image in `outputs/`.

8. Create a platform publishing pack.
   - Generate `outputs/<project>-publishing-pack.md` for Douyin, WeChat Channels, and Xiaohongshu.
   - Include title options, body copy, hashtags/topics, pinned comment, AI-assisted disclosure text, source/date note, and platform-specific compliance notes.
   - Avoid claims that imply guaranteed results, academic ghostwriting, platform evasion, bypassing review, copyright misuse, or illegal access.
   - For AI-assisted videos, include a clear AI-assisted creation note when the platform or content context calls for it.
   - For GitHub claims, include the capture date for Star counts and avoid treating open-source popularity as product endorsement.
   - Read `references/platform-publishing-pack.md` when preparing platform copy or policy notes.

9. Validate before delivery.
   - Run media checks with `ffprobe`.
   - Export a preview sheet from the final MP4.
   - Inspect key frames for text density, wrong highlights, missing Star count, missing subtitles, IP overlap, platform-safe subtitle placement, and unrelated element occlusion.
   - Confirm the platform publishing pack exists and avoids high-risk wording for the target platforms.
   - Run visual-manifest validation when a manifest is produced:

```bash
python3 <skill>/scripts/validate_visual_manifest.py work/<slug>/visual-manifest.json
```
   - Run production-gate validation before delivery:

```bash
python3 <skill>/scripts/validate_production_gate.py work/<slug>/video-brief.json
```

## Scripted Production Path

Prefer this repeatable pipeline before writing custom Remotion code:

1. Fetch structured GitHub metadata:

```bash
python3 <skill>/scripts/fetch_github_metadata.py obra/superpowers \
  --output work/<slug>/metadata.json
```

Set `GITHUB_TOKEN` when available to avoid GitHub API rate limits. If the API is limited, the script falls back to GitHub HTML and marks `source` as `GitHub HTML fallback`; use that output for production but treat missing secondary fields such as license or releases as unknown.

2. Capture real GitHub screenshots and stable crops:

```bash
python3 <skill>/scripts/capture_github_screenshots.py obra/superpowers \
  --output-dir work/<slug>/screenshots \
  --branch "$(python3 -c 'import json; print(json.load(open("work/<slug>/metadata.json")).get("default_branch","main"))')" \
  --paths skills skills/test-driven-development/SKILL.md .codex-plugin/plugin.json
```

3. Create a structured brief/storyboard:

```bash
python3 <skill>/scripts/create_video_brief.py \
  --metadata work/<slug>/metadata.json \
  --screenshots work/<slug>/screenshots/screenshots-manifest.json \
  --output work/<slug>/video-brief.json \
  --output-prefix <project>-case \
  --audience "AI users" \
  --duration 90 \
  --language zh-CN
```

4. Use `video-brief.json` as the source of truth for script writing, screenshot selection, subtitle chunks, IP roles, cover content, and render outputs.

5. After rendering, run QA:

```bash
python3 <skill>/scripts/qa_check.py \
  --brief work/<slug>/video-brief.json \
  --outputs-dir outputs
```

If final filenames differ from the brief, pass explicit paths such as `--video outputs/superpowers-case-v2-90s-vertical.mp4 --cover outputs/superpowers-case-v2-cover.png`.

6. Generate the platform publishing pack:

```bash
python3 <skill>/scripts/create_publishing_pack.py \
  --brief work/<slug>/video-brief.json \
  --output outputs/<project>-publishing-pack.md
```

The scripts are intentionally conservative. They produce metadata, screenshots, crops, brief/storyboard JSON, production-gate checks, visual-manifest checks, and QA reports; the agent still chooses the final edit, exact captions, and visual rhythm.

## Visual System

Use the bundled IP assets in `assets/ip/`:

- `xiao-g-laser-head-cutout.png`
- `xiao-g-laser-route-cutout.png`
- `xiao-g-laser-key-cutout.png`
- `xiao-g-ip-guide.png`

Theme:

- White or very light background
- Black text and linework
- Red laser/infinity-eye as the primary brand color
- Blue only for structure/flow
- Orange only for energy, unlocking, or accent dots

Avoid large gradients, stock backgrounds, unreadable screenshots, too many labels, and dense paragraph text.

## Quality Gate

Before final response, confirm these are true:

- GitHub Star count is visible at least once.
- The cover image includes the repo/project name and Star signal.
- Subtitles exist throughout the final video.
- Every highlight points to the correct UI element or code section.
- The three IP forms appear and move in meaningful roles.
- The first 3 seconds contain a concrete hook, not a generic topic label.
- The video includes a real or representative usage flow and at least one readable evidence card.
- The final seconds include the creator signature/account positioning and a clear closing line.
- The platform publishing pack includes Douyin, WeChat Channels, and Xiaohongshu copy plus compliance notes.
- The output video, cover, narration text, narration audio, preview sheet, and publishing pack are in `outputs/`.

For detailed production notes, read `references/production-checklist.md`.

For the structured JSON format, read `references/video-brief-schema.md`.

For platform copy and compliance notes, read `references/platform-publishing-pack.md`.
