---
status: draft
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-09-anthropic-agent-capabilities-announcement.md
platform: blog
created: 2026-04-10
last-updated: 2026-04-10
tags: [draft, overview, anthropic, agents]
pair-article: drafts/how-to-create-first-claude-managed-agent.md
---

<!-- HOOK: "Anthropic killed 1000+ agent startups." 这条推发出来的时候，Managed Agents 上线还不到 24 小时。它到底做了什么？这篇文章拆解架构、分析风险、给你一个决策框架。 -->

# Claude Managed Agents 全面解析：它解决什么问题，适合谁，有什么风险

> 想直接动手？看配套教程：[手把手创建你的第一个 Claude Managed Agent](how-to-create-first-claude-managed-agent.md)

"Anthropic killed 1000+ agent startups."

"There goes a whole YC batch."——这条推文在发布当天获得了 200 万浏览。

2026 年 4 月 9 日，Anthropic 发布 Claude Managed Agents（公开 Beta）。一句话：**你定义 agent 做什么，Anthropic 负责跑。**

怎么理解它的定位？

```
Messages API     →  自己造车、自己开
Agent SDK        →  自己开车，平台给你导航
Managed Agents   →  自动驾驶，你只说去哪
```

如果你用过 Claude Code，Managed Agents 就是 Claude Code 的 API 化——同样的工具集、同样的 harness 设计，只不过现在跑在云端、可以通过 API 调用、可以无人值守地异步运行。

---

## 问题：搭 Agent 基础设施有多痛

用 Messages API 构建一个能跑起来的 agent，你要自己搞定：

1. **Agent loop** — 调用模型 → 解析工具调用 → 执行工具 → 把结果喂回模型 → 循环
2. **沙盒** — 代码执行需要隔离环境，不能让 agent 把你的服务器搞挂
3. **工具执行** — bash、文件操作、网络请求的安全调度
4. **上下文管理** — prompt caching、compaction、长对话处理
5. **状态恢复** — session 断了怎么办？harness 挂了怎么办？

行业共识：这套基础设施要 **3-6 个月**的工程量。而真正有价值的工作——定义 agent 做什么——只占你 10% 的时间。

Managed Agents 把这 5 件事全包了。你只管两件事：**定义 agent** 和**消费结果**。

---

## 架构：为什么它能做到这些

这是 Managed Agents 最精妙的设计。来自 Anthropic 工程团队的架构博客，核心思想：把大脑、双手、记忆解耦成三个独立组件。

![[managed-agents-architecture.png]]

**Brain（大脑）= Claude 模型 + Harness 控制循环**

Harness 是无状态的。它调用模型、路由工具调用，仅此而已。可以随时重启或替换，不丢失任何状态。

**Hands（双手）= 容器 + 工具**

8 个内置工具：bash、read、write、edit、glob、grep、web_fetch、web_search——和 Claude Code 完全一致。所有工具遵循统一接口。容器**惰性创建**：只在工具真正需要时才启动。

**Session（记忆）= Append-only 事件日志**

存在 harness 外部，持久化。它才是整个系统的 source of truth——不是 harness，不是容器。任何组件崩溃都不影响 session 数据。

**为什么这么设计？** 传统 agent 架构把状态绑在 harness 上——harness 挂了，session 就没了。Managed Agents 把状态外化，harness 变成纯粹的无状态执行器。带来三个好处：

- **容错**：组件可以独立失败和恢复
- **可审计**：所有操作都在 event log 里
- **性能**：惰性容器创建让 p50 TTFT 提升 ~60%，p95 提升 >90%

---

## 你得到什么

### 核心能力（公开 Beta）

**三个资源模型：** 创建一个 Agent（配置模板：模型 + system prompt + 工具），创建一个 Environment（容器模板：包 + 网络策略），然后按需启动 Session（运行实例）。Agent 和 Environment 创建一次、反复复用，Session 每个任务创建一个。

**工具系统：** 一行代码启用全部 8 个内置工具（`agent_toolset_20260401`），也可以逐个开关。支持自定义工具（你的代码执行，结果流回 agent）和 MCP 服务器集成。OAuth token 在安全 vault 里，永远不进入代码沙盒。

**事件流式：** 所有交互通过双向事件进行，SSE 实时推送。你可以在 agent 工作过程中发送新消息引导方向，或直接中断。

**安全：** 每个 session 获得隔离容器。凭证永远不进入执行沙盒。网络策略支持 unrestricted（开发）和 limited + 白名单（生产）。

### 研究预览功能（需要额外申请）

**Outcomes（目标驱动）：** 你定义 rubric，一个独立的 Grader agent 评估产出——不是让 agent 自己评价自己（那会有自我评估偏差）。Agent 自动迭代直到 Grader 满意，最多 20 轮。

