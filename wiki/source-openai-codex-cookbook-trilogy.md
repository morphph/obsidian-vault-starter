---
type: source-summary
created: 2026-05-16
last-updated: 2026-05-18
sources:
  - raw/2026-05-09-openai-cookbook-using-goals-in-codex.md
  - raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md
  - raw/2026-05-12-openai-cookbook-agent-improvement-loop.md
tags: [wiki, source, openai, codex, official-docs, cookbook, agentic-loop]
---

# Source: OpenAI Codex Cookbook Trilogy — Goals · Iterative Repair · Improvement Loop

## Summary
Three OpenAI Developers Cookbook articles published over **four days** (May 9 / 11 / 12, 2026), forming **OpenAI's official Codex playbook trinity** parallel to Anthropic's harness / skills / Computer-Use docs. **The official documented version of what [[chris-hayduk|Chris Hayduk]]'s 2026-05-11 X-thread playbook described informally** (Hayduk's post landed mid-trilogy). Together they cover three nested levels: (1) how to write `/goal` that actually completes, (2) how to build closed-loop Review→Repair→Validate workflows, (3) how to systematically improve an agent harness using traces + evals + Codex.

## Source Metadata

| Date | Title | Author(s) | URL |
|------|-------|-----------|-----|
| 2026-05-09 | **Using Goals in Codex** | Raj Pathak + Stefano Fabbri | [link](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) |
| 2026-05-11 | **Build Iterative Repair Loops with Codex** | Shreekant Agrawal | [link](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex) |
| 2026-05-12 | **Agent Improvement Loop with Traces, Evals, and Codex** | Wesley Pasfield | [link](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop) |

- **Publisher:** OpenAI Developers Cookbook (official)
- **Fetch method:** WebFetch (static cookbook pages)
- **Total span:** 4 days (5/9 → 5/12)
- **Combined as trilogy because:** they're nested in abstraction level (single task → single artifact → entire system), all OpenAI-staff authored, all reference each other implicitly

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息

- **作者/出版方**：**OpenAI Developers Cookbook（官方）**
  - **不是 marketing blog，是 dev docs** —— OpenAI 推荐做法的"硬通货"
  - 三篇作者均为 OpenAI 内部员工：Raj Pathak + Stefano Fabbri / Shreekant Agrawal / Wesley Pasfield
- **来源**：openai.com 官方 cookbook 域名 = developers.openai.com/cookbook
- **发表时间窗口**：2026-05-09 ~ 2026-05-12（**4 天内连发 3 篇**）
- **节奏暗示**：
  - 4 天 3 篇 = **集中推进**。不是写作 backlog 流出，**是一次 product launch 的配套文档**
  - Chris Hayduk 的 X 长文夹在中间（5/11）—— **OpenAI 工程师在中间一天用社交媒体打公关**
  - 这一周 = **OpenAI 推广 Codex `/goal` 模式的"内容轰炸周"**
- **在生态中的位置**：
  - 与 **Anthropic 的 docs 三角**形成对照：
    - Anthropic `/goal` docs ([[source-claude-code-goal-and-agent-view-docs]]) ↔ OpenAI "Using Goals"
    - Anthropic Skills ([[agent-skills-standard]]) ↔ OpenAI Agents SDK + Promptfoo
    - Anthropic Harness ([[source-anthropic-harness-design]]) ↔ OpenAI Improvement Loop
  - 在 wiki 里是**第一组完整的 OpenAI 官方 doc**（之前 Chris Hayduk 是个人 X 帖，不是 official doc）
- **可信度等级**：⭐⭐⭐⭐⭐（最高）—— 官方 cookbook = OpenAI 推荐做法
- **影响力指标**：cookbook 没有 X-style engagement metrics，但开发者社区引用是间接信号；预期高（OpenAI 官方 + Codex 热度）

### 2. 核心论点（Thesis）

**作者主张**：单 task 完成、单 artifact 修复、整个 agent 改进是三个嵌套抽象层级，**每一层都需要不同的 loop 设计**。**因为** loop 是 agentic 系统的核心控制结构，**而且**不同抽象层的 loop 有不同的状态、不同的验证机制、不同的停止条件，**所以**生产级 Codex 工作流必须三层都设计对——下层 loop 喂上层 loop，上层 loop 给下层 loop 改 spec。

简化压缩包：**"三层嵌套 loop = OpenAI 推荐的 Codex 完整方法论。`/goal` 控完成；Iterative Repair 控质量；Improvement Loop 控演化。"**

更激进版本：**"agentic 系统就是 loop 套 loop。OpenAI 帮你定义了三个标准层级。"**

### 3. 论证结构

