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

<!-- HOOK: Anthropic 在 2026 年 4 月 9 日发布了 Claude Managed Agents。不是又一个 agent framework，而是一个完整的托管基础设施——你定义 agent 是谁、在哪里跑、做什么，剩下的全部交给平台。这篇文章拆解它的每一个核心概念。 -->

# Claude Managed Agents 全面解析

> 配套实战教程：[How to Create My First Claude Managed Agent](how-to-create-first-claude-managed-agent.md)

2026 年 4 月 9 日，Anthropic 正式发布 Claude Managed Agents（公开 Beta）。这不是一个 SDK 或 framework——它是一个**全托管的 agent 运行平台**。你不需要自己写 agent loop、不需要管容器、不需要处理 tool execution 的基础设施。你定义好 agent、environment、session，平台帮你跑。

一句话定位：**Messages API 是你自己开车，Managed Agents 是你叫了一辆自动驾驶出租车。**

## 为什么需要 Managed Agents

用 Messages API 构建 agent 意味着你要自己搞定：

- Agent loop（调用模型 → 解析工具调用 → 执行工具 → 把结果喂回模型 → 循环）
- 沙盒（代码执行需要隔离环境）
- 工具执行（bash、文件操作、网络请求的安全调度）
- 上下文管理（prompt caching、compaction、长对话处理）
- 状态持久化（session 断了怎么恢复）

Managed Agents 把这些全包了。你只管两件事：**定义 agent 做什么**和**消费 agent 产出的结果**。

适用场景：
- 长时间运行的任务（几分钟到几小时，大量工具调用）
- 异步工作（提交任务，稍后获取结果）
- 不想维护 agent 基础设施的团队

不适用：需要极细粒度控制 agent loop 的场景——那还是用 Messages API + Agent SDK。

---

## 核心概念：三个资源

整个系统围绕三个核心资源运转：

### 1. Agent（智能体配置）

Agent 是一个**可复用的配置**，不是一个运行中的实例。你可以把它理解为一个"角色模板"。

| 字段 | 说明 |
|------|------|
| `name` | 名称（必填） |
| `model` | 使用哪个 Claude 模型（必填）。支持所有 4.5+ 模型 |
| `system` | System prompt，定义行为和人格 |
| `tools` | 工具配置（内置工具集、自定义工具、MCP 工具） |
| `mcp_servers` | 连接的 MCP 服务器 |
| `skills` | 领域知识包，支持 progressive disclosure |
| `callable_agents` | 可调用的其他 agent（多智能体，研究预览） |
| `description` | 描述 |
| `metadata` | 自定义键值对 |

**关键特性：**
- Agent 有版本管理。每次 update 生成新版本，支持查看完整版本历史。
- Update 使用乐观并发控制（传入当前 `version`），避免竞争写入。
- 可以 archive（只读，现有 session 继续跑，不能新建 session）。

**模型选择：**
| 模型 | 定位 |
|------|------|
| `claude-opus-4-6` | 最强智能，复杂任务 |
| `claude-sonnet-4-6` | 速度与智能的最佳平衡（推荐默认选择） |
| `claude-haiku-4-5` | 最快，简单任务 |

Opus 还支持 fast mode：`model={"id": "claude-opus-4-6", "speed": "fast"}`。

### 2. Environment（运行环境）

Environment 定义了 agent 跑在什么样的容器里——安装什么包、能访问什么网络。

**包管理器支持：**

| 字段 | 包管理器 |
|------|----------|
| `pip` | Python |
| `npm` | Node.js |
| `apt` | 系统包 |
| `cargo` | Rust |
| `gem` | Ruby |
| `go` | Go modules |

**网络策略：**
- `unrestricted`（默认）：完全开放出站访问，平台安全黑名单生效
- `limited`：只允许 `allowed_hosts` 列表中的域名，另有 `allow_mcp_servers` 和 `allow_package_managers` 开关

**关键特性：**
- 不分版本——update 直接覆盖
- 多个 session 可以引用同一个 environment
- 每个 session 获得自己隔离的容器实例（共享配置，隔离运行）

### 3. Session（会话实例）

Session 是一个**正在运行的 agent 实例**。它绑定一个 Agent 配置 + 一个 Environment，然后开始干活。

Session 的本质是一个 **append-only 的事件日志**。所有对话、工具调用、结果、状态变化都记录在这个日志里。这个日志存在 harness 外面，是整个系统的 source of truth。

Session 状态流转：
```
创建 → running（处理中）→ idle（等待输入）→ running → idle → ...
                              ↘ terminated（不可恢复的错误）
          rescheduled（临时错误，自动重试）↗
```

