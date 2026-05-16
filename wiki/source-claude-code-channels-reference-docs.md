---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-channels-reference.md
tags: [claude-code, official-docs, channels, mcp, reference, server-protocol]
---

# Source: Channels reference — Build your own channel

## Summary
Official Anthropic technical reference for **building MCP servers that act as [[source-claude-code-channels-docs|channels]]** — the protocol contract for capability declaration, notification events, reply tools, sender gating, permission relay. Anyone who can write an MCP server can build a custom one-way (webhook receiver) or two-way (chat bridge) channel.

## The capability declaration

A channel server declares one or both of:
- `experimental.claude/channel: {}` — required. Registers notification listener.
- `experimental.claude/channel/permission: {}` — optional. Enables [permission relay](#permission-relay).
- `tools: {}` — optional. Required only for two-way channels (Claude calls a reply tool).

## Notification format — what pushes into the session

`notifications/claude/channel` with params:

| Field | Type | Description |
| :--- | :--- | :--- |
| `content` | string | Event body — becomes body of `<channel>` tag |
| `meta` | Record<string, string> | Each entry becomes attribute on `<channel>` tag (chat_id, severity, etc.) — keys must be identifier chars |

```ts
await mcp.notification({
  method: 'notifications/claude/channel',
  params: {
    content: 'build failed on main',
    meta: { severity: 'high', run_id: '1234' }
  }
})
```

Arrives as:
```text
<channel source="your-channel" severity="high" run_id="1234">
build failed on main
</channel>
```

> [!warning]
> Notifications are **NOT acknowledged**. `await` resolves when written to transport, not when Claude processes it. If session hasn't loaded channel or org policy blocks, events are **silently dropped**. For delivery confirmation, expose a reply tool Claude can call to report status back.

Events queue in order. Multiple events arriving while Claude is busy are delivered together on next turn.

## Building a one-way webhook receiver (canonical pattern)

Single-file Bun server:
- Declares `claude/channel` capability
- Connects via stdio transport (Claude Code spawns as subprocess)
- HTTP listener (e.g., `:8788`) forwards POST bodies as channel notifications

Server runs locally (hostname `127.0.0.1`), is spawned by Claude Code (no separate process management), and dies with the session.

Register in `.mcp.json`:
```json
{
  "mcpServers": {
    "webhook": { "command": "bun", "args": ["./webhook.ts"] }
  }
}
```

Test with development flag (since custom channels aren't on approved allowlist during research preview):
```bash
claude --dangerously-load-development-channels server:webhook
```

## Two-way reply tool (chat bridges)

Add `tools: {}` capability + standard MCP `ListToolsRequestSchema` + `CallToolRequestSchema` handlers. Tool schema typically accepts `chat_id` + `text`. The `instructions` field of the server constructor tells Claude **when to reply and which attribute to pass back** (e.g., echo the `chat_id` from the inbound tag).

## Sender gating (security boundary)

```ts
const allowed = new Set(loadAllowlist())

async function onInbound(message) {
  if (!allowed.has(message.from.id)) return  // sender, NOT room
  await mcp.notification({ ... })
}
```

Gate on `message.from.id`, not `message.chat.id`. In group chats these differ — gating on room would let anyone in allowlisted group inject.

## Permission relay (v2.1.81+)

A two-way channel can opt in to receive **the same permission prompt the terminal shows**, format it for the remote platform, and accept a yes/no verdict.

### Outbound: `notifications/claude/channel/permission_request`

| Field | Description |
| :--- | :--- |
| `request_id` | **5 lowercase letters, no `l`** (so doesn't read as `1` or `I` on phone) |
| `tool_name` | Bash, Write, Edit, etc. |
| `description` | Human-readable summary of this call |
| `input_preview` | Tool args as JSON string, truncated 200 chars |

The local terminal dialog **does NOT display this ID** — server is the only path to learn it.

### Inbound verdict: `notifications/claude/channel/permission`

Parse remote reply with regex like `/^\s*(y|yes|n|no)\s+([a-km-z]{5})\s*$/i`. Emit verdict notification with `request_id` + `behavior: 'allow' | 'deny'`.

Local terminal dialog stays open. First answer to arrive wins. Different format falls through as normal message to Claude. Right format wrong ID = silently dropped.

> [!warning]
> **Only declare `claude/channel/permission` capability if your channel gates sender carefully** — anyone who can reply through the channel can approve/deny tool use in your session.

## Package as plugin

Wrap channel in plugin, publish to marketplace. Users install with `/plugin install`, enable per session with `--channels plugin:<name>@<marketplace>`.

A channel on your own marketplace **still needs `--dangerously-load-development-channels`** to run during research preview — only Anthropic-curated allowlist runs without the dev flag. Submit to official marketplace for security review.

## Connections
- Related: [[source-claude-code-channels-docs]], [[source-claude-code-mcp-docs]], [[source-claude-code-plugins-docs]], [[permission-system]]
- The technical underbelly of [[source-claude-code-channels-docs|channels]]
- Builds on standard [[source-claude-code-mcp-docs|MCP]] — channels are MCP servers with capability extensions

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-channels-reference.md | Initial creation from official reference |