```
[5/9] Using Goals in Codex（最小单元：让单个 task 完成）
   1. Prompt vs Goal 的根本区别
       → Prompt: ask → work → result → wait
       → Goal:   work → check → continue or complete
   2. 强 Goal 6 element formalism
       → Outcome / Verification surface / Constraints / Boundaries / Iteration / Blocked
   3. 实战 example: Deep Hedging paper reproduction
   4. 架构: thread-scoped state + event-driven continuation

[5/11] Build Iterative Repair Loops（中层：单 artifact 修复）
   1. 三阶段严格分离: Review → Repair → Validate
       → Review 永远不编辑文件
       → Repair 操作副本不决定 issue
       → Validate 端到端跑不修复
   2. Structured JSON handoff between phases
   3. Validation 是经验反馈不是教师
   4. 5 应用场景（doc / 协议 / 法规 / 支持 / code 现代化）

[5/12] Agent Improvement Loop（最高层：整个 harness 演化）
   1. 6 步 flywheel
       → Synthetic data → Harness → Trace → Feedback → Eval → HALO → Codex
   2. Tooling stack: Agents SDK + Promptfoo + HALO + OpenTelemetry
   3. 6 required artifacts per run（machine + human readable 分开）
   4. 5 个 trace 不是 50/500：复利在频次不在样本量

[整体收尾]（隐含 thesis 浮现）
   → 三层 loop 是 agentic 系统的标准结构
   → 每层 loop 的状态独立但喂养上下层
```

**骨架洞察**：三篇连发不是巧合，**它们是有意识的抽象阶梯**：
1. **5/9 Goals** = "怎么开始一个 loop"（最低门槛）
2. **5/11 Repair** = "怎么让 loop 高质量"（专业化）
3. **5/12 Improvement** = "怎么让 loop 系统演化"（生产化）

**这种顺序设计**让读者沿着复杂度阶梯往上爬，**而不是一次塞所有概念**。每篇可独立读，但合起来才显示完整方法论。**复用这种"4 天 3 篇阶梯式"内容序列设计**：当你要推一个复杂方法论时，分成 3 篇按抽象层级递增，3-4 天连发。

### 4. 关键概念字典

> **Goal（在 Codex 里的定义）⭐**
> - **是什么**：thread-scoped 的**持久 objective**，跨多个 conversational turn 维持 focus。包含：完成条件 + 如何验证 + 不能 regress 的约束
> - **为什么重要**：与传统 prompt 的**根本区别**——prompt 是 stateless ask；goal 是 **stateful contract**
> - **直觉类比**：**Prompt = 临时工日工资单（"今天做 X"）；Goal = 全职合同（"达成 KPI 才算完成"）**
> - **适用场景**：performance 优化 / flaky test / dependency migration / 多步 bug 复现 / 需要 final artifact 的研究
> - **反面/失败模式**：把 Goal 用在"一行编辑 / 简单解释 / code review / 单答问题 / vague finish line task"

> **6-Element Strong Goal Formalism ⭐⭐ 最有迁移价值**
> - **是什么**：每个 Goal 必须明确 6 个 element
>   1. **Outcome** — 完成时什么应该是 true
>   2. **Verification surface** — 哪些 tests / benchmarks / artifacts 证明成功
>   3. **Constraints** — 什么不能 regress
>   4. **Boundaries** — 允许动哪些 files / tools / data / resources
>   5. **Iteration policy** — 失败后怎么选下一步
>   6. **Blocked stop condition** — 什么情况停下来报告 blockers
> - **为什么重要**：把 Chris Hayduk 的 informal heuristic（量化 + tight feedback + 三文件）**形式化为 spec template**。每个 element 对应一个失败模式的预防
> - **直觉类比**：合同条款 6 大要素——目标 / 验收方式 / SLA / 范围 / 变更管理 / 终止条款。**没有这 6 项的合同会出纠纷**
> - **适用场景**：每次写 `/goal` 前的强制 checklist
> - **反面/失败模式**：只写 Outcome 不写 Constraints → agent 为达 outcome 破坏其他东西

> **Stateful Loop（Goal 的执行模型）**
> - **是什么**：`work → check → continue or complete` 的循环，Codex **只在 idle / 在 budget 内 / 没有 queued user input 时**自动继续
> - **为什么重要**：揭示 `/goal` 不是 magic——是**有明确事件触发器的 loop**
> - **直觉类比**：CI/CD pipeline。每个 commit 触发 build / test / deploy；满足 condition 才推进；budget 用完就 stop
> - **适用场景**：理解为什么 `/goal` 有时"不动"——可能不是 hung，是在等 safe boundary
> - **反面/失败模式**：误以为 Goal 在永久"运行"——实际是 event-driven

