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
- AI-generated key art must not be used as evidence. Keep generated visuals for atmosphere, IP action, cover appeal, transitions, and brand moments only.
- Do not fake a human screencast. Avoid decorative mouse cursors, fake clicks, fake scrolling, and fake text selection. If real browser interaction is not recorded, use stable screenshots, readable crops, evidence cards, zooms, pans, and precise highlights.

## Production Account Gate

- Content angle: define one `script_strategy.core_angle` before writing narration. It must describe the viewer problem, not only the repo category.
- Account point of view: define why `凸先生，AI 全栈流程` should explain this repo, so the video sounds like part of a series rather than a generic repo recap.
- HKR score: rate `happy`, `knowledge`, and `resonance` from 1-5. Production videos should score at least 4 in two dimensions and never below 3.
- Viewer doubt: name the beginner's skeptical question and answer it in simple Chinese before introducing dense repo details.
- Micro-story: build the narration as challenge -> evidence -> process -> result -> boundary -> signature.
- Anti-AI-fluff scan: remove generic openings, report-style transitions, abstract efficiency claims, empty tool labels, unsupported hype, and README recitation.
- Human voice: the narration should sound like a knowledgeable person explaining the project to a friend, with concrete names, mild judgment, and clear boundaries.
- Escalation: order multiple capabilities from easiest to understand to most convincing proof. Merge beats that do not raise clarity or curiosity.
- First 3 seconds: open with a concrete pain, contradiction, or curiosity gap. Do not open with a generic project name.
- First 10 seconds: pass the beginner clarity gate. A non-expert viewer must understand what the project is, who it is for, and what pain it solves.
- Define the project in one plain-language sentence before introducing commands, file names, or framework jargon.
- Convert first-use technical terms into user benefits, for example `spec = 先把需求说清楚`, `TDD = 先写测试证明结果`, `review gate = 合并前再检查一遍`.
- Prefer before/after explanation over feature lists: show the messy old way, then the controlled new way.
- Add a `so what` moment every 10-15 seconds: explain why the feature matters to the viewer, not only what the repo contains.
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
- Use red boxes/circles for exact UI/file regions; use dimming masks for focus; use arrows sparingly.
- Prefer no highlight over an inaccurate highlight. A wrong red mark damages trust more than an unmarked screenshot.
- If the exact line/circle/box/underline placement is not obvious, do not mark the screenshot. Keep it clean or convert the point into a readable evidence card.
- Do not add marks for visual excitement. A mark is allowed only when the target is exact, named in narration, and can be verified after render.
- If a screenshot pans or zooms, keep the highlight anchored to the visible target.
- Remove any highlight whose target cannot be verified.
- Bind every red mark to a precise target such as a phrase, file path, command, Star count, UI button, table row, or generated artifact name.
- Do not use vague targets such as `top area`, `middle section`, `this panel`, `button area`, `标题区域`, or `这一块`.
- Define highlight coordinates in a known coordinate space: `source_crop_pixels`, `rendered_frame_pixels`, or `normalized_frame`.
- When a screenshot is scaled, cropped, or animated, verify the final rendered-frame position, not only the source screenshot position.
- For code/GitHub screenshots, the highlight should cover the exact line/title/button being discussed, with small padding only. It should not swallow adjacent unrelated lines.
- Do not highlight a broad panel unless the narration explicitly refers to the whole panel.
- Verify highlight placement on exported frames or the preview sheet after motion is applied.
- Record `target_evidence_asset`, `target_text_or_ui`, `coordinate_space`, `box_or_anchor`, `verification_method`, `verified_frame`, and `accuracy_checked: true` in the visual manifest.
- During manual QA, inspect at least every frame that contains a highlight. If a red box/circle is off-target, remove or fix it before final render.

## Layout And Occlusion Rules

