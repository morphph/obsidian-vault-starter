---
type: source-summary
created: 2026-04-21
last-updated: 2026-04-21
sources:
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
tags: [wiki, source, github, agentic, resolver, production]
---

# Source: GBrain + GStack — GitHub Deep Scan

## Summary
GitHub Deep Scan of [[garry-tan|Garry Tan]]'s open-source production stack: **[[gbrain]]** (9,718 ⭐) and **[[gstack]]** (78,692 ⭐). Fetched 2026-04-21 via `gh` CLI. Primary payoff: the [[resolvers|resolver]] pattern, [[check-resolvable]], [[trigger-evals]], and the [[agent-skills-standard|Agent Skills standard]] are all **running real TypeScript code**, not theory. The Manidis filing-rules doc exists verbatim. `check-resolvable` is `src/core/check-resolvable.ts`. `gbrain doctor --fix` auto-rewrites inlined rules into callouts.

## Source
- **GBrain**: github.com/garrytan/gbrain — "Garry's Opinionated OpenClaw/Hermes Agent Brain" (TypeScript)
- **GStack**: github.com/garrytan/gstack — "23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, QA"
- **Fetched**: 2026-04-21 via `gh` CLI (tree + README + SKILL.md + CLAUDE.md + RESOLVER.md + filing-rules + manifest.json)

## 要点解读

### 1. GBrain 的 RESOLVER.md —— 具体长什么样
Garry 文章里说"resolver 是一张路由表"，但从来没展示过完整例子。deep scan 让我们看到全貌：

```markdown
| Trigger | Skill |
|---------|-------|
| Every inbound message | skills/signal-detector/SKILL.md |
| "What do we know about", "tell me about", "search for" | skills/query/SKILL.md |
| Creating/enriching a person or company page | skills/enrich/SKILL.md |
| User shares a link, article, tweet, or idea | skills/idea-ingest/SKILL.md |
| Meeting transcript received | skills/meeting-ingestion/SKILL.md |
```

**关键发现：**
- 不是 JSON / YAML，是**纯 markdown 表格**（好理由：LLM 天然最擅长读 markdown）
- 触发词是**自然语言短语列表**，不是正则 —— 让 LLM 做模糊匹配
- 有一节专门的 **"Disambiguation rules"**（当多个 skill 都能匹配时的处理顺序）
- 底部有 **"Conventions (cross-cutting)"** 指向 `skills/conventions/` 里那些要被所有 skill 参考的文档

**对咱们的启示：** 我们可以把 CLAUDE.md 里的 "Commands" 表升级成一个类似 RESOLVER.md 的明确触发表。

### 2. `_brain-filing-rules.md` —— Manidis 修复方案的原样
Garry 文章说"一份共享的 filing rules 文档修好了 10 个 skill"。deep scan 里就是这份文档，核心是一张**误归档对照表**：

| Wrong | Right | Why |
|-------|-------|-----|
| Analysis of a topic → sources/ | → appropriate subject directory | sources/ is for raw data only |
| Article about a person → sources/ | → people/ | Primary subject is a person |
| Research about a company → sources/ | → companies/ | Primary subject is a company |
| Reusable framework → sources/ | → concepts/ | It's a mental model |
| Tweet thread about policy → media/ | → civic/ or concepts/ | media/ is for content ops |

加上 "Iron Law: Back-Linking" + "Citation Requirements" + "Raw Source Preservation" 三条硬性规则。

**关键设计：** 不是"告诉 skill 该怎么做"，而是"枚举已知的错法 + 每个错法的 why"。这是 RLHF-friendly 的 prompt 工程。

### 3. check-resolvable 是**真代码**，不是概念
从 GBrain 的 CLAUDE.md：
> `src/core/check-resolvable.ts` — Resolver validation: **reachability, MECE overlap, DRY checks, structured fix objects**. v0.14.1: `CROSS_CUTTING_PATTERNS.conventions` is an array. New `extractDelegationTargets()` parses `> **Convention:**`, `> **Filing rule:**`, and inline backtick references. DRY suppression is proximity-based via `DRY_PROXIMITY_LINES = 40`.

**三种检查：**
1. **Reachability**：每个 skill 能不能从 RESOLVER.md 触达
2. **MECE overlap**：不同 skill 的 triggers 有没有重叠（false positive 的源头）
3. **DRY**：被多处 inline 的规则要被提取成 callout

还有配套的 `src/core/dry-fix.ts`：
> `gbrain doctor --fix` engine. `autoFixDryViolations(fixes, {dryRun})` rewrites inlined rules to `> **Convention:** see [path](path).` callouts via three shape-aware expanders (bullet / blockquote / paragraph). **Five guards**: working-tree-dirty, no-git-backup, inside-code-fence, already-delegated (40-line proximity), ambiguous-multi-match, block-is-callout.

**工程教训：** 自动修 markdown 要防 5 种坑。Garry 的代码都考虑了。

### 4. `skills/testing/SKILL.md` —— trigger-evals 的实际形态
在生产里，trigger-evals 不是一个 eval suite，而是一个 **"skill validation framework"** skill：

```markdown
## Contract
This skill guarantees:
- Every skill directory has a SKILL.md file
- Every SKILL.md has valid YAML frontmatter (name, description)
- Every SKILL.md has required sections (Contract, Anti-Patterns, Output Format)
- manifest.json lists every skill directory
- RESOLVER.md references every skill in the manifest
- No MECE violations (duplicate triggers across skills)

Automated: `bun test test/skills-conformance.test.ts test/resolver.test.ts`
```

