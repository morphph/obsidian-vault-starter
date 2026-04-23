# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** 生成了一篇中文对比文章，主题为 Claude Memory vs CLAUDE.md 两套持久化机制。

**Key Exchanges:**
- 输出了完整的 compare 类型文章草稿，slug: `claude-memory-vs-claude-md`，frontmatter 已配置，含 related_blog 和 related_glossary 交叉链接。

**Decisions Made:**
- 文章定位：CLAUDE.md 管"怎么做"（团队规则、版本控制），Memory 管"跟谁做、为什么做"（个人上下文、自动积累）
- 两者互补而非替代，推荐搭配 Skills 构成三层架构

**Action Items:**
- 确认文章是否已写入 `drafts/` 目录（对话中只见到输出内容，未见 Write 工具调用）
- 若未落盘，需执行写入并更新 `wiki/log.md`