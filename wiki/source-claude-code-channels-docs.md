---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-channels.md
tags: [claude-code, official-docs, channels, push-events, mcp, chat-bridge, webhooks, research-preview]
---

# Source: Push events into a running session with channels

## Summary
Official Anthropic doc on **channels** in [[claude-code]] — research-preview MCP server type (v2.1.80+) that **pushes events INTO a running session** so Claude reacts while you're away. Two-way channels (chat bridges) also accept replies through the same channel. Plugin-installed; Telegram, Discord, iMessage included in research preview. **The inversion of MCP**: standard MCP servers are pull-based (Claude queries on demand), channels are push-based (external systems trigger).

## How channels differ from related primitives

| Feature | Direction | Best for |
| :--- | :--- | :--- |
| Standard [[source-claude-code-mcp-docs\|MCP server]] | Claude pulls (queries on demand) | Claude reads/queries external system during a task |
| **Channels** | External pushes IN | React to events that happen while away from terminal |
| [[claude-code-monitor-tool\|Monitor tool]] | Local stdout watch | React to lines from a local shell command |
| Hooks | Claude's own action triggers | Internal lifecycle reactions |
| [[source-claude-code-scheduled-tasks-docs\|Scheduled tasks]] | Time-driven | Poll on a timer |
| [[source-claude-code-routines-docs\|Routines]] | Cloud-hosted; schedule + API + GitHub triggers | Run when laptop closed |
| Remote Control | Drive local session from claude.ai/mobile | Steer in-progress session |

Three official channels at research preview launch:
- **Telegram**: BotFather token → pair via `/telegram:access pair` → allowlist
- **Discord**: Developer Portal → Message Content Intent → pair → allowlist
- **iMessage** (macOS only): Full Disk Access for `chat.db` → self-chat works automatically

Plus **fakechat** demo (localhost UI for testing without external service).

## The threat model — sender allowlist

> Ungated channel = prompt injection vector. Anyone who can reach your endpoint can put text in front of Claude.

Every approved channel maintains a **sender allowlist**:
- Telegram/Discord bootstrap via pairing flow
- iMessage detects user's own Apple ID addresses automatically
- Pairing: user DMs bot → bot replies with pairing code → user approves in Claude session → ID added to allowlist

Gating must be on **sender identity** (`message.from.id`), NOT chat/room identity (`message.chat.id`). In group chats these differ — gating on room would let anyone in an allowlisted group inject.

## Enterprise gating — two managed settings

| Setting | Purpose |
| :--- | :--- |
| `channelsEnabled` | Master switch. **Default DIFFERS by auth**: claude.ai Team/Enterprise blocks until admin enables; Console API key allows unless managed settings deployed. |
| `allowedChannelPlugins` | Which plugins can register. Replaces Anthropic list when set. Set per-plugin: `[{ marketplace, plugin }, ...]` |

Pro/Max users without an org skip these entirely. Being in `.mcp.json` isn't enough to push messages — server must also be named in `--channels`.

## Two-way channels can relay permission prompts

If channel declares `claude/channel/permission` capability (v2.1.81+), Claude Code forwards tool approval prompts to the channel. Remote user replies `yes <id>` or `no <id>`. Both the local terminal dialog AND remote stay live — first answer wins. **Anyone who can reply through the channel can approve/deny tool use** — only declare this capability if you've gated sender carefully.

Relay covers tool-use approvals (Bash, Write, Edit). Does NOT cover project trust or MCP server consent dialogs.

## Usage pattern

```bash
claude --channels plugin:telegram@claude-plugins-official
```

Channels only deliver events while session is open. For always-on: run Claude in background process or persistent terminal. For non-interactive `-p`: terminal-input tools (multiple choice, plan mode approval) disabled.

## Concrete use cases

- **Chat bridge** — ask Claude from phone via Telegram/Discord/iMessage; work happens against your real files on your machine
- **Webhook receiver** — CI failure / error tracker / deploy pipeline alerts arrive in already-open session where Claude has files open + remembers what you were debugging
- **Permission relay** — approve risky tool calls from phone while away from terminal

## Where this fits in our wiki

Channels is **brand new** — replaces a gap. The existing [[claude-code-monitor-tool]] is the closest concept but **fundamentally different**: Monitor watches local stdout, Channels receives external pushes. The Monitor wiki page table should add Channels as a 5th category.

## Connections
- Related: [[claude-code]], [[source-claude-code-mcp-docs]], [[source-claude-code-channels-reference-docs]], [[source-claude-code-plugins-docs]], [[claude-code-monitor-tool]], [[source-claude-code-scheduled-tasks-docs]], [[source-claude-code-routines-docs]]
- Architectural sibling of [[claude-code-monitor-tool]]: both invert polling, but Monitor watches local commands while channels receive external events via MCP
- Pairs with [[source-claude-code-mcp-docs]] — channels extend the MCP protocol with the `claude/channel` capability

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-channels.md | Initial creation — new push-based MCP extension, no prior wiki coverage |
