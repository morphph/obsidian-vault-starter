---
type: source-summary
created: 2026-05-20
last-updated: 2026-05-20
sources:
  - raw/2026-05-20-openai-codex-subagents-docs.md
tags: [wiki, source, openai, codex, subagents, parallel, official-docs]
---

# Source: OpenAI Codex Subagents

## Summary
Codex Subagents spawn specialized agents in parallel and collect results in one response. Default-enabled, **`max_threads=6`** concurrency, **`max_depth=1`** nesting (prevents recursion). Three built-in agents (default / worker / explorer), TOML-configured custom agents at `~/.codex/agents/` or `.codex/agents/`, optional per-agent `sandbox_mode` / `model` / `mcp_servers`. Experimental **`spawn_agents_on_csv`** primitive for batch audits across many similar items. Per-agent sandbox inheritance with runtime propagation.

## Source Metadata
- **URL:** https://developers.openai.com/codex/subagents
- **Publisher:** OpenAI Developers (official docs)
- **Fetch date:** 2026-05-20

---

## 要点解读（12-Section Compressed Study Guide）

### 1. 元信息
官方 docs；与 Claude Code subagents 直接对应；2026 年内成熟。

### 2. 核心论点
单 agent 顺序处理复杂任务慢且容易混淆角色；spawn 专用 subagent 并行 + 收集结果 = 更快 + 更清晰职责分离。

### 3. 论证结构
```
1. 3 个 built-in 角色（default / worker / explorer）
   → 默认即可用
2. 自定义 agent TOML
   → 角色 specialization
3. max_threads 限并发，max_depth 限递归
   → 防爆炸
4. spawn_agents_on_csv 批处理
   → 重复审计的结构化原语
```

### 4. 关键概念字典

> **`max_threads = 6` (默认)**
> - **是什么**：同时跑的 subagent 上限
> - **为什么重要**：防止 token 爆炸 + 模型 API rate limit
> - **反面**：调大到 20+ 时 API 队列堆积，反而慢

> **`max_depth = 1` (默认)**
> - **是什么**：subagent 是否能 spawn 自己的 subagent
> - **为什么重要**：防止递归爆炸 —— 1 = subagent 不能再 spawn，只有 parent 能
> - **直觉类比**：fork bomb prevention

> **`spawn_agents_on_csv` (实验)**
> - **是什么**：从 CSV 行批量 spawn 同 prompt 模板的 worker，每个 worker 调用 `report_agent_job_result` 一次
> - **为什么重要**：把"对 1000 个文件做同样审计"变成 first-class 原语
> - **直觉类比**：MapReduce 的轻量版

> **Sandbox inheritance + runtime propagation**
> - **是什么**：subagent 默认继承 parent sandbox；运行时改 `/permissions` 会向下传
> - **为什么重要**：safety 一致性 + 不会因为 spawn 而绕开 sandbox

### 5. 框架与心智模型

**典型 3-agent triad（OpenAI 给的 PR review 例子）**：

```
pr_explorer (read-only)
    → 提供"代码地图"

reviewer (gpt-5.4, 高 reasoning effort)
    → 提供"质量判断"

docs_researcher (有 MCP server)
    → 提供"API 验证"
```

**这是 Iterative Repair Loop 的并发实现**：Review/Repair/Validate 三阶段也可以做成三个 subagent。

### 6. 关键数据
- **3** 个 built-in agent
- **`max_threads = 6`** 默认并发
- **`max_depth = 1`** 默认（禁递归）
- **CSV batch** 通过 `spawn_agents_on_csv` 实验性原语

### 7. 关键引语
> "Codex only spawns a new agent when you explicitly ask it to do so."
> ⭐ 不是隐式 spawn —— prompt 里没 trigger 不会 fork。

> "Each worker must call `report_agent_job_result` exactly once."
> ⭐ CSV batch 的 invariant。

### 8. 实操指南

**custom agent 模板**（`.codex/agents/reviewer.toml`）：
```toml
name = "reviewer"
description = "Focused PR reviewer for correctness and security"
developer_instructions = """
You are a senior reviewer. Read the diff and flag:
- correctness bugs
- security issues
- missing edge case handling
Do not edit files. Output structured JSON.
"""
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
```

### 9. 对比与反对意见

**vs Claude Code subagents**：
- 形状一致：explicit spawn / per-agent sandbox / MCP per agent
- Codex 多了：`spawn_agents_on_csv` 批处理原语
- Anthropic 多了：first-class TUI agent view + worktree 自动隔离
- **大方向 parity**

### 10. wiki 连接

- [[source-claude-code-subagents-docs]] —— 跨厂商对应
- [[source-claude-code-agents-overview]] —— Anthropic 的多 agent 视角
- [[iterative-repair-loop]] —— 三阶段可用 subagent 实现
- [[source-openai-codex-cookbook-trilogy]] —— trilogy 的 Iterative Repair 三阶段适合用 subagent triad 落地

### 11. 对用户启示
- 短期：blog2video chapter splitter 里 reviewer/repairer/validator 可以用 subagent triad 实现
- 中期：写 "OpenAI Codex Subagent 三阶段中文实操" SEO 真空

### 12. 一句话总结
**"Codex Subagents = explicit parallel spawn + per-agent sandbox + CSV batch；与 Claude Code subagents 大方向 parity，CSV 批处理是 Codex 独有的批量审计原语。"**

---

## Connections
- Related: [[source-claude-code-subagents-docs]], [[source-claude-code-agents-overview]], [[iterative-repair-loop]], [[source-openai-codex-cookbook-trilogy]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-20 | raw/2026-05-20-openai-codex-subagents-docs.md | Initial creation |
