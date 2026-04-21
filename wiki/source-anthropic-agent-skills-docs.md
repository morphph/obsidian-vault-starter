---
type: source-summary
created: 2026-04-21
last-updated: 2026-04-21
sources:
  - raw/2026-04-21-anthropic-agent-skills-docs.md
tags: [wiki, source, skills, agentic, docs]
---

# Source: Anthropic — Extend Claude with Skills (Official Docs)

## Summary
Claude Code's official documentation for the [[agent-skills-standard|Agent Skills standard]]. Fetched 2026-04-21 to confirm and extend the [[resolvers]] research track. Key validation: **Anthropic's `description` field is explicitly documented as the resolver entry** ("Claude uses this to decide when to apply the skill"). Also surfaced concrete constraints that drive [[context-rot]]: 1,536-char cap per skill entry, 1% context-window budget, `SLASH_COMMAND_TOOL_CHAR_BUDGET` escape hatch.

## Source
- **Primary URL**: https://docs.claude.com/en/docs/claude-code/skills (redirects through docs.anthropic.com → code.claude.com)
- **Open standard**: https://agentskills.io
- **Fetched**: 2026-04-21 via WebFetch (3 redirects)

## 要点解读

### 1. Agent Skills 是一个跨厂商开放标准，不是 Claude 专属
Anthropic 官方明确：
> "Claude Code skills follow the **Agent Skills open standard** (agentskills.io), which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection."

意思是：skill 格式（SKILL.md + YAML frontmatter）是**厂商中立**的。Cursor、Codex、Hermes、OpenClaw 都可以各自实现。GStack 的 "10 hosts" 就是这个标准的第一个跨运行时证据。

### 2. `description` 字段 = canonical resolver —— 官方认证
关键一行（照抄）：
> "`description`: What the skill does and when to use it. **Claude uses this to decide when to apply the skill.**"

这**彻底验证** Garry Tan 那句"description is the resolver"。不是比喻，是官方机制。

实现细节（这是 Garry 文章没讲到的）：
- description + when_to_use 两字段在 skill listing 里被合并
- 总长度 **1,536 字符**封顶
- 整个 skill listing 在 context 中占 **1% of context window**（fallback 8,000 chars）
- 可以用 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 调大

**这也解释了 context rot 的机制层面：** skill 多到 description 被截断时，Claude 看不到触发关键词 → 路由失败。Context rot 不是抽象概念，是字符预算超限的直接结果。

### 3. Progressive Disclosure —— "200 行 vs 20,000 行"的官方实现
> "In a regular session, **skill descriptions are loaded into context so Claude knows what's available, but full skill content only loads when invoked.**"

这是 Garry 的 resolver 论断在 Claude Code 里的落地：
- 写 CLAUDE.md 20,000 行 = 所有内容都在 context（drown）
- 写成 20 个 skill + description = 20 行在 context，body 按需加载（float）

还有一个微妙的点：一旦 skill 被 invoke 了，body 就**永久驻留在 session 里**（"enters the conversation as a single message and stays there"）。所以 skill 更像"懒加载的 fat modules"，不是"每次重读"。

### 4. Custom Commands 已经被合并进 Skills
重要的向后兼容说明：
> "`.claude/commands/deploy.md` 和 `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Your existing `.claude/commands/` files keep working."

差别：
- Commands：单文件
- Skills：目录结构，支持 supporting files（reference docs、scripts、examples）

**对本 vault 的启示：** 我们的 `.claude/commands/ingest.md` 现在是单文件。如果想支持 supporting files（例：ingest rules，filing fixture），可以迁成 `.claude/skills/ingest/SKILL.md` 目录结构，不破坏现有行为。

### 5. `paths:` glob 的双重身份
> "`paths`: Glob patterns that limit when this skill is activated. **Uses the same format as path-specific rules.**"

这其实是在文档里确认：`.claude/skills/*/` 的 `paths:` 和 `.claude/rules/*/` 的 `paths:` 是同一个机制。换句话说，本 vault 已有的 `.claude/rules/wiki-page-format.md (paths: wiki/**)` 就是 **filing-by-context resolver** 的落地。

### 6. 两个具体的故障诊断流程（对 trigger-evals 直接可用）
文档给出了 Anthropic 官方的 "routing failure" 排查步骤：

**如果 skill 该触发但没触发：**
1. 检查 description 里是否包含用户自然会说的关键词
2. 用 "What skills are available?" 确认 skill 在列表里
3. 换个说法重新问
4. 直接 `/skill-name` 手动触发

**如果 skill 触发过头：**
1. 让 description 更具体
2. 加 `disable-model-invocation: true` 改成手动触发

👉 **这就是 [[trigger-evals]] 两种失败模式的官方调试 playbook，可以直接写进我们的 resolver-evals 测试集。**

### 7. 三个官方资源（本 vault 以后可能用到）
- `/en/sub-agents#preload-skills-into-subagents` —— 把 skill 作为参考资料预加载到子 agent
- `/en/memory#path-specific-rules` —— `paths:` glob 的详细用法
- `/en/permissions` —— 用 `Skill(name)` 语法做 allow/deny

## Pages created from this source
- [[agent-skills-standard]] — concept (open standard + Anthropic implementation reference)

## Pages updated from this source
- [[resolvers]] — added "description as canonical resolver" (official wording); 1,536-char cap; SLASH_COMMAND_TOOL_CHAR_BUDGET
- [[context-rot]] — added mechanistic explanation (description truncation = routing failure)
- [[check-resolvable]] — added Anthropic's official "routing failure" troubleshooting playbook
- [[trigger-evals]] — added official two-failure-mode debugging steps
- [[claude-code]] — added Agent Skills open standard reference; progressive disclosure lifecycle

## Connections
- Related: [[agent-skills-standard]], [[resolvers]], [[thin-harness-fat-skills]], [[context-rot]], [[context-noise-governance]], [[claude-code]], [[documentation-layers]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-21 | raw/2026-04-21-anthropic-agent-skills-docs.md | Initial creation |
