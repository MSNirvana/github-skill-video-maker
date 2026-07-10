# Video Brief Schema

The pipeline uses `video-brief.json` as the source of truth between research, screenshot capture, script writing, and rendering.

Required top-level fields:

- `schema_version`: integer
- `slug`: filesystem-safe project slug
- `repo`: GitHub metadata from `fetch_github_metadata.py`
- `screenshots`: screenshot manifest paths from `capture_github_screenshots.py`
- `audience`: target audience
- `duration_seconds`: target duration
- `language`: narration/subtitle language
- `style`: e.g. `evidence-explainer`
- `theme`: color/style hints
- `ip_roles`: role mapping for head/route/key IP characters
- `required_outputs`: expected output filenames
- `storyboard`: scene list
- `qa`: booleans for required quality gates
- `visual_manifest`: optional path to the visual manifest that records screenshot rationale, highlight targets, and overlap checks
- `image2_strategy`: optional plan for generated key art, including cover, first frame, chapter posters, prompt, negative prompt, text overlay plan, and evidence boundaries
- `hook`: first-3-second hook with pain, contradiction, and viewer reason to continue
- `why_watch`: one sentence explaining what the viewer gets from watching
- `real_case_flow`: prompt/input -> Skill action -> output artifacts -> value
- `proof_moment`: the strongest trust-building visual or claim
- `cover_hook`: function-first cover title that directly explains what the Skill/project does; curiosity hooks may be secondary copy
- `cta`: final viewer action
- `creator_signature`: account identity, account focus, and closing line
- `retention_beats`: time-coded beats for stop-scroll, trust, proof, insight, and close
- `evidence_cards`: readable evidence cards or crops used for mobile clarity
- `sound_design`: planned emphasis/transition/click/pop moments
- `publishing_pack`: platform copy requirements and expected output filename
- `beginner_clarity`: plain-language explanation gate for non-expert viewers
- `script_strategy`: content angle, HKR score, micro-story, human voice, and anti-AI-fluff checks
- `subtitle_strategy`: dual-layer subtitle plan with insight subtitles and complete line subtitles
- `platform_safety_note`: the unobtrusive on-video note `纯干货分享，不存在站外引流`, including placement and overlap checks

Recommended storyboard scene ids:

- `cover`
- `pain`
- `repo-proof`
- `workflow`
- `skills`
- `deep-dive`
- `install`
- `boundary`
- `value`
- `signature`

Recommended `platform_safety_note` fields:

- `text`: always `纯干货分享，不存在站外引流`
- `placement`: preferably `upper_right` or `upper_edge`
- `style`: small, low-emphasis, readable, and visually secondary
- `avoid_zones`: include `line_subtitle`, `insight_subtitle`, `evidence`, `star_badge`, and `ip`
- `qa`: confirm it is not near bottom subtitles and does not cover key evidence

Recommended `image2_strategy` fields:

- `enabled`: boolean
- `uses`: e.g. `["cover_key_art", "first_frame_key_art", "chapter_key_art", "signature_key_art"]`
- `style_reference`: the user's IP/style direction
- `prompt`: final image2 prompt or prompt template
- `negative_prompt`: text and visual defects to avoid
- `text_policy`: usually `overlay_critical_text_in_remotion`; use `generated_text_allowed` only after manual verification
- `evidence_policy`: `generated_art_is_not_evidence`
- `outputs`: generated asset paths
- `qa`: checks for readable title zone, IP consistency, no fake UI, no fake Star count, no text errors, no evidence confusion

Use the brief to prevent drift: the Star count in narration, cover, and visual badges should come from `repo.stars_label`; screenshot names should come from `screenshots`; final output filenames should match `required_outputs`. Generate custom final naming with `create_video_brief.py --output-prefix <prefix>` when producing versions or a branded series.

Recommended per-scene additions:

- `evidence`: list of screenshots/crops/cards with `source_url_or_path`, `narration_claim`, `target_region`, and `why_this_screenshot`
- `highlights`: list of exact red boxes/circles, arrows, underlines, or laser marks with `target`, `target_evidence_asset`, `target_text_or_ui`, `coordinate_space`, `box_or_anchor`, `verification_method`, `verified_frame`, and `accuracy_checked`
- `layout_zones`: reserved zones for `header`, `evidence`, `insight_subtitle`, `line_subtitle`, `ip`, and `callout`

