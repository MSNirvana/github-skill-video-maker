# Platform Distribution Risk Guardrails

Use these rules for any video or publishing copy intended for Douyin, WeChat Channels, or Xiaohongshu. Default to `strict_platform_safe` unless the user explicitly requests a non-platform technical demo.

## Core Rule

Keep the content complete inside the platform. Explain what the project does, show evidence, and invite only in-platform engagement. Do not direct viewers to another website, app, mini program, account, private message, comment-delivery flow, offline channel, or third-party software action.

## Public Content Must Not Contain

- Raw URLs, domains, shortened links, browser address bars, or text styled as an address
- QR codes, contact details, account handles, group invitations, or cross-platform usernames
- `项目地址`, `仓库地址`, `链接`, `评论区获取`, `主页获取`, `私信领取`, `扫码`, `复制地址`, `去官网`, `前往网站`, `跳转`, `站外`, or `引流`
- Instructions or commands to download, install, clone, register for, open, or use third-party software, plugins, apps, websites, or mini programs
- Promises to send files, templates, prompts, source code, or links through comments, profiles, private messages, groups, or other channels
- An anti-evasion note such as `纯干货分享，不存在站外引流`; it does not cure the underlying risk and can itself become a review signal

## Allowed In-Platform Framing

- Explain the project function, workflow, evidence, limitations, and viewer decision
- Name the project or repository as factual identity, without presenting an address or telling viewers where to obtain it
- State `公开仓库页面，Star 数为制作时截图数据` with a capture date
- Use CTAs such as `收藏这条视频`, `关注下一期`, `评论你更想看哪个环节`, or `转发给需要的人`
- Use the platform's native AI-content label; if an on-video label is needed, use only `AI 辅助创作`

## Screenshot Rules

Keep original captures in `work/` for audit. Build separate public crops for the video and cover:

- Keep: project name, Star count, README/SKILL evidence, relevant output artifact, source/date label
- Remove or mask: browser/address bars, raw URLs, QR codes, contact handles, Code/Clone/Download controls, installation commands, package-manager commands, sign-up buttons, and unrelated outbound calls to action
- Replace risky setup screenshots with a readable compatibility or workflow evidence card
- Inspect every cover and key frame at full size; OCR-like review must include tiny browser titles and screenshot text, not only large captions

## Copy Rules

- Store the source URL only in internal metadata or the production brief
- In the publishing pack's public sections, use only project name, source type, Star count, and capture date
- Pinned comments must discuss the topic; they must not distribute or promise access to project materials
- Do not use `安装`, `下载`, or `使用第三方软件` as a public CTA. Describe compatibility or workflow boundaries without directing action
- Hashtags should prefer `#开源项目`, `#AI工作流`, and topic terms; do not use hashtags as a hidden destination hint

## Blocking QA

Run `scripts/validate_platform_safety.py` against the final brief, narration, subtitles, publishing pack, and renderer source. Also inspect the final cover and preview sheet manually because text embedded in screenshots cannot be reliably validated from source text alone.

Any remaining external-channel signal is blocking. Remove it and rerun the scan before delivery.
