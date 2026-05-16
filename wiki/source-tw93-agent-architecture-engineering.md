---
type: source-summary
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-03-19-tw93-agent-architecture-and-engineering.md
tags: [wiki, source, agent-architecture, chinese, tw93]
---

# Source: Tw93 — 你不知道的 Agent：原理、架构与工程实践

## Summary
Long-form X article by **Tw93** (@hitw93), 2026-03-19. **1.69M views, 10,590 bookmarks.** The sequel to his earlier 2.8M-view Claude Code piece (now [[source-tw93-claude-code-architecture-governance]]). Systematic deep-dive into Agent architecture: **control flow, context engineering, tool design, memory, multi-agent organization, evaluation, observability, security** — then walks through OpenClaw's implementation as a concrete worked example. **The most comprehensive Chinese-language Agent engineering essay in our wiki.**

## Source
- **URL:** https://x.com/hitw93/status/2034627967926825175
- **Posted:** 2026-03-19 1:48 PM
- **Engagement (at fetch, 2026-05-16):** 1,694,131 views · 10,590 bookmarks · 5,089 likes · 1,302 reposts · 121 replies
- **Bookmark-to-like ratio:** ~2.08× (very high reference-saving intent)
- **Fetch method:** Playwright MCP
- **Companion piece:** [[source-tw93-claude-code-architecture-governance]] (his 2026-03-12 Claude Code piece)

## 要点解读

### 1. **三个改变了的判断（开篇就给）⭐**
Tw93 罕见地直接说"整理之后这几处我原来想错了"：
- **更贵的模型带来的提升没有想象中那么大**
- **Harness 和验证测试质量对成功率影响更大**
- 调试 Agent 行为时**优先检查工具定义**（多数工具选错都出在描述不准）
- **评测系统本身的问题，往往比 Agent 出问题更难发现**

这是少见的"诚实修订"开篇 —— 直接说哪几条判断和直觉不同。值得单独记下：**模型升级不是杠杆点，Harness 才是。**

### 2. **Workflow vs Agent —— Anthropic 的清晰定义 ⭐**
最简洁的术语澄清：
- **Workflow**：执行路径**由代码预先写死**
- **Agent**：执行路径**由 LLM 动态决定**

**核心区别在控制权掌握在谁手里。** 很多标着 Agent 的产品深入看其实更接近 Workflow。**两者并无高下。**

再加上 **五种 canonical patterns**（大多数 AI 系统都是这五种的组合）：
1. **Prompt Chaining** —— 顺序步骤
2. **Routing** —— 分类后定向到不同流程
3. **Parallelization** —— 分段（并发）+ 投票（多次取共识）
4. **Orchestrator-Workers** —— 中央 LLM 动态分解
5. **Evaluator-Optimizer** —— 生成器 + 评估器循环

**对 builder 的启示：很多场景不需要完整 Agent 自主权，几种 pattern 搭起来就够了。** 新建 [[agent-vs-workflow]] 完整抓住这个 taxonomy。

### 3. **Harness 比模型更关键 —— OpenAI Agent-First 案例 ⭐**
最有冲击的数据：**OpenAI 内部 3 个工程师 5 个月写了百万行代码，1500 个 PR，传统开发 10 倍速度。**

不是模型多强，是几个工程决策做对了：
- **知识必须在代码库本身** —— 外部文档对运行中的 Agent 不可见
- **AGENTS.md 只保留约 100 行作为索引**，细节拆到各 docs 目录按需引用

这跟 [[garry-tan|Garry Tan]] 的 [[resolvers|resolver]] 模式完美呼应 —— **"AGENTS.md 100 行" = 路由表，不是知识库**。Garry 是同一个洞察。

Harness 包含四部分：**验收基线 + 执行边界 + 反馈信号 + 回退手段**。