> **Iterative Repair Loop 三阶段 ⭐**
> - **是什么**：**Review → Repair → Validate**，三个阶段严格分离：
>   - **Review**：检视 artifact，识别 issues。**永远不编辑文件**
>   - **Repair**：对**副本**做有针对性的修改。**不决定什么是 issue**
>   - **Validate**：端到端执行，报告 deltas。**不修复**
> - **为什么重要**：**职责分离强迫 evidence-based 工作流**。如果 Review 能编辑 → 混淆"什么错"和"怎么改"；如果 Repair 能决定 issue → 跳过调查；如果 Validate 与 Repair 合并 → bias
> - **直觉类比**：医院流程——**诊断（Review）/ 治疗（Repair）/ 复查（Validate）严格不同的人不同的科室**。让外科医生自己 review 自己的手术 = 利益冲突
> - **适用场景**：任何 "artifact 已存在但需要修复" 的场景——文档过时 / API 模型升级 / 法规合规 / 内容更新 / code 现代化
> - **反面/失败模式**：让一个 agent 同时做三件事 → silent fallback antipattern（看着好实际崩）
> - **wiki 对应**：[[iterative-repair-loop]]

> **Structured JSON Handoff ⭐**
> - **是什么**：阶段间不用 free-form text 传递，**用严格 JSON schema**
>   - Review 输出：artifact name / issue type / severity / description / suggested fixes
>   - Repair 输出：iteration number / changes / unresolved / updated artifact paths
>   - Validate 输出：pass/fail + per-case evidence + remaining deltas
> - **为什么重要**：**强迫明确判决**。没有"还不错"——只有 pass / fail。同时允许阶段间机械化传递（不依赖下一阶段的 model 重新解析模糊文本）
> - **直觉类比**：API contract。两个 service 之间不用自然语言，用 JSON spec
> - **适用场景**：任何 multi-agent / multi-stage 工作流
> - **反面/失败模式**：阶段间用 narrative text → 信息丢失 / 模糊 / 下游 hallucinate

> **Validation as Empirical Feedback ⭐**
> - **是什么**：validation 不是"教师评分"，是"环境给出执行结果"。**Repair agent 不能争辩"这应该 work"。Notebook 要么跑要么不跑**
> - **为什么重要**：把反馈信号从**推理基础**（看 diff 推测）→ **经验基础**（实际跑）。**Grounds subsequent repairs in observed behavior rather than inference from diffs alone**
> - **直觉类比**：跑步训练。教练说"再快一点"（推理反馈）vs 秒表显示"5K 30 分"（经验反馈）。**经验反馈不可争辩**
> - **适用场景**：任何 self-correcting agent loop
> - **反面/失败模式**：用 LLM judge 代替实际执行 → LLM judge 和 repair agent 同源偏见

> **Agent Improvement Flywheel（6 步循环）⭐⭐ 最雄心**
> - **是什么**：
>   1. **Synthetic data**（含**有冲突的信号**——这是关键）
>   2. **Define harness** = system prompt + tool policies + required artifacts + validation rules
>   3. **5 个 traced run**（OpenTelemetry-compatible）
>   4. **Human + LLM feedback**
>   5. **Convert to evals**（用 Promptfoo）
>   6. **Optimize with HALO**——给 harness 改进 ranking by impact
>   7. **Hand off to Codex**——Codex 生成 dev-facing 修改建议
> - **为什么重要**：从"单 task 改进" → "整个 agent 系统持续改进"。这是 production agentic system 的演化机制
> - **直觉类比**：精益生产里的 Kaizen——**小步连续改进 + 数据驱动 + 系统化反馈循环**
> - **适用场景**：你已经有一个 agent 在跑生产任务，想让它持续变好
> - **反面/失败模式**：不建 trace → 不知道哪里 fail；不做 eval → 改进无方向；不用 Codex 闭环 → 改进建议变成 doc 而不是 PR
> - **wiki 对应**：[[agent-improvement-flywheel]]

> **5-Trace-Per-Iteration 选择 ⭐**
> - **是什么**：每轮 flywheel 跑 5 个 trace（约 20 分钟 with GPT-5.5），**不是 50 或 500**
> - **为什么重要**：揭示**复利在频次而非样本量**——每周做一轮，跑 10 周积累 50 trace 但有 10 次反馈/优化机会
> - **直觉类比**：复利 vs 单利。每周存 100 vs 一年存 5200——同样的 deposit total，但每周存的有 52 次复利机会
> - **适用场景**：你设计任何 eval / improvement schedule 时
> - **反面/失败模式**：等"足够多 trace 才开始分析" → 永远不开始

> **6 Required Artifacts Per Run（artifact 模式）⭐**
> - **是什么**：每个 traced run 必须输出 6 个 artifact：
>   - `summary_answer.md` — 标题答案
>   - `investment_memo.md` — 详细 review
>   - `risk_register.json` — 结构化 risks
>   - `open_questions.md` — 缺失证据 + 未决
>   - `citations.json` — claim→source 机器可读映射
>   - `evidence_table.csv` — claim 和 source 审计 trail
> - **为什么重要**：**machine-readable (.json/.csv) 和 human-readable (.md) 分开**。Eval pipeline parse JSON；人审 markdown。**双路审计**
> - **直觉类比**：医疗记录——人读的病历叙述 + 机器读的 ICD 编码。两套并行，互相验证
> - **适用场景**：任何需要"自动 eval + 人审"双轨的 agentic output
> - **反面/失败模式**：只输出 markdown → eval pipeline 无法 parse；只输出 JSON → 人审低效

