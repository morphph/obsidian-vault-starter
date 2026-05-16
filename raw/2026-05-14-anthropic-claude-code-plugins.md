# Claude Code Official Docs — Plugins (Discover + Create + Reference bundle)

Captured 2026-05-14 from:
- https://code.claude.com/docs/en/discover-plugins.md
- https://code.claude.com/docs/en/plugins.md
- https://code.claude.com/docs/en/plugins-reference.md (TBD — see separate file if fetched)

---

## Part 1: Discover and install prebuilt plugins through marketplaces

> Find and install plugins from marketplaces to extend Claude Code with new skills, agents, and capabilities.

Plugins extend Claude Code with skills, agents, hooks, MCP servers. Marketplaces are catalogs of plugins.

### How marketplaces work

Two-step:
1. **Add the marketplace** — registers catalog with Claude Code. No plugins installed yet.
2. **Install individual plugins** — browse and install.

### Official Anthropic marketplace

`claude-plugins-official` automatically available. Run `/plugin` → Discover tab. Or claude.com/plugins.

```shell
/plugin install github@claude-plugins-official
```

If "not found in any marketplace": run `/plugin marketplace update claude-plugins-official` to refresh, or `/plugin marketplace add anthropics/claude-plugins-official` if not added before.

### Official marketplace categories

#### Code intelligence (LSP)

Built-in LSP tool: jump to definitions, find references, see type errors immediately after edits.

| Language | Plugin | Binary required |
| --- | --- | --- |
| C/C++ | `clangd-lsp` | `clangd` |
| C# | `csharp-lsp` | `csharp-ls` |
| Go | `gopls-lsp` | `gopls` |
| Java | `jdtls-lsp` | `jdtls` |
| Kotlin | `kotlin-lsp` | `kotlin-language-server` |
| Lua | `lua-lsp` | `lua-language-server` |
| PHP | `php-lsp` | `intelephense` |
| Python | `pyright-lsp` | `pyright-langserver` |
| Rust | `rust-analyzer-lsp` | `rust-analyzer` |
| Swift | `swift-lsp` | `sourcekit-lsp` |
| TypeScript | `typescript-lsp` | `typescript-language-server` |

What Claude gains:
* **Automatic diagnostics**: after every edit, language server analyzes changes, reports errors/warnings. Claude sees type errors, missing imports, syntax issues without running compiler/linter.
* **Code navigation**: jump to definitions, find references, type info on hover, list symbols, find implementations, trace call hierarchies. More precise than grep-based search.

#### External integrations (pre-configured MCP servers)

* Source control: `github`, `gitlab`
* Project management: `atlassian`, `asana`, `linear`, `notion`
* Design: `figma`
* Infrastructure: `vercel`, `firebase`, `supabase`
* Communication: `slack`
* Monitoring: `sentry`

#### Development workflows

* `commit-commands`: Git commit workflows
* `pr-review-toolkit`: Specialized agents for PR review
* `agent-sdk-dev`: Tools for building with Agent SDK
* `plugin-dev`: Toolkit for creating plugins

#### Output styles

* `explanatory-output-style`: Educational insights
* `learning-output-style`: Interactive learning mode

### Add marketplaces

```shell
# GitHub repo
/plugin marketplace add anthropics/claude-code

# Other Git hosts
/plugin marketplace add https://gitlab.com/company/plugins.git

# Specific branch/tag
/plugin marketplace add https://gitlab.com/company/plugins.git#v1.0.0

# Local paths
/plugin marketplace add ./my-marketplace

# Remote URLs
/plugin marketplace add https://example.com/marketplace.json
```

### Install plugins

```shell
/plugin install plugin-name@marketplace-name
```

Installation scopes:
* **User scope** (default): install for yourself across all projects
* **Project scope**: install for all collaborators on this repo (`.claude/settings.json`)
* **Local scope**: install for yourself in this repo only

> [!warning]
> Make sure you trust a plugin before installing. Anthropic does not control what MCP servers, files, or other software are included.

### Manage installed plugins

```shell
/plugin disable plugin-name@marketplace-name
/plugin enable plugin-name@marketplace-name
/plugin uninstall plugin-name@marketplace-name
```

CLI scope option:
```shell
claude plugin install formatter@your-org --scope project
```

### Apply plugin changes without restarting

```shell
/reload-plugins
```

### Auto-update

Claude Code auto-updates marketplaces and installed plugins at startup. Official Anthropic marketplaces have auto-update enabled by default. Third-party and local development: disabled by default.

