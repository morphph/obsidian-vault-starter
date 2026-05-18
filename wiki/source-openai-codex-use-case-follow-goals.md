---
type: source-summary
created: 2026-05-18
last-updated: 2026-05-18
sources:
  - raw/2026-05-09-openai-codex-use-case-follow-goals.md
tags: [wiki, source, openai, codex, goal, use-case, templates]
---

# Source: OpenAI Codex Use Case — Follow a Goal

## Summary
OpenAI 官方 Codex use-case 页面（约 2026-05-09 发布）。是 [[source-openai-codex-cookbook-trilogy|cookbook 页面]] 的**实操 companion** —— cookbook 给 6-element 形式化框架，本页给 5-step 操作流程 + 3 类场景的 ready-to-use templates（migration / prototype / prompt optimization）。第一个明确写出 "tighten the goal rather than adding ad hoc instructions mid-run" 这个反 anti-pattern 的官方源。

## Source Metadata
- **URL:** https://developers.openai.com/codex/use-cases/follow-goals
- **Author:** OpenAI Developers (official Codex docs)
- **Estimated publish:** ~2026-05-09
- **Fetch date:** 2026-05-18
- **Fetch method:** WebFetch

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
- **作者**：OpenAI Developers（官方 docs channel）
- **来源**：developers.openai.com/codex/use-cases
- **影响力指标**：无（官方文档不公开）
- **在 OpenAI 输出中的位置**：3-tier 文档矩阵的**操作层**
  - **Awareness**: [[source-openai-long-horizon-tasks-codex|long-horizon blog]]（为什么）
  - **Conceptual**: [[source-openai-codex-cookbook-trilogy|cookbook Using Goals]]（什么）
  - **Operational（本页）**: use-case Follow a Goal（怎么做）

### 2. 核心论点（Thesis）
**OpenAI 主张**：用 /goal 不是"喊一句 prompt 就走"，需要明确的 5-step setup（命名目标和 stop 条件 / 指向源材料 / 定义 validation 产物 / 要求 checkpoint reporting / 用 /goal 命令监控），**因为**长跑任务的偏差代价高，**所以**目标定义本身就是工作的一部分（不是 prelude）。

简化压缩包：**"/goal 前的 setup 工作就是任务的一半 —— 5 步 setup + 3 类场景模板 + 'tighten the goal' 原则。"**

### 3. 论证结构
```
1. When to use（4 类场景）
2. Core principle（define done first）
3. 5-step setup process（操作流程）
4. Basic syntax（一行模板）
5. 3 个具体场景例子（migration / prototype / prompt-optim）
6. Standard vs Goal-driven 对比
7. Lifecycle commands（pause/resume/clear）
8. Recommended operational patterns（包括 "tighten the goal"）
```

短而完整。**这就是给用户照着抄的页面**，没有理论装饰。

### 4. 关键概念字典

> **"Define what 'done' means before starting"（开始前先定义"完成"）**
> - **是什么**：跑 /goal 前最重要的一步 —— 必须能用一句话说清楚"什么时候算完"
> - **为什么重要**：这是整个 use case 的 entry condition。不能回答"什么时候算完"= 不能用 /goal
> - **直觉类比**：像签合同 vs 口头说"我们做做看" —— 前者有明确交付条件，后者永远做不完
> - **适用场景**：每次启动 /goal 之前的强制 checklist
> - **反面/失败模式**：先启动 /goal 再"边跑边想 done 是什么" —— 这是 vibe loop，不是 goal loop

> **5-Step Setup Process（5 步 setup 流程）**
> - **是什么**：(1) 命名 objective + stopping condition; (2) 指向 source 材料; (3) 定义 validation artifacts; (4) 要求 checkpoint reporting; (5) 用 /goal 命令监控
> - **为什么重要**：把"启动 /goal"从一个 verb 变成一个 5-step process，让用户慢下来想清楚
> - **直觉类比**：像航前 checklist —— 不是为了麻烦，是为了避免起飞后才发现问题
> - **适用场景**：每次首次定义某类任务的 goal 时
> - **反面/失败模式**：跳过 step 3-4 → agent 不知道怎么证明完成 + 你不知道它跑到哪了

