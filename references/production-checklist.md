# Production Checklist

## Screenshot Requirements

- Repository overview: capture the GitHub page with repo name and Star count visible.
- Star close-up: if the Star count is too small in the overview, create a cropped or zoomed shot showing the star button/count clearly.
- Feature evidence: capture exact files or sections being discussed.
- Install evidence: capture official install instructions or plugin config.
- Skill evidence: for Skill videos, capture the skills directory and at least one representative `SKILL.md`.
- Visual manifest: every final screenshot/crop/evidence card must list `scene_id`, `source_url_or_path`, `narration_claim`, `target_region`, and `why_this_screenshot`.
- No filler screenshots: remove any capture that does not directly support the narration claim in its scene.
- Mobile readability: if the important UI text is unreadable at 1080x1920, replace the full screenshot with a crop, zoom path, or redrawn evidence card that preserves the source meaning.
- Real case proof: for Skill videos, include at least one usage/process sequence showing prompt/input, routing or action, generated/expected artifacts, and user value.
- GitHub full-page screenshots establish source trust; feature explanations should use zoomed crops or redrawn evidence cards that are readable without pausing.

## Production Account Gate

- First 3 seconds: open with a concrete pain, contradiction, or curiosity gap. Do not open with a generic project name.
- Viewer promise: make clear why the target viewer should continue watching.
- Real case flow: include prompt/input, Skill action/routing, output artifact, and why that artifact matters.
- Proof moment: include at least one visual that makes the claim credible immediately, such as Star count, exact Skill file rule, real command output, or generated artifact.
- Evidence cards: use readable cards for any GitHub/code text that would be too small on mobile.
- Visual rhythm: avoid nine evenly paced slides. Include at least one punch-in, reveal, comparison, or before/after moment every 10-15 seconds.
- Sound design plan: define emphasis, transition, click, pop, or whoosh moments even if the final renderer uses lightweight generated sounds.
- CTA: end with a concrete action such as follow, collect, comment for template, or view the next Skill.
- Creator signature: reserve the final 3-6 seconds for account identity and closing line. For this user's series, default to `我是凸先生，专注 AI 全栈流程，我们下次再见！`
- Do not deliver as production-ready if hook, real case flow, proof moment, CTA, or creator signature is missing.

## Highlight Rules

- Highlight only the thing being named in narration.
- Use red boxes for exact UI/file regions; use dimming masks for focus; use arrows sparingly.
- If a screenshot pans or zooms, keep the highlight anchored to the visible target.
- Remove any highlight whose target cannot be verified.
- Bind every red mark to a precise target such as a phrase, file path, command, Star count, UI button, table row, or generated artifact name.
- Do not highlight a broad panel unless the narration explicitly refers to the whole panel.
- Verify highlight placement on exported frames or the preview sheet after motion is applied.
- Record highlight target, box/anchor, and verification frame in the visual manifest.

## Layout And Occlusion Rules

- Reserve zones before rendering: header/title, evidence/screenshot, subtitle safe area, IP character area, Star badge, and callout/highlight area.
- Keep subtitles above the social-platform bottom crop area and away from IP characters.
- Do not let IP characters cover important screenshot text, Star counts, command outputs, captions, or callouts.
- Avoid stacking unrelated decorations, particles, cards, tags, or labels over evidence. Remove elements that are not doing explanatory work.
- Export key frames or a contact sheet and check overlap between subtitles, IP, labels, callouts, highlights, Star badges, screenshots, and cover text.

## Subtitle Rules

- Use Chinese subtitles for Chinese videos.
- Prefer 1 line, allow 2 lines, avoid more.
- Use high-contrast text with a subtle white or dark translucent backing.
- Keep subtitles away from the bottom app UI/social-platform crop zone when possible.

## Cover Rules

- 1080x1920 unless the user requests another size.
- Include project name, one short promise, GitHub Star signal, and at least one IP character.
- Do not make the cover a text wall.
- Use a curiosity-driven cover hook. Avoid generic main titles such as only `科研写作助手`; prefer a concrete promise such as `别让 AI 直接写论文` or `先证据，后正文`.

## IP Motion Roles

- Head: observes, warns, stamps conclusions, blinks/glows.
- Route: draws or pulls process lines, connects steps.
- Key: unlocks installation/access, rotates key ring, introduces setup.
- Each IP appearance needs a story role in the storyboard. If an IP is only decoration, remove it or give it a job.

## Delivery Bundle

Save final user-facing files in `outputs/`:

- `<project>-case-90s-vertical.mp4`
- `<project>-case-cover.png`
- `<project>-case-narration.txt`
- `<project>-case-narration.mp3`
- `<project>-case-preview-sheet.jpg`
- `<project>-publishing-pack.md`

## Platform Publishing Pack

- Generate a publishing pack for Douyin, WeChat Channels, and Xiaohongshu before final delivery.
- Include for each platform: 3 title options, final recommended title, body copy, hashtags/topics, pinned comment, AI-assisted disclosure, source/date note, and risk notes.
- Tailor copy to the platform:
  - Douyin: stronger first line, concise body, clear AI-assisted/source note, direct follow/comment CTA.
  - WeChat Channels: slightly more trust-oriented, account positioning, source note, comment/forward CTA.
  - Xiaohongshu: searchable title, practical notes, collection/comment CTA, no exaggerated “种草” claims.
- Avoid high-risk wording: `代写论文`, `保过`, `包过`, `稳赚`, `一键赚钱`, `破解`, `绕过审核`, `官方推荐`, `100%`, `无风险`, `自动洗稿`, `搬运`, `盗版`, and unsupported superlatives such as `全网第一`.
- Add a Star/date note when GitHub popularity is mentioned, for example `Star 数为制作时截图数据`.
- State boundaries plainly for sensitive domains such as education, finance, medical, legal, credentialing, and security tooling.
- Add an AI-assisted disclosure when the video uses AI narration, AI image/video generation, AI clone voice, or synthetic characters.

## Script QA

- Run `fetch_github_metadata.py` before scripting so Star count, license, default branch, topics, and release/tag data are current. Prefer `GITHUB_TOKEN`; if the script uses HTML fallback, secondary fields may be sparse.
- Run `capture_github_screenshots.py` before designing visuals. Pass the metadata `default_branch` when capturing repo paths. Treat crop boxes as starting points; verify visually.
- Run `create_video_brief.py` before rendering so metadata, screenshots, IP roles, required outputs, and scene intent are in one JSON file.
- Fill production fields in `video-brief.json`: `hook`, `why_watch`, `real_case_flow`, `proof_moment`, `cover_hook`, `cta`, `creator_signature`, `retention_beats`, `evidence_cards`, and `sound_design`.
- Run `validate_production_gate.py` before rendering and again before delivery.
- Maintain `visual-manifest.json` during editing for screenshot selection, highlight targets, and layout/occlusion checks. Validate it with `scripts/validate_visual_manifest.py`.
- Run `qa_check.py` after rendering. It checks required files, media tracks, dimensions, and brief-level Star data. Use explicit `--video`, `--cover`, `--narration-text`, `--narration-audio`, and `--preview` arguments when final filenames differ from the brief. It still requires manual visual inspection for subtitles, highlight correctness, and IP overlap.
- Pass `--publishing-pack outputs/<project>-publishing-pack.md` to `qa_check.py` when the publishing pack filename differs from the brief.
