# OpenAI Codex Agent Skills (Documentation)

**Source:** https://developers.openai.com/codex/skills
**Publisher:** OpenAI Developers (official docs)
**Fetch date:** 2026-05-20
**Fetch method:** WebFetch

---

## Definition

> "A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably."

## Open standard

Codex skills "build on the open agent skills standard" from **agentskills.io** — **the same standard Anthropic uses for its Skills**. This is a notable cross-vendor convergence: skill files written for one vendor are largely portable to the other.

## Directory structure

```
my-skill/
  SKILL.md           (required — instructions + metadata)
  scripts/           (optional — executable code)
  references/        (optional — documentation)
  assets/            (optional — templates, resources)
  agents/openai.yaml (optional — UI / dependency config)
```

## SKILL.md format

Required frontmatter:
- `name`
- `description`

(Same structure as Anthropic skills.)

## Progressive disclosure

Codex initially receives only skill **names, descriptions, file paths**. Full `SKILL.md` instructions load **only when a skill is selected**.

Initial skills list capped at ~8,000 characters to avoid prompt bloat.

## Invocation methods

1. **Explicit:** user types `$skill-name` (or `/skills` command browser)
2. **Implicit:** Codex auto-selects based on task ↔ skill description match

## Discovery scopes

- Repository: `.agents/skills` at various directory levels
- User: `$HOME/.agents/skills`
- Admin: `/etc/codex/skills`
- System: bundled with Codex

## Distribution: plugins

For broader reusability, skills are packaged as **plugins** — installable distribution format bundling multiple skills with optional app integrations and MCP servers.

## Best practices (per docs)

- "Keep each skill focused on one job"
- Favor instruction-based approaches over scripts unless deterministic behavior is required
- `$skill-creator` tool guides initial creation

---

## Cross-vendor portability assessment

| Property | Codex skill | Anthropic skill | Portable? |
|---|---|---|---|
| SKILL.md frontmatter (`name`, `description`) | Yes | Yes | ✓ |
| Progressive disclosure | Yes | Yes | ✓ |
| `scripts/`, `references/`, `assets/` dirs | Yes | Yes | ✓ |
| Invocation syntax | `$skill-name` | `/skill-name` | ✗ (small fix) |
| Discovery scope | `.agents/skills` | `.claude/skills` | ✗ (directory rename) |
| Vendor-specific YAML | `agents/openai.yaml` | n/a | ✗ |

**Practical port time:** A Matt Pocock-style Claude Code skill (e.g. `grill-with-docs`) → Codex skill: rename directory, rename invocation syntax, optional YAML drop. **<1 hour per skill** for typical cases.

**Strategic implication:** The agentskills.io shared standard means tooling like Matt Pocock's `mattpocock/skills` library could be ported to Codex with modest effort. This eliminates the "vendor lock-in" friction for skill-driven workflows.