**Multi-Agent（多智能体）：** 一个 Coordinator 委派任务给专业 agent，每个 agent 有自己的上下文隔离线程，但共享文件系统。只有一级委派，不能套娃。

**Memory Stores（持久化记忆）：** 跨 session 携带学习成果。Agent 自动在开始时读取、完成后写入——不需要额外 prompt。每次写入生成不可变版本，支持审计和 redact。

---

## 谁在用

Managed Agents 不是 PPT 产品。发布时已经有 5 家公司在生产环境跑：

| 公司 | 怎么用 | 结果 |
|------|--------|------|
| **Notion** | 并行任务委派，工程师在 workspace 里直接 ship 代码 | 知识工作者不离开 Notion 就能生成演示和网站 |
| **Rakuten** | 跨部门部署专业 agent | 每个专业 agent **一周内**部署完成 |
| **Asana** | AI Teammates 嵌入项目管理工作流 | Agent 自动 pick up 被分配的任务 |
| **Sentry** | 根因分析 + 自动代码修复 | 自动生成修复 PR |
| **Vibecode** | 应用部署加速 | 部署速度 **10x** 提升 |

---

## 该不该用？决策框架

### 三向对比

| | Messages API | Agent SDK | Managed Agents |
|---|---|---|---|
| **你负责** | 一切 | Agent loop + 工具执行 | 定义 agent + 消费结果 |
| **基础设施** | 你自己的 | 你自己的 | Anthropic 的云 |
| **适合** | 极细粒度控制 | 自定义 agent 行为 | 快速上线、异步长任务 |
| **上手时间** | 周 ~ 月 | 天 ~ 周 | 小时 ~ 天 |
| **锁定程度** | 低 | 中 | 高 |

### 用 Managed Agents，当你...

- 任务需要长时间运行（几分钟到几小时，大量工具调用）
- 需要异步工作（提交任务，稍后获取结果）
- 团队不想维护 agent 基础设施
- 已经选定 Claude 作为模型
- 工作负载是间歇式的（按 session-hour 计费比包月服务器便宜）

### 自己搭，当你...

- 需要极细粒度控制 agent loop 的行为
- 多云部署或需要在自己的基础设施上运行
- 不能接受数据流经第三方云
- 需要 Managed Agents 尚未支持的功能

---

## 诚实的风险

好的文章不只讲优点。以下是你在决策前应该知道的：

**Beta 状态。** 功能可能变化，API 可能调整。Anthropic 承诺 beta header 版本化，但早期用户需要接受不稳定性。

**Vendor lock-in。** 一旦 agent 跑在 Anthropic 的基础设施上，迁移到 Agent SDK 或自建方案大约需要 **4-8 周工程量**。你的 agent 定义、环境配置、session 历史都在他们的平台上。

**成本真相。** $0.08/session-hour 听起来便宜。但算一笔账：
- 1 个 agent 跑 24/7 ≈ **$58/月**（纯运行费，不含 token）
- 10 个 agent 跑 24/7 ≈ **$580/月**
- 再加上 token 费用（Sonnet 4.6: $3/$15 per million tokens）

间歇式工作负载很划算，但常驻 agent 的成本会快速累积。

**数据流向。** 你的代码、文件、对话——一切都流经 Anthropic 的云。如果你处理敏感数据或有合规要求，这是一个真实的考量。

**研究预览功能。** Outcomes、Multi-Agent、Memory 目前需要额外申请。不要基于这些功能做架构决策——它们可能改变。

---

## 定价速查

| 组成 | 费用 |
|------|------|
| Token 消耗 | 标准 Claude 费率 |
| Session 运行时间 | $0.08/session-hour |

Rate limits: 创建端点 60 req/min，读取端点 600 req/min。

所有请求需要 header: `anthropic-beta: managed-agents-2026-04-01`。

SDK 支持 Python、TypeScript、Go、Java、C#、Ruby、PHP。另有 `ant` CLI。

---

## 接下来

**想动手试试？** [手把手创建你的第一个 Claude Managed Agent](how-to-create-first-claude-managed-agent.md) — 从零到跑通，10 分钟。

**想看官方文档？** [Claude Managed Agents Overview](https://platform.claude.com/docs/en/managed-agents/overview) | [Engineering Blog: Decoupling the Brain from the Hands](https://www.anthropic.com/engineering/managed-agents)

**值得持续关注：** 三个研究预览功能（Outcomes、Multi-Agent、Memory）一旦 GA，Managed Agents 的价值会再上一个台阶——特别是 Outcomes 的 rubric-driven 自动迭代，这可能改变 agent 的质量保证方式。

<!-- CTA: Claude Managed Agents 公开 Beta 已开放给所有 API 账户。如果你的场景是异步长任务、不想管基础设施、且能接受 Anthropic 云——现在是最好的上车时机。 -->
