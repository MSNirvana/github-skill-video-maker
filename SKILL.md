---
name: github-skill-video-maker
description: Create branded vertical explainer videos for GitHub repositories, Codex/Claude/Cursor/Kimi Skills, plugins, MCP tools, and open-source AI projects using a scriptable production pipeline. Use when the user asks to make or revise a video that introduces a GitHub project or Skill, especially when requirements include real screenshots, GitHub Star counts, structured video briefs/storyboards, subtitles, animated IP characters, unified covers, Remotion packaging, Doubao narration, QA checks, evidence-based visual explainers, or platform-ready publishing copy for Douyin/WeChat Channels/Xiaohongshu.
---

# GitHub Skill Video Maker

## Output Standard

Create a polished vertical explainer video that feels like a clear evidence-based explanation, not a text-heavy slide deck or a fake human screencast.

Production output:

- `1080x1920`, `30fps`, about `90s`, H.264 MP4 with AAC audio
- A separate cover image using the same visual system when needed for QA, first-frame design, or an explicitly requested cover export
- Optional `image2` key-art assets for production-grade covers, first frames, chapter openers, and branded end cards
- Narration script and generated narration audio
- Dual-layer Chinese subtitles: a short on-screen insight label plus complete line-by-line narration subtitles
- Strict in-platform distribution by default: no public URLs, QR codes, account/contact handles, third-party download or installation directions, or language that sends viewers to comments, profiles, private messages, websites, apps, or mini programs
- Preview sheet of key frames
- A platform publishing pack for Douyin, WeChat Channels, and Xiaohongshu
- Internal production files may include cover images, preview sheets, narration text/audio, subtitle files, briefs, visual manifests, QA reports, screenshots, and Remotion source. Keep these in `work/` or `outputs/` for rebuild and QA, but do not treat them as final desktop deliverables unless the user explicitly asks.
- Final desktop delivery defaults to only two files: the final `.mp4` video and the platform publishing pack `.md`.
- When archiving final deliverables for this user's production account, copy only those two files to `/Users/gaoyunhong/Desktop/凸先生/视频素材/<YYYYMMDD> <SkillName>`; use the Skill/project name after the date, for example `20260710 Claude-video`, and do not add daily sequence numbers.

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
   - Keep factual evidence real. Do not use image generation to fabricate GitHub pages, Star counts, repository UI, command output, benchmark results, or product screenshots.
   - Keep the original screenshot internally for evidence, then create a distribution-safe crop for the final edit. The public crop must omit browser addresses, raw URLs, QR codes, contact details, clone/download/install controls, and unrelated third-party calls to action. Preserve the project name, Star count, and exact evidence being discussed.