> **"Tighten the goal" Pattern（收紧目标模式）**
> - **是什么**：当 agent 跑偏时，**rewrite goal**，**不要**用 ad hoc 指令往里加东西
> - **为什么重要**：保持 source of truth 单一。Ad hoc 指令是 conversation-level state，会随 compaction 丢失；rewritten goal 是 durable
> - **直觉类比**：像写法律合同 —— 发现条款有漏洞时，**重新签订**（durable），不是在合同上手写注释（conversation-level）
> - **适用场景**：calibration phase 发现 agent misunderstand 时
> - **反面/失败模式**：在 chat 里追加 "actually also do X" → 下次 context reset 时 X 没了，agent 又跑偏

> **"Goal-driven vs Standard" Operating Mode（goal 模式 vs 标准模式）**
> - **是什么**：standard mode 每 turn 后等用户；goal mode 自动 validate + 自主进入下一 turn
> - **为什么重要**：明确两种模式的 user role 差异 —— standard 是 "co-pilot"，goal 是 "delegate"
> - **直觉类比**：standard 像跟同事配对编程；goal 像派同事去解决问题然后 review 结果
> - **适用场景**：决定某任务该用哪种模式
> - **反面/失败模式**：用 goal mode 处理需要 taste 决策的任务 → agent 持续做错方向

### 5. 框架与心智模型

**核心框架：5-Step Setup Process（启动 /goal 的强制 checklist）**

| Step | 动作 | 反例（如果跳过） |
|------|-----|---------------|
| 1. Name objective + stopping condition | "Migrate auth from X to Y until all tests pass" | "Improve auth" → 永远不完 |
| 2. Point to source materials | "Read docs/auth-migration-spec.md and src/auth/*.ts" | agent 找文件找半天，或自己猜 |
| 3. Define validation artifacts | "npm test exits 0 + npm run typecheck exits 0" | agent 不知道怎么证明完成 |
| 4. Request checkpoint reporting | "After each milestone, write to docs/status.md with progress / verified / remaining / blockers" | 你不知道跑到哪了 |
| 5. Monitor via /goal commands | `/goal` (status) / `/goal pause` / `/goal resume` / `/goal clear` | 出问题没法干预 |

**3 类场景模板**（可直接抄）：

**Migration**：
```
/goal Migrate this project from [legacy stack] to [target stack].
Ensure all screens remain visually identical, using playwright interactive to verify.
```

**Prototype**：
```
/goal Implement PLAN.md, creating tests for each milestone and verifying output with playwright interactive.
```

**Prompt Optimization**：
```
/goal Optimize prompts in [file] until eval suite reaches [target score].
After each change, run [eval command], inspect failures, and keep edits minimal.
```

### 6. 关键数据与例证
**无量化数据**。OpenAI 官方文档不放 case study。所有"举例"都是 prompt templates，不是 outcome data。

### 7. 关键引语

> **"Use `/goal` when a task needs Codex to keep working across turns toward a verifiable stopping condition."**
> 当一个任务需要 Codex 跨多 turn 朝可验证的停止条件持续工作时，用 /goal。
> ⭐ OpenAI 对 /goal 适用边界的官方一句话定义。

> **"Define what 'done' means before starting."**
> 开始前先定义"完成"是什么意思。
> ⭐ 整个文档的 core principle，可作为博客 subhead。

> **"Tighten vague goals rather than adding ad hoc instructions mid-run."**
> 跑偏时收紧模糊的 goal，不要在中途加临时指令。
> ⭐ 这是 anti-anti-pattern 金句 —— 跟 [[source-nurijanian-goal-for-pms|George]] 的 "stop, edit spec, restart" 完全一致，官方背书。

> **"Let Codex work independently without constant monitoring—it will stop when confident it has reached the stopping condition."**
> 让 Codex 独立工作，不要持续监控 —— 它达到 stopping condition 后会自己停。
> ⭐ 这是 trust-the-loop 的官方鼓励，区别 standard mode 的 co-pilot 思维。