**输出文件：** Agent 把交付物写到 `/mnt/session/outputs/`，通过 Files API 获取。

---

## 架构设计：Brain / Hands / Session

这是 Managed Agents 最精妙的设计，来自 Anthropic 工程团队的架构博客。

### 核心思想：解耦三个组件

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Brain     │     │    Hands    │     │   Session   │
│ Claude +     │────▶│ Containers  │     │ Append-only │
│ Harness Loop │     │ + Tools     │     │ Event Log   │
└─────────────┘     └─────────────┘     └─────────────┘
   stateless          lazy provision       durable state
   可重启              按需创建             source of truth
```

**Brain（大脑）= Claude 模型 + Harness 控制循环**
- Harness 是无状态的。它调用模型、路由工具调用，仅此而已。
- 可以随时重启或替换，不丢失任何状态——因为状态在 session 里。

**Hands（双手）= 容器 + 工具**
- 所有工具都遵循统一接口：`execute(name, input) → string`
- 不管是 bash 命令、文件操作还是 API 调用，harness 看到的都是同一种东西
- **惰性创建**：容器只在工具真正需要时才启动，不是 session 创建时就启动

**Session（记忆）= Append-only 事件日志**
- 存在 harness 外部，持久化
- 通过 `getEvents()` 访问，支持 positional slices
- 每次工具调用通过 `emitEvent(id, event)` 记录
- 任何组件崩溃都不影响 session 数据

### 为什么这么设计

传统 agent 架构把状态绑在 harness 上——harness 挂了，session 就没了。Managed Agents 把状态外化到 session 日志，harness 变成纯粹的无状态执行器。这带来了：
- **容错**：组件可以独立失败和恢复
- **可审计**：所有操作都在 event log 里
- **可重放**：理论上可以从 event log 重建任何时刻的状态

### 性能数据

惰性容器创建带来了显著的性能提升：
- **p50 TTFT（首 token 时间）提升 ~60%**
- **p95 TTFT 提升 >90%**

因为不需要在 session 开始时就创建容器，只有当 agent 真正要执行 bash 或写文件时才 provision。

---

## 工具系统

### 内置工具（agent_toolset_20260401）

| 工具 | 功能 |
|------|------|
| `bash` | 执行 bash 命令 |
| `read` | 读文件 |
| `write` | 写文件 |
| `edit` | 字符串替换编辑 |
| `glob` | 文件模式匹配 |
| `grep` | 正则文本搜索 |
| `web_fetch` | 抓取 URL 内容 |
| `web_search` | 搜索网页 |

和 Claude Code 的工具集完全一致——因为 Managed Agents 本质上就是 Claude Code 的云端托管版。

**工具控制粒度：**

```python
# 全部启用
tools=[{"type": "agent_toolset_20260401"}]

# 禁用特定工具
tools=[{"type": "agent_toolset_20260401",
        "configs": [{"name": "web_fetch", "enabled": False}]}]

# 只启用特定工具
tools=[{"type": "agent_toolset_20260401",
        "default_config": {"enabled": False},
        "configs": [{"name": "bash", "enabled": True},
                    {"name": "read", "enabled": True}]}]
