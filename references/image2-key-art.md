# Image2 Key Art

Use this reference when the user wants image2-quality visuals or provides image2-generated artwork.

## Role In The Pipeline

Image2 is optional. It is for attention and brand power, not factual proof, and it should be used only when it clearly improves the result.

Consider it for:

- Cover hero art
- First-frame hero art
- Chapter transition posters
- Branded closing/signature art
- Optional thumbnail variants

Do not use it for:

- GitHub pages
- Star counts
- Code screenshots
- Command output
- Benchmark numbers
- Real product UI
- Any claim that must be verifiably true

## Use/Skip Decision

Start with the baseline series system: light background, black linework, red laser/infinity-eye accents, real screenshots/evidence cards, Remotion text/fact overlays, and animated IP roles.

Use image2 only if the generated asset is better than the baseline on all three checks:

- **Clarity:** a muted mobile viewer understands what the Skill/project does faster.
- **Brand:** the user's IP is more recognizable, not smaller or more generic.
- **Click value:** the cover/first frame feels stronger without becoming vague AI atmosphere.

Skip image2 or revert to the baseline if it creates generic dark tech vibes, style discontinuity, weak IP presence, fake-looking UI, unreadable text, or weaker first-glance comprehension.

## Integration When Used

Prefer:

`image2 key-art background + Remotion exact text/fact overlay`

This gives the video a strong poster look while keeping titles, Star counts, source notes, and platform-safe text exact.

If image2 renders Chinese text directly, inspect every character at full resolution. If any text is wrong, unclear, warped, or too stylized for mobile, regenerate or cover it with Remotion text.

## Prompt Template

Use this structure and customize the bracketed parts:

```text
Vertical 9:16 high-impact Chinese short-video cover key art.
Theme: [plain function of the Skill/project].
Core message: [function-first title meaning, but leave clean space for text overlay].
Visual style: cinematic black and red tech energy, strong contrast, sharp poster composition, glowing red laser/infinity-eye motif, premium AI workflow atmosphere.
Characters: use the user's three IP roles: black main mascot with red infinity laser eyes as the central leader, white route/robot helper with laptop or workflow lines, white key helper holding a key/unlock symbol.
Scene: [specific metaphor, e.g. Skill factory, workflow forge, launch platform, code cockpit].
Composition: large clean title-safe area at the top, central IP action scene, lower workflow icons or platform stage, no dense paragraphs.
Mood: powerful, practical, learning + practice + growth, not cute-only.
Aspect ratio: 9:16, mobile cover, ultra-detailed, polished, high production value.
```

Negative prompt:

```text
No fake GitHub UI, no fake Star count, no unreadable Chinese text, no random English words, no extra fingers, no deformed mascot eyes, no unrelated logos, no stock-photo people, no beige/blue corporate style, no clutter covering title area.
```

## Cover Text Plan

Use Remotion overlays for:

- Main title: function-first, e.g. `教你创建自己的 Skill`
- Subtitle: one value line, e.g. `把提示词、流程和经验封装成可复用能力`
- Star badge: from verified metadata
- Source/date note if needed

Image2 may include decorative labels such as `学习`, `实践`, `成长`, but do not rely on generated text for factual claims.

## Visual Manifest Record

For every generated key-art asset, record:

```json
{
  "asset": "work/<slug>/image2/cover-key-art.png",
  "generation_model": "image2",
  "prompt": "...",
  "negative_prompt": "...",
  "intended_use": "cover_key_art",
  "source_references": ["user IP assets", "style reference image"],
  "factual_claims_allowed": false,
  "text_verified": true,
  "overlay_text_in_remotion": true,
  "qa": {
    "ip_consistent": true,
    "no_fake_ui_or_star_count": true,
    "title_safe_area_clear": true,
    "mobile_readable": true
  }
}
```

## When To Regenerate

Regenerate or edit the image if:

- The IP character no longer resembles the user's IP.
- Chinese text is wrong or hard to read.
- It invents fake UI, logos, Star counts, or code.
- The title-safe area is blocked.
- The scene is visually strong but does not explain the Skill's function.
- The palette drifts away from the series identity.