3. Write a low-text case script.
   - Use this structure unless the user gives a better one: pain point -> project identity -> real workflow -> key capabilities -> compatibility/boundary -> value.
   - Read `references/script-writing-methodology.md` before writing narration, cover hooks, insight subtitles, or publishing copy.
   - Read `references/platform-risk-guardrails.md` before writing any narration, subtitle, CTA, cover, screenshot title, or publishing copy intended for Douyin, WeChat Channels, or Xiaohongshu.
   - Define a `script_strategy` in the brief before drafting: `core_angle`, `viewer_doubt`, `plain_answer`, `hkr_score`, `micro_story`, `human_voice_rules`, `anti_ai_fluff_scan`, and `escalation_beats`.
   - Treat the repo as evidence for a human problem. Do not write a README summary or a feature list unless the viewer pain and workflow value are already clear.
   - Use a compact story arc: challenge -> evidence -> process -> result -> boundary -> signature.
   - Add a beginner clarity gate before writing the final script: the first 10 seconds must answer `what is it`, `who is it for`, and `what pain does it solve` in plain language.
   - Translate every first-use technical term into a simple user benefit. For example, explain `spec` as `先把需求说清楚`, not only as a command name.
   - Prefer before/after framing over feature lists: `before: agent writes directly` -> `after: agent follows spec, plan, test, review`.
   - Every 15 seconds, include a plain `so what` moment that tells the viewer why the capability matters.
   - Run an anti-AI-fluff pass before recording TTS. Remove generic openings, report-style transitions, unsupported hype, abstract efficiency claims, and empty tool labels.
   - Avoid on-screen paragraphs. On-screen text should be short labels or emphasis words.
   - Use narration for explanation, visuals for evidence.
   - For Skill videos, include at least one real or representative usage flow: user prompt/input -> Skill routing/action -> generated or expected artifacts -> value. Do not rely only on repo browsing.
   - Before finalizing the cover title, first-frame title, opening line, narration body, subtitle highlights, or platform copy, create a punchy packaging layer: at least 3 `玩梗标题`, 3 `反差标题`, and 3 `干货标题`. Prefer funny, meme-friendly hooks that remain true and are quickly grounded by evidence. Avoid stiff titles like `某某项目案例` unless used only as a fallback.
   - Carry the same `谈笑中讲干货` voice through the whole script, not only the title. Use quoted playful phrases such as `“全家桶”`, `“一人公司”`, `“AI 部门”`, or `“岗位表”` to signal entertainment framing, then explain the real workflow value with evidence.
   - Before rendering, define a production gate in the brief: `hook`, `why_watch`, `real_case_flow`, `proof_moment`, `cover_hook`, `cta`, and `creator_signature`.
   - The final 3-6 seconds must include a recognizable creator signature: who is speaking, what the account focuses on, and a closing line. For this user's series, default to: `我是凸先生，专注 AI 全栈流程，我们下次再见！`
   - Do not proceed to final render if the script has no strong first-3-second hook, no real case flow, no proof moment, no CTA, or no creator signature.
   - Keep the CTA entirely in-platform: follow, save this video, comment on the topic, or watch the next episode. Do not tell viewers where to obtain the project, how to leave the platform, or how to install/download/use third-party software.

4. Build the video.
   - Use Remotion or an equivalent code-driven renderer for predictable motion.
   - Use screenshots as the primary visual material.
   - Do not simulate a human screencast with decorative mouse cursors, fake scrolling, fake clicks, or fake text selection. Use stable screenshot crops, evidence cards, zooms, pans, and precise highlights instead. If a cursor appears, it must either come from real recorded interaction or perform a concrete, semantically correct pointing action; otherwise omit it.
   - Use zoom, pan, crop, spotlight masks, callout arrows, and red boxes only on exact areas being discussed.
   - Never “randomly circle” UI. If the highlighted area is not semantically correct, remove or reposition it.
   - If you cannot clearly decide exactly where a line, circle, box, underline, or laser mark should go, do not draw it. Keep the screenshot clean, or replace the explanation with a readable evidence card. A pure screenshot is always better than a decorative or uncertain mark.
   - Do not add markings just to make a screenshot look more dynamic. Every mark must answer: `what exact text/control/row is this`, `why is it named in narration`, and `how was the rendered position verified`.
   - Bind every red box, red circle, underline, arrow, or laser mark to an explicit target: exact text phrase, UI control, file path, command, Star count, table row, or generated artifact. Broad panel highlights are allowed only when the narration names the whole panel.
   - Do not place a highlight by visual guesswork after scaling or cropping. Define the target in a known coordinate space, such as `source_crop_pixels`, `rendered_frame_pixels`, or `normalized_frame`.
   - For every final highlight, record `target_evidence_asset`, `target_text_or_ui`, `coordinate_space`, `box_or_anchor`, `verification_method`, `verified_frame`, and `accuracy_checked` in the visual manifest.
   - If a highlight cannot be anchored to the named target after render, remove the highlight or replace it with a readable evidence card. An unmarked screenshot is better than a wrong red mark.
   - Verify highlights against exported frames or a preview sheet after all motion, scaling, and cropping are applied, not only against the source screenshot.
   - Reserve stable zones for header/title, evidence screenshots, subtitles, IP characters, Star badges, and callouts. Do not let decorative or unrelated elements overlap evidence, subtitles, or each other.
   - Keep the entire bottom subtitle stack visually clean. Do not place persistent presenter avatars, large IP badges, or decorative characters beside, behind, or between the insight subtitle and line subtitle. Use the proven series layout where the bottom safe area belongs to subtitles only; IP characters should sit near evidence or callouts above the subtitle band.
   - Do not place anti-evasion wording such as `纯干货分享，不存在站外引流` on screen. It does not neutralize risky content and may itself trigger review. Use the platform's native AI-content disclosure when required; an optional on-video label may say only `AI 辅助创作`.
   - Do not show raw URLs, domains, QR codes, contact/account handles, browser address bars, repository clone/download controls, package-install commands, or directions to comments/profiles/private messages. Crop, mask, or replace them with a factual evidence card that keeps only the project name, Star count, source label, and claim-relevant text.
   - Treat `image2` as an optional upgrade, not a default requirement. Use it only when it clearly improves account identity, cover click value, and viewer comprehension compared with the baseline Remotion/IP/screenshot visual system. If generated art feels generic, weakens the IP, reduces clarity, or creates style discontinuity, skip it or revert to the baseline system.
   - Prefer generating image2 art as text-light or text-free backgrounds with reserved title zones, then overlay exact Chinese titles, project names, Star counts, and platform-safe text in Remotion. If image2 renders text inside the artwork, inspect it manually; regenerate or cover it with Remotion text if any character is wrong.
   - Record every generated key-art asset in the visual manifest with `generation_model`, `prompt`, `intended_use`, `factual_claims_allowed: false`, and `text_verified`.

