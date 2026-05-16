# Claude Code Official Docs — Channels reference

Captured 2026-05-14 from https://code.claude.com/docs/en/channels-reference.md

> Build an MCP server that pushes webhooks, alerts, and chat messages into a Claude Code session. Reference for the channel contract: capability declaration, notification events, reply tools, sender gating, and permission relay.

> [!note]
> Channels are in research preview and require Claude Code v2.1.80 or later.

A channel is an MCP server that pushes events into a Claude Code session so Claude can react to things happening outside the terminal.

One-way channels forward alerts, webhooks, monitoring events. Two-way channels (chat bridges) also expose a reply tool. A channel with trusted sender path can opt in to relay permission prompts.

## Overview

A channel is an MCP server that runs on the same machine as Claude Code. Claude Code spawns it as subprocess and communicates over stdio.

* **Chat platforms** (Telegram, Discord): plugin polls platform's API. No URL to expose.
* **Webhooks** (CI, monitoring): server listens on local HTTP port. External systems POST → server pushes payload to Claude.

## What you need

* `@modelcontextprotocol/sdk` package
* Node.js-compatible runtime (Bun, Node, or Deno)

Your server needs to:
1. Declare `claude/channel` capability so Claude Code registers notification listener
2. Emit `notifications/claude/channel` events when something happens
3. Connect over stdio transport

During research preview, custom channels aren't on approved allowlist. Use `--dangerously-load-development-channels` to test locally.

## Example: build a webhook receiver

Single-file server using Bun:

```ts title="webhook.ts"
#!/usr/bin/env bun
import { Server } from '@modelcontextprotocol/sdk/server/index.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

const mcp = new Server(
  { name: 'webhook', version: '0.0.1' },
  {
    capabilities: { experimental: { 'claude/channel': {} } },
    instructions: 'Events from the webhook channel arrive as <channel source="webhook" ...>. They are one-way: read them and act, no reply expected.',
  },
)

await mcp.connect(new StdioServerTransport())

Bun.serve({
  port: 8788,
  hostname: '127.0.0.1',
  async fetch(req) {
    const body = await req.text()
    await mcp.notification({
      method: 'notifications/claude/channel',
      params: {
        content: body,
        meta: { path: new URL(req.url).pathname, method: req.method },
      },
    })
    return new Response('ok')
  },
})
```

Register in `.mcp.json`:

```json
{
  "mcpServers": {
    "webhook": { "command": "bun", "args": ["./webhook.ts"] }
  }
}
```

Test:

```bash
claude --dangerously-load-development-channels server:webhook
```

Send:
```bash
curl -X POST localhost:8788 -d "build failed on main: https://ci.example.com/run/1234"
```

Arrives as:
```text
<channel source="webhook" path="/" method="POST">build failed on main: https://ci.example.com/run/1234</channel>
```

## Test during research preview

```bash
# Testing a plugin you're developing
claude --dangerously-load-development-channels plugin:yourplugin@yourmarketplace

# Testing a bare .mcp.json server (no plugin wrapper yet)
claude --dangerously-load-development-channels server:webhook
```

The bypass is per-entry. `channelsEnabled` organization policy still applies.

## Server options

| Field | Type | Description |
| :--- | :--- | :--- |
| `capabilities.experimental['claude/channel']` | object | Required. Always `{}`. Registers notification listener. |
| `capabilities.experimental['claude/channel/permission']` | object | Optional. Declares channel can receive permission relay requests. |
| `capabilities.tools` | object | Two-way only. Standard MCP tool capability. |
| `instructions` | string | Recommended. Added to Claude's system prompt. |

## Notification format

Server emits `notifications/claude/channel` with two params:

| Field | Type | Description |
| :--- | :--- | :--- |
| `content` | string | Event body, delivered as body of `<channel>` tag |
| `meta` | Record<string, string> | Each entry becomes attribute on `<channel>` tag for routing context (chat ID, sender, severity). Keys must be identifiers. |

```ts
await mcp.notification({
  method: 'notifications/claude/channel',
  params: {
    content: 'build failed on main: https://ci.example.com/run/1234',
    meta: { severity: 'high', run_id: '1234' },
  },
})
```