Disable all auto-updates: `DISABLE_AUTOUPDATER` env var.
Keep plugin auto-updates while disabling Claude Code: `DISABLE_AUTOUPDATER=1 FORCE_AUTOUPDATE_PLUGINS=1`.

### Team marketplaces

Add to project's `.claude/settings.json`:
```json
{
  "extraKnownMarketplaces": {
    "my-team-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  }
}
```

### Security

Plugins and marketplaces are highly trusted components — can execute arbitrary code on your machine with your user privileges. Only install from sources you trust. Orgs can restrict via managed marketplace restrictions.

---

## Part 2: Create plugins

> Create custom plugins to extend Claude Code with skills, agents, hooks, and MCP servers.

### When to use plugins vs standalone

| Approach | Skill names | Best for |
| :--- | :--- | :--- |
| Standalone (`.claude/`) | `/hello` | Personal workflows, project-specific |
| Plugins (with `.claude-plugin/plugin.json`) | `/plugin-name:hello` | Sharing, versioning, distributing |

Start with standalone for iteration, convert to plugin when ready to share.

### Quickstart

1. Create plugin directory:
```bash
mkdir my-first-plugin
mkdir my-first-plugin/.claude-plugin
```

2. Create manifest at `.claude-plugin/plugin.json`:
```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

3. Add skill:
```bash
mkdir -p my-first-plugin/skills/hello
```

`skills/hello/SKILL.md`:
```markdown
---
description: Greet the user with a friendly message
disable-model-invocation: true
---

Greet the user warmly and ask how you can help them today.
```

4. Test:
```bash
claude --plugin-dir ./my-first-plugin
```

Then: `/my-first-plugin:hello`

Skill arguments — `$ARGUMENTS` placeholder:
```markdown
---
description: Greet the user with a personalized message
---

Greet the user named "$ARGUMENTS" warmly...
```

`/my-first-plugin:hello Alex` → "Alex" replaces `$ARGUMENTS`.

### Plugin structure

| Directory | Location | Purpose |
| :--- | :--- | :--- |
| `.claude-plugin/` | Plugin root | Contains `plugin.json` manifest |
| `skills/` | Plugin root | Skills as `<name>/SKILL.md` directories |
| `commands/` | Plugin root | Skills as flat Markdown files (legacy — use `skills/`) |
| `agents/` | Plugin root | Custom agent definitions |
| `hooks/` | Plugin root | Event handlers in `hooks.json` |
| `.mcp.json` | Plugin root | MCP server configurations |
| `.lsp.json` | Plugin root | LSP server configurations |
| `monitors/` | Plugin root | Background monitor configurations in `monitors.json` |
| `bin/` | Plugin root | Executables added to Bash tool's PATH while plugin enabled |
| `settings.json` | Plugin root | Default settings applied when plugin enabled |

> [!warning]
> Don't put `commands/`, `agents/`, `skills/`, or `hooks/` inside `.claude-plugin/`. Only `plugin.json` goes inside `.claude-plugin/`.

### Add Skills

Plugins can include Agent Skills. Model-invoked: Claude automatically uses them.

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── code-review/
        └── SKILL.md
```

After installing, `/reload-plugins`.

### Add LSP servers

For languages without official LSP plugin, `.lsp.json`:
```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

### Add background monitors

`monitors/monitors.json` watches logs, files, external status:
```json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]
```

Each stdout line delivered to Claude as notification during session. Claude Code starts each monitor automatically when plugin active.

### Ship default settings

`settings.json` at plugin root. Currently only `agent` and `subagentStatusLine` supported:
```json
{
  "agent": "security-reviewer"
}
```

Activates one of plugin's custom agents as main thread, applying its system prompt, tool restrictions, model.

### Test locally

```bash
claude --plugin-dir ./my-plugin
```

Multiple plugins:
```bash
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two
```

Test packaged `.zip`:
```bash
claude --plugin-dir ./my-plugin.zip
claude --plugin-url https://example.com/my-plugin.zip
```

After changes: `/reload-plugins`.

### Convert standalone to plugin

1. Create `my-plugin/.claude-plugin/plugin.json`
2. Copy files:
```bash
cp -r .claude/commands my-plugin/
cp -r .claude/agents my-plugin/
cp -r .claude/skills my-plugin/
```
3. Migrate hooks from settings to `my-plugin/hooks/hooks.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npm run lint:fix" }]
      }
    ]
  }
}
```

### Submit to official marketplace

* claude.ai/settings/plugins/submit
* platform.claude.com/plugins/submit

Plugin hints: recommend your plugin from your CLI.

---

## See plugins-reference.md raw file for complete technical specifications (manifest schema, version management, debugging tools, etc.)