5. Add subtitles.
   - Every final video must use a dual-layer subtitle system:
     - `insight subtitle`: short, persistent key point near the relevant evidence or scene center, such as `先流程，后生成`.
     - `line subtitle`: complete line-by-line narration subtitle in the lower safe area.
   - The insight subtitle explains the scene conclusion; the line subtitle preserves the full spoken meaning for silent viewing.
   - Treat the final generated narration audio as the timing source for line subtitles. Generate or calibrate line subtitle timestamps after the final TTS audio exists.
   - Do not hand-estimate line subtitle timings from scene durations, script paragraphs, word counts, or an earlier draft audio. If the voice, speed, text, or provider changes, regenerate or re-align the line subtitle timestamps.
   - Use forced alignment, ASR transcription with timestamps, TTS word/sentence boundary metadata, or a manual pass against the final MP4/audio. Record the chosen method in `subtitle_strategy.alignment_method`.
   - Keep line subtitles short enough to read on mobile: prefer one line, allow two lines, never use dense paragraphs.
   - Reserve separate zones for insight subtitle, line subtitle, evidence, and IP characters; do not let either subtitle layer cover core screenshots or Star badges.

6. Integrate the IP.
   - Use all three bundled IP roles when the video is long enough:
     - `head`: insight, pain point, warning, conclusion
     - `route`: workflow, connection, process, platform support
     - `key`: artifact, access concept, compatibility, output, or decision point; do not use it to encourage third-party installation/download in a public-platform video
   - Animate IP characters with motion-design techniques: entrance, bobbing, tilt, glow pulse, route drawing, unlock ring, or pointing/callout behavior.
   - IP must participate in the explanation, not sit as decoration.
   - IP must never occupy the bottom subtitle stack. If an IP character makes the line subtitles, insight subtitles, or bottom composition feel crowded, move it above the subtitle band or remove it. A clean subtitle area is more important than showing an extra character.

