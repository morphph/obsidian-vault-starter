---
status: draft
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-09-anthropic-agent-capabilities-announcement.md
platform: blog
created: 2026-04-09
last-updated: 2026-04-09
tags: [draft, tutorial, anthropic, agents]
---

<!-- HOOK: Anthropic just shipped Claude Managed Agents — a hosted service that lets you deploy autonomous AI agents without building your own infrastructure. Here's how to go from zero to a working agent in under 10 minutes. -->

# How to Create My First Claude Managed Agent

Anthropic launched Claude Managed Agents on April 9, 2026. Instead of building your own agent loop, container sandbox, and tool execution layer, you get all of that managed for you. Claude can read files, run shell commands, search the web, and execute code — autonomously, in a secure cloud container.

This guide walks you through creating your first agent, from setup to streaming results.

## What You'll Build

A coding assistant agent that can:
- Write and execute code in a cloud container
- Read and edit files
- Search the web for information
- Stream results back to you in real-time

Total cost for this tutorial: a few cents in tokens + $0.08/session-hour.

## The Mental Model: 3 Things You Create

Before writing any code, understand the three resources you'll work with:

| Resource | What it is | Create once or per-task? |
|----------|-----------|------------------------|
| **Agent** | The "who" — model, system prompt, tools | Once. Reuse across sessions. |
| **Environment** | The "where" — container config, packages, network | Once. Reuse across sessions. |
| **Session** | The "what" — a running instance doing a specific task | Per task. |

Think of it like this: you define an Agent (the brain) and an Environment (the workspace), then spin up Sessions (the actual work) whenever you need something done.

## Prerequisites

- An Anthropic API key ([get one here](https://console.anthropic.com/settings/keys))
- Python 3.8+ or Node.js 18+ (or just curl)

Install the SDK:

```bash
# Python
pip install anthropic

# TypeScript
npm install @anthropic-ai/sdk
```

Set your API key:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Step 1: Create an Agent

An agent is a reusable configuration — the model, system prompt, and tools bundled together. Create it once, reference it by ID forever.

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
# Save this ID — you'll use it for every session
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

**What's `agent_toolset_20260401`?** It enables all 8 built-in tools at once: Bash, Read, Write, Edit, Glob, Grep, Web Fetch, and Web Search. You can disable specific tools if you want tighter control — more on that later.

**What about model choice?** All Claude 4.5+ models work. `claude-sonnet-4-6` is the sweet spot for most agent work. Use `claude-opus-4-6` for harder tasks, `claude-haiku-4-5` for speed.

## Step 2: Create an Environment

An environment defines the container where your agent runs. Think of it as a VM template — packages, network access, mounted files.

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

This creates a basic container with full outbound network access. For production, you'll want to lock this down:

```python
# Production: restrict network to specific hosts
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

Supported package managers: `pip`, `npm`, `apt`, `cargo`, `gem`, `go`. Packages are cached across sessions sharing the same environment.

## Step 3: Start a Session

A session is a running agent instance. It references your agent config and environment, then does the actual work.

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

At this point, the session exists but the agent is idle — waiting for you to tell it what to do.

## Step 4: Send a Message and Stream the Response

This is where it gets interesting. You send a user message, and the agent starts working — writing code, running commands, searching the web — streaming everything back to you in real-time via Server-Sent Events (SSE).

### Python

```python
with client.beta.sessions.events.stream(session.id) as stream:
    # Send the user message after the stream opens
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

    # Process streaming events
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent finished.")
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
    console.log(`\n[Using tool: ${event.name}]`);
  } else if (event.type === "session.status_idle") {
    console.log("\n\nAgent finished.");
    break;
  }
}
```

### What You'll See

```
I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
[Using tool: write]
[Using tool: bash]
The script ran successfully. Let me verify the output file.
[Using tool: bash]
fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

Agent finished.
```

The agent autonomously decided to: write a Python file, execute it, then verify the output. You didn't tell it how — just what.

## What's Happening Under the Hood

When you send a user event, the platform:

1. **Provisions a container** — based on your environment config. Containers are provisioned lazily (only when tools need them), which is why p50 time-to-first-token is fast.
2. **Runs the agent loop** — Claude reads your message, decides which tools to use, executes them, reads results, decides next step. Repeat.
3. **Streams events** — every tool call, every response, every status change comes back as an SSE event.
4. **Goes idle** — when the agent has nothing more to do, it emits `session.status_idle`.

The session is an append-only event log. The harness is stateless. If anything crashes, the session state survives. This is the core architectural insight — the session, not the harness, is the source of truth.

## Controlling Your Agent's Tools

The `agent_toolset_20260401` enables everything by default. To restrict tools:

```python
# Only allow file operations — no bash, no web
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

You can also add custom tools — define a schema, and Claude will call your code:

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

When the agent calls your custom tool, the session pauses. You execute the tool on your side, send back the result, and the agent continues.

## Steering Mid-Execution

Sessions are interactive. You can redirect the agent while it's working:

```python
# Send a follow-up message to change direction
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

Or interrupt it entirely:

```python
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt"}],
)
```

## Quick Reference

### Required Headers (all requests)

```
anthropic-version: 2023-06-01
anthropic-beta: managed-agents-2026-04-01
x-api-key: YOUR_API_KEY
```

### Pricing

| Component | Cost |
|-----------|------|
| Tokens | Standard Claude rates |
| Session runtime | $0.08/session-hour |

### Supported Models

| Model | Best for |
|-------|---------|
| `claude-opus-4-6` | Most intelligent, complex agent tasks |
| `claude-sonnet-4-6` | Best balance of speed and intelligence |
| `claude-haiku-4-5` | Fastest, simple tasks |

### SDKs

Python, TypeScript, Go, Java, C#, Ruby, PHP — all via the `anthropic` package. Plus `ant` CLI (Homebrew: `brew install anthropics/tap/ant`).

## What's Next

This tutorial covers the basics. Claude Managed Agents has three more powerful features in research preview:

- **Outcomes** — define what "done" looks like with a rubric, and the agent iterates until it meets your criteria (with a separate grader agent to avoid self-evaluation bias)
- **Multi-agent** — one coordinator agent delegates to specialized agents, each running in its own context-isolated thread
- **Memory** — persistent memory stores that survive across sessions, so your agent remembers user preferences, project conventions, and past mistakes

[Request access](https://claude.com/form/claude-managed-agents) to try these features.

For the full API reference: [platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)

<!-- CTA: Try building your first Claude Managed Agent — the beta is open to all API accounts. Start with Sonnet 4.6, unrestricted networking, and the full toolset. You can always lock things down later. -->
