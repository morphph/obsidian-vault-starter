# Claude Code Official Docs — Extend Claude with skills (2026-05-14 refresh)

Captured 2026-05-14 from https://code.claude.com/docs/en/skills.md

**Refresh of:** raw/2026-04-21-anthropic-agent-skills-docs.md (now superseded for sections that have changed)

> Create, manage, and share skills to extend Claude's capabilities in Claude Code. Includes custom commands and bundled skills.

Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`.

Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure, or when a section of CLAUDE.md has grown into a procedure rather than a fact. A skill's body loads only when used, so long reference material costs almost nothing until needed.

> [!note]
> Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Existing `.claude/commands/` files keep working. Skills add: directory for supporting files, frontmatter to control invocation, ability for Claude to load them automatically.

Claude Code skills follow the Agent Skills open standard (agentskills.io), which works across multiple AI tools. Claude Code extends with: invocation control, subagent execution, dynamic context injection.

## Bundled skills

Available in every session: `/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api`. Prompt-based: give Claude detailed instructions and orchestrates the work with its tools. Marked **Skill** in commands reference.

## Getting started

### Create your first skill

Example: skill that summarizes uncommitted changes.

```bash
mkdir -p ~/.claude/skills/summarize-changes
```

`~/.claude/skills/summarize-changes/SKILL.md`:
```yaml
---
description: Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed, wants a commit message, or asks to review their diff.
---

## Current changes

!`git diff HEAD`

## Instructions

Summarize the changes above in two or three bullet points, then list any risks you notice such as missing error handling, hardcoded values, or tests that need updating. If the diff is empty, say there are no uncommitted changes.
```

The `` !`git diff HEAD` `` uses dynamic context injection: Claude Code runs command and replaces line with output before Claude sees skill content.

Test:
```text
What did I change?
/summarize-changes
```

### Where skills live

| Location | Path | Applies to |
| :--- | :--- | :--- |
| Enterprise | Managed settings | All users in org |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Where plugin is enabled |

Enterprise overrides personal; personal overrides project. Plugin skills use `plugin-name:skill-name` namespace.

#### Live change detection

Adding, editing, removing skill under `~/.claude/skills/`, project `.claude/skills/`, or `.claude/skills/` inside `--add-dir` directory takes effect WITHIN current session without restart. Creating top-level skills directory that didn't exist at session start requires restart.

#### Automatic discovery from parent and nested directories

Project skills load from `.claude/skills/` in starting directory and every parent directory up to repo root. When working with files in subdirectories, Claude Code also discovers skills from nested `.claude/skills/` directories on demand (monorepo support).

Each skill is a directory with `SKILL.md` entrypoint:
```text
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output
└── scripts/
    └── validate.sh    # Script Claude can execute
```

## Configure skills

### Types of skill content

**Reference content**: conventions, patterns, style guides, domain knowledge. Runs inline.

**Task content**: step-by-step for specific action (deployments, commits). Often invoked directly with `/skill-name`. Add `disable-model-invocation: true` to prevent automatic triggering.

```yaml
---
name: deploy
description: Deploy the application to production
context: fork
disable-model-invocation: true
---
```

Keep body concise — content [stays in context across turns](#skill-content-lifecycle). State what to do, not how/why.

### Frontmatter reference

All fields optional. Only `description` recommended.

| Field | Required | Description |
| :--- | :--- | :--- |
| `name` | No | Display name. If omitted, directory name. Lowercase letters, numbers, hyphens (max 64 chars). |
| `description` | Recommended | What skill does + when to use. Truncated at 1,536 chars in skill listing. |
| `when_to_use` | No | Additional context for invocation. Appended to description. |
| `argument-hint` | No | Hint during autocomplete. Example: `[issue-number]`. |
| `arguments` | No | Named positional args for `$name` substitution. |
| `disable-model-invocation` | No | Prevents Claude from auto-loading. Also prevents preloading into subagents. Default: `false`. |
| `user-invocable` | No | Hide from `/` menu. Default: `true`. |
| `allowed-tools` | No | Tools without permission prompt when skill active. |
| `model` | No | Override session model for rest of turn. |
| `effort` | No | Override session effort: `low`, `medium`, `high`, `xhigh`, `max`. |
| `context` | No | Set to `fork` to run in forked subagent context. |
| `agent` | No | Which subagent type when `context: fork` set. |
| `hooks` | No | Lifecycle hooks scoped to this skill. |
| `paths` | No | Glob patterns limiting when skill activated. |
| `shell` | No | `bash` (default) or `powershell` for `` !`command` `` blocks. |

#### Available string substitutions

| Variable | Description |
| :--- | :--- |
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` | Specific argument by 0-based index |
| `$N` | Shorthand for `$ARGUMENTS[N]` |
| `$name` | Named argument from frontmatter `arguments` list |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_EFFORT}` | Current effort level |
| `${CLAUDE_SKILL_DIR}` | Directory containing SKILL.md (resolves correctly for plugin skills) |

Indexed args use shell-style quoting. `/my-skill "hello world" second` → `$0` = `hello world`, `$1` = `second`.

### Add supporting files

Reference supporting files from SKILL.md so Claude knows what each contains.

> [!tip]
> Keep SKILL.md under 500 lines. Move detailed reference material to separate files.

### Control who invokes a skill

| Frontmatter | You invoke | Claude invokes | When loaded into context |
| :--- | :--- | :--- | :--- |
| (default) | Yes | Yes | Description always in context, full skill loads when invoked |
| `disable-model-invocation: true` | Yes | No | Description NOT in context, full skill loads when you invoke |
| `user-invocable: false` | No | Yes | Description always in context, full skill loads when invoked |

In regular session, skill descriptions loaded into context so Claude knows what's available, but full skill content only loads when invoked. Subagents with preloaded skills work differently: full content injected at startup.

### Skill content lifecycle

When skill invoked, rendered SKILL.md enters conversation as single message and stays for rest of session. Claude Code does NOT re-read skill file on later turns — write standing instructions, not one-time steps.

Auto-compaction carries invoked skills forward within token budget. Most recent invocation of each skill re-attached after summary, keeping first 5,000 tokens. Combined budget: 25,000 tokens.

If skill seems to stop influencing behavior, content is usually still present and model choosing other tools. Strengthen description and instructions, or use hooks to enforce deterministically. Re-invoke after compaction to restore full content.

### Pre-approve tools for a skill

`allowed-tools` grants permission while skill active. Does NOT restrict which tools are available.

```yaml
---
name: commit
description: Stage and commit the current changes
disable-model-invocation: true
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)
---
```

### Pass arguments to skills

`$ARGUMENTS`:
```yaml
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---