7. Create a unified cover.
   - Same IP theme, same colors, same title treatment, same repo/Star signal.
   - Cover should work as the first-frame visual language for a series.
   - Use a function-first cover title: the main title must directly explain what the project or Skill does in plain Chinese before using a curiosity hook. For example, prefer `教你创建自己的 Skill` or `把提示词做成 Skill` over only `别把提示词换个壳`.
   - Apply the same rule to the first video frame: a viewer should understand the Skill's purpose from the title/subtitle even with audio muted.
   - Do not default to image2 for production-account covers. Start from the proven baseline visual system: light background, real screenshots/evidence cards, black linework, red laser/infinity-eye accents, animated IP roles, and Remotion text/fact overlays. Add image2 only after a visual-lift check shows it beats the baseline on clarity, brand consistency, and click value.
   - Do not let image2 replace factual badges. GitHub Star count, source/date notes, and repo names should be overlaid from verified metadata unless the generated text has been manually checked and is exact.
   - Export it as a separate image in `outputs/`.

8. Create a platform publishing pack.
   - Generate `outputs/<project>-publishing-pack.md` for Douyin, WeChat Channels, and Xiaohongshu.
   - Include title options, body copy, hashtags/topics, pinned comment, AI-assisted disclosure text, source/date note, and platform-specific compliance notes.
   - Avoid claims that imply guaranteed results, academic ghostwriting, platform evasion, bypassing review, copyright misuse, or illegal access.
   - For AI-assisted videos, include a clear AI-assisted creation note when the platform or content context calls for it.
   - For GitHub claims, include the capture date for Star counts and avoid treating open-source popularity as product endorsement.
   - Read `references/platform-publishing-pack.md` when preparing platform copy or policy notes.
   - Keep source URLs only in internal work metadata. Public titles, body copy, pinned comments, and hashtags may name the project and source type, but must not contain raw URLs, project-address language, download/install directions, or directions to comments/profiles/private messages for obtaining anything.

9. Validate before delivery.
   - Run media checks with `ffprobe`.
   - Export a preview sheet from the final MP4.
   - Inspect key frames for text density, wrong highlights, missing Star count, missing subtitles, IP overlap, platform-safe subtitle placement, and unrelated element occlusion.
   - Confirm the platform publishing pack exists and avoids high-risk wording for the target platforms.
   - Run the external-channel safety scanner on the final brief, narration, subtitles, publishing pack, and Remotion/render source. Treat any finding as blocking:

```bash
python3 <skill>/scripts/validate_platform_safety.py \
  --brief work/<slug>/video-brief.json \
  --text outputs/<project>-case-narration.txt \
  --text outputs/<project>-case-subtitles.srt \
  --text work/<slug>/<project>.tsx \
  --text outputs/<project>-publishing-pack.md
```
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

## Model Routing and Cost Control

The same Codex conversation can act as the production controller for the whole video workflow: research, script, TTS calls, screenshots, Remotion rendering, FFmpeg checks, QA, and publishing copy. Within that workflow, model choice is a routing decision:

- Use the strongest available reasoning model for high-leverage judgment: repo research, fact interpretation, first-15-second hook, final narration strategy, platform-risk review, screenshot/evidence selection, visual QA, and nontrivial Remotion fixes.
- Use lower-cost external LLMs for draftable work: README summaries, title candidates, publishing-copy first drafts, subtitle chunk drafts, visual asset lists, and first-pass sensitive-word scans.
- Use deterministic local tools instead of LLMs whenever possible: GitHub metadata fetching, screenshot capture, crop/contact-sheet generation, audio conversion, SRT alignment from final audio, `ffprobe`, Remotion rendering, file copying, and manifest validation.
- Doubao BigTTS or other speech providers are narration/audio services, not script reasoning models. Treat voice changes as audio changes: regenerate or re-align subtitles after final TTS.
- Do not claim that the active Codex model can be dynamically replaced unless the current Codex session explicitly exposes model switching. External model calls are allowed only when API `base_url`, key, and model name are configured and reachable.
- If an external model is unavailable, too weak for the task, or changes factual meaning, route that step back to the stronger model and record the reason in the brief.

Each production brief should include a `model_routing` section that records planned model tiers, external providers, deterministic steps, fallbacks, and cost notes. The goal is to save tokens on repeatable drafting and machine work while keeping the account-facing quality gates on a strong model.

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

## Image2 Key Art

Read `references/image2-key-art.md` before using image2 or when the user provides image2-generated visuals.

