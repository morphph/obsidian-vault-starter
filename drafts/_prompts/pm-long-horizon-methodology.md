# Prompt：撰写 PM 视角的长跑 AI 任务方法论文章

## 主题

我想写一篇中文长文，**从 PM（产品经理）的视角**讲清楚：如何让 AI agent 跑通一个长跑任务（long-horizon task）。

目标读者是想用 AI 自主开发的 PM / 独立 builder / 非全职工程师 —— 不是工程师视角的 "how to set up the loop"，而是 PM 视角的 "如何把一个需求做到 agent 能自主跑完"。

## 我现在的判断（可挑战）

我目前的理解是：**AFK / autonomous loop / Ralph Wiggum 不是按一个按钮的魔法，而是 PM 完整工作流程的最后一段**。前面还有 discovery、写 spec、定义验收标准、持久化到文件等等。很多人误以为 "AFK = 一句话 prompt + 开 loop"，这是 vibe coding 的延伸，不是 PM 工作。

但这只是我现阶段的假设，**你看完源之后可以挑战这个 framing**。如果有更好的角度（比如不分阶段，而是按"4 个反模式"组织；或者按"3 个心智转换"组织）请告诉我。

## 核心信息源（全部已 ingest 在 wiki/）

起手先 read `wiki/index.md` 看完整 catalog。围绕这个主题的关键页面：

**方法论核心**：
- Matt Pocock 的 idea-to-AFK-agent flow（`wiki/idea-to-afk-agent-flow.md` 及关联 sandcastle / grill-with-docs / context-md-pattern / vertical-slicing / hitl-vs-afk）
- George Nurijanian 的 PM 视角 /goal 方法论（`wiki/source-nurijanian-goal-for-pms.md` + `wiki/goal-template.md` + `wiki/agent-ready-requirements.md`）
- OpenAI 官方 long-horizon 三层文档（`wiki/source-openai-long-horizon-tasks-codex.md` awareness 层 / `wiki/source-openai-codex-cookbook-trilogy.md` conceptual 层 / `wiki/source-openai-codex-use-case-follow-goals.md` operational 层）
- Claude Code /goal 官方（`wiki/claude-code-goal.md`）
- Chris Hayduk 的三文件 pattern（`wiki/source-chrishayduk-codex-goals-effectively.md` + `wiki/agentic-loop-tracking-files.md`）

**支撑源**：
- Khairallah 的 context engineering（`wiki/source-khairallah-context-engineering.md`）
- Ralph Wiggum 历史脉络（`wiki/ralph-wiggum.md`）

## 写作风格

- **中文为主体**。英文只在两处：概念原名（中文译名后加括号注）+ 关键原文引语保留英文附中文意译。不要平行翻译。
- **每个论点必须挂源**：用 `[[wiki-page-name]]` 引用。
- **PM 视角**：不要陷入 "如何配置 Stop hook" 这类工程细节。
- **可以反共识**：George Nurijanian 的语气，实操、克制、有立场。

## 输出

保存到 `drafts/pm-long-horizon-methodology.md`（或你建议的更好文件名）。

## 第一步

**不要直接开写**。先 read `wiki/index.md` 和上面列的核心源，然后告诉我：
1. 你看完之后对这个主题的 framing / 结构有什么提议？（可以同意我的 5 阶段假设，也可以提出完全不同的组织方式）
2. 你看到哪些有趣的角度 / 反共识洞察 / 跨源对比，是值得作为文章 hook 的？
3. 对齐 framing 之后再开始 draft。