- Reserve zones before rendering: header/title, evidence/screenshot, subtitle safe area, IP character area, Star badge, and callout/highlight area.
- Keep subtitles above the social-platform bottom crop area and away from IP characters.
- Keep the bottom subtitle stack clean. Do not place a persistent presenter avatar, large IP badge, or decorative character beside, behind, or between the insight subtitle and line subtitle. Match the proven series layout where IP characters explain evidence above the subtitle band, while the bottom area belongs to subtitles only.
- Do not let IP characters cover important screenshot text, Star counts, command outputs, captions, or callouts.
- Avoid stacking unrelated decorations, particles, cards, tags, or labels over evidence. Remove elements that are not doing explanatory work.
- Export key frames or a contact sheet and check overlap between subtitles, IP, labels, callouts, highlights, Star badges, screenshots, and cover text.
- When image2 key art is used, reserve clean overlay zones before rendering: title, subtitle, Star/source badge, IP motion, evidence crop, and bottom subtitle safe area.
- Add the small note `纯干货分享，不存在站外引流` in a low-emphasis non-subtitle zone, preferably upper-right or upper edge. It must not be near the bottom line subtitles and must not cover evidence, Star badges, IP characters, or key labels.

## Subtitle Rules

- Use Chinese subtitles for Chinese videos.
- Use a dual-layer subtitle system:
  - `Insight subtitle`: a short key point or scene conclusion placed near the evidence or in a reserved mid-screen zone.
  - `Line subtitle`: complete line-by-line narration subtitles placed in a consistent lower safe area.
- Insight subtitles should be 4-14 Chinese characters when possible and should not repeat the line subtitle verbatim.
- Line subtitles should preserve the full spoken meaning for silent viewing. Prefer 1 line, allow 2 lines, avoid more.
- Final narration audio is the timing source for line subtitles. Generate or calibrate line subtitle timestamps after the final TTS audio file is produced.
- Never hand-estimate line subtitle timing from scene duration, script paragraphs, text length, or a previous audio draft.
- If the narration text, TTS provider, voice type, speech rate, pronunciation style, or audio edit changes, regenerate or re-align the line subtitle timestamps before rendering.
- Acceptable alignment methods: forced alignment, ASR transcription with sentence timestamps, TTS word/sentence boundary metadata, or a manual timing pass against the final MP4/audio.
- Store the method and source file in `subtitle_strategy.alignment_method` and `subtitle_strategy.timing_source`.
- Use high-contrast text with a subtle backing or stroke for both layers.
- Reserve separate zones for insight subtitle, line subtitle, evidence screenshots, IP characters, and Star badges.
- The reserved line-subtitle and insight-subtitle zones should not share horizontal or vertical space with persistent IP/presenter elements. If the layout feels crowded, remove the bottom IP before shrinking subtitles.
- Keep line subtitles away from the bottom app UI/social-platform crop zone when possible.
- Do not deliver as production-ready if the video only has sparse keyword captions and no complete line subtitles.
- Do not deliver as production-ready if the line subtitles visibly lead or lag the narration, even when all files exist and media QA passes.

## Cover Rules

- 1080x1920 unless the user requests another size.
- Include project name, one short promise, GitHub Star signal, and at least one IP character.
- The main cover title must be function-first: directly say what the project or Skill does in plain viewer language. Use the curiosity hook as a secondary line when needed.
- The first video frame should follow the same clarity rule as the cover. A muted viewer should immediately understand `what this Skill does`, not only feel a vague pain point.
- For production-account covers, do not default to image2. Start from the baseline series system, then use image2 only if a side-by-side check proves it improves clarity, brand consistency, and click value. If image2 looks generic, weakens the IP, or slows comprehension, revert to the baseline cover.
- Do not make the cover a text wall.
- Use a curiosity-driven cover hook. Avoid generic main titles such as only `科研写作助手`; prefer a concrete promise such as `别让 AI 直接写论文` or `先证据，后正文`.
- For Skill videos, prefer titles such as `教你创建自己的 Skill`, `把提示词做成 Skill`, or `把 AI 流程封装成 Skill` over indirect hooks such as `别把提示词换个壳`.
- If image2 produces Chinese title text, inspect every character at full resolution. Regenerate, mask, or replace with Remotion text if the text is wrong, warped, ambiguous, or too stylized to read on mobile.