### 4. **上下文工程的反直觉之处：稳定的大系统提示比频繁变动的小提示成本更低 ⭐**
这条是最反直觉的关键点。背后是 Prompt Caching 的机制 ——
- KV cache 命中前提是**精确前缀匹配**
- 任何 token 不同都破坏匹配
- **稳定的大系统提示一次性付写入成本，后续每次调用享受 90% 折扣**
- 频繁小变化的系统提示反而每次都是写入价

**对设计的影响：常驻层短而稳定不只为省 token，是为保护 cache 命中。** Skills 延迟加载的好处也在这里：**按需注入不破坏稳定前缀**。

我把这点更新到了 [[prompt-cache-optimization]]。

### 5. **Skills 设计：描述符是路由条件，不是功能介绍 ⭐⭐**
最有迁移价值的 Skills 写法洞察：
> "**何时该用我** 比 **我能做什么** 重要得多。"

**反例（anti-examples）不是可选项**：
- 没反例 → 准确率从 73% 掉到 53%
- 加反例 → 升到 85%，**响应时间还降了 18.1%**

**最直接的写法**：`Use when / Don't use when` + 几条反例。

Tw93 给的**三个 Skills 反模式：**
- 几百行工作手册全塞进 Skill 正文（应该拆 supporting files）
- 一个 Skill 试图覆盖 review、deploy、debug、incident 五件事
- 有副作用的 Skill 没显式限制调用时机

把这些更新到了 [[agent-skills-standard]]。

### 6. **Initializer Agent + Coding Agent —— 长任务最优解 ⭐**
长任务最常见的失败不是单步报错，**是 session 结束时任务没做完**。即使 compaction 也挡不住。

**正确做法**：拆两个 Agent：
- **Initializer Agent** 只第一轮跑一次：生成 `feature-list.json`、初始 git commit、`claude-progress.txt`。**把任务变成可持久化的外部状态。**
- **Coding Agent** 循环执行多 session：每次从 `claude-progress.txt` + git log 恢复现场，定位当前任务，实现，跑测试，更新 `passes` 字段，提交退出

**进度放文件里不放上下文里**。所有功能 `passes: true` 才算完成。

这正是 [[ralph-wiggum|Ralph Wiggum]] 模式的结构化版本。

### 7. **多 Agent 三件事必须先有 (协议、任务图、隔离边界) ⭐**
多 Agent 协作一旦靠自然语言对齐就会出问题。模型记不稳谁承诺了什么、谁在等谁。**协议先于协作：**
- **JSONL inbox 协议** —— 主 Agent → 子 Agent 派发，子 Agent 只回**摘要**（搜索和调试细节留在子 Agent 自己的上下文）
- **`.tasks/`** —— 记录任务图和依赖
- **`.worktrees/`** —— 隔离每个子 Agent 的文件修改

**顺序：协议先定，隔离先做，再谈协作和并行。**

**多 Agent 错误层层放大（值得记）**：
> "A 偏 → B 强化 → C 叠加 → 所有 Agent 收敛到同一个高置信度的错误结论"
>
> 解决：**交叉验证**（让某个 Agent 独立判断，不顺前面结论走）。

### 8. **评测系统本身可能是 bug —— 这是最大的盲区**
"看到 Agent 表现下降，立刻改 Agent" 是个常见误区。**评测系统出问题时，你拿到的是失真信号，基于它改 Agent 方向可能从一开始就错。**

**Pass@k vs Pass^k 不能混用：**
- Pass@k 适合开发阶段（理论上能不能做到）
- Pass^k 适合上线前（已有功能有没有被改坏）

**Anthropic 的机票预订例子（这个故事值得记）：**
Opus 4.5 一次运行中**发现了航空公司政策的漏洞**，给用户找到更便宜方案。**按预设路径打分会判失败，按最终结果是更好方案。** 这就是 transcript vs outcome 的区别 —— **只看执行过程会漏掉这种情况**。

20-50 个真实失败案例就够启动评测。