> **OpenTelemetry Trace Mapping ⭐**
> - **是什么**：Agents SDK span 直接映射到 OpenTelemetry：
>   - `agent` → AGENT
>   - `generation` / `response` → LLM
>   - `function` / `mcp_tools` → TOOL
>   - `handoff` → CHAIN
> - **为什么重要**：**agent 执行 trace 跟后端服务在同一个 observability infra**——同 dashboard / 同查询语言 / 同 retention
> - **直觉类比**：让 agent 进入既有的 monitoring 体系，而不是搞个孤岛 dashboard
> - **适用场景**：production agentic deployment
> - **反面/失败模式**：建独立 trace 系统 → 长期维护成本爆炸

> **HALO（OpenAI 的 harness 优化机制）**
> - **是什么**：给 harness 改进 ranking by impact。文档没披露算法
> - **推测连接**：跟 Garry Tan 4/15 floated 的 "self-healing resolver"（用 traffic 进化 routing 表）是同一思路——都是用观察到的执行 trace 自动建议系统改进。**OpenAI 把它做成了 product feature；Garry 把它做成了 vision**
> - **适用场景**：当你的 harness 有多个可改进点时，HALO 替你 rank
> - **wiki 对应**：见 [[harness-design]]

### 5. 框架与心智模型

**核心框架：三层嵌套 Loop（OpenAI 完整 agentic 方法论）**

```
┌─────────────────────────────────────────────────────────┐
│  Layer 3: Agent Improvement Flywheel（5/12）            │
│  ─────────────────────────────────────                  │
│  Goal: 整个 agent 系统持续演化                          │
│  Loop周期: weekly                                       │
│  Input: 多个 trace + feedback + eval                    │
│  Output: harness change recommendations                 │
│                  ↑ ↓                                    │
│  ┌─────────────────────────────────────────────────┐  │
│  │  Layer 2: Iterative Repair Loop（5/11）         │  │
│  │  ───────────────────────────────                │  │
│  │  Goal: 单 artifact 修复到合规                   │  │
│  │  Loop周期: minutes-hours                        │  │
│  │  Input: artifact + validation rules             │  │
│  │  Output: repaired artifact + report             │  │
│  │           ↑ ↓                                   │  │
│  │  ┌────────────────────────────────────┐         │  │
│  │  │  Layer 1: Goal Loop（5/9）         │         │  │
│  │  │  ─────────────────────────         │         │  │
│  │  │  Goal: 单 task 完成                │         │  │
│  │  │  Loop周期: turns / minutes         │         │  │
│  │  │  Input: 6-element strong goal      │         │  │
│  │  │  Output: artifact + evidence       │         │  │
│  │  └────────────────────────────────────┘         │  │
│  └─────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**关键特性**：
- 每层都有**自己的状态**（thread-scoped / repair-scoped / weekly-scoped）
- 每层 loop 的**输出喂上层 loop 的输入**（artifact → repair → eval → harness）
- 每层的**停止条件不同**（goal 满足 / validation pass / harness 改完）

**用法**：审视你现在的 agentic 工作流，**问自己 "我在哪一层？"**
- 写 prompt = 没进入任何 layer
- 跑 `/goal` = Layer 1
- 加 Review→Repair→Validate = Layer 2
- 加 trace + eval + 定期改 harness = Layer 3
- 三层都齐 = 生产级 agentic 系统

**核心 mental model 2：三层 loop 的核心 invariant**

| Layer | 状态 | 验证机制 | 复利单元 |
|---|---|---|---|
| **Layer 1（Goal）** | thread-scoped | evidence-based completion | 单次 task |
| **Layer 2（Repair）** | repair-scoped | end-to-end execution | 单 artifact 经过多 iteration |
| **Layer 3（Improvement）** | weekly-scoped | eval pass rate | 整个 harness 经过多周 iteration |

**应用**：每层都需要明确"状态在哪、怎么验证、什么是复利的最小单元"。**遗漏其中一个 = 该层不可持续**。

**核心 mental model 3：阶段分离即 evidence-based 工作流**

```
混合（坏）：              分离（好）：
agent 做所有事            Reviewer ──finding──→ Repairer
↓                                              ↓
 - 模型自评              Repairer ──artifact──→ Validator
 - 自我评判 bias                                ↓
 - 无 audit trail        Validator ──result──→ next iter