## Image2 Key-Art Rules

- Consider image2 for cover hero art, first-frame hero art, chapter transition posters, and final signature art only when it clearly outperforms the baseline Remotion/IP/screenshot system.
- Keep generated artwork consistent with the user's IP: black/red energy, laser/infinity-eye motif, white/black IP roles, tech/workflow atmosphere.
- Prefer text-light prompts with reserved space for Remotion overlays.
- Never ask image2 to invent GitHub Star counts, repo UI, code snippets, user results, platform logos, or factual evidence.
- Store generated assets in `work/<slug>/image2/` and copy final user-facing key art to `outputs/` only when needed. Do not copy key art to the final desktop delivery folder unless the user explicitly asks for cover/key-art files.
- Record `generation_model`, `prompt`, `negative_prompt`, `intended_use`, `source_references`, `text_verified`, and `factual_claims_allowed` in the visual manifest.
- Add AI-assisted disclosure to publishing copy whenever generated key art appears in the final video or cover.

## IP Motion Roles

- Head: observes, warns, stamps conclusions, blinks/glows.
- Route: draws or pulls process lines, connects steps.
- Key: unlocks installation/access, rotates key ring, introduces setup.
- Each IP appearance needs a story role in the storyboard. If an IP is only decoration, remove it or give it a job.

## Delivery Bundle

Keep production and QA files in `work/` or `outputs/` as needed:

- `<project>-case-90s-vertical.mp4`
- `<project>-case-cover.png`
- `<project>-case-narration.txt`
- `<project>-case-narration.mp3`
- `<project>-case-preview-sheet.jpg`
- `<project>-publishing-pack.md`

Archive only the two production-account deliverables to the user's desktop folder by default:

- `<project>-case-90s-vertical.mp4`
- `<project>-publishing-pack.md`

Do not copy cover images, preview sheets, narration text/audio, subtitle files, briefs, manifests, QA reports, screenshots, or source files into `/Users/gaoyunhong/Desktop/凸先生/视频素材/<YYYYMMDD> <SkillName>` unless the user explicitly asks for them.

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
- Fill `script_strategy` with `core_angle`, `viewer_doubt`, `plain_answer`, `account_point_of_view`, `hkr_score`, `micro_story`, `anti_ai_fluff_scan`, `human_voice_rules`, `escalation_beats`, and QA booleans.
- Fill production fields in `video-brief.json`: `hook`, `why_watch`, `real_case_flow`, `proof_moment`, `cover_hook`, `cta`, `creator_signature`, `retention_beats`, `evidence_cards`, and `sound_design`.
- Fill `beginner_clarity` with `plain_definition`, `target_user`, `pain_solved`, `first_10_seconds`, `jargon_translations`, and `so_what_beats`.
- Fill `subtitle_strategy` with both `insight_subtitles` and `line_subtitles`; sparse keyword captions are not enough.
- Fill `subtitle_strategy.timing_source` with the final narration audio path and `subtitle_strategy.alignment_method` with the actual alignment method used.
- Run `validate_production_gate.py` before rendering and again before delivery.
- Maintain `visual-manifest.json` during editing for screenshot selection, highlight targets, and layout/occlusion checks. Validate it with `scripts/validate_visual_manifest.py`.
- If image2 assets are used, include generated key-art records in `visual-manifest.json` and manually inspect them for wrong text, fake UI, logo/copyright risk, IP mismatch, and factual confusion.
- Treat visual-manifest highlight failures as blocking. The final video is not production-ready if any red box/circle lacks target evidence, coordinate space, verification method, or exported-frame confirmation.
- Run `qa_check.py` after rendering. It checks required files, media tracks, dimensions, and brief-level Star data. Use explicit `--video`, `--cover`, `--narration-text`, `--narration-audio`, and `--preview` arguments when final filenames differ from the brief. It still requires manual visual inspection for subtitles, highlight correctness, and IP overlap.
- Pass `--publishing-pack outputs/<project>-publishing-pack.md` to `qa_check.py` when the publishing pack filename differs from the brief.
