# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** 生成了一篇中文对比文章草稿：Codex CLI vs Claude Code

**Key Exchanges:**
- 无对话记录，仅输出了一篇完整的比较文章草稿（markdown 格式，面向 LoreAI 博客）

**Decisions Made:**
- 文章定位：两者不是竞争关系，而是互补工具，核心差异是「异步委托 vs 实时协作」
- 推荐框架：任务边界清晰 → Codex；探索性/复杂重构 → Claude Code；最优解是两者并用
- 文章结构：TL;DR → 概览 → 核心对比表 → 架构差异 → 上下文系统 → 多任务 → 安全 → 场景推荐 → FAQ

**Lessons Learned:**
- Codex CLI 核心优势：云端异步、沙箱隔离、GitHub 原生集成、Pro/Plus 免费
- Claude Code 核心优势：本地实时、七层可编程架构（CLAUDE.md + SKILL.md + Hooks + MCP）、探索性任务
- 关键区分维度：交互模式（异步 vs 同步）> 模型质量差异

**Action Items:**
- 检查 frontmatter 中的 `related_blog` 链接是否与实际已发布文章 slug 一致（codex-complete-guide, claude-code-seven-programmable-layers, codex-vscode, first-few-days-with-codex-cli）
- 文章待人工润色后发布到 LoreAI `/zh/compare/` 路径下