```

### 自定义工具

你定义 schema，Claude 发起调用，你的代码执行，结果返回。Session 在等待你返回结果时进入 `requires_action` 状态。

### MCP 集成

Managed Agents 原生支持 MCP（Model Context Protocol）服务器。OAuth token 存在安全 vault 里，Claude 通过专用 proxy 调用 MCP 工具——token 永远不会进入代码执行沙盒。

### 工具确认机制

权限策略支持两种模式：
- `always_allow`：直接执行
- `always_ask`：agent 暂停，等待你发送 `user.tool_confirmation`（allow 或 deny）

---

## 事件系统与流式传输

Managed Agents 的所有交互都通过事件（Events）进行。这是一个双向系统：

### 你发给 Agent 的事件

| 类型 | 说明 |
|------|------|
| `user.message` | 用户消息 |
| `user.interrupt` | 中断 agent 执行 |
| `user.custom_tool_result` | 返回自定义工具结果 |
| `user.tool_confirmation` | 批准/拒绝工具调用 |
| `user.define_outcome` | 定义目标（研究预览） |

### Agent 发回的事件

| 类型 | 说明 |
|------|------|
| `agent.message` | 文字回复 |
| `agent.thinking` | 思维过程（extended thinking） |
| `agent.tool_use` | 内置工具调用 |
| `agent.tool_result` | 内置工具结果 |
| `agent.custom_tool_use` | 自定义工具调用 |
| `agent.mcp_tool_use` / `mcp_tool_result` | MCP 工具调用与结果 |
| `agent.thread_message_sent` / `received` | 多智能体消息 |
| `agent.thread_context_compacted` | 上下文压缩发生 |

### Session 级事件

| 类型 | 说明 |
|------|------|
| `session.status_running` | 正在处理 |
| `session.status_idle` | 完成，等待输入。附带 `stop_reason` |
| `session.status_rescheduled` | 临时错误，自动重试 |
| `session.status_terminated` | 不可恢复错误 |
| `session.outcome_evaluated` | 目标评估完成 |
| `session.thread_created` / `thread_idle` | 多智能体线程 |

### Stop Reasons

| 原因 | 含义 |
|------|------|
| `end_turn` | Agent 自然结束 |
| `max_tokens` | 单轮 token 上限 |
| `requires_action` | 需要你介入（自定义工具结果、工具确认） |

### 流式协议

通过 SSE（Server-Sent Events）实时获取 agent 的所有输出：

```
GET /v1/sessions/{id}/stream
Accept: text/event-stream
```

你可以在 agent 执行过程中随时发送新的 `user.message` 来引导方向，或发送 `user.interrupt` 中断执行。

---

## 三大研究预览功能

这三个功能需要额外的 beta header：`managed-agents-2026-04-01-research-preview`

### 1. Outcomes（目标驱动模式）

这是 Managed Agents 最有野心的功能。它把 session 从"对话"升级为"工作"——你定义目标和评分标准，agent 自动迭代直到达标。

**工作流程：**

```
你定义 rubric（评分标准）
        ↓
发送 user.define_outcome 事件
        ↓
Agent 开始工作，产出第一版
        ↓
┌──────────────────────────────┐
│ Grader（独立上下文窗口）       │
│ 逐条评估 rubric criteria      │
│ 返回：满足 / 具体 gap          │
└──────────────────────────────┘
        ↓
  satisfied? → idle
  needs_revision? → Agent 根据反馈迭代 → 再次评估
  max_iterations_reached? → 最后一次修改 → idle
  failed? → rubric 与任务不匹配 → idle
```

**为什么用独立的 Grader？**

避免自我评估偏差。如果让 agent 自己评价自己的输出，它会倾向于认为自己做得不错。独立 Grader 有自己的上下文窗口，只看到 rubric 和产出物，不看到实现过程。

**Rubric 最佳实践：**
- 每个标准独立评分，不要模糊描述
- 不要写"数据看起来不错"，要写"每一列都有正确的数据类型，空值比例 < 5%"
- 可以用 Files API 上传 rubric 供多个 session 复用
- 启动技巧：给 Claude 一个高质量样本，让它分析优点，把分析转化为 rubric

**交付物：** Agent 写入 `/mnt/session/outputs/`，通过 Files API 获取。

`max_iterations` 默认 3 次，最多 20 次。

### 2. Multi-Agent（多智能体协调）

一个 Coordinator agent 指挥多个专业 agent 协同工作。

**架构：**

```
Coordinator（主线程）
  ├── Agent A: Code Reviewer（线程 A）
  ├── Agent B: Test Writer （线程 B）
  └── Agent C: Researcher  （线程 C）
