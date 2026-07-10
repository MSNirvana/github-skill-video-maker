# Script Writing Methodology

Use this reference before writing narration, insight subtitles, cover hooks, or publishing copy.

The goal is not to imitate any creator's private voice. The goal is to turn a GitHub project into a clear, trustworthy, beginner-friendly short-video story with the user's own account positioning.

## Content Angle Gate

Before writing the final script, define the angle in one sentence:

- `core_angle`: the human problem this repo solves, not just what the repo contains.
- `viewer_doubt`: the first skeptical question a beginner would ask.
- `plain_answer`: a direct answer in simple Chinese.
- `account_point_of_view`: why `凸先生，AI 全栈流程` is the right account to explain it.

Avoid repo-summary angles such as `这是一个开源 Skill 项目`. Prefer viewer-benefit angles such as `它把一次性提示词，变成可复用的 AI 工作流程`.

## HKR Video Test

Score each script idea from 1 to 5:

- `happy`: does the opening create curiosity, surprise, or a reason to stop scrolling?
- `knowledge`: will the viewer learn a concrete new idea, workflow, or judgment?
- `resonance`: does it name a real pain AI users already feel?

Production-ready scripts should score at least `4` in two dimensions and never below `3` in any dimension. If the score is weak, change the angle before writing more narration.

## Micro-Story Structure

For a 60-120 second repo video, write as a compact story:

1. Challenge: what is painful, confusing, or wasteful for the viewer today?
2. Evidence: show the real repo, Star count, file, command, or artifact that proves this is not filler.
3. Process: show the workflow step by step, using screenshots or readable evidence cards.
4. Result: show what becomes easier, safer, faster, or more reusable.
5. Boundary: say who should not use it or what it cannot promise.
6. Signature: close with account identity and a next action.

Use this structure to create momentum. Do not turn it into a feature list.

## Human Voice Rules

Narration should sound like a knowledgeable person explaining a project to a friend:

- Use concrete names: repo name, command, file path, Skill name, platform name, Star count.
- Use plain benefits before jargon. Example: `spec` becomes `先把需求说清楚`, then mention the term.
- Use mild personal judgment when useful: `我觉得这个项目真正有价值的地方是...`
- Admit uncertainty or boundaries when the repo does not prove a claim.
- Use short oral sentences. One spoken line should usually contain one idea.
- Add a direct viewer address only where it helps: `如果你也经常让 AI 重复做同一类任务...`

## Anti-AI-Fluff Scan

Rewrite any narration that contains these patterns:

- Generic openings: `随着 AI 的发展`, `在当今 AI 时代`, `今天给大家介绍一个项目`.
- Report-style transitions: `首先`, `其次`, `最后`, `综上所述`, `值得注意的是`, `不难发现`, `接下来让我们`.
- Abstract filler: `赋能`, `提升效率`, `解决痛点`, `生态闭环`, unless followed by a concrete example.
- Empty tool labels: `AI 工具`, `某个模型`, `相关技术`, when the real name is known.
- README recitation: listing features without showing who uses them and why they matter.
- Unsupported hype: `神器`, `颠覆`, `全网第一`, `必备`, unless the evidence and platform policy support the claim.

## Escalation Beats

When explaining multiple capabilities, order them from easiest to most surprising:

1. Basic recognition: what the repo is.
2. First useful action: what a beginner can do with it.
3. Workflow value: how it changes the way AI work is organized.
4. Proof moment: the one screenshot, file rule, or output artifact that makes the viewer trust it.
5. Viewer decision: who should save, try, or skip it.

Each beat should raise clarity or curiosity. If two beats feel equal, merge them.

## Script QA

Before final rendering, answer these checks in `script_strategy.qa`:

- Does the first 10 seconds pass `what is it / who uses it / what pain does it solve`?
- Is the script built around one core angle, not a pile of features?
- Is there at least one real case flow with input, action, output, and value?
- Does every claim have visual evidence or a clear boundary?
- Would a beginner understand the video without opening GitHub?
- Does the narration sound like a human explanation rather than an AI summary?