Notifications not acknowledged. If session hasn't loaded server as channel, events dropped silently. Events queue in order. If several arrive while Claude busy, delivered together on next turn.

## Expose a reply tool

If channel is two-way (chat bridge), expose standard MCP tool that Claude can call to send messages back. Three components:

1. `tools: {}` in `Server` constructor capabilities
2. Tool handlers (schema + send logic)
3. `instructions` string telling Claude when/how to call tool

```ts
mcp.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: 'reply',
    description: 'Send a message back over this channel',
    inputSchema: {
      type: 'object',
      properties: {
        chat_id: { type: 'string', description: 'The conversation to reply in' },
        text: { type: 'string', description: 'The message to send' },
      },
      required: ['chat_id', 'text'],
    },
  }],
}))

mcp.setRequestHandler(CallToolRequestSchema, async req => {
  if (req.params.name === 'reply') {
    const { chat_id, text } = req.params.arguments
    send(`Reply to ${chat_id}: ${text}`)
    return { content: [{ type: 'text', text: 'sent' }] }
  }
  throw new Error(`unknown tool: ${req.params.name}`)
})
```

## Gate inbound messages

Ungated channel = prompt injection vector. Check sender against allowlist before calling `mcp.notification()`.

```ts
const allowed = new Set(loadAllowlist())

if (!allowed.has(message.from.id)) {  // sender, not room
  return  // drop silently
}
await mcp.notification({ ... })
```

Gate on sender's identity, not chat/room identity. In group chats these differ — gating on room would let anyone in allowlisted group inject.

## Relay permission prompts

> [!note]
> Requires Claude Code v2.1.81 or later.

Two-way channel can opt in to receive same permission prompt and relay to remote device. Both stay live: answer in terminal or phone, first answer wins.

Relay covers tool-use approvals (Bash, Write, Edit). Not project trust or MCP server consent dialogs.

### How relay works

1. Claude Code generates short request ID, notifies server
2. Server forwards prompt + ID to chat app
3. Remote user replies with yes/no + that ID
4. Inbound handler parses reply into verdict. Claude Code applies if ID matches open request.

### Permission request fields

`notifications/claude/channel/permission_request` params:

| Field | Description |
| --- | --- |
| `request_id` | Five lowercase letters from a-z without 'l' (so doesn't read as `1` or `I` on phone) |
| `tool_name` | Tool name (Bash, Write) |
| `description` | Human-readable summary of this tool call |
| `input_preview` | Tool args as JSON string, truncated to 200 chars |

Verdict: `notifications/claude/channel/permission` with `request_id` and `behavior` ('allow' or 'deny').

### Add relay to chat bridge

1. `claude/channel/permission: {}` in experimental capabilities
2. Notification handler for `notifications/claude/channel/permission_request`
3. Check in inbound handler that recognizes `yes <id>`/`no <id>`

```ts
const PERMISSION_REPLY_RE = /^\s*(y|yes|n|no)\s+([a-km-z]{5})\s*$/i

async function onInbound(message) {
  if (!allowed.has(message.from.id)) return

  const m = PERMISSION_REPLY_RE.exec(message.text)
  if (m) {
    await mcp.notification({
      method: 'notifications/claude/channel/permission',
      params: {
        request_id: m[2].toLowerCase(),
        behavior: m[1].toLowerCase().startsWith('y') ? 'allow' : 'deny',
      },
    })
    return
  }

  await mcp.notification({
    method: 'notifications/claude/channel',
    params: { content: message.text, meta: { chat_id: String(message.chat.id) } },
  })
}
```

Local terminal dialog stays open. Different format → falls through as normal message. Right format wrong ID → server emits verdict but Claude Code finds no open request, drops silently.

## Package as a plugin

Wrap channel in plugin and publish to marketplace. Users install with `/plugin install`, enable per session with `--channels plugin:<name>@<marketplace>`.

A channel published to your own marketplace still needs `--dangerously-load-development-channels` to run, since it isn't on approved allowlist. Submit to official marketplace (channel plugins go through security review).

## See also

* Channels — installing/using Telegram, Discord, iMessage, fakechat
* Working channel implementations on GitHub
* MCP for underlying protocol
* Plugins to package
