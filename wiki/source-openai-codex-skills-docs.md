---
type: source-summary
created: 2026-05-20
last-updated: 2026-05-20
sources:
  - raw/2026-05-20-openai-codex-skills-docs.md
tags: [wiki, source, openai, codex, skills, agentskills-standard, cross-vendor, official-docs]
---

# Source: OpenAI Codex Agent Skills

## Summary
Codex Agent Skills package instructions + scripts + references into reusable workflow modules. **Built on the open agentskills.io standard — the same standard Anthropic uses**. SKILL.md + optional `scripts/` `references/` `assets/` + optional `agents/openai.yaml`. Progressive disclosure: only names + descriptions + paths load initially (8K char cap), full SKILL.md loads on selection. Explicit `$skill-name` or implicit auto-selection. **Cross-vendor portability is realistic** —— Matt Pocock's Claude Code skills can be ported to Codex with directory rename + invocation syntax fix.

## Source Metadata
- **URL:** https://developers.openai.com/codex/skills
- **Publisher:** OpenAI Developers (official docs)
- **Fetch date:** 2026-05-20

---

## 要点解读（12-Section Compressed Study Guide）

### 1. 元信息
官方 docs；**显式 build on agentskills.io open standard** —— 这是 2026 年最 underappreciated 的 cross-vendor 收敛信号。

### 2. 核心论点
agent 的能力不应是 prompt-hardcode 进系统的，**应该是模块化、可分发、跨 agent runtime 互通的 skill 包**。

简化压缩包：**"Skill = agent 的可分发 npm package。"**

### 3. 论证结构
```
1. SKILL.md 是 skill 的"package.json"
2. progressive disclosure 防 prompt bloat
3. agentskills.io 让 skill 跨 vendor
4. plugin 是 skill 的"npm registry"
```

### 4. 关键概念字典

> **agentskills.io 开放标准 ⭐⭐**
> - **是什么**：跨 vendor 的 skill 文件格式标准
> - **为什么重要**：**这是 PM 应该重视的"行业收敛"信号** —— Anthropic 和 OpenAI 同时支持同一标准 = 写一次 skill，理论上跨 runtime 复用
> - **直觉类比**：像 LSP（Language Server Protocol）—— Microsoft 提出，VS Code / Vim / Emacs 都支持
> - **战略含义**：Matt Pocock 的 `mattpocock/skills` (87K stars) 可以理论上 1 小时移植到 Codex

> **Progressive disclosure**
> - **是什么**：初始 prompt 只塞 skill 元信息（name + description + path），上限 ~8000 字符；selected 时才加载完整 SKILL.md
> - **为什么重要**：让 1000 个 skill 共存不爆 context window
> - **直觉类比**：IDE 的 import on demand

> **`$skill-name` 显式 vs 隐式 invocation**
> - **是什么**：`$grill-with-docs` 显式触发；或 Codex 看 task 自动匹配 description 选 skill
> - **反面**：description 写得模糊 → 隐式选错 skill

### 5. 框架与心智模型

**Skill 复用 4 层 hierarchy**：
```
admin level (/etc/codex/skills)         - 公司强制
user level ($HOME/.agents/skills)       - 个人复用
repo level (.agents/skills)             - 项目专用
system level (bundled with Codex)       - 内置
```

### 6. 关键数据
- **8000 字符** 初始 prompt budget for skills list
- **agentskills.io** open standard

### 7. 关键引语
> "A skill packages instructions, resources, and optional scripts so Codex can follow a workflow reliably."

> "Keep each skill focused on one job."

### 8. 实操指南

**Skill minimal structure**：
```
my-skill/
  SKILL.md           # required (name + description frontmatter)
  scripts/           # optional
  references/        # optional
  assets/            # optional
  agents/openai.yaml # optional
```

**SKILL.md frontmatter**：
```markdown
---
name: chapter-splitter
description: Split narration.md into chapter-tagged video script
---
# Instructions

[Full skill body]
```

### 9. 对比与反对意见

**vs Anthropic Skills**：
- **同标准 (agentskills.io)** —— 文件结构几乎一致
- 差异 1：discovery 目录 `.agents/skills` vs `.claude/skills`
- 差异 2：invocation `$skill` vs `/skill`
- 差异 3：可选 vendor yaml (`agents/openai.yaml`)

**移植 Matt Pocock skill 到 Codex**：
1. 目录 rename `.claude/skills` → `.agents/skills`
2. invocation syntax 在文档里换
3. 删除 vendor-specific yaml 或加 `openai.yaml`
4. **典型耗时 < 1 小时**

### 10. wiki 连接

- [[source-anthropic-agent-skills-docs]] —— 跨厂商对应
- [[mattpocock-skills-library]] —— 87K star Claude Code skills，可移植
- [[grill-with-docs]] —— Matt 的 discovery skill，可移植
- [[agent-skills-standard]] —— wiki 已有的 agentskills.io 标准页

### 11. 对用户启示

#### 短期
- **写 methodology 文章时，把 agentskills.io 跨厂商共标准作为"跨 vendor 收敛"的最强证据**（比 hooks GA 还要明显，因为是 *同一文件格式*）

#### 中期
- 自己写 wiki 的 5 个 slash command（/ingest /draft /query /lint /visualize）可以改写为 agentskills.io 兼容的 skill 包 —— 之后可跨 Claude/Codex 运行

#### 长期
- "agentskills.io 标准下的跨厂商 skill 复用"是中文真空 SEO 题材

### 12. 一句话总结
**"Codex Skills + Anthropic Skills 同标准 (agentskills.io) = 写一次跨 runtime 复用；这是 2026 年最 underappreciated 的 cross-vendor 信号。"**

---

## Connections
- Related: [[source-anthropic-agent-skills-docs]], [[mattpocock-skills-library]], [[grill-with-docs]], [[agent-skills-standard]], [[source-openai-codex-subagents-docs]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-20 | raw/2026-05-20-openai-codex-skills-docs.md | Initial creation |
