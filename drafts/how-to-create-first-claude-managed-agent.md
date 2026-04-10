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

<!-- HOOK: Anthropic 刚发布了 Claude Managed Agents——一个托管服务，让你不用自建基础设施就能部署自主 AI agent。这篇教程带你从零到跑通，10 分钟以内。 -->

# 手把手创建你的第一个 Claude Managed Agent

> 配套概念解析：[Claude Managed Agents 全面解析](claude-managed-agents-overview.md)

Anthropic 在 2026 年 4 月 9 日发布了 Claude Managed Agents。不用自己写 agent loop，不用管容器沙盒，不用处理工具执行层——这些全部托管。Claude 可以在安全的云端容器里读写文件、跑 shell 命令、搜索网页、执行代码，全程自主完成。

这篇教程带你从环境搭建到流式获取结果，完整走一遍。

## 你会构建什么

一个 coding assistant agent，能够：
- 在云端容器里写代码、执行代码
- 读写文件
- 搜索网页获取信息
- 实时流式返回结果

整个教程花费：几美分的 token + $0.08/session-hour。

## 心智模型：你只需要创建三样东西

写代码之前，先理解三个核心资源：

| 资源 | 它是什么 | 创建一次还是每次？ |
|------|---------|-------------------|
| **Agent** | "谁"——模型、system prompt、工具 | 创建一次，跨 session 复用 |
| **Environment** | "在哪"——容器配置、包、网络 | 创建一次，跨 session 复用 |
| **Session** | "做什么"——一个正在执行具体任务的运行实例 | 每个任务创建一个 |

类比：你定义一个 Agent（大脑）和一个 Environment（工作台），然后按需启动 Session（具体的活）。

## 前置准备

- Anthropic API key（[在这里获取](https://console.anthropic.com/settings/keys)）
- Python 3.8+ 或 Node.js 18+（或者直接用 curl）

安装 SDK：

```bash
# Python
pip install anthropic

# TypeScript
npm install @anthropic-ai/sdk
```

设置 API key：

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## 第一步：创建 Agent

Agent 是一个可复用的配置——模型、system prompt 和工具打包在一起。创建一次，之后用 ID 引用就行。

### Python

```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    system="You are a helpful coding assistant. Write clean, well-documented code.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)

print(f"Agent ID: {agent.id}")
# 保存这个 ID——每次创建 session 都要用
```

### TypeScript

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const agent = await client.beta.agents.create({
  name: "Coding Assistant",
  model: "claude-sonnet-4-6",
  system: "You are a helpful coding assistant. Write clean, well-documented code.",
  tools: [{ type: "agent_toolset_20260401" }],
});

console.log(`Agent ID: ${agent.id}`);
```

### curl

```bash
curl -s https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "name": "Coding Assistant",
    "model": "claude-sonnet-4-6",
    "system": "You are a helpful coding assistant. Write clean, well-documented code.",
    "tools": [{"type": "agent_toolset_20260401"}]
  }'
```

**`agent_toolset_20260401` 是什么？** 一次性启用全部 8 个内置工具：Bash、Read、Write、Edit、Glob、Grep、Web Fetch、Web Search。需要更细粒度的控制可以单独禁用——后面会讲。

**模型怎么选？** 所有 Claude 4.5+ 模型都支持。`claude-sonnet-4-6` 是大多数 agent 任务的最佳平衡点。复杂任务用 `claude-opus-4-6`，追求速度用 `claude-haiku-4-5`。

## 第二步：创建 Environment

Environment 定义 agent 运行的容器——安装什么包、能访问什么网络。

### Python

```python
environment = client.beta.environments.create(
    name="quickstart-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")
```

### TypeScript

```typescript
const environment = await client.beta.environments.create({
  name: "quickstart-env",
  config: {
    type: "cloud",
    networking: { type: "unrestricted" },
  },
});

console.log(`Environment ID: ${environment.id}`);
```

这会创建一个拥有完全出站网络权限的基础容器。生产环境建议锁紧：

```python
# 生产环境：限制网络到特定域名
environment = client.beta.environments.create(
    name="prod-env",
    config={
        "type": "cloud",
        "packages": {
            "pip": ["pandas", "numpy", "requests"],
            "npm": ["express"],
        },
        "networking": {
            "type": "limited",
            "allowed_hosts": ["api.yourapp.com"],
            "allow_package_managers": True,
        },
    },
)
```

支持的包管理器：`pip`、`npm`、`apt`、`cargo`、`gem`、`go`。包会在共享同一 environment 的 session 间缓存。

## 第三步：启动 Session

Session 是一个正在运行的 agent 实例。它引用你的 agent 配置和 environment，然后开始干活。

### Python

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="My first agent session",
)

print(f"Session ID: {session.id}")
```

### TypeScript

```typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  title: "My first agent session",
});

console.log(`Session ID: ${session.id}`);
```

到这里 session 已经创建，但 agent 处于 idle 状态——等你告诉它做什么。

