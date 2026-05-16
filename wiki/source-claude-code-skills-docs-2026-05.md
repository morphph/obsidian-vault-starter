---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-skills-refresh.md
supersedes:
  - source-anthropic-agent-skills-docs
tags: [claude-code, official-docs, skills, refresh, frontmatter, lifecycle]
---

# Source: Extend Claude with skills (2026-05-14 refresh)

## Summary
Refreshed Anthropic docs on **Claude Code skills** at `code.claude.com/docs/en/skills.md` — supersedes [[source-anthropic-agent-skills-docs]] (2026-04-21). Conceptually unchanged (still Agent Skills standard, 1,536-char cap, progressive disclosure), but adds: **`paths` glob field** for conditional auto-load, **`hooks` field** for skill-scoped lifecycle hooks, **`shell` field** (bash/powershell), **`skillOverrides` setting** for visibility control without editing SKILL.md, **bundled skills** (`/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api`), and **monorepo nested discovery**. Conflict-clear: all old [[agent-skills-standard]] facts remain true.

## What's new since 2026-04-21

### 6 new frontmatter fields

| Field | Description |
| :--- | :--- |
| `paths` | Glob patterns limiting when skill auto-activates. Comma-separated string or YAML list. Same format as path-specific rules. |
| `hooks` | Lifecycle hooks scoped to this skill (PreToolUse, PostToolUse, Stop) — fires only during skill invocation |
| `shell` | `bash` (default) or `powershell` for `` !`cmd` `` blocks in skill |
| `arguments` | Named positional args. With `arguments: [issue, branch]`, `$issue` = first arg, `$branch` = second |
| `when_to_use` | Additional trigger context appended to `description`. **Both share 1,536-char cap.** |
| `argument-hint` | Display hint during autocomplete: `[issue-number]` |

### 6 new substitution variables

- `$ARGUMENTS[N]` / `$N` — argument by 0-based index
- `$name` — named argument from `arguments` frontmatter
- `${CLAUDE_SESSION_ID}` — current session ID
- `${CLAUDE_EFFORT}` — current effort level (low/medium/high/xhigh/max)
- `${CLAUDE_SKILL_DIR}` — directory containing SKILL.md (resolves correctly for plugin skills)

### `skillOverrides` setting (new)

Control skill visibility from `settings.json` (or `.claude/settings.local.json`) WITHOUT editing SKILL.md. Useful for shared-repo skills you don't want to edit:

```json
{
  "skillOverrides": {
    "legacy-context": "name-only",
    "deploy": "off"
  }
}
```

| Value | Listed to Claude | In `/` menu |
| :--- | :--- | :--- |
| `"on"` | Name + description | Yes |
| `"name-only"` | Name only | Yes |
| `"user-invocable-only"` | Hidden | Yes |
| `"off"` | Hidden | Hidden |

`/skills` menu writes it for you: highlight skill, `Space` to cycle states, `Enter` to save. **Plugin skills are NOT affected by `skillOverrides`** — manage via `/plugin` instead.

### Bundled skills (renamed and expanded)

`/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api` are now official bundled skills (prompt-based — give Claude instructions and let it orchestrate). Listed alongside built-in commands in commands reference, marked **Skill** in Purpose column.

### Monorepo nested discovery

When working with files in subdirectories, Claude Code discovers skills from **nested `.claude/skills/`** directories on demand. Editing `packages/frontend/x.ts` → also loads from `packages/frontend/.claude/skills/`.

This is the filesystem-level [[resolvers|resolver]] pattern: **the path you're editing IS the routing signal**.

### Live change detection

Adding, editing, removing skill takes effect WITHIN current session — **no restart needed**. Creating a top-level skills directory that didn't exist when session started still requires restart.

### Skills from `--add-dir`

`--add-dir` flag grants file access, not configuration discovery — except skills. `.claude/skills/` within added directory is loaded automatically. **Subagents, commands, output styles from `--add-dir` are NOT loaded.**

## What's unchanged (confirmed)

All from [[agent-skills-standard]]:
- 1,536-char cap per skill (description + when_to_use combined)
- 1% context window budget (fallback 8,000 chars), raise via `SLASH_COMMAND_TOOL_CHAR_BUDGET` or `skillListingBudgetFraction`
- Skill body single message stays for session (no re-read on later turns)
- Auto-compaction 25K total / 5K per skill, most recent first
- Plugin skills namespaced as `plugin-name:skill-name`
- Scope priority: enterprise > personal > project > plugin
- `disable-model-invocation: true` for user-only invocation
- `user-invocable: false` for Claude-only invocation
- `context: fork` runs skill as forked subagent
- Dynamic context injection via `` !`command` `` (disable via `disableSkillShellExecution`)
- `allowed-tools` grants permission without restricting (does NOT limit which tools are callable)

## Resolved ambiguity (was previously vague)

- **CLAUDE_SKILL_DIR**: explicitly documents that for plugin skills this resolves to the skill's subdirectory in the plugin, NOT the plugin root. Critical for path-based references.
- **`paths` glob behavior**: "Claude loads the skill automatically ONLY when working with files matching the patterns" — was previously a community feature, now official.

## Connections
- Related: [[claude-code]], [[agent-skills-standard]], [[source-claude-code-subagents-docs]], [[source-claude-code-plugins-docs]], [[source-claude-code-hooks-docs]], [[resolvers]], [[context-rot]], [[skillify-meta-skill]]
- **Supersedes**: [[source-anthropic-agent-skills-docs]] for fields listed above. Old page kept for history.
- [[agent-skills-standard]] page should be updated with the 6 new fields (see conflict ledger)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-skills-refresh.md | Initial refresh from current docs — additive over 2026-04-21 version |
