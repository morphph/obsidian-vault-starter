---
type: source-summary
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-09-openai-cookbook-using-goals-in-codex.md
  - raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md
  - raw/2026-05-12-openai-cookbook-agent-improvement-loop.md
tags: [wiki, source, openai, codex, official-docs, cookbook]
---

# Source: OpenAI Codex Cookbook Trilogy — Goals · Iterative Repair · Improvement Loop

## Summary
Three OpenAI Developers Cookbook articles published over four days (May 9 / 11 / 12, 2026), forming **OpenAI's official Codex playbook trinity** parallel to Anthropic's harness / skills / Computer-Use docs. **The official documented version of what [[chris-hayduk|Chris Hayduk]]'s 2026-05-11 X-thread playbook described informally.** Together they cover: (1) how to write goals that complete, (2) how to build closed-loop repair workflows, (3) how to systematically improve an agent harness over time. All three are practical, code-heavy, written by OpenAI staff.

## Sources

| Date | Title | Author | URL |
|------|-------|--------|-----|
| 2026-05-09 | **Using Goals in Codex** | Raj Pathak + Stefano Fabbri | [link](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) |
| 2026-05-11 | **Build Iterative Repair Loops with Codex** | Shreekant Agrawal | [link](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex) |
| 2026-05-12 | **Agent Improvement Loop with Traces, Evals, and Codex** | Wesley Pasfield | [link](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop) |

Fetch method: WebFetch (all three are static cookbook pages)

## 要点解读

### 1. **三篇拼起来 = OpenAI 官方版"完整 Codex 实践 trilogy" ⭐**
这三篇在四天内连发，不是巧合。OpenAI 在系统地推 Codex 作为生产级 agentic CLI 的方法论。三个层级覆盖：

| 层级 | 文章 | 解决的问题 |
|------|------|-----------|
| **单 task 完成** | Using Goals in Codex | 怎么写一个能稳定完成的 `/goal` |
| **单 artifact 修复** | Iterative Repair Loops | 怎么让 agent 关掉自己的 review → repair → validate 循环 |
| **整个 agent 改进** | Agent Improvement Loop | 怎么用 trace + 反馈 + eval 把 agent 的 harness 持续迭代 |

**和 Anthropic 的 docs 对照：**
- Anthropic 的 [[claude-code-goal|`/goal`]] docs ≈ OpenAI 的 "Using Goals"
- Anthropic 的 [[agent-skills-standard|Skills]] docs ≈ OpenAI 的 Agents SDK + Promptfoo
- Anthropic 的 [[computer-and-browser-use|Computer Use]] docs ≈ OpenAI 还没出对应版

**跨厂商收敛信号 +1**：`/goal`、tool-as-state、structured handoff、trace-based observability —— 都是双方都在做的事。

### 2. **强 Goal 的 6 个要素 ⭐⭐ —— 比 Chris Hayduk 的版本更结构化**
OpenAI 官方版给的 **6 个 element**：

1. **Outcome** — 完成时什么应该是 true
2. **Verification surface** — 哪些 tests / benchmarks / artifacts / reports 证明成功
3. **Constraints** — 什么不能 regress
4. **Boundaries** — 允许的 files / tools / data / resources
5. **Iteration policy** — 失败后怎么选下一步
6. **Blocked stop condition** — 什么情况下停下来报告 blockers

**Weak Goal：** "Improve performance"

**Strong Goal（OpenAI 给的样板，可以直接抄）：**
> "Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Use only the checkout service and related tests. Between iterations, record changes, benchmark results, and next experiments to attempt. If blocked, stop with attempted paths, evidence, and blockers."

**对比 Chris Hayduk 的 3 个 tips：**
- Chris: 量化目标 + 紧 feedback loop + 三个 markdown 文件
- 官方：6 个 element + thread-scoped state + evidence-based completion

**两者不矛盾，是不同抽象层级**。Chris 是 *practitioner heuristics*；官方是 *complete formalism*。一起读最完整。

### 3. **Iterative Repair Loop —— 三阶段分离的关键设计 ⭐**
**Review → Repair → Validate**，三阶段**严格分离**：

| 阶段 | 做什么 | **不**做什么 |
|------|------|--------|
| **Review** | 检视 artifact，识别 issues | **永远不编辑文件** |
| **Repair** | 对**副本**做有针对性的修改 | 不决定什么是 issue |
| **Validate** | 端到端执行，报告 deltas | 不修复 |

**为什么分离这么关键：**
- 如果 Review 能编辑 → 混淆"什么是错的"和"该怎么做"
- 如果 Repair 能决定什么是错的 → 跳过调查直接行动（Tw93 说的"agent 有正确工具却选了聪明"）
- 如果 Validate 和 Repair 合并 → eval 被自己模型的 output bias

**结构化 JSON handoff** —— 每阶段输出严格 schema 的 JSON，**强迫明确的判决**（没有"还不错"），允许阶段间机械化传递。

**Validation 是反馈不是教师 ⭐：**
> "Validation executes notebooks end-to-end, capturing execution failures as structured feedback. **This grounds subsequent repairs in observed behavior rather than inference from diffs alone.**"

Repair agent 不能争辩"这应该 work"。Notebook 要么跑要么不跑。**反馈信号是经验的，不是编辑的。**

新建 [[iterative-repair-loop]] 抓住这个 pattern。