Recommended highlight fields:

- `target`: exact thing named in narration, such as `GitHub Star count 75.3k` or `Spec-Driven Development title`
- `target_evidence_asset`: final screenshot/crop/card asset that contains the target
- `target_text_or_ui`: exact visible text, UI control, command, file path, line title, or artifact name being marked
- `coordinate_space`: one of `source_crop_pixels`, `rendered_frame_pixels`, or `normalized_frame`
- `box_or_anchor`: exact box/anchor in that coordinate space
- `verification_method`: how placement was checked, for example `exported_frame_manual`, `preview_sheet_manual`, or `pixel_coordinate_check`
- `verified_frame`: exported frame path or preview frame where the marker was inspected after scaling/motion
- `accuracy_checked`: boolean, must be `true` only after render-frame inspection
- `allow_broad_panel`: optional boolean, only when the narration explicitly names the whole panel

Highlight timing rule:

- Check highlight placement after all Remotion scaling, crop, zoom, pan, and motion are applied.
- Do not use broad/vague highlight targets unless `allow_broad_panel` is true and the narration names the whole panel.
- Remove or redraw any red mark that cannot be verified against the final rendered frame.

Recommended `beginner_clarity` fields:

- `plain_definition`: one sentence that explains what the project is without jargon
- `target_user`: who should care
- `pain_solved`: what concrete pain it removes
- `first_10_seconds`: how the opening answers what it is, who it is for, and why it matters
- `jargon_translations`: mapping of technical terms to plain Chinese benefits
- `so_what_beats`: time-coded moments that explain why a feature matters to the viewer

Recommended `script_strategy` fields:

- `core_angle`: one sentence describing the viewer problem and why this repo matters
- `viewer_doubt`: the skeptical beginner question the video must answer
- `plain_answer`: direct answer to the doubt in simple Chinese
- `account_point_of_view`: why this account is the right one to explain the repo
- `hkr_score`: `happy`, `knowledge`, and `resonance` scores from 1 to 5
- `micro_story`: `challenge`, `evidence`, `process`, `result`, `boundary`, and `signature`
- `human_voice_rules`: notes for concrete names, mild judgment, boundaries, and oral sentence style
- `anti_ai_fluff_scan`: banned or rewritten phrases found before TTS
- `escalation_beats`: ordered beats from basic recognition to proof moment and viewer decision
- `qa`: booleans for one core angle, no README summary, beginner understandability, evidence-backed claims, and human voice

Recommended `subtitle_strategy` fields:

- `mode`: `dual-layer`
- `insight_subtitles`: short scene-level key points or conclusions
- `line_subtitles`: complete narration subtitle chunks for silent viewing
- `timing_source`: final narration audio path used to time line subtitles
- `alignment_method`: how line subtitle timestamps were generated or calibrated, such as `forced_alignment`, `asr_sentence_timestamps`, `tts_sentence_boundaries`, or `manual_audio_pass`
- `safe_zones`: reserved screen zones for insight subtitles and line subtitles
- `qa`: checks for complete coverage, audio sync, readability, and no overlap with evidence/IP/Star badges

Line subtitle timing rule:

- Treat final narration audio as the source of truth.
- Do not derive line subtitle timestamps only from storyboard scene ranges, text length, paragraph boundaries, or earlier draft audio.
- Regenerate or re-align line subtitles whenever narration text, TTS provider, voice type, speech rate, or audio editing changes.
- Each `line_subtitles` item should include start/end timing from the final audio and text that matches the spoken line closely enough for silent viewing.

The final edit should also keep a `visual-manifest.json` with the same scene ids. Use `scripts/validate_visual_manifest.py` before delivery.

The final delivery should also include a publishing pack. Recommended fields:

- `output`: expected Markdown filename in `outputs/`
- `platforms`: default `["douyin", "wechat_channels", "xiaohongshu"]`
- `ai_disclosure_required`: boolean
- `source_date_note`: exact capture date or repository metadata date for Star/source claims
- `risk_terms`: phrases to avoid or rewrite

Use `scripts/validate_production_gate.py` to check required production fields. Treat production-gate failures as blocking for account-ready videos.
