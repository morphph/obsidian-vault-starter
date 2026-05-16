---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-plugins.md
  - raw/2026-05-14-anthropic-claude-code-plugins-reference.md
tags: [claude-code, official-docs, plugins, marketplaces, distribution, skills, lsp]
---

# Source: Plugins (Discover + Create + Reference)

## Summary
Official Anthropic docs on **the Claude Code plugin system** — bundles three pages: discover/install via marketplaces, create your own, complete technical reference. Plugins are self-contained directories of components (skills, agents, hooks, MCP servers, LSP servers, background monitors) that share, version, and distribute Claude Code extensions across projects and teams. The official `claude-plugins-official` marketplace ships with 30+ pre-built plugins for LSP/integrations/workflows.

## When plugins vs standalone `.claude/`

| Approach | Skill names | Best for |
| :--- | :--- | :--- |
| Standalone (`.claude/`) | `/hello` | Personal workflows, project-specific |
| Plugins (with `.claude-plugin/plugin.json`) | `/plugin-name:hello` (namespaced) | Sharing, versioning, distribution |

> [!tip]
> Start with standalone for iteration → convert to plugin when ready to share.

## Official marketplace plugin categories

### Code intelligence — LSP plugins
Pre-built LSP plugins for 11 languages: `clangd-lsp`, `csharp-lsp`, `gopls-lsp`, `jdtls-lsp`, `kotlin-lsp`, `lua-lsp`, `php-lsp`, `pyright-lsp`, `rust-analyzer-lsp`, `swift-lsp`, `typescript-lsp`. Each requires the corresponding language server binary on the system.

What Claude gains from LSP:
- **Automatic diagnostics**: after every edit, language server reports errors/warnings. Claude sees type errors, missing imports, syntax issues without running compiler/linter.
- **Code navigation**: jump to definitions, find references, type info on hover, list symbols, find implementations, trace call hierarchies. **More precise than grep-based search.**

### External integrations (pre-configured MCP)
`github`, `gitlab`, `atlassian`, `asana`, `linear`, `notion`, `figma`, `vercel`, `firebase`, `supabase`, `slack`, `sentry`.

### Development workflows
`commit-commands`, `pr-review-toolkit`, `agent-sdk-dev`, `plugin-dev`.

### Output styles
`explanatory-output-style`, `learning-output-style`.

## Plugin structure (the reference card)

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json     # manifest (required)
├── skills/             # SKILL.md directories
├── commands/           # legacy flat markdown (use skills/)
├── agents/             # custom agent definitions
├── hooks/hooks.json    # event handlers
├── .mcp.json           # MCP servers
├── .lsp.json           # LSP servers
├── monitors/monitors.json  # background watchers
├── bin/                # executables added to PATH while plugin enabled
└── settings.json       # default settings (only `agent` + `subagentStatusLine` keys supported)
```

> [!warning]
> Common mistake: don't put `commands/`, `agents/`, `skills/`, `hooks/` inside `.claude-plugin/`. **Only `plugin.json` goes inside `.claude-plugin/`.**

## Installation scopes

| Scope | Where |
| :--- | :--- |
| **User** (default) | Across all your projects |
| **Project** | `.claude/settings.json` — for all collaborators on this repo |
| **Local** | This repo only, not shared |
| **Managed** | Org admin via managed settings, cannot be modified |

## Add marketplaces — four sources

```bash
/plugin marketplace add anthropics/claude-code                       # GitHub
/plugin marketplace add https://gitlab.com/company/plugins.git       # any Git
/plugin marketplace add https://gitlab.com/company/plugins.git#v1.0.0  # specific ref
/plugin marketplace add ./my-marketplace                              # local
/plugin marketplace add https://example.com/marketplace.json          # remote URL
```

## Background monitors — new plugin component

`monitors/monitors.json` watches logs, files, or external status. Each stdout line delivered to Claude as notification during session. Claude Code starts each monitor automatically when plugin is active — **no need to ask Claude to start it**.

```json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]
```

Relates to but distinct from [[claude-code-monitor-tool]] (the in-session Monitor tool) — monitors here are plugin-level + auto-started.

## Default settings via plugin

A plugin's `settings.json` can ship default `agent` (main thread takes that subagent's system prompt) or `subagentStatusLine`. Unknown keys silently ignored.

```json
{
  "agent": "security-reviewer"
}
```

Activates a custom agent as the main thread when plugin enabled. Settings from `settings.json` take priority over `settings` declared in `plugin.json`.

## Test locally during development

```bash
claude --plugin-dir ./my-plugin
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two   # multiple
claude --plugin-dir ./my-plugin.zip                           # .zip (v2.1.128+)
claude --plugin-url https://example.com/my-plugin.zip         # remote .zip
```

`--plugin-dir` plugin with same name as installed marketplace plugin **takes precedence for that session** — useful for testing changes without uninstalling.

After changes: `/reload-plugins` (also picks up skills, agents, hooks, plugin MCP/LSP).

## Submit to official marketplace

- claude.ai/settings/plugins/submit
- platform.claude.com/plugins/submit

Listed plugins can have your own CLI prompt Claude Code users to install via plugin hints.

## Auto-update behavior

Official Anthropic marketplaces: **auto-update enabled by default**. Third-party + local development: disabled by default. Disable entirely: `DISABLE_AUTOUPDATER=1`. Keep plugin auto-updates while disabling Claude Code: `DISABLE_AUTOUPDATER=1 FORCE_AUTOUPDATE_PLUGINS=1`.

## Security boundary

> [!warning]
> Plugins and marketplaces are **highly trusted components** that execute arbitrary code with your user privileges. Only install from sources you trust. Orgs can restrict marketplaces with managed marketplace restrictions.

## Connections
- Related: [[claude-code]], [[agent-skills-standard]], [[source-claude-code-subagents-docs]], [[source-claude-code-hooks-docs]], [[source-claude-code-mcp-docs]], [[source-claude-code-channels-docs]], [[gstack]], [[gbrain]]
- Distribution layer for everything in [[agent-skills-standard]] + [[source-claude-code-subagents-docs|subagents]] + [[source-claude-code-hooks-docs|hooks]]
- [[gstack]] (Garry Tan's open-source skills library, 87K+ stars) is essentially a plugin marketplace pattern at scale

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-plugins.md | Initial creation — bundles discover + create |
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-plugins-reference.md | Added technical reference (manifest schema, CLI commands) |