**关键洞察：** 生产系统对 trigger-evals 的实现是**三层合一的完整性检查**：manifest.json ↔ RESOLVER.md ↔ 每个 SKILL.md。如果这三层任何一处不同步，testing skill 报错。

### 5. SKILL.md 的结构契约
每个 GBrain skill 都遵守同一个结构：
```
---
name: xxx
version: 1.0.0
description: |
  ...
triggers:
  - "trigger phrase 1"
  - "trigger phrase 2"
tools:
  - op1
  - op2
mutating: true/false
---

# Title

## Contract
This skill guarantees: ...

## Phases
1. ...
2. ...

## Output Format
```

## Anti-Patterns
- ...
```

**对比 Anthropic 官方 SKILL.md（[[agent-skills-standard]]）：**
- 官方：`description` 单字段 + 可选 `when_to_use`
- GBrain：`triggers: []` 显式数组 + `Contract/Phases/Output Format/Anti-Patterns` 结构化 body

GBrain 相当于在 Anthropic 标准上**加了更严的契约**。

### 6. `skills/manifest.json` —— machine-readable skill registry
每个 skill 在 manifest 里有 `{name, path, description}`。这是 RESOLVER.md 和 SKILL.md 之间的机器可读中间层 —— testing skill 用它做三方完整性验证。

### 7. GStack 的 "10 Hosts" 系统 —— Agent Skills 标准的跨运行时证明
GStack 的 SKILL.md 是**从 `.tmpl` 模板生成的**。同一份 skill 源 → `bun run gen:skill-docs --host <agent>` 生成 10 种运行时的变体：

| Agent | Install dir |
|-------|-------------|
| Claude Code | `~/.claude/skills/gstack-*/` |
| OpenAI Codex CLI | `~/.codex/skills/gstack-*/` |
| Cursor | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `~/.factory/skills/gstack-*/` |
| OpenCode / Slate / Kiro / Hermes / GBrain / OpenClaw | ... |

**这是 [[agent-skills-standard|Agent Skills 开放标准]]的第一个跨厂商证明** —— 同一套方法论可以编译到 10 种 agent 运行时。GStack 的 78K 星很大程度上来自"能同时服务所有 agent 的开发者"。

### 8. Minions —— latent/deterministic 的运行时实现
GBrain 的 Minions 是 Postgres 原生的任务队列。Garry 的**"latent vs deterministic"**原则在这里落地为自动路由：
```
- Deterministic (same input → same output) → Minions (Postgres-native, $0 tokens, millisecond)
- Judgment (needs assessment) → Sub-agents (LLM, tokens, slow)
```

生产基准对比（从 README）：
| | Minions | sessions_spawn（sub-agent） |
|---|---|---|
| Wall time | 753ms | >10,000ms（gateway timeout）|
| Token cost | $0.00 | ~$0.03 |
| Success | 100% | 0% |

**教训：** 把 deterministic work（拉数据、parse JSON、写 page）丢给 LLM sub-agent 是最烂的架构，哪怕 LLM 能做。正确做法是做出一个 boring job queue。

### 9. Team Mode + auto-update —— 消除 version drift
GStack 的 team mode：
> `./setup --team` + `gstack-team-init required` → teammates get gstack automatically on first Claude Code session. Fast auto-update check, throttled to once/hour, network-failure-safe.
> **No vendored files in your repo, no version drift, no manual upgrades.**

**对咱们的启示：** 如果本 vault 的 skill 以后有人 fork，"所有人用同一个最新版本" 可以靠类似机制实现，不需要 git submodule 或者 npm link。

### 10. BrainBench v1 —— 知识图谱的定量胜利
GBrain README 里有一个 benchmark 对比**图谱搜索 vs 纯向量搜索 vs grep**：
- Recall@5: 83% → **95%**（+12pt）
- Precision@5: 39% → **45%**
- Graph-only F1: **86.6% vs grep's 57.8%** (+28.8pt)

**对咱们的启示：** 如果本 vault 未来需要从 "flat files + index" 升级到有类型关系的知识图谱（`[[person]]` + `[[company]]` + 明确类型边），有可量化的收益预期 —— 且 Garry 提供了开源实现参考。

## Pages created from this source
- [[agent-skills-standard]] — concept
- [[source-gbrain-gstack-deep-scan]] — this page

## Pages updated from this source
- [[gbrain]] — massive expansion: 17,888 pages / 4,383 people / 723 companies, 21 crons, built in 12 days; BrainBench numbers; Minions job queue; real file paths (RESOLVER.md, _brain-filing-rules.md, check-resolvable.ts, dry-fix.ts); SKILL.md contract; manifest.json registry
- [[gstack]] — massive expansion: 78,692 stars; 10-host template system; 23-skill specialist roster; team mode auto-update; Karpathy quote + 810× productivity claim
- [[resolvers]] — added concrete RESOLVER.md format; three-layer artifact (RESOLVER.md + manifest.json + SKILL.md); two implementations comparison
- [[check-resolvable]] — confirmed as real TypeScript code; added MECE overlap + DRY proximity (40-line); gbrain doctor --fix auto-remediation; five guards
- [[trigger-evals]] — reframed as "three-layer integrity check" (manifest ↔ resolver ↔ SKILL); added skills/testing/SKILL.md as production reference
- [[thin-harness-fat-skills]] — added 10-host template system as proof the standard generalizes
- [[openclaw]] — confirmed as one of GStack's 10 host targets

## Connections
- Related: [[gbrain]], [[gstack]], [[garry-tan]], [[resolvers]], [[check-resolvable]], [[trigger-evals]], [[agent-skills-standard]], [[thin-harness-fat-skills]], [[latent-vs-deterministic]], [[openclaw]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Initial creation |
