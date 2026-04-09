---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
tags: [wiki, architecture, agentic, practice]
---

# Context Noise Governance

## Summary
The practice of actively managing what enters the LLM context window to maximize signal-to-noise ratio. [[tw93]] argues context problems are usually **noise problems, not capacity problems** — useful info gets drowned by irrelevant content. Governance happens through layered loading, output filtering, and explicit compression instructions.

## Details

### The Hidden Cost Breakdown (200K context)
| Category | Tokens | Notes |
|----------|--------|-------|
| System instructions | ~2K | Fixed |
| Skill descriptors | ~1-5K | Every enabled Skill, always resident |
| MCP tool definitions | ~10-20K | **Biggest hidden killer** — each server ~4-6K |
| LSP state | ~2-5K | Fixed |
| CLAUDE.md | ~2-5K | Semi-fixed |
| Memory | ~1-2K | Semi-fixed |
| **Dynamic available** | **~160-180K** | Conversation, files, tool results |

5 MCP servers = 25K tokens (12.5%) in fixed overhead alone.

### Recommended Context Layering
- **Always resident** → CLAUDE.md: project contract, build commands, prohibitions
- **Path-loaded** → `.claude/rules/`: language/directory/file-type specific
- **On-demand** → Skills: workflows, domain knowledge
- **Isolated** → Subagents: large explorations, parallel research
- **Not in context** → Hooks: deterministic scripts, audit, blocking

Rule: "偶尔用的东西就不要每次都加载进来" (Don't load things you only occasionally need every time)

### Tool Output Noise
Tool outputs (cargo test, git log, grep) can dump thousands of lines. Claude doesn't need all of it — just "passed or failed, and where it failed."
- RTK (Rust Token Killer): auto-filters command output before reaching Claude (open source: github.com/rtk-ai/rtk)
- Always pipe Hook output through `| head -30` to avoid polluting context

### Compact Instructions Pattern
Default compression deletes "re-readable" content but also discards architecture decisions. Write explicit priorities in CLAUDE.md:
```markdown
## Compact Instructions
Preserve in priority order:
1. Architecture decisions (NEVER summarize)
2. Modified files and key changes
3. Current verification status
4. Open TODOs and rollback notes
5. Tool outputs (can delete, keep pass/fail only)
```

### HANDOFF.md Pattern
Before starting new sessions, have Claude write a HANDOFF.md: current progress, what was tried, what worked/didn't, next steps. Next Claude instance reads only this file — doesn't depend on compression quality.

### Skill Descriptor Optimization
Every enabled Skill's descriptor is always in context:
- Inefficient (~45 tokens): long multi-sentence description
- Efficient (~9 tokens): "Use for PR reviews with focus on correctness."
- High-freq (>1/session): keep auto-invoke, optimize descriptor
- Low-freq (<1/session): disable-auto-invoke, manual trigger only

## Connections
- Related: [[context-management]], [[claude-code]], [[prompt-cache-optimization]], [[session-memory]], [[dreaming]], [[documentation-layers]]
- This is the practitioner's complement to [[context-management]] — Troy Hua documents the internal 7-layer mechanism; Tw93 documents external governance strategies
- HANDOFF.md pattern parallels [[zero-friction-capture]] — both ensure knowledge survives context boundaries
- [[documentation-layers]] is a concrete implementation of the layering strategy described here — a self-regulating table that prevents Layer 1 bloat

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-tw93-claude-code-architecture-governance.md | Initial creation |
| 2026-04-09 | raw/2026-04-09-claude-md-self-audit.md | Added link to documentation-layers as concrete implementation |