新建 [[agent-evaluation-traps]] 把这部分完整抓住。

### 9. **OpenClaw 五层架构 —— 给 [[openclaw]] 页加了大量细节**
Tw93 把 OpenClaw 拆成五层：
1. **Gateway** —— WebSocket 服务统一路由消息
2. **Channel 适配器** —— 23+ 渠道统一接口，新增渠道不改 Agent 代码
3. **Pi Agent** —— 维护主循环、会话状态、调度
4. **工具集** —— shell / fs / web / browser / MCP，按 ACI 原则设计
5. **上下文 + 记忆** —— Skills 延迟加载 + MEMORY.md，50% token 阈值自动整合

**关键工程决策：**
- Channel 和 Agent 通过 **MessageBus** 解耦（cron / heartbeat 让系统不再只有用户消息一个入口）
- 同一 sessionKey 必须串行（否则并发写历史 + compact 有竞态）
- **Session 由 AgentLoop 统一管理，不下沉到 Channel 层** → 换 Discord / 飞书核心代码不动
- **任务超过半小时 → 崩溃恢复是必选项不是可选项**

### 10. **Prompt Injection 防御：source-sink 模型 ⭐**
> "单靠输入过滤基本挡不住。**重点不是识别所有攻击，而是让 Agent 即使被注入也没机会把危险动作执行出来。**"

实操：
- **不给 Agent 不需要的工具**（没 sink，source 注入无法落地）
- **写操作执行前必须用户确认**，不能静默执行
- **外部内容进入上下文时显式标注来源**
- **关键操作引入独立 LLM 复核**

### 11. **八个常见反模式（直接抄）**
1. 系统提示当知识库 → 关键规则被忽略
2. 工具数量失控 → Agent 频繁选错
3. 验证闭环缺失 → 说完成了但没法验证
4. 多 Agent 无边界 → 状态漂移
5. 记忆不整合 → 长对话第 20 轮后决策质量下降
6. 没有评测 → 改了不知道有没有回归
7. **过早引入多 Agent → 协调开销超并行收益。先验证单 Agent 上限再扩展**
8. **约束靠期望不靠机制 → 规则在文档里 Agent 选择性遵守。改用工具验证 / Linter / Hook**

## Pages created from this source
- [[agent-vs-workflow]] — concept (Anthropic taxonomy + 5 patterns)
- [[agent-evaluation-traps]] — concept (Pass@k vs Pass^k + grader / env failure modes)
- [[source-tw93-agent-architecture-engineering]] — this page

## Pages updated from this source
- [[tw93]] — added 2nd major article + production observations
- [[openclaw]] — 5-layer architecture deep-dive + key engineering decisions (MessageBus, session at AgentLoop layer, cron+heartbeat)
- [[harness-design]] — "Harness > Model" framing + OpenAI Agent-First case study (1M LOC, 1500 PRs, 10x speed by 3 engineers in 5 months)
- [[prompt-cache-optimization]] — "stable-large prompt costs less than dynamic-small one" insight + Skills-延迟加载-protects-cache
- [[agent-skills-standard]] — Skills design insights: Use-when/Don't-use-when format, 73%→53%→85% accuracy data, three anti-patterns
- [[multi-agent-architecture]] — JSONL inbox + worktree + task graph; protocol-before-collaboration ordering
- [[verification-loops]] — eval-system-itself-as-bug as a category; transcript vs outcome distinction
- [[ralph-wiggum]] — Initializer + Coding Agent split as structured Ralph pattern

## Connections
- Related: [[tw93]], [[agent-vs-workflow]], [[agent-evaluation-traps]], [[openclaw]], [[harness-design]], [[multi-agent-architecture]], [[prompt-cache-optimization]], [[agent-skills-standard]], [[verification-loops]], [[ralph-wiggum]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-03-19-tw93-agent-architecture-and-engineering.md | Initial creation |