Fix GitHub issue $ARGUMENTS following our coding standards.
```

`/fix-issue 123` → "Fix GitHub issue 123 following our coding standards..."

By position:
```yaml
Migrate the $0 component from $1 to $2.
```

`/migrate-component SearchBar React Vue` → SearchBar / React / Vue.

## Advanced patterns

### Inject dynamic context

`` !`<command>` `` runs shell commands BEFORE skill content sent to Claude. Output replaces placeholder.

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`
```

Multi-line: fenced code block with ` ```! `.

Disable via `disableSkillShellExecution: true` in settings.

> [!tip]
> Include `ultrathink` anywhere in skill content for deeper reasoning.

### Run skills in a subagent

`context: fork` for isolation. Skill content becomes prompt that drives subagent. No conversation history.

> [!warning]
> `context: fork` only makes sense for skills with explicit instructions. Guidelines like "use these API conventions" without a task → subagent receives guidelines but no actionable prompt.

| Approach | System prompt | Task | Also loads |
| :--- | :--- | :--- | :--- |
| Skill with `context: fork` | From agent type (Explore, Plan, etc.) | SKILL.md content | CLAUDE.md |
| Subagent with `skills` field | Subagent's markdown body | Claude's delegation message | Preloaded skills + CLAUDE.md |

### Restrict Claude's skill access

Three ways:

**Disable all skills** in `/permissions`:
```text
# Deny rules:
Skill
```

**Allow/deny specific** with permission rules:
```text
Skill(commit)
Skill(review-pr *)
Skill(deploy *)  # deny
```

**Hide individual** with `disable-model-invocation: true`.

### Override skill visibility from settings

`skillOverrides` controls visibility without editing SKILL.md.

| Value | Listed to Claude | In `/` menu |
| :--- | :--- | :--- |
| `"on"` | Name + description | Yes |
| `"name-only"` | Name only | Yes |
| `"user-invocable-only"` | Hidden | Yes |
| `"off"` | Hidden | Hidden |

```json
{
  "skillOverrides": {
    "legacy-context": "name-only",
    "deploy": "off"
  }
}
```

## Generate visual output

Skills can bundle and run scripts. One pattern: interactive HTML files that open in browser. The codebase-visualizer example uses Python script to generate `codebase-map.html` with collapsible tree, file sizes, file type colors. Script path: `${CLAUDE_SKILL_DIR}/scripts/visualize.py`.

This pattern works for: dependency graphs, test coverage reports, API docs, database schema visualizations. Bundled script does work, Claude handles orchestration.

## Troubleshooting

### Skill not triggering

1. Description includes keywords users would naturally say
2. Skill appears in "What skills are available?"
3. Rephrase request to match description
4. Invoke directly with `/skill-name`

### Skill triggers too often

1. Make description more specific
2. Add `disable-model-invocation: true`

### Skill descriptions cut short

Budget scales at 1% of model's context window. Run `/doctor` to see if budget overflowing.

Raise via `skillListingBudgetFraction` setting or `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var. Free budget by setting low-priority skills to `"name-only"` in `skillOverrides`. Trim `description` and `when_to_use` text — 1,536 char cap configurable with `maxSkillDescriptionChars`.

## Related resources

* Debug your configuration
* Subagents
* Plugins
* Hooks
* Memory (CLAUDE.md)
* Commands
* Permissions
