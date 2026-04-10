---
status: draft
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-09-anthropic-agent-capabilities-announcement.md
platform: blog
created: 2026-04-09
last-updated: 2026-04-10
tags: [draft, tutorial, anthropic, agents]
pair-article: drafts/claude-managed-agents-overview.md
---

<!-- HOOK: 自己搭 agent 基础设施要 3-6 个月。用 Claude Managed Agents，10 分钟从零到跑通。这篇教程用一个真实场景带你走一遍。 -->

# 手把手创建你的第一个 Claude Managed Agent

> 概念深入解析：[Claude Managed Agents 全面解析](claude-managed-agents-overview.md)

自己搭 agent 基础设施的痛，做过的人都知道：agent loop、容器沙盒、工具执行调度、上下文管理、断点恢复——光这套基础设施就要 3-6 个月，而你真正想做的事（定义 agent 的行为）只占 10% 的时间。

Claude Managed Agents 把这些全包了。**你定义 agent 做什么，Anthropic 负责跑。**

这篇教程用一个真实场景带你从零跑通。不是 Fibonacci——我们让 agent 分析一个 Python 项目，找出所有 TODO 注释，生成一份结构化的清单。这是你日常可能真的会用到的东西。

## 心智模型：三样东西

开始之前，你只需要理解三个资源：

| 资源 | 类比 | 创建频率 |
|------|------|---------|
| **Agent** | 大脑——模型 + system prompt + 工具 | 创建一次，反复复用 |
| **Environment** | 工位——容器配置、包、网络 | 创建一次，反复复用 |
| **Session** | 一次任务——绑定大脑和工位，开始干活 | 每个任务一个 |

就这么简单。定义大脑，准备工位，启动任务。

## 前置准备

```bash
# 安装 SDK（选一个）
pip install anthropic        # Python
npm install @anthropic-ai/sdk  # TypeScript

# 设置 API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

## 从零到跑通

### 定义 Agent

第一步是告诉平台"这个 agent 是谁"。Agent 是一个可复用的配置——创建一次，以后每个任务都引用同一个 ID。

```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="Code Analyst",
    model="claude-sonnet-4-6",
    system="You are a code analysis assistant. When given a codebase, analyze it thoroughly and produce structured reports.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)