### 4. **Agent Improvement Flywheel —— 6 步 ⭐⭐**
最雄心的一篇。**单 task 改进 → 整个 agent 系统持续改进**。

6 步循环：
1. **Synthetic data**（含**有冲突的信号** —— 这是关键，因为 agent 在冲突处失败）
2. **Define harness** —— system prompt + tool policies + required artifacts + validation rules
3. **5 个 traced run**（OpenTelemetry-compatible）
4. **Human + LLM feedback**
5. **Convert to evals**（用 Promptfoo）
6. **Optimize with HALO** —— 给 harness 改进 ranking by impact
7. **Hand off to Codex** —— Codex 生成开发者面向的修改建议

**为什么 5 个 trace 而不是 50/500：** 在 GPT-5.5 下大约 20 分钟一轮。**5 个足以暴露失败模式但不烧整天**。复利在于**每周做一轮**，不在于一次大量采样。

**6 个 required artifact per run（可以抄）：**
| Artifact | 用途 |
|----------|------|
| `summary_answer.md` | 标题答案 |
| `investment_memo.md` | 详细 review with evidence sections |
| `risk_register.json` | 结构化 risks + 证据 |
| `open_questions.md` | 缺失证据 + 未决问题 |
| `citations.json` | 机器可读的 claim→source 映射 |
| `evidence_table.csv` | claim 和 source 的审计 trail |

**关键设计**：**machine-readable (.json/.csv) 和 human-readable (.md) 分开**。Eval pipeline parse JSON；人审 markdown。

新建 [[agent-improvement-flywheel]] 抓住这个 pattern。

### 5. **OpenTelemetry trace = 跨平台 agent 可观测性 ⭐**
最 underrated 的工程细节：Agents SDK span 直接映射到 OpenTelemetry：
- `agent` → AGENT
- `generation` / `response` → LLM
- `function` / `mcp_tools` → TOOL
- `handoff` → CHAIN

**意味着 agent 执行 trace 跟后端服务在同一个 observability infrastructure 里** —— 同一个 dashboard、同一个查询语言、同一个 retention。**Production 来说非常 powerful**。

### 6. **HALO 是 OpenAI 的 self-healing-resolver 雏形（推测）**
HALO 给 harness 改进 ranking by impact。文档没披露算法。**但跟 Garry Tan 4/15 floated 的 "self-healing resolver"（用 traffic 进化 routing 表）是同一思路** —— 都是用观察到的执行 trace 自动建议系统改进。

OpenAI 把它做成了 product feature；Garry 把它做成了 vision。**收敛到了同一个解法。**

### 7. **6 个失败模式（值得记 —— 不是 AI 专属，是 diligence 专属）**
Cookbook 的 diligence agent 例子明确针对的失败：
- 把管理层叙述当作经过验证的指标（即使结构化数据不一致）
- 报告未验证的估计（如 NRR）像是官方批准
- 把母账户集中度 collapse 成弱化的法人视图
- 夸大认证（"SOC 2 完成" 但只是 Type I）
- **产出漂亮答案但 citations 不完整**

**最后一条**是 agent 版的 [[silent-fallback-antipattern|silent fallback antipattern]] —— 看着好，一查就崩。

### 8. **生产 stack（直接列出来供参考）**
- **OpenAI Agents SDK** —— 执行
- **Promptfoo** —— eval（Node-based）
- **HALO** —— optimization ranking
- **OpenTelemetry JSON Lines** —— trace transport
- **Local Python utilities**:
  - `check_evidence_coverage.py` —— audit citations against real files
  - `validate_output_contract.py` —— verify required artifacts exist with expected schema

### 9. **对本 vault 的具体启示**
- `/lint` 可以**正式分阶段**化为 Review→Repair→Validate（这次的 lint 我已经做得接近，但还可以更结构化）
- `/draft` 在反复修改时可以用 iterative repair pattern
- `/ingest` 可以加 `citations.json` + `evidence_table.csv` 输出 —— 让我们的 ingest 也变成"6 artifact per run"模式
- 长期：加一个 `/improve` weekly workflow 走最近 `/lint` + ingest log → 提出 wiki 约定的修改建议

## Pages created from this source
- [[iterative-repair-loop]] — concept (Review → Repair → Validate three-phase pattern)
- [[agent-improvement-flywheel]] — concept (6-step trace-to-harness-change flywheel)
- [[source-openai-codex-cookbook-trilogy]] — this page (combined source summary for all three articles)

## Pages updated from this source
- [[chris-hayduk]] — added "official version" cross-reference for the three OpenAI cookbook docs
- [[claude-code-goal]] — added cross-vendor parallel + 6-elements goal-writing formalism from official docs
- [[agentic-loop-tracking-files]] — referenced (PLAN/EXPERIMENTS/SCRATCHPAD pattern is consistent with the 6-artifact pattern)
- [[verification-loops]] — eval-as-feedback insight reinforced
- [[index]], [[log]]

## Connections
- Related: [[chris-hayduk]], [[iterative-repair-loop]], [[agent-improvement-flywheel]], [[claude-code-goal]], [[agentic-loop-tracking-files]], [[verification-loops]], [[agent-evaluation-traps]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-09-openai-cookbook-using-goals-in-codex.md | Initial creation (article 1 of 3) |
| 2026-05-16 | raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md | Added article 2 of 3 |
| 2026-05-16 | raw/2026-05-12-openai-cookbook-agent-improvement-loop.md | Added article 3 of 3 |
