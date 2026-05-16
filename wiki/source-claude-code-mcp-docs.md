---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-mcp.md
tags: [claude-code, official-docs, mcp, integrations, plugins]
---

# Source: Connect Claude Code to tools via MCP

## Summary
Official Anthropic doc on **Model Context Protocol (MCP)** in [[claude-code]] — the open-source standard for AI-tool integrations that lets Claude Code reach into databases, issue trackers, monitoring dashboards, designs, and webhooks. MCP servers are the **only way to expose non-Claude tools** to any parallel-work approach (subagents, agent view, agent teams). The Anthropic Directory at claude.ai/directory lists reviewed connectors — same MCP infrastructure as `claude mcp add`.

## What MCP unlocks (canonical examples)

- "Add the feature described in JIRA ENG-4521 and create a PR on GitHub"
- "Check Sentry and Statsig for the usage of feature ENG-4521"
- "Find emails of 10 random users who used ENG-4521 in our Postgres DB"
- "Update standard email template based on new Figma designs posted in Slack"
- "Create Gmail drafts inviting these 10 users to feedback session"
- React to external events — an MCP server can act as a [[source-claude-code-channels-docs|channel]] pushing messages into your session

## Server config schema (all four transports)

MCP servers live in `.mcp.json` (project), `~/.claude.json` (user), or managed settings.

| Transport | Purpose |
| :--- | :--- |
| `stdio` | Spawns command as subprocess, communicates over stdin/stdout |
| `http` | HTTP endpoint |
| `sse` | Server-Sent Events stream |
| `ws` | WebSocket |

Stdio is most common for local servers. HTTP/SSE/WS for remote.

## Three install scopes

| Scope | File | Visible to |
| :--- | :--- | :--- |
| **Project** | `.mcp.json` at repo root | Everyone who clones (after workspace trust) |
| **User** | `~/.claude.json` | All your sessions across projects |
| **Managed** | Enterprise managed settings | All users in org |

## Permission model — workspace trust + per-server consent

Project `.mcp.json` servers require:
1. Workspace trust dialog on first `claude` invocation
2. Per-server consent dialog on first run

Once accepted, server is auto-spawned at session start. **Servers do NOT run until consented to** — this is the security boundary.

## MCP servers as channels (the new bridge)

A regular MCP server lets Claude **query** external systems on demand. A server that declares the `claude/channel` capability becomes a [[source-claude-code-channels-docs|channel]] — **pushing events into a running session** so Claude can react while you're away. Same underlying protocol; channels add capability declaration + notification handler. See [[source-claude-code-channels-reference-docs]].

## Subagent-scoped MCP servers

Subagents can have MCP servers the main conversation doesn't have. In [[source-claude-code-subagents-docs|subagent frontmatter]]:

```yaml
mcpServers:
  - playwright:                        # inline definition, scoped to this subagent
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  - github                             # reference to already-configured server
```

Keeps the MCP server's tool descriptions out of the main conversation context (token savings). Plugin subagents **do not support** `mcpServers` frontmatter.

## Channel-style MCP (capability extension)

MCP standard tools (the `tools: {}` capability) are pull-based — Claude calls them. Channels add push-based notifications (`notifications/claude/channel`). Same protocol, different direction. See [[source-claude-code-channels-reference-docs]] for full schema.

## Connections
- Related: [[claude-code]], [[source-claude-code-channels-docs]], [[source-claude-code-channels-reference-docs]], [[source-claude-code-plugins-docs]], [[source-claude-code-subagents-docs]], [[managed-agents-architecture]]
- Pairs with [[claude-managed-agents]] — both use MCP servers as the "hands" of an agent; Managed Agents hosts servers in Anthropic cloud, MCP servers in Claude Code run on your machine
- MCP servers can be installed via [[source-claude-code-plugins-docs|plugins]] (pre-configured bundles like the official `github`, `slack`, `linear` plugins)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-mcp.md | Initial creation from official MCP docs |