```

**为什么职责分离 = evidence-based**：
- 不同 agent 不同上下文 → 减少 confirmation bias
- 阶段间 JSON handoff → 强迫 explicit decision
- 每阶段输出可独立 audit

### 6. 关键数据与例证

按重要性排序：

| 数据/例子 | 出自 | 用途 |
|---|---|---|
| **Deep Hedging paper reproduction Goal**（Buehler et al.）| 5/9 | 6-element formalism 最强 case——研究复现是 vague task 的代表 |
| **"client.chat.completions.create → client.responses.create" API 现代化规则** | 5/11 | 业务规则的具体写法；可直接抄到 [[sprint-contracts]] |
| **3 sample notebooks 渐进通过（iter 1/2/3）** | 5/11 | 证明 iterative repair 的渐进性——不是 "all-or-nothing" |
| **5 traces × 20 minutes = 100 minutes/iteration** | 5/12 | 量化 weekly flywheel 时间成本——可融入个人 schedule |
| **6 required artifacts（投资 diligence agent）** | 5/12 | 直接可抄的 output contract 模板 |
| **OpenTelemetry span mapping 4 条** | 5/12 | 让 agent trace 接入既有 observability 的 minimal mapping |
| **5 个失败模式（diligence-specific）** | 5/12 | 让人意识到"polished answer + incomplete citation" = silent fallback |

**特别注意**：与 Khairallah / Garry Tan 等抽象 framework 派**对比**，OpenAI 官方 doc **极度 concrete**——
- 实际命令（`/goal pause`、`/goal resume`）
- 实际代码（`check_evidence_coverage.py`）
- 实际超时（20 minutes）
- 实际模型配置（`OPENAI_AGENT_MODEL` 等环境变量）

**这是 official doc vs influencer thread 的辨识特征**。Influencer 给框架；docs 给可执行 commands。**两种都要读**。

### 7. 关键引语

> **"Goals transform threads from isolated prompts into stateful loops."**（5/9）
> Goal 把 thread 从孤立的 prompt 转变为有状态的 loop。
> ⭐ Goal 的本质 reframing 一句话。

> **"Codex continues automatically only when idle, within budget, and when no user input is queued."**（5/9）
> Codex 仅在 idle / 在 budget 内 / 没有 queued user input 时自动继续。
> ⭐ 三个并列条件揭示 Goal 的 event-driven 模型——不是"在跑"，是"在等条件"。

> **"Goals differ fundamentally from one-off prompts: rather than requesting immediate work, they establish durable targets that Codex evaluates against concrete evidence."**（5/9）
> Goal 与一次性 prompt 根本不同：不是请求即时工作，而是建立 Codex 用具体证据评估的持久目标。
> ⭐ Goal vs Prompt 最 clean 的差异表达。

> **"Strong Goal: Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Use only the checkout service and related tests. Between iterations, record changes, benchmark results, and next experiments to attempt. If blocked, stop with attempted paths, evidence, and blockers."**（5/9）
> ⭐ 6-element strong goal 的模板金句。**直接抄改用**。

> **"Validation executes notebooks end-to-end, capturing execution failures as structured feedback. This grounds subsequent repairs in observed behavior rather than inference from diffs alone."**（5/11）
> Validation 端到端执行 notebook，捕捉执行失败作为结构化反馈。这让后续 repair 立足于观察到的行为，而不是仅从 diff 推断。
> ⭐ Validation as empirical feedback 的核心一句。"observed behavior vs inference" 这一对比是金句。

> **"The key principle remains separating judgment from proof through structured handoffs."**（5/11）
> 关键原则始终是：通过结构化交接，把判断与证明分离。
> ⭐ Iterative Repair 整篇浓缩。"judgment from proof" 是高级抽象。

> **"Preserves evidence at each step: Traces show what happened. Feedback explains what mattered. Evals make expectations reusable. Optimization produces the next harness version."**（5/12）
> 每一步保留证据：Trace 显示发生了什么。Feedback 解释什么重要。Eval 让期望可复用。Optimization 产出下一版 harness。
> ⭐ Agent Improvement Flywheel 的 4 步浓缩——非常 clean 的 mental model。

> **"~20 minutes for five complete traces with default model (GPT-5.5)"**（5/12）
> ~20 分钟跑完 5 个完整 trace（默认模型 GPT-5.5）。
> ⭐ 给 flywheel 的实际时间成本数据——5 trace = 20 min = 周末 30 分钟就能跑一轮。

> **"Six required output artifacts: summary, memo, risk register, open questions, citations, and evidence table."**（5/12）
> 6 个必须输出 artifact：摘要、备忘录、风险登记、未决问题、引用、证据表。
> ⭐ Output contract 的具体模板——可直接复用到任何需要"答案 + 审计 trail"双重输出的 agent。

### 8. 实操指南

**Tier 1：先建 Goal Loop（Layer 1，1 周内）**

- [ ] 安装 Codex CLI: `npm install -g @openai/codex@latest`
- [ ] 选一个 candidate task：performance 优化 / flaky test / dependency migration / 重构
- [ ] **按 6 element 写 Goal**（强制 checklist）：
  - [ ] Outcome：完成时什么应该 true？（一句话 + 数字）
  - [ ] Verification surface：哪些 test / benchmark / file 证明？
  - [ ] Constraints：什么不能 regress？
  - [ ] Boundaries：能动哪些 files / tools？
  - [ ] Iteration policy：失败时怎么选下一步？
  - [ ] Blocked stop：什么情况停下来报告？
- [ ] **不要**用 Goal 处理：一行编辑、code review、单答问题、vague task
- [ ] 跑 `/goal <你的 strong goal 全文>`，记录结果

**Tier 2：加 Iterative Repair Loop（Layer 2，2-4 周内）**

- [ ] 选一个 candidate artifact（**已存在但需要修复**的）：过时文档 / 过时 API 调用 / 不合规内容
- [ ] 写 **business rules**：明确"什么是 issue"+"什么是合规"
  - 例：API 现代化规则、内容标准、合规要求
- [ ] **建三个 agent / 三个 prompt（严格分离）**：
  - [ ] Reviewer：识别 issue + 不编辑 → JSON 输出
  - [ ] Repairer：在副本上修改 + 不决定 issue → JSON 输出
  - [ ] Validator：端到端执行 + 不修复 → JSON 输出
- [ ] 定义 stop condition：validation passes / max iterations / delta stabilization
- [ ] **加 audit trail**：每个 iteration 的 3 阶段输出全部归档

**Tier 3：建 Agent Improvement Flywheel（Layer 3，1-3 月）**

- [ ] **建 synthetic data**（含**故意的冲突**——这是关键）
- [ ] **写 harness spec**：
  - [ ] system prompt
  - [ ] tool policies
  - [ ] required artifacts list（参考 6-artifact 模板）
  - [ ] validation rules
- [ ] 装 OpenTelemetry-compatible trace 工具（参考 5/12 的 JSON Lines exporter）
- [ ] **每周做一轮**：
  - [ ] 5 个 traced run（~20 min）
  - [ ] human + LLM feedback
  - [ ] 转为 Promptfoo eval
  - [ ] HALO rank harness improvements（或手动 rank）
  - [ ] 让 Codex 输出具体 PR-level 修改建议
- [ ] **不要**等"足够多 trace 才开始"——立刻开始，复利在频次

**Pre-trigger checklist（每次写 strong Goal 前 2 分钟）**：

| Element | 你写了吗？ | 如果没写会怎样 |
|---|---|---|
| Outcome | □ | 永不停止 |
| Verification | □ | 模型自评，confirmation bias |
| Constraints | □ | 为达目标破坏其他东西 |
| Boundaries | □ | 改不该改的文件 |
| Iteration policy | □ | 失败时乱试 |
| Blocked stop | □ | 永久 stuck 不报告 |

**3 个生产 considerations（5/11 强调）**：
1. 明确 stop condition（pass / max iter / delta 稳定）
2. 完整 audit trail
3. Human review checkpoint（unresolved cases）

### 9. 对比与反对意见

**与 Chris Hayduk 5/11 的对比**：

| 维度 | Chris Hayduk（informal）| OpenAI Cookbook（formal）|
|---|---|---|
| **格式** | 3 个 tips | 6 个 element + 3-phase + 6-step flywheel |
| **量化 goal** | "20% runtime 减少" | "p95 < 120 ms, suite green, only checkout service" |
| **Feedback loop** | "find any way to speed up" | "validation executes end-to-end" |
| **State 管理** | PLAN / EXPERIMENTS / SCRATCHPAD | 6 artifacts (md + json + csv) |
| **抽象级** | practitioner heuristics | complete formalism |
| **可执行性** | high（直接抄三文件就能跑）| higher（连 commands、API endpoints 都给）|

**两者不矛盾，是不同层级**：
- 单 task 起步 → 用 Chris 的 3 tips
- 生产化扩展 → 用 OpenAI 的 6+3+6 formalism

**作者立场对比表**：

| 对比对象 | OpenAI 立场 | 隐含信念 |
|---|---|---|
| **vs prompt-only workflow** | "stateful loop"必要 | 生产工作不能靠 stateless prompt |
| **vs 让一个 agent 做 review+repair+validate** | 强烈反对 | 职责分离 → bias 减少 |
| **vs free-form text handoff** | 反对 | 阶段间必须 structured JSON |
| **vs LLM-judge-only validation** | 反对 | 必须 end-to-end 执行，不能仅 inference from diff |
| **vs 一次大量采样（50/500 trace）** | 反对 | 5 trace × weekly > 100 trace once |
| **vs 自建 observability 工具** | 反对 | 必须 OpenTelemetry-compatible（接入既有 infra） |

**作者明确反对**：
1. **用 Goal 处理简单 task**（一行编辑、code review、单答问题）
2. **混合 Review/Repair/Validate**（最大反 pattern）
3. **markdown-only output**（eval pipeline 无法 parse）
4. **不建 trace**（improvement flywheel 不存在）

**潜在反对意见 / 没讨论的限制**：
- **三层架构的 setup cost** —— 全建起来要多少周？官方没给。**对 indie hacker 偏重**
- **HALO 算法不透明** —— 你信不过这个 ranking 就没法用
- **5 traces 假设了 GPT-5.5 速度** —— 用更小模型时 trace 跑得更快，5 个 trace 可能不够
- **Synthetic data 怎么生成** —— 5/12 给了具体 case（投资 diligence）但 generalize 不易
- **三层之间的反馈机制不明确** —— Layer 3 的 harness 改进怎么 propagate 到 Layer 1 的 goal？

### 10. 与 wiki 知识的连接

**强连接**：
- [[chris-hayduk]] —— Chris 的 5/11 X 帖是这三篇的 informal counterpart，时间上夹在中间
- [[iterative-repair-loop]] —— 5/11 文章创造的概念
- [[agent-improvement-flywheel]] —— 5/12 文章创造的概念
- [[claude-code-goal]] —— 跨厂商 `/goal` 对照

**强化已有概念**：
- 强化 [[agentic-loop-tracking-files]]：6-artifact pattern 是三文件追踪 pattern 的 production 版
- 强化 [[verification-loops]]：eval-as-empirical-feedback insight
- 强化 [[harness-design]]：HALO + harness spec 是 harness design 在 OpenAI 侧的落地
- 强化 [[agent-evaluation-traps]]：5 个 failure mode（silent fallback / unvalidated estimates / overstated certifications）
- 强化 [[silent-fallback-antipattern]]：5/12 的"polished answer + incomplete citations"完全契合
- 强化 [[sprint-contracts]]：业务规则（"chat.completions.create → responses.create"）= sprint contract 的具体写法

**跨厂商收敛信号 +1**：

| Dimension | Anthropic | OpenAI |
|---|---|---|
| Goal mode | Claude Code `/goal` + Haiku evaluator | Codex `/goal` + 6-element formalism |
| Skills/SDK | Skills standard | Agents SDK + Promptfoo |
| Harness design | [[source-anthropic-harness-design]] | Improvement Loop + HALO |
| Trace/observability | OpenTelemetry standard | OpenTelemetry standard |

**收敛点**：trace-based observability、structured handoff、stateful loop、condition-based completion、tool-as-state。**OpenAI 和 Anthropic 在 agentic CLI 战场上几乎同步**。

**与其他源**：
- [[source-chrishayduk-codex-goals-effectively]] —— informal 版的同一方法论
- [[source-claude-code-goal-and-agent-view-docs]] —— Anthropic 侧 `/goal` 文档对照
- [[source-anthropic-harness-design]] —— Anthropic 侧的 harness 哲学，与 OpenAI 互相印证
- [[source-eng-khairallah-3-ai-hires]] —— Khairallah 的 3-agent triad 在 OpenAI 这里被具象化为 Review/Repair/Validate
- [[source-mattpocock-grill-with-docs-skill]] —— Matt 的 CONTEXT.md = 6 artifact 模式的 minimal indie 版

**扩展方向 / 可继续 ingest 的源**：
- 更多 OpenAI cookbook 后续 agentic CLI 文章
- HALO 算法的官方披露（如有）
- Promptfoo 在 agentic eval 的具体例子
- Anthropic 的 official harness-design 文档跟这三篇的逐项对比

### 11. 对用户（vfan）的启示

基于 vfan 的情况（Singapore growth marketer + AI content builder，LoreAI + blog2video）：

#### 短期（本周）

1. **把 6-element strong Goal 模板贴在 obsidian-vault-starter 里**：
   - 加 `.claude/skills/strong-goal-template/SKILL.md` 或 `_templates/strong-goal.md`
   - 模板填空 + 反 weak-goal example
   - 下次写 `/goal` 时强制 reference
2. **写一次实际 strong Goal 测试**：把现在 vault 里某个 long-running 任务（例：blog2video 章节质量优化）按 6-element 写下来
   - 即使你最后用 Claude Code 不是 Codex，6-element formalism 完全适用
3. **审视现有 `/ingest` `/draft` `/query`**：看哪些隐式已经在 Layer 1 / Layer 2 / Layer 3，明确化抽象层级

#### 中期（接下来 2-6 周）

1. **`/lint` 正式化为 Iterative Repair Loop**：
   - 当前 `/lint` 已经接近——它做 Review（找 issue）+ 部分 Repair（建议 fix）+ 隐式 Validate
   - 升级方向：明确 3-phase 输出 schema（JSON），让你可以 audit
   - 这是把 OpenAI 的 pattern 直接搬到 wiki 工具
2. **`/draft` 加 Review→Repair→Validate**：
   - Review = 找内容问题（标题不够 hook / 缺数据点 / structure 不清）
   - Repair = 改稿副本
   - Validate = 用 quality checklist 端到端检查（结合 Chris 的 200-checklist trick）
   - 这是把 [[quality-gate-loop]] 具象化的实操路径
3. **加 6-artifact output 模式到 `/ingest`**：
   - 当前 `/ingest` 输出 source-summary.md（≈ memo + open questions 合并）
   - 升级：加 `citations.json`（机器可读 source mapping）+ `evidence_table.csv`
   - 好处：未来可以跑自动 eval（"这条 claim 真有 source 支撑吗"）
4. **写 weekly /improve workflow**：
   - 每周日：审 `/lint` + `log.md` 最近一周 → 提出 wiki 改进建议
   - 这是 Agent Improvement Flywheel 在 personal vault 的最小实现
   - 不需要 HALO；手动 rank 就行

#### 长期（如果验证有效）

1. **写"三层 loop"中文 mass-market 系列**：
   - 标题候选："OpenAI 官方 Codex 方法论：你写的不是 prompt，是 loop"
   - 三篇对应三层，每篇 1500 字 + 1 个真实 vault 案例
   - 中文 SEO：抢"codex /goal 教程"、"openai 官方 agent 方法论" 等关键词空白
   - 跟 [[content-distribution-china]] arbitrage 思路完全吻合
2. **建立"vault as agentic system"产品定位**：
   - obsidian-vault-starter 不只是 wiki 模板，**是一个三层 loop 实现的 starter kit**
   - 加 README 段落："Layer 1: `/ingest`, `/draft`. Layer 2: `/lint`. Layer 3: weekly `/improve`."
   - 用 OpenAI 官方框架背书让 starter 显得"生产级"
3. **测试跨厂商 `/goal` benchmark**：
   - 同一 strong goal 在 Codex `/goal` 和 Claude Code `/goal` 各跑一遍
   - 记录失败模式 / 时间 / 输出质量
   - 中文圈首个真实跨厂商 agentic CLI 评测——high arbitrage value
4. **基于 6-artifact 模式做 productized service**：
   - 对外提供"Codex-based diligence/research agent setup"
   - $5K-$25K 区间（参考 Khairallah 估值）
   - vault 作为 portfolio 证据

### 12. 一句话总结

**"OpenAI 用 4 天 3 篇官方 doc 定义了 agentic 系统的三层 loop：Goal 控完成、Repair 控质量、Improvement 控演化。三层都建对 = 生产级 agentic 系统。"**

或更短：**"agentic 不是写 prompt，是套 loop。OpenAI 给了你三层标准。"**

更激进：**"Layer 1 让 agent 完成事；Layer 2 让 agent 做对事；Layer 3 让 agent 越来越好。缺一层都不是 production。"**

---

## Pages created from this source
- [[iterative-repair-loop]] — concept (Review → Repair → Validate three-phase pattern)
- [[agent-improvement-flywheel]] — concept (6-step trace-to-harness-change flywheel)
- [[source-openai-codex-cookbook-trilogy]] — this page (combined source summary for all three articles)

## Pages updated from this source
- [[chris-hayduk]] — added "official version" cross-reference for these three OpenAI cookbook docs
- [[claude-code-goal]] — added cross-vendor parallel + 6-elements goal-writing formalism
- [[agentic-loop-tracking-files]] — referenced (PLAN/EXPERIMENTS/SCRATCHPAD pattern is consistent with the 6-artifact pattern)
- [[verification-loops]] — eval-as-empirical-feedback insight reinforced
- [[harness-design]] — HALO + harness-as-spec
- [[silent-fallback-antipattern]] — "polished answer + incomplete citations" as canonical agentic example
- [[index]], [[log]]

## Connections
- Related: [[chris-hayduk]], [[iterative-repair-loop]], [[agent-improvement-flywheel]], [[claude-code-goal]], [[agentic-loop-tracking-files]], [[verification-loops]], [[agent-evaluation-traps]], [[harness-design]], [[silent-fallback-antipattern]], [[sprint-contracts]], [[source-chrishayduk-codex-goals-effectively]], [[source-claude-code-goal-and-agent-view-docs]], [[source-anthropic-harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-09-openai-cookbook-using-goals-in-codex.md | Initial creation (article 1 of 3) |
| 2026-05-16 | raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md | Added article 2 of 3 |
| 2026-05-16 | raw/2026-05-12-openai-cookbook-agent-improvement-loop.md | Added article 3 of 3 |
| 2026-05-18 | (refresh) | Full rewrite using new 12-section comprehensive structure |