print(f"Agent ID: {agent.id}")  # 保存这个 ID
```

`agent_toolset_20260401` 一行代码启用全部 8 个内置工具：Bash、Read、Write、Edit、Glob、Grep、Web Fetch、Web Search。和 Claude Code 的工具集完全一致。

模型怎么选？**Sonnet 4.6 是 agent 任务的最佳平衡点。** 别默认用 Opus——贵 5 倍但对大多数 agent 任务没必要。Haiku 适合简单、高频的轻量任务。

### 准备 Environment

接下来告诉平台"agent 跑在什么环境里"。

```python
environment = client.beta.environments.create(
    name="analysis-env",
    config={
        "type": "cloud",
        "packages": {
            "pip": ["pylint", "black"],
        },
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")
```

Environment 定义容器模板——安装什么包、能访问什么网络。同样创建一次，所有相关 session 都引用同一个。每个 session 获得自己隔离的容器实例，互不干扰。

### 启动 Session，发消息

现在万事俱备。创建 session，发消息，看 agent 工作。

```python
# 创建 session
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Analyze TODO items",
)

# 打开 stream，发消息，实时获取结果
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": """Clone https://github.com/pallets/flask (shallow clone).
Find all TODO and FIXME comments in the Python files.
Generate a report saved to /mnt/session/outputs/todo-report.md with:
- Total count
- Each item with file path, line number, and the comment content
- Grouped by directory""",
                    },
                ],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[工具: {event.name}]")
            case "session.status_idle":
                print("\n\n✅ 完成。")
                break
```

### 你会看到什么

```
I'll clone the Flask repository and analyze it for TODO/FIXME comments.
[工具: bash]
Repository cloned. Now scanning for TODO and FIXME comments...
[工具: grep]
[工具: bash]
Found 23 TODO/FIXME items across 12 files. Generating the report...
[工具: write]

Report saved to /mnt/session/outputs/todo-report.md

✅ 完成。
```

停一下，想想刚才发生了什么。

你只说了"做什么"——clone repo、找 TODO、生成报告。**agent 自己决定了怎么做：** 用 bash 执行 git clone，用 grep 搜索注释，再用 write 生成报告文件。没有人告诉它用哪个工具、按什么顺序。

这就是 Managed Agents 的核心价值：你描述目标，agent 自主规划和执行。

### 为什么这能工作

底层的架构设计让这成为可能：

1. **容器惰性创建** — session 创建时不启动容器，只有当 agent 第一次调用 bash 或 write 时才 provision。这就是为什么启动速度很快。
2. **Harness 无状态** — 控制循环不持有任何状态。状态全在 session 的事件日志里。如果 harness 崩溃，重启后从日志恢复。
3. **Session 是 source of truth** — 一个 append-only 的事件日志，记录了所有对话、工具调用和结果。任何组件挂了都不影响这份日志。

> 想深入了解这个架构？看 [Anthropic 工程博客: Decoupling the Brain from the Hands](https://www.anthropic.com/engineering/managed-agents)

---

## 进阶：从 Hello World 到生产级

### 限制工具权限

默认全部 8 个工具都开启。生产环境应该只给 agent 需要的：

```python
# 只读分析 agent——不能写文件、不能跑命令
agent = client.beta.agents.create(
    name="Read-Only Analyst",
    model="claude-sonnet-4-6",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "default_config": {"enabled": False},
            "configs": [
                {"name": "read", "enabled": True},
                {"name": "glob", "enabled": True},
                {"name": "grep", "enabled": True},
            ],
        },
    ],
)
```

最小权限原则：code review agent 不需要 bash，调研 agent 不需要 write。

### 自定义工具

内置工具不够用？你可以定义自己的：

```python
agent = client.beta.agents.create(
    name="Ticket Agent",
    model="claude-sonnet-4-6",
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "custom",
            "name": "create_ticket",
            "description": "Create a ticket in the project tracker. Use when you identify an issue that needs follow-up.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "priority": {"type": "string", "enum": ["low", "medium", "high"]},
                    "body": {"type": "string"},
                },
                "required": ["title", "priority", "body"],
            },
        },
    ],
)
```

当 agent 调用自定义工具时，session 暂停（`requires_action`）。你在自己这边执行，发回结果，agent 继续。

### 中途引导和中断

Session 是交互式的。agent 在工作过程中，你可以改变方向或直接叫停：

```python
# 改变方向
client.beta.sessions.events.send(
    session.id,
    events=[{
        "type": "user.message",
        "content": [{"type": "text", "text": "也把 HACK 和 XXX 注释加上。"}],
    }],
)

# 或者直接中断
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt"}],
)
```

---

## 踩坑提醒

写完 happy path，说几个实际会遇到的问题：

**成本意识。** $0.08/session-hour + token 费用。一个 session 跑 30 分钟 ≈ $0.04 运行费 + 几美分 token。很便宜。但如果你跑 24/7 常驻 agent，那是 $58/月/agent 纯运行费。间歇式任务最划算。

**模型选择。** 别默认 Opus。Sonnet 4.6 是 agent 任务的最佳平衡——更快、更便宜（$3/$15 vs $15/$75 per million tokens），对大多数任务效果一样好。先用 Sonnet，只在任务确实需要更强推理时升级 Opus。

**网络策略。** 开发时 `unrestricted` 没问题，但生产环境**一定要用 `limited` + 白名单**。默认的 unrestricted 有安全黑名单，但你不会想让你的 agent 可以访问整个互联网。

**Session 清理。** Session 不会自动消失。完成后记得 archive 或 delete，否则它们会一直挂在那里。

**Beta 状态。** 这是公开 Beta，不是 GA。API 可能调整，功能可能变化。不要在 mission-critical 场景中当作唯一方案。

---

## 速查表

### Headers

```
anthropic-version: 2023-06-01
anthropic-beta: managed-agents-2026-04-01
x-api-key: YOUR_API_KEY
```

### 模型

| 模型 | 适用 | Token 价格 (input/output per M) |
|------|------|------|
| `claude-sonnet-4-6` | 推荐默认 | $3 / $15 |
| `claude-opus-4-6` | 复杂推理 | $15 / $75 |
| `claude-haiku-4-5` | 轻量高频 | $0.80 / $4 |

### 定价

标准 Claude token 费率 + $0.08/session-hour。

### SDK

Python、TypeScript、Go、Java、C#、Ruby、PHP — 全部通过 `anthropic` 包。另有 `ant` CLI。

---

## 接下来

试着把例子换成你自己的场景。几个方向：

- 让 agent 审查 PR diff 并生成 review 报告
- 让 agent 爬取竞品网站并生成对比分析
- 让 agent 读取日志文件并做根因分析

三个研究预览功能值得关注：**Outcomes**（定义评分标准，agent 自动迭代到达标）、**Multi-Agent**（coordinator 委派专业 agent）、**Memory**（跨 session 记住上下文）。这些功能 GA 后会让 Managed Agents 的价值再上一个台阶。

Notion、Asana、Sentry、Rakuten 已经在用 Managed Agents 构建产品。如果你的场景是异步长任务、不想管基础设施——现在是最好的上手时机。

> 想深入了解所有概念和架构？看 [Claude Managed Agents 全面解析](claude-managed-agents-overview.md)

<!-- CTA: Beta 已开放给所有 API 账户。从 Sonnet 4.6 + 全工具集开始，跑起来再说。 -->
