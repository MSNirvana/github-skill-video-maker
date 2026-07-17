# IP Character Storytelling

Read this reference when the production account should be led by the three IP characters rather than by a repository walkthrough.

The editorial premise is:

> The IP characters are the recurring protagonists. Each GitHub project is the event, tool, candidate, or problem they encounter in that episode.

Use working role names until the creator approves permanent public names. Do not invent new lore, catchphrases, or relationships as verified brand facts.

## Character Bible

### Black Character: Audience Proxy

- Dramatic job: raise the viewer's doubt, tease exaggerated claims, and create the opening conflict.
- Personality: skeptical, quick, slightly cheeky, never malicious.
- Questions: `这东西到底干嘛？`, `真能用，还是又一份说明书？`, `别急，先看证据。`
- Evidence behavior: points at a real doubt, screenshot, Star count, or boundary. It never declares an untested feature true.
- Best states: `black-point`, `black-crossed-arms`, `black-surprised`, `black-reach`.
- Must not become a permanent corner avatar or repeat the narration word for word.

### Route Character: Builder

- Dramatic job: turn the doubt into a visible test or a 2-4 step workflow.
- Personality: action-first, practical, patient with beginners.
- Questions: `输入是什么？`, `中间怎么走？`, `最后产出什么？`
- Evidence behavior: owns process diagrams, before/after transitions, real inputs, and representative outputs.
- Best states: `silicon-run`, route drawing, connection, process, and progress states.
- Must not claim that a workflow succeeded unless the result or repository evidence is visible.

### Key Character: Product Judge

- Dramatic job: inspect the result, state the boundary, and give the final viewer decision.
- Personality: calm, concise, mildly strict.
- Questions: `结果能不能验收？`, `适合谁？`, `什么情况别急着用？`
- Evidence behavior: owns checklists, artifact reveals, compatibility, limitations, and verdicts.
- Best states: key reveal, unlock ring, decision card, approval/rejection stamp.
- Must not use the key metaphor to direct viewers to download, install, register, or leave the platform.

## Relationship Engine

The default relationship is `doubt -> build -> verify`:

1. Black Character voices an exaggerated request or the viewer's suspicion.
2. Route Character converts it into a concrete test or workflow.
3. A real obstacle, missing condition, or boundary interrupts the easy answer.
4. Key Character checks the evidence and gives a qualified verdict.
5. 凸先生 closes with the account point of view and creator signature.

The conflict must be resolved by evidence, not by a character simply saying that the project is good.

## Narrative Modes

Record `ip_narrative.mode` in the brief.

- `ip-led-story`: default for production-account videos where the topic supports a relatable incident, experiment, interview, or workplace metaphor.
- `hybrid-evidence`: use for technical, policy-sensitive, security, medical, legal, financial, or complex projects. The characters open and interpret the evidence, but the evidence remains dominant.
- `evidence-explainer`: use only when character framing would trivialize the topic or make the explanation less clear. The three roles may still appear in restrained visual duties.

Do not force comedy into serious risk, loss, safety, or compliance scenes.

## Episode Structures

### Traffic Episode: 35-55 Seconds

1. `0-3s`: Black Character creates a concrete conflict or absurd-but-true request.
2. `3-8s`: one beginner sentence explains what the project does.
3. `8-15s`: real repo identity and Star proof.
4. `15-35s`: Route Character runs one representative workflow with readable evidence.
5. `35-45s`: obstacle or boundary; Key Character verifies the result.
6. `45-55s`: one-sentence verdict and creator signature.

### Depth Episode: 60-90 Seconds

Use `conflict -> plain definition -> repo proof -> test input -> process -> proof result -> limitation -> viewer decision -> signature`. Add a retention change every 8-12 seconds and a plain `so what` at least every 15 seconds.

### Brand Episode: 20-40 Seconds

Focus on a recurring relationship, running joke, or account worldview. A project may appear as a prop, but the episode must still teach one useful idea.

Recommended account mix over a 10-video cycle:

- 4 traffic episodes
- 4 depth episodes
- 2 brand episodes

## Recurring Series Frames

Choose one frame per episode. Do not mix several premises in one short video.

- `AI 工具实验室`: a claim enters the lab and must pass one visible test.
- `一人公司开会`: the three roles disagree about how one person should use AI.
- `翻车救援`: begin with a failed workflow and use the project to repair one specific step.
- `GitHub 项目面试`: the project is a candidate; Stars are popularity evidence, the demo is the practical test, and limitations are the probation note.
- `观点对决`: two characters argue; the third resolves it using repository evidence.