Consider image2 only when it clearly beats the baseline Remotion/IP/screenshot system for:

- `cover_key_art`: high-click cover hero image
- `first_frame_key_art`: first-frame visual matching the cover
- `chapter_key_art`: 1-3 visual posters for major section transitions
- `signature_key_art`: branded closing image

Do not use image2 for:

- GitHub screenshots, Star counts, file contents, command outputs, benchmark results, UI highlights, or any evidence that must be true

When image2 is used, the preferred integration pattern is `image2 background + Remotion factual/text overlay`. This keeps generated art separate from exact titles, Star counts, subtitles, and platform-safe text.

Before keeping image2 in the final render, compare it against the baseline cover/first-frame direction. Reject image2 if it looks like generic AI atmosphere, makes the IP smaller or less recognizable, breaks the white/red/black series identity, or slows down the viewer's understanding of what the project does.

## Quality Gate

Before final response, confirm these are true:

- GitHub Star count is visible at least once.
- The cover image includes the repo/project name and Star signal.
- The cover and first frame use a function-first title that directly says what the Skill/project does; curiosity hooks may support it but must not replace clarity.
- If image2 key art is used, generated visuals are separated from factual evidence, critical text is verified or overlaid, and the visual manifest records the prompt and intended use.
- Subtitles exist throughout the final video.
- The video uses dual-layer subtitles: concise insight labels plus complete line-by-line narration subtitles.
- The bottom subtitle stack is clean: no persistent presenter avatar or IP element crowds, touches, or competes with the insight subtitle or line subtitle.
- Line subtitles are aligned to the final narration audio, not hand-estimated from the storyboard.
- The first 10 seconds pass the beginner clarity gate: a non-expert can tell what the project is, who uses it, and what pain it solves.
- The script has a clear `script_strategy`: one core angle, HKR score, micro-story, anti-AI-fluff pass, human voice check, and escalation beats.
- Professional terms are translated into plain benefits before or when they first appear.
- Every highlight points to the correct UI element or code section.
- Every red box/circle/arrow is anchored to an explicit target in the visual manifest and verified on an exported frame after render.
- Screenshots stay clean whenever highlight placement is uncertain; no decorative or confidence-free red marks are allowed.
- The video does not fake a human screencast with decorative cursors or fake interaction.
- No anti-evasion note uses `站外` or `引流`; use the platform's native disclosure or the neutral label `AI 辅助创作` only when needed.
- The public video, cover, narration, subtitles, and publishing copy contain no raw URL, QR code, contact handle, download/install instruction, project-address CTA, or direction to comments/profiles/private messages for obtaining anything.
- GitHub evidence uses distribution-safe crops: project identity and Star proof remain visible while address bars, raw URLs, clone/download controls, package-install commands, QR codes, and unrelated calls to action are removed.
- The three IP forms appear and move in meaningful roles.
- The first 3 seconds contain a concrete hook, not a generic topic label.
- The cover title, opening line, narration body, subtitle highlights, and platform copy include a punchy or funny hook while staying evidence-backed and platform-safe.
- The video includes a real or representative usage flow and at least one readable evidence card.
- The final seconds include the creator signature/account positioning and a clear closing line.
- The platform publishing pack includes Douyin, WeChat Channels, and Xiaohongshu copy plus compliance notes.
- The output video and publishing pack are present. Internal QA/build files such as cover, narration text/audio, preview sheet, subtitles, brief, manifest, and reports may stay in `work/` or `outputs/`, but the final desktop delivery folder contains only the `.mp4` and publishing pack `.md` unless the user explicitly requests more.

For detailed production notes, read `references/production-checklist.md`.

For script angle, HKR scoring, micro-story structure, and anti-AI-fluff checks, read `references/script-writing-methodology.md`.

For the structured JSON format, read `references/video-brief-schema.md`.

For platform copy and compliance notes, read `references/platform-publishing-pack.md`.

For external-channel, third-party-action, screenshot-crop, CTA, and final-scan rules, read `references/platform-risk-guardrails.md`.
