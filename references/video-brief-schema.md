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
- `style`: e.g. `case-walkthrough`
- `theme`: color/style hints
- `ip_roles`: role mapping for head/route/key IP characters
- `required_outputs`: expected output filenames
- `storyboard`: scene list
- `qa`: booleans for required quality gates
- `visual_manifest`: optional path to the visual manifest that records screenshot rationale, highlight targets, and overlap checks
- `hook`: first-3-second hook with pain, contradiction, and viewer reason to continue
- `why_watch`: one sentence explaining what the viewer gets from watching
- `real_case_flow`: prompt/input -> Skill action -> output artifacts -> value
- `proof_moment`: the strongest trust-building visual or claim
- `cover_hook`: curiosity-driven cover title
- `cta`: final viewer action
- `creator_signature`: account identity, account focus, and closing line
- `retention_beats`: time-coded beats for stop-scroll, trust, proof, insight, and close
- `evidence_cards`: readable evidence cards or crops used for mobile clarity
- `sound_design`: planned emphasis/transition/click/pop moments
- `publishing_pack`: platform copy requirements and expected output filename

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

Use the brief to prevent drift: the Star count in narration, cover, and visual badges should come from `repo.stars_label`; screenshot names should come from `screenshots`; final output filenames should match `required_outputs`. Generate custom final naming with `create_video_brief.py --output-prefix <prefix>` when producing versions or a branded series.

Recommended per-scene additions:

- `evidence`: list of screenshots/crops/cards with `source_url_or_path`, `narration_claim`, `target_region`, and `why_this_screenshot`
- `highlights`: list of exact red boxes, arrows, underlines, or laser marks with `target`, `box_or_anchor`, and `verified_frame`
- `layout_zones`: reserved zones for `header`, `evidence`, `subtitle`, `ip`, and `callout`

The final edit should also keep a `visual-manifest.json` with the same scene ids. Use `scripts/validate_visual_manifest.py` before delivery.

The final delivery should also include a publishing pack. Recommended fields:

- `output`: expected Markdown filename in `outputs/`
- `platforms`: default `["douyin", "wechat_channels", "xiaohongshu"]`
- `ai_disclosure_required`: boolean
- `source_date_note`: exact capture date or repository metadata date for Star/source claims
- `risk_terms`: phrases to avoid or rewrite

Use `scripts/validate_production_gate.py` to check required production fields. Treat production-gate failures as blocking for account-ready videos.
