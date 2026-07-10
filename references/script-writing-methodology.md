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

## Viral Packaging Layer

Before finalizing the cover title, first-frame title, opening line, and platform titles, create a punchier packaging layer. The goal is to make dry technical value feel like a joke shared with the viewer, then quickly back it with evidence.

Generate at least 9 title candidates in 3 buckets:

- `玩梗标题`: uses internet-native language, mild exaggeration, roleplay, or a funny metaphor. Example: `一人公司？一个 Skill 全家桶全搞定！`
- `反差标题`: creates curiosity by naming a contradiction. Example: `不是 AI 不够强，是你让它一人打全场`
- `干货标题`: clearer and slightly safer for platforms/search. Example: `把 AI 助手拆成一支专家团队`

Recommended title selection:

- Prefer a title with a hook first and a real value second: `一人公司？一个 Skill 全家桶全搞定！`
- Keep the factual anchor in the subtitle, cover badge, or first 10 seconds: repo name, Star count, role count, install path, or real file evidence.
- Make the viewer smile, then immediately answer `所以它到底有什么用`.

Allowed comedic devices:

- `一人公司`, `全家桶`, `打工人`, `别让 AI 加班到冒烟`, `一个助手演全公司`, `AI 部门开张`, `把 AI 从临时工变成正式工`
- Mild roast of workflow habits: `你不是缺模型，你是缺分工`
- Concrete analogy: `岗位说明书`, `项目经理`, `流水线`, `工具箱`, `说明书`, `团队编制`

Do not use humor that creates false claims:

- No guaranteed outcomes such as `全自动搞定`, `一键起飞`, `100% 提效`, `躺赚`, `保过`.
- No official endorsement unless verified.
- No platform evasion, cheating, scraping, piracy, or academic misconduct framing.
- If the title uses `全搞定` or similar hook, the narration must quickly narrow it: `不是自动替你完成所有事，而是把常见角色和流程打包好`.

Opening line pattern:

- Start with a funny pain: `你让一个 AI 写前端、审代码、做增长，它都快被你安排成联合创始人了。`
- Then define plainly: `Agency Agents 做的事，是把 AI 拆成可安装的专家角色。`
- Then show proof: `制作时 GitHub 大约 130k Stars，仓库里有 299 个 agent 文件。`

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
- Add light humor where it clarifies the point, not where it distracts from evidence.
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
- Stiff platform titles: `某某项目介绍`, `一个 GitHub 项目案例`, `AI 全栈流程里为什么...`. Rewrite these into punchy-but-true hooks.

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
- Are the title and opening at least mildly funny or surprising without making unsupported claims?