### 8. 实操指南

**首次启动 /goal 的 5-step checklist**：
- [ ] **Step 1 — 命名 objective + stop condition**
  - 一句话：what done looks like
  - 必须 verifiable
- [ ] **Step 2 — 指向 source materials**
  - 列出 agent 要读的所有文件 / docs / issues
  - 用绝对路径或相对清晰路径
- [ ] **Step 3 — 定义 validation artifacts**
  - 哪些命令需要 exit 0
  - 哪些文件需要存在或不存在
  - 哪些 metric 需要达到阈值
- [ ] **Step 4 — 要求 checkpoint reporting**
  - 模板："After each milestone, write to docs/status-{feature}.md with: current checkpoint / what's verified / what remains / blockers"
- [ ] **Step 5 — Lifecycle 监控**
  - `/goal` 看状态
  - `/goal pause` 暂停（如果发现跑偏）
  - `/goal resume` 重新开始
  - `/goal clear` 完全停止

**"Tighten the goal" 操作流程**：
- [ ] Pause loop（`/goal pause`）
- [ ] 不要在 chat 里追加指令
- [ ] 直接 rewrite 完整 /goal 命令（含更精准的 stopping condition）
- [ ] Resume / 重新 invoke

### 9. 对比与反对意见

| 对比对象 | 作者立场 | 隐含信念 |
|---|---|---|
| **vs Standard 单 turn 用法** | 不是替代，是补充 | Standard 适合短任务，/goal 适合长任务 |
| **vs One-off edits** | /goal 不适合 | Overhead > benefit |
| **vs Vague objectives** | 反对 | "Make this better" 不能用 /goal |
| **vs 中途追加 instructions** | 强烈反对 | Tighten goal, don't patch with comments |
| **vs Constant monitoring** | 反对（用 /goal 后就该 trust） | 不 trust 就用 standard mode |

**作者隐含承认的限制**：
- 没说 stopping condition 写不清楚怎么办
- 没说 agent 反复 fail validation 怎么办
- 没说 multi-agent 场景

### 10. 与 wiki 知识的连接

**强连接**：
- [[claude-code-goal]] — 跨 vendor sibling 命令
- [[source-openai-codex-cookbook-trilogy]] — cookbook 是 conceptual companion
- [[source-openai-long-horizon-tasks-codex]] — long-horizon blog 是 awareness companion
- [[source-nurijanian-goal-for-pms]] — George 的 6-section PM template 是这个 5-step 的扩展版

**强化已有概念**：
- 强化 [[source-nurijanian-goal-for-pms]]："tighten the goal" 是 George 的 "calibration phase" 的官方背书
- 强化 [[sprint-contracts]]：5-step setup 是 contract 写作的实操版

### 11. 对用户（vfan）的启示

#### 短期（本周）
- 任何时候想用 /goal，**先打开这个页面跑一遍 5-step checklist**
- 把 3 类模板存到你自己的 spec library

#### 中期（接下来 2-4 周）
- 把 5-step setup 和 George 的 6-section template 整合 —— 5-step 是 quick start，6-section 是 deep version
- 建立你的"tighten the goal"习惯：发现跑偏立刻 pause，不要在 chat 里 patch

#### 长期
- 中文版文章可以引用 OpenAI 官方的 "define done before starting" 作为 thesis 锚点

### 12. 一句话总结

**"启动 /goal 前 5 步 setup 就是任务的一半 —— 没定义清楚 done 就不要按下 /goal。"**

---

## Connections
- Related: [[claude-code-goal]], [[source-openai-codex-cookbook-trilogy]], [[source-openai-long-horizon-tasks-codex]], [[source-nurijanian-goal-for-pms]], [[source-chrishayduk-codex-goals-effectively]], [[agentic-loop-tracking-files]], [[sprint-contracts]], [[idea-to-afk-agent-flow]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-18 | raw/2026-05-09-openai-codex-use-case-follow-goals.md | Initial creation — 5-step setup process + 3 scenario templates + "tighten the goal" pattern |