## Dialogue And Narration Rules

- Keep the main narrator responsible for facts and continuity. Character beats should create questions, reactions, transitions, or verdicts.
- Use 3-5 character beats in a 45-60 second episode and 5-7 in a 60-90 second episode.
- A character line should usually be one short spoken sentence or a 2-8 character visual bubble, not a paragraph.
- Do not give all three characters dialogue in every scene.
- Use at most one major joke per 10-15 seconds. Let evidence scenes breathe.
- Let each joke reveal a viewer pain, false assumption, workflow mistake, or boundary. Remove jokes that only decorate the topic.
- Keep project facts, Stars, supported features, results, and limitations in narrator/evidence language, not in unverified roleplay.

## Motion And Composition

- Assign one `lead_character` per scene. Allow at most one `supporting_character` unless the scene is the cover, a deliberate chapter merge, or the signature.
- Keep all IP characters above the bottom subtitle band and outside the evidence target.
- Reserve all-three-character compositions for the cover, one optional merge beat, and the closing signature.
- Every character entrance must perform a story action: question, point, carry an input, trace a route, react to proof, inspect an output, or give a verdict.
- Do not use continuous bobbing as the only motion. Combine entrance, pose change, prop interaction, route drawing, scale emphasis, reaction, and exit.
- Freeze or reduce character motion while the viewer must read a screenshot, Star badge, code line, or subtitle.
- Remove a character if its presence makes evidence, subtitles, or hierarchy less clear.

Recommended action-state mapping:

| State | Story use | Avoid |
| --- | --- | --- |
| `black-point` | asks the core question or points to evidence | pointing at an approximate target |
| `black-crossed-arms` | skepticism, boundary, or failed claim | using it as generic idle art |
| `black-surprised` | proof reveal or unexpected result | repeated reactions with no new information |
| `black-reach` | receives an input, artifact, or candidate | implying a download or off-platform action |
| `silicon-run` | starts a test or moves the workflow forward | looping through an entire reading scene |
| route drawing | connects 2-4 verified process steps | decorative paths with no semantic labels |
| key reveal | artifact inspection and final decision | implying guaranteed access or success |

## Brief Fields

Recommended `ip_narrative` fields:

- `mode`: one of `ip-led-story`, `hybrid-evidence`, or `evidence-explainer`
- `series_frame`: one recurring series frame
- `episode_premise`: one sentence describing what happens in this episode
- `episode_type`: `traffic`, `depth`, or `brand`
- `roles`: working name, dramatic job, personality, allowed actions, and forbidden uses for each character
- `conflict`: the viewer doubt or workflow problem that starts the story
- `obstacle`: the real condition, failure, or boundary that prevents an easy answer
- `resolution_evidence`: the screenshot, artifact, result, or boundary that resolves the conflict
- `character_beats`: ordered list with `scene_id`, `character`, `intent`, `line_or_reaction`, `action_state`, and `evidence_target`
- `scene_cast`: one lead and zero or one support character for each scene
- `qa`: role consistency, evidence resolution, meaningful movement, subtitle safety, and remove-the-IP test

## Production Gate

An IP-led episode is not production-ready unless all are true:

- The opening conflict can be understood without knowing GitHub.
- Each character performs a different dramatic job.
- Removing the characters would remove the episode's question, experiment, or verdict, not only its decoration.
- The project appears as evidence inside a story, not as a README read aloud.
- The obstacle or boundary is real and is not invented for drama.
- The final verdict says who benefits and what the project does not guarantee.
- Character motion never covers subtitles, Star proof, screenshots, or exact highlight targets.
- A viewer can still understand the project with audio muted through the function-first title, evidence, insight subtitles, and line subtitles.

## Example Skeleton

For a theme-building Skill, use the premise `公司新招了一个 Skill，第一天就要给 Codex 换工装`:

1. Black Character objects to the unexpected request.
2. Narrator defines the Skill plainly: it turns supplied IP artwork into a reusable Codex desktop theme.
3. Show the real repository identity and current Star evidence.
4. Route Character carries one supplied Hero image through the real theme workflow.
5. Show a real before/after or finished theme, not a fabricated UI.
6. Key Character checks interaction preservation and states the implementation boundary.
7. End with the viewer decision and the fixed creator signature.

Keep the main cover title function-first, for example `给 Codex 换上你的 IP 主题`. Use `新同事第一天，就改公司工装？` as secondary curiosity copy rather than replacing the plain function.
