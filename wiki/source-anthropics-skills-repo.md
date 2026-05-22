---
type: source-summary
created: 2026-05-22
last-updated: 2026-05-22
sources:
  - raw/2026-05-22-repo-anthropics-skills.md
tags: [wiki, source, anthropic, claude-code, skills, repo]
---

# Source: anthropics/skills (Official Repo GitHub Deep Scan)

## Summary
Official Anthropic Skills repo (138.9K⭐ / 16.4K forks / actively maintained). 17 example SKILL.md files, the headline meta-skill `skill-creator` (Anthropic's official playbook for creating + improving + optimizing skills), a minimal template (just `name` + `description`), and a one-line spec pointer to agentskills.io. Distributed as Claude Code plugin marketplace with 3 plugins. **Reveals 4 things the official docs don't:** (1) "pushy descriptions" counter-intuitive guidance — Claude undertriggers, fight it with aggressive language; (2) concrete progressive-disclosure budgets — ~100 words metadata / <500 lines body / unlimited resources; (3) full ML-style optimization workflow with train/test split + iteration workspaces + 5-round description optimization; (4) the 4 improvement principles (generalize / lean / explain why / bundle repeated work) — the official answer to "how do I make my skill better."

## Source Metadata
- **URL:** https://github.com/anthropics/skills
- **Maintainer:** Keith Lazuka (klazuka@anthropic.com)
- **Vitals (2026-05-22):** 138,882 stars · 16,386 forks · last commit 2026-05-22
- **License:** Apache 2.0 (example skills); source-available (document skills: docx/pdf/pptx/xlsx); Apache 2.0 (claude-api)
- **Fetch method:** GitHub Deep Scan (gh CLI)

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
**作者**：Anthropic 官方（marketplace.json 显示维护人是 Keith Lazuka @klazuka@anthropic.com，但代表整个公司）。**Insider 中的 insider**——他们建造了 Claude 本人，他们对"怎么写 skill 让 Claude 用得好"的话语权是 max。

**来源**：github.com/anthropics/skills 官方 repo。配套 4 个官方支持页（claude support center 的 What/Using/Creating skills 三篇 + engineering blog "Equipping agents..."）。

**影响力指标（2026-05-22）**：138,882 stars / 16,386 forks（GitHub 全站前 30 规模）；今天还在更新；通过 `/plugin marketplace add anthropics/skills` 直接装到 Claude Code。

**与已有 wiki 资源的关系**：和官方 docs（[[source-claude-code-skills-docs-2026-05]]）是**互补不是重复**——docs 讲规范（spec、frontmatter 字段、storage 优先级），这个 repo 讲**实战**（17 个真实例子 + skill-creator 元技能）。**看 docs 学语法，看 repo 学写法。**

### 2. 核心论点
Anthropic 主张：**创建一个 skill 不是写 prompt，而是做一个迷你 ML 项目**——有 train/test split、有 baseline 对照、有 quantitative + qualitative 双轨评估、有 iteration 循环。**因为** Claude 默认会 "undertrigger" skill（不该用却不用，比错用更常见），**所以**写好 skill 的真正难点不在"内容"而在"触发"——description 才是核心 deliverable，body 是次要的。

压缩到一句话：**"Skill 是 prompt 工程的 ML 化——用 train/test 评估法治理 latent space 的 undertriggering 问题。"**

### 3. 论证结构
```
1. 三层 progressive disclosure 是物理基础
   → metadata(~100词) / body(<500行) / resources(无限)
2. Skill 的成功 = 触发对 × 内容对
   → 触发对 = description 工程问题
   → 内容对 = 写法 + 持续优化问题
3. 解决触发对：description optimization loop
   → 20 个 realistic 查询 / 60-40 train-test / 3× 重跑 / 5 轮 / 按 test 选最优
4. 解决内容对：迭代评估循环
   → with-skill vs baseline 并行跑 / 自动 + 人工双评 / iteration-N 文件夹
5. 4 大改进原则
   → 泛化 / 精简 / 解释 why / 把重复脚本沉淀进 scripts/
```

### 4. 关键概念字典

> **Pushy Description（激进描述）**
> 因为 Claude 倾向于 undertrigger（该用不用），description 要写得**主动一点**：除了"做什么"还要明示"什么时候必须用"，包括用户没明说但意图相关的场景。**这是官方承认的反直觉发现**。
> 对照 [[agent-skills-standard]] 里 Tw93 的"Don't use when..."——pushy positives + explicit negatives 才是完整版。

> **Three-Level Progressive Disclosure**
> metadata (~100 词) / SKILL.md body (<500 行理想值) / bundled resources (无限)。这是物理预算，决定 skill 库能做多大不爆 context。补全了 [[source-claude-code-skills-docs-2026-05]] 里 1,536 字符 description cap 之外的 body / resources 层预算。

> **Description Optimization Loop**
> 20 个 realistic 查询 → 60/40 train/test 切分 → 每个查询跑 3 次取触发率 → Claude 提议改进 → 在 train/test 上重测 → 最多 5 轮 → 按 test score 选最优。**Prompt 工程从手艺变工程的关键产物**——之前 [[skillify-meta-skill]] 里 Garry Tan 的 resolver eval 是手工版；Anthropic 包装成 `scripts.run_loop` 一行命令。

> **Realistic Test Query**
> trigger eval 查询必须有现实味道——文件路径 + 个人背景 + 列名/数值 + 公司名 / URL + 一点 backstory，可以小写、有 typo、有 abbreviation。**这是整套 description 优化的输入质量上限**。

> **The 4 Improvement Principles**
> 1. Generalize from feedback（不要 overfit）2. Keep prompt lean（读 transcript 删没拉动作用的）3. Explain the why（不要 ALWAYS/NEVER 大写）4. Look for repeated work（3 个 test 都自己写了同一个脚本？沉淀进 scripts/）。**Iteration 第 2 轮以后的核心方法论**。

> **Quantitative Eval Workspace Structure**
> `<skill-name>-workspace/iteration-N/eval-N/{with_skill,without_skill}/outputs/` + `eval_metadata.json` + `timing.json` + `grading.json`。**Load-bearing**——eval-viewer HTML 假设这个目录结构存在。文件结构就是 contract。

### 5. 框架与心智模型

**核心框架：Skill 创建/优化的两层循环**

```
外层（Iteration Loop）：
    Draft → 跑测试 → 人工 review → 改进 → 重复
    直到：用户满意 / 反馈全空 / 没明显进步

内层（Description Optimization Loop）：
    20 query eval set → 60/40 split → run × 3 → Claude 提议改进 → 测试 → 选 best
    最多 5 轮，按 test score 选优
```

**套用到 LoreAI 示范**：把 "glossary entry generator prompt"当 skill，draft 一版 → 选 3-5 个真实英文 SaaS 术语 → 跑 with-prompt 和 baseline → 你/产品人 review → 改进。内层：写 20 个真实查询测 description（一半 should-trigger 一半 should-not）。

### 6. 关键数据与例证
| 数据 | 支撑什么 | 用途 |
|---|---|---|
| 138.9K stars / 16.4K forks | Anthropic 官方 social proof | 中文版科普文引用 |
| 17 个示例 skill | Skill 不是抽象概念，是 working code | 选 skill-creator + mcp-builder 细读 |
| ~100 词 / <500 行 / 无限 | 三层预算具体数字 | 写自己 skill 时直接对照 |
| 60/40 + 3× + 5 iter max | Description 优化是 ML 问题 | 可直接抄这个配置 |
| 20 query (8-10 + 8-10) | 评估集 minimum viable size | 自己 prompt 评估集大小参考 |
| "undertrigger > overtrigger" | 官方观察的 failure mode 主方向 | 验证 pushy description 反直觉建议 |

### 7. 关键引语

> "Currently Claude has a tendency to 'undertrigger' skills... please make the skill descriptions a little bit 'pushy'."
> ⭐ 全 repo 最重要的实操建议，反直觉

> "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag."
> ⭐ Anthropic 自己反对 prompt engineering 的"硬规则"流派

> "Today's LLMs are smart. They have good theory of mind and when given a good harness can go beyond rote instructions."
> ⭐ 一个非常 humanist 的 LLM 观

> "Rather than put in fiddly overfitty changes, or oppressively constrictive MUSTs, if there's some stubborn issue, you might try branching out and using different metaphors."
> ⭐ 反 over-engineering 的官方立场

> "This task is pretty important (we are trying to create billions a year in economic value here!) and your thinking time is not the blocker."
> ⭐ 提醒：skill 不是要快速产出，是要深思

> "There's a trend now where the power of Claude is inspiring plumbers to open up their terminals, parents and grandparents to google 'how to install npm'."
> ⭐ 用户群下沉的官方观察

### 8. 实操指南

**官方 Checklist（写一个新 skill）：**
- [ ] 回答 4 问（做什么 / 何时触发 / 输出格式 / 是否需要 test cases）
- [ ] 写 SKILL.md draft（YAML frontmatter + 激进 description + markdown body，<500 行，imperative form，explain why 不堆 MUST）
- [ ] 设置 bundled resources：scripts/（deterministic）references/（domain variants）assets/（输出模板）
- [ ] 写 2-3 个真实测试 prompt，存到 `evals/evals.json`
- [ ] 同一回合内并行跑 with_skill 和 baseline
- [ ] 跑后立刻存 `timing.json`
- [ ] Grade 后跑 aggregate_benchmark 出 `benchmark.json + .md`
- [ ] 跑 generate_review.py 启动 HTML viewer
- [ ] 按 4 大原则改进
- [ ] 进入下一轮 iteration-N
- [ ] 跑 description optimization loop
- [ ] Package 出 `.skill` 文件

### 9. 对比与反对意见
| 对比对象 | Anthropic 立场 | 隐含信念 |
|---|---|---|
| vs 保守精确 description | 反对——写得 pushy 一点 | Undertriggering 比 overtriggering 常见 |
| vs ALWAYS/NEVER 大写规则 | 黄色警告，应 reframe + explain why | LLM 有 theory of mind |
| vs "评估靠 vibes" | 反对——quantitative + qualitative 双轨 | Skill 是要被用百万次的产品 |
| vs "test pass 就行" | 反对——看 transcript 不只看 output | 让模型浪费时间的部分要删 |

**Anthropic 隐含承认的限制**：
- skill-creator 是给 Claude Code 用的—— Claude.ai 上无 subagents，quantitative benchmark 没意义
- Description optimization loop 需要 `claude` CLI——Claude.ai 用不了
- **简单查询（"read this PDF"）即使 description 完美匹配也不会触发**——所以 skill 适合复杂、多步、专门化任务，**不适合**单步小任务

### 10. 与 wiki 知识的连接

**强连接**：
- [[anthropic-skill-creator]] — 这次新建的 entity 页，专门记 skill-creator 元技能
- [[anthropics-skills-repo]] — 这次新建的 entity 页，repo 本身
- [[agent-skills-standard]] — 这个 repo 是该标准的 canonical implementation
- [[skillify-meta-skill]] — 同思想两种实现，互补不竞争
- [[trigger-evals]] — `skill-creator` 的 20 query eval 是 trigger-evals 的官方实施版
- [[source-mattpocock-skills-repo]] — Matt 的 5-skill workflow 和 Anthropic 的 4 改进原则精神一致
- [[source-khairallah-claude-skills-automate-workflow]] — Khairallah 的 Three-Question/Three-Scenario Test 是 **简化版** Anthropic 流程

**强化已有概念**：
- 强化 [[agent-skills-standard]]：补全 metadata/body/resources 的具体词数预算 + `references/` 域变体组织模式
- 强化 [[skillify-meta-skill]]：Anthropic 官方实现给 Garry 的 Skillify Manifesto 提供"原厂参考实现"
- 强化 [[trigger-evals]]：20 query / 60-40 / 3× / 5 iter 是该 pattern 的 production-grade 实施

**挑战/补充**：
- 轻微挑战 [[agent-skills-standard]] 的"front-load the key use case"——Anthropic 说要 **pushy**（更广），不只是 front-load
- 补充 [[trigger-evals]]：trigger eval queries 必须 realistic，给了 good vs bad 对照例子

**扩展方向**：
- ✅ 下一个目标：anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- ⚪ 可选：agentskills.io 开放标准 / support.claude.com 三篇 user-facing 文档 / 单独 deep-read `skills/mcp-builder/SKILL.md`

### 11. 对用户（vfan）的启示

**短期（本周）：**
1. 审视现有 6 个 `.claude/commands/`，用 4 大改进原则做一次审计（ALWAYS/NEVER 硬规则？重复 bash 脚本？description 够不够 pushy？）
2. 给 `/ingest` 写 20 个 trigger eval queries，看哪些 route 错了
3. 回填 [[agent-skills-standard]]：把 pushy description + 3 层进度披露具体词数补进 wiki

**中期（接下来 2-4 周）：**
1. 把 LoreAI glossary entry generator 做成正经 skill：bundled `scripts/check_term_exists.py` + SKILL.md + `assets/template.md` + `evals/` 跑 train/test
2. 同样做 blog2video chapter generator
3. 写一篇中文文章："用 ML 思路工程化你的 AI 工作流" —— underexplored 中文方向

**长期（如方向被验证）：**
1. 建立自己的 skill library，参考 Anthropic 的 3-plugin 结构：`loreai-skills` / `blog2video-skills` / `content-marketing-skills`
2. 用 `.claude-plugin/marketplace.json` 做成 Claude Code marketplace；README 引流 LoreAI
3. **bilingual 套利的具体玩法**：你读了 Anthropic 原文 + Garry + Matt + Khairallah 4 个版本，能写出别人写不出的中文 AI 内容

### 12. 一句话总结

**"Skill 是 prompt 的 ML 化——Anthropic 教你用 train/test/iteration 把 LLM 工作流变成可优化的工程产物。"**

---

## Pages Created
- [[anthropics-skills-repo]] — entity 页，repo 本身
- [[anthropic-skill-creator]] — entity 页，skill-creator 元技能
- [[source-anthropics-skills-repo]] (this page) — 完整 12-section 解读

## Pages Updated
- [[agent-skills-standard]] — 补充 pushy description + 3-tier 词数 + 文件夹 anatomy
- [[skillify-meta-skill]] — 加 Anthropic 官方实现对比
- [[trigger-evals]] — 加 Anthropic 20-query / 60-40 / 3× / 5-iter 实施版
- [[anthropic]] — 注册 anthropics/skills repo + skill-creator
- [[index]], [[log]]

## Connections
- Related: [[anthropics-skills-repo]], [[anthropic-skill-creator]], [[anthropic]], [[agent-skills-standard]], [[skillify-meta-skill]], [[trigger-evals]], [[skill-as-method-call]], [[thin-harness-fat-skills]], [[source-mattpocock-skills-repo]], [[source-khairallah-claude-skills-automate-workflow]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-22 | raw/2026-05-22-repo-anthropics-skills.md | Initial creation — full 12-section study guide |
