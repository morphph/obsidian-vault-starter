---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-mattpocock-chapter-creator-thread.md
tags: [wiki, source, x-thread, matt-pocock, workflow]
---

# Source: Matt Pocock — Chapter-Creator AFK Flow (X Screenshot)

## Summary
Matt's 6-step tweet describing how he built an automatic video-chapter creator: `/grill-with-docs` → prototype prompt → agent built TUI on live data → iterate system prompt → AFK one-shot. This is the **seed text** for the idea-to-AFK-agent runbook.

## 要点解读

### 1. 6 步流程的真正洞察：你不直接写 AFK agent
Tweet 表面读起来是"我做了个 chapter creator"。但**真正的方法论是**：从"想法"到"AFK agent 自动跑"中间有 5 个中间步骤。直接跳到 AFK 是新手错误——你会写出一个跑得很久但产出垃圾的 loop。**正确路径是**：先 interactive 把 prompt 调到位，**再** AFK。

### 2. /grill-with-docs 是 Phase 1 的入口
"I wanted to create..."（含糊愿望）→ "/grill-with-docs"（结构化澄清）。一句模糊的"我想要"经过 grilling 变成具体的 spec + CONTEXT.md。**这是从想法到可执行 prompt 的最重要转换。**

### 3. "Prototype the prompt" —— 步骤 3 是关键 unlock
他对 agent 说："let's prototype the prompt passed to the agent，not really knowing what to expect."

**注意"passed to the agent"——他已经在为 AFK 设计**，但不知道中间需要什么脚手架。Agent 主动给他造了 TUI（步骤 4），这是 agent emergent behavior：当你说"我要把这个 prompt 给另一个 agent"，当前 agent 会推断你需要 dev tools。

**实操：**你也可以这样说："让我们 prototype 这个准备给 AFK agent 的 prompt"，不要预设具体形态。让 agent 推断你需要什么 dev infrastructure。

### 4. TUI on live data —— Phase 3 的核心模式
这是把 [[html-as-output-format]] / [[throwaway-editors]] 的逻辑搬到 terminal：**为 prompt 调试做一个一次性的 UI，pointing at your real production data**。看到真实输入和输出，比看 spec 文档好 10 倍。

**为什么 terminal 而不是 HTML？**因为他在 dev loop 里，terminal 更快；prompt iteration 不需要漂亮 UI。**实操：**任何 AFK pipeline 开发都要先建这个调试 surface（TUI 或简单 HTML），不要直接调线上。

### 5. "until it was awesome" —— 隐式的人工 quality gate
没有 formal eval，没有打分系统。就是看 output。**为什么 Matt 用得起这个：**他对自己的 chapter creator 输出"什么是好"有清晰直觉。**对你：**做你熟悉领域的 AFK pipeline 时这样也行；做不熟悉领域时需要 formal eval（参考 [[verification-loops]] / [[quality-gate-loop]]）。

### 6. AFK 是 reward, not entry point
最后一步"AFK agent one-shotted it"——AFK 是 prompt 收敛之后的奖励，不是入口。前面 5 步都是为了让 AFK 这一步可靠。**这是 Ralph 文献里常被忽略的：所有人都讨论 loop，但 prompt-convergence 阶段才是质量决定点。**

### 7. 同一个 agent 扮演 3 个角色
Discovery → Prototype → Execution 全是 Claude Code 做的，只是 prompt 和上下文不同。**没有 specialized model**，是 same model with different role prompts。这是 [[skill-as-method-call]] 的实践——skills 让 agent 在不同阶段表现成不同 agent。

## Connections
- [[matt-pocock]]
- [[idea-to-afk-agent-flow]] (the unpacked methodology)
- [[grill-with-docs]] (Phase 1)
- [[sandcastle]] (Phase 5 infrastructure)
- Related: [[throwaway-editors]], [[html-as-output-format]]

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Captured from screenshot (X URL not preserved) |
