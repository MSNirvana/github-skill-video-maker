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
- `viral_packaging`: title/opening packaging layer with meme, contrast, and practical title candidates
- `subtitle_strategy`: dual-layer subtitle plan with insight subtitles and complete line subtitles
- `platform_distribution_safety`: strict in-platform distribution mode, public-copy restrictions, screenshot-crop status, and final-scan QA
- `platform_safety_note`: optional neutral AI disclosure; omit by default or use only `AI 辅助创作`
- `model_routing`: planned strong-model, low-cost-model, and deterministic-tool routing for cost control

Recommended storyboard scene ids:

- `cover`
- `pain`
- `repo-proof`
- `workflow`
- `skills`
- `deep-dive`
- `compatibility`
- `boundary`
- `value`
- `signature`

Recommended `platform_distribution_safety` fields:

- `mode`: default `strict_platform_safe`
- `external_routing_free`: public content contains no raw URL/domain, QR/contact detail, project-address CTA, or directions to comments/profiles/private messages
- `third_party_action_free`: public content contains no download/install/clone/register/open/use instruction for third-party software, apps, sites, plugins, or mini programs
- `public_copy_url_free`: platform titles, body copy, pinned comments, hashtags, narration, and subtitles contain no raw URL/domain
- `distribution_crops_verified`: public screenshot crops remove address bars, raw URLs, QR/contact details, clone/download controls, package-install commands, and unrelated outbound calls to action
- `native_ai_label`: use the platform's native AI-content disclosure when required
- `qa`: final text scan and manual cover/preview inspection booleans

Recommended optional `platform_safety_note` fields:

- `enabled`: boolean, default false
- `text`: empty by default; if enabled, use only `AI 辅助创作`
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

Recommended `model_routing` fields:

- `controller`: the current Codex conversation or orchestration surface that owns the full workflow
- `strong_model_tasks`: high-leverage judgment steps that should stay on the strongest available reasoning model
- `low_cost_model_tasks`: draftable or low-risk text tasks that can be delegated to cheaper external LLMs
- `deterministic_tool_tasks`: local/API steps that should not spend LLM tokens
- `external_providers`: configured external providers with `name`, `base_url`, `model`, and `status`; never store secret keys in the brief
- `fallback_policy`: when to route a task back to the strong model
- `cost_notes`: expected token-saving choices and quality tradeoffs
- `qa`: checks that final facts, script, subtitles, visual evidence, and platform risk were reviewed by the strong model or manually verified

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

Recommended `viral_packaging` fields:

- `meme_titles`: at least 3 funny or meme-like titles
- `contrast_titles`: at least 3 contradiction/curiosity titles
- `practical_titles`: at least 3 clearer search-friendly titles
- `recommended_title`: the strongest title that is funny but true
- `opening_line`: the first spoken line or first-frame line that earns attention
- `body_voice`: how the narration body and publishing body keep the same fun-but-useful voice
- `factual_anchor`: repo name, Star count, role count, install command, or file evidence used to ground the hook
- `boundary_clarifier`: short line that narrows any playful exaggeration, such as `不是一键替你干完所有活，而是把常用角色和流程打包好`
- `qa`: checks for no false guarantees, no fake official endorsement, and beginner clarity

The final edit should also keep a `visual-manifest.json` with the same scene ids. Use `scripts/validate_visual_manifest.py` before delivery.

The final delivery should also include a publishing pack. Recommended fields:

- `output`: expected Markdown filename in `outputs/`
- `platforms`: default `["douyin", "wechat_channels", "xiaohongshu"]`
- `ai_disclosure_required`: boolean
- `source_date_note`: exact capture date or repository metadata date for Star/source claims
- `risk_terms`: phrases to avoid or rewrite

Use `scripts/validate_production_gate.py` to check required production fields. Treat production-gate failures as blocking for account-ready videos.