```

**关键设计：**
- 所有 agent 共享同一个容器和文件系统
- 每个 agent 有自己独立的**线程（thread）**——独立的上下文窗口和对话历史
- 线程是持久的：coordinator 可以对同一个 agent 发送后续指令，agent 保留之前的上下文
- **只有一级委派**：coordinator → callees，callees 不能再调用其他 agent
- 每个 callable agent 独立配置：可以用不同模型、不同 system prompt、不同工具集

**Session 状态聚合：** 任何一个线程处于 `running`，整个 session 就是 `running`。主线程显示所有活动的精简视图，需要细节可以 drill down 到具体线程。

**适合委派的任务：**
- Code review（只读工具 + 专注的 system prompt）
- 测试生成（写测试 + 运行测试，不碰生产代码）
- 调研（web 工具，总结发现汇报给 coordinator）

### 3. Memory Stores（持久化记忆）

让 agent 跨 session 携带学习成果：用户偏好、项目惯例、之前犯的错、领域知识。

**工作方式：**
- 创建 Memory Store（workspace 级别的文本文档集合）
- Attach 到 session 的 `resources[]` 数组
- Agent **自动**在开始工作前检查 memory store，完成后写入学习成果——不需要额外 prompt

**自动注入的 Memory 工具：**
| 工具 | 功能 |
|------|------|
| `memory_list` | 列出 memories，按路径前缀过滤 |
| `memory_search` | 全文搜索 |
| `memory_read` | 读取内容 |
| `memory_write` | 创建或覆盖 |
| `memory_edit` | 修改现有 memory |
| `memory_delete` | 删除 |

**限制：**
- 每个 session 最多 attach 8 个 memory stores
- 单个 memory 最大 100KB（约 25K tokens）
- 访问模式：`read_write` 或 `read_only`

**版本与审计：**
- 每次写入都生成不可变的 memory version（`memver_...`）
- 支持按 memory_id、操作类型、session_id、时间范围过滤版本
- **Redact**：可以擦除历史版本的内容但保留审计轨迹（合规用途：PII、泄漏的 secrets、用户删除请求）
- 乐观并发控制：通过 `content_sha256` precondition 防止并发写入冲突

**使用模式：**
- 共享参考资料（read-only，跨多个 session）
- 按用户/团队/项目组织不同 store
- 用内容预填充 store，agent 启动前就有上下文

---

## 安全模型

三个层面的安全设计：

### 1. 容器隔离
每个 session 获得独立的容器实例，即使引用同一个 environment。

### 2. 凭证隔离
**Credentials 永远不会进入代码执行沙盒。** 三种认证模式：
- 在沙盒初始化时用凭证拉取资源（如 git clone），凭证不暴露给后续代码
- OAuth token 存在安全 vault，通过专用 proxy 访问
- MCP 工具通过绑定 session 的 token 调用 proxy

### 3. 网络控制
- 默认 unrestricted 有安全黑名单
- 生产环境建议用 `limited` + 白名单

---

## 配套发布的四项 API 能力

Managed Agents 不是孤立发布的。Anthropic 同时推出了四个配套的 beta 功能：

| 功能 | 说明 |
|------|------|
| **Code Execution Tool** | Python 沙盒执行。数据分析、可视化、科学计算。50 小时/org/天免费，超出 $0.05/小时 |
| **MCP Connector** | API 原生连接远程 MCP 服务器，不需要写 client 代码。自动处理连接管理和工具发现 |
| **Files API** | 上传文档一次，跨对话重复引用。和 Code Execution 集成 |
| **Extended Prompt Caching** | 1 小时 TTL（标准是 5 分钟）。长时间 agent 工作流成本降低最多 90% |

---

## 定价

| 组成 | 费用 |
|------|------|
| Token 消耗 | 标准 Claude 费率 |
| Session 运行时间 | $0.08/session-hour |

Rate limits:
- 创建类端点（agents, sessions, environments）：60 请求/分钟
- 读取类端点（retrieve, list, stream）：600 请求/分钟

---

## API 速查

所有请求需要的 headers：
```
anthropic-version: 2023-06-01
anthropic-beta: managed-agents-2026-04-01
x-api-key: YOUR_API_KEY
```

研究预览功能额外需要：
```
anthropic-beta: managed-agents-2026-04-01-research-preview
```

**SDK 支持：** Python, TypeScript, Go, Java, C#, Ruby, PHP — 全部通过 `anthropic` 包。

**CLI 工具：** `ant`（Anthropic CLI），通过 Homebrew、curl 或 Go 安装。

---

## 总结：怎么理解 Managed Agents 的定位

```
Messages API     →  你自己造车、自己开
Agent SDK        →  你自己开车，平台给你导航
Managed Agents   →  自动驾驶，你只说去哪
```

Managed Agents 解决的是 **agent infrastructure** 问题。绝大多数团队想要的不是"构建 agent framework 的能力"，而是"让 agent 帮我完成工作的能力"。你不需要理解 agent loop 怎么跑、容器怎么管、prompt caching 怎么做——你只需要定义 agent 是谁、环境是什么样、目标是什么。

如果你之前用过 Claude Code，Managed Agents 就是 Claude Code 的 API 化。同样的工具集（bash, read, write, edit, glob, grep, web_fetch, web_search），同样的 harness 设计理念，只不过现在你可以通过 API 调用、可以跑在云端、可以无人值守地异步运行。

> 想动手试试？看配套教程：[How to Create My First Claude Managed Agent](how-to-create-first-claude-managed-agent.md)

<!-- CTA: Claude Managed Agents 公开 Beta 已开放给所有 API 账户。从 Sonnet 4.6 + 全工具集开始，五分钟就能跑起来你的第一个 managed agent。 -->