## 第四步：发送消息，流式获取响应

这是最有趣的部分。你发一条用户消息，agent 就开始工作——写代码、跑命令、搜索网页——通过 SSE（Server-Sent Events）实时把一切流式返回给你。

### Python

```python
with client.beta.sessions.events.stream(session.id) as stream:
    # 打开 stream 后发送用户消息
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
                    },
                ],
            },
        ],
    )

    # 处理流式事件
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[使用工具: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent 完成。")
                break
```

### TypeScript

```typescript
const stream = await client.beta.sessions.events.stream(session.id);

await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
        },
      ],
    },
  ],
});

for await (const event of stream) {
  if (event.type === "agent.message") {
    for (const block of event.content) {
      process.stdout.write(block.text);
    }
  } else if (event.type === "agent.tool_use") {
    console.log(`\n[使用工具: ${event.name}]`);
  } else if (event.type === "session.status_idle") {
    console.log("\n\nAgent 完成。");
    break;
  }
}
```

### 你会看到的输出

```
I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
[使用工具: write]
[使用工具: bash]
The script ran successfully. Let me verify the output file.
[使用工具: bash]
fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

Agent 完成。
```

Agent 自主决定了：写一个 Python 文件、执行它、验证输出。你只说了"做什么"，没说"怎么做"。

## 底层发生了什么

当你发送一个用户事件，平台会：

1. **启动容器**——根据你的 environment 配置。容器是惰性创建的（只在工具需要时才启动），所以 p50 首 token 时间很快。
2. **运行 agent loop**——Claude 读取你的消息，决定用什么工具，执行，读取结果，决定下一步。循环。
3. **流式推送事件**——每个工具调用、每个回复、每个状态变化都作为 SSE 事件返回。
4. **进入 idle**——当 agent 没有更多事情要做，它发出 `session.status_idle`。

Session 是一个 append-only 的事件日志。Harness 是无状态的。任何组件崩溃都不会丢失 session 数据——session 而不是 harness 才是 source of truth。这是核心架构洞察。

## 控制 Agent 的工具权限

`agent_toolset_20260401` 默认全部开启。要限制：

```python
# 只允许文件操作——禁用 bash 和 web
agent = client.beta.agents.create(
    name="File Editor Only",
    model="claude-sonnet-4-6",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "default_config": {"enabled": False},
            "configs": [
                {"name": "read", "enabled": True},
                {"name": "write", "enabled": True},
                {"name": "edit", "enabled": True},
            ],
        },
    ],
)
```

还可以添加自定义工具——你定义 schema，Claude 调用你的代码：

```python
agent = client.beta.agents.create(
    name="Weather Agent",
    model="claude-sonnet-4-6",
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get current weather for a location. Use this when the user asks about weather conditions.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
)
```

当 agent 调用你的自定义工具时，session 暂停。你在自己这边执行工具、发回结果，agent 继续工作。

## 执行中途引导方向

Session 是交互式的。你可以在 agent 工作过程中重定向它：

```python
# 发送后续消息改变方向
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [{"type": "text", "text": "Actually, also add a plot using matplotlib."}],
        },
    ],
)
```

或者直接中断：

```python
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt"}],
)
```

## 速查表

### 所有请求必需的 Headers

```
anthropic-version: 2023-06-01
anthropic-beta: managed-agents-2026-04-01
x-api-key: YOUR_API_KEY
```

### 定价

| 组成 | 费用 |
|------|------|
| Token 消耗 | 标准 Claude 费率 |
| Session 运行时间 | $0.08/session-hour |

### 模型选择

| 模型 | 适用场景 |
|------|---------|
| `claude-opus-4-6` | 最强智能，复杂 agent 任务 |
| `claude-sonnet-4-6` | 速度与智能的最佳平衡 |
| `claude-haiku-4-5` | 最快，简单任务 |

### SDK

Python、TypeScript、Go、Java、C#、Ruby、PHP——全部通过 `anthropic` 包。另有 `ant` CLI（Homebrew: `brew install anthropics/tap/ant`）。

## 接下来看什么

这篇教程覆盖了基础用法。Claude Managed Agents 还有三个更强大的研究预览功能：

- **Outcomes（目标驱动）**——定义"完成"的标准（rubric），agent 自动迭代直到达标。独立的 grader agent 评估，避免自我评估偏差。
- **Multi-Agent（多智能体）**——一个 coordinator agent 委派任务给专业 agent，每个 agent 在自己的上下文隔离线程里运行。
- **Memory（持久化记忆）**——跨 session 的 memory stores，agent 记住用户偏好、项目惯例和过去的教训。

> 想深入了解所有概念？看配套文章：[Claude Managed Agents 全面解析](claude-managed-agents-overview.md)

<!-- CTA: 现在就试试创建你的第一个 Claude Managed Agent——Beta 已对所有 API 账户开放。从 Sonnet 4.6 + 完全网络权限 + 全工具集开始，之后再按需收紧。 -->
