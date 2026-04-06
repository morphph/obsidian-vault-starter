---
source: agent
created: 2026-03-09
tags: [aeo, research, todo]
---

# AEO 案例研究：被 Claude 直接引用的内容源

## TODO
研究以下这些 source 是怎么做到被 Claude 直接检索和引用的。它们的内容结构、SEO/AEO 策略值得拆解，对 [[LoreAI]] 的 [[AEO as distribution strategy]] 有直接参考价值。

核心问题：**这些站点做对了什么，让 AI agent 在搜索时优先抓取并引用它们？**

## 被引用的 Sources

### 专题指南类（结构化教程）
- [Claude Code /simplify and /batch Commands Guide — claudefa.st](https://claudefa.st/blog/guide/mechanics/simplify-batch-commands)
- [Claude Code Scheduled Tasks: Complete Setup Guide — claudefa.st](https://claudefa.st/blog/guide/development/scheduled-tasks)
- [Claude Code Worktrees Guide — claudefa.st](https://claudefa.st/blog/guide/development/worktree-guide)
- [Claude Code Batch Processing Complete Guide — SmartScope](https://smartscope.blog/en/generative-ai/claude/claude-code-batch-processing/)
- [/simplify and /batch 完整指南 — Vibe Sparking AI](https://www.vibesparking.com/en/blog/ai/claude-code/2026-03-02-claude-code-simplify-batch-commands-guide/)
- [Scheduled Tasks: How to Put Claude on Autopilot — atal upadhyay](https://atalupadhyay.wordpress.com/2026/03/02/scheduled-tasks-how-to-put-claude-on-autopilot/)

### 个人实践类（经验分享）
- [How I'm Using /simplify & /batch to x10 My Code Reviews — Joe Njenga / Medium](https://medium.com/@joe.njenga/how-im-using-claude-code-new-simplify-batch-to-x10-my-code-reviews-888780a6a42a)
- [Some Claude Code Tips That Actually Changed How I Work — Ian Adera / Medium](https://ianodad.medium.com/some-claude-code-tips-that-actually-changed-how-i-work-b34f35b3dc73)
- [How I use Claude Code (+ my best tips) — Builder.io](https://www.builder.io/blog/claude-code)

### 官方/一手信息源
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [Run prompts on a schedule — Claude Code Docs](https://code.claude.com/docs/en/scheduled-tasks)
- [Boris Cherny (Anthropic) 发布 /simplify 和 /batch — Threads](https://www.threads.com/@boris_cherny/post/DVR-HzBkqRd/)
- [Anthropic turns Claude Code into a background worker — The Decoder](https://the-decoder.com/anthropic-turns-claude-code-into-a-background-worker-with-local-scheduled-tasks/)

### 聚合/Release Notes
- [Claude Code Release Notes March 2026 — Releasebot](https://releasebot.io/updates/anthropic/claude-code)
- [Building Automated Claude Code Workers with Cron — blle.co](https://www.blle.co/blog/automated-claude-code-workers)

## 初步观察（待验证）

- **claudefa.st** 被引用最多（3次），它的模式是：针对每个功能写一篇结构化指南，URL path 语义清晰（`/guide/mechanics/`, `/guide/development/`）
- **SmartScope** 也多次出现，走的是 "Complete Guide" 长文路线
- 功能发布后 **1 周内** 就有高质量指南的站点被引用率最高 — 速度是 AEO 的关键变量
- 标题里带 "Complete Guide"、"Setup Guide" 等结构化关键词的内容更容易被抓取

## 下一步
- [ ] 拆解 claudefa.st 的内容结构和发布节奏
- [ ] 对比 [[LoreAI]] 现有内容结构，找差距
- [ ] 测试：下次 Claude Code 发新功能时，LoreAI 能否在 1 周内发布结构化指南并被引用
