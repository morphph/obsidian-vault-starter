# 仓库架构审查 — findings

> 审查日期：2026-08-04 · 基线 commit：`4b88cb9` · 读取范围：白名单（未读 `raw/**`、未读 `wiki/*.md`（`index.md`/`log.md` 除外）、未进 `*/references/vendor/**`）
> 每条结论带 `file:line` 证据。无法从白名单内证实的，显式标注「不确定」。

---

## TL;DR

`.agents/` 不是 `.claude/` 的镜像，而是一条**更新、且是唯一在用**的内容流水线——2026-07-29 之后每一次 `/research` 产出的都是 `.agents/` 形状的产物（`source-ledger.md`），而 Claude Code 只加载 `.claude/`，所以你今天敲 `/research` 拿到的是 2026-07-17 冻结的旧版，`/topic` 根本不可达。三个根级注册表（CLAUDE.md、README.md、AGENTS.md）没有任何一个提到 `.agents/` 的存在，README.md:143-148 甚至明确声称它已被删除。此外 Hermes 对外契约的三个动词零测试，pyproject 声明的三个依赖零使用、真正需要的 `anthropic` 未声明。

---

## 1. 双 harness 现状

### 1.1 分歧逐项清点

`.claude/skills/` 3 个技能，`.agents/skills/` 6 个。逐项：

| 技能 | `.claude/` | `.agents/` | 关系 | 判定 |
|---|---|---|---|---|
| `excalidraw-diagram` | 577 行 | 577 行 | 4 行机械替换差异 | **坏** |
| `ingest` | 192 行 | 192 行 | 4 行机械替换差异 | **坏** |
| `research` | 339 行 | 222 行 | 完全重写，产物契约不同 | **有意** |
| `draft` | `.claude/commands/draft.md`（186 行） | `.agents/skills/draft/`（151 行 + 3 references） | 独立演化 | **有意** |
| `topic` | 不存在 | 176 行 + 4 references | 新增阶段 | **有意** |
| `source-command-lint` | `.claude/commands/lint.md`（68 行） | 74 行 | 自动迁移包装 | **坏** |

**（a）机械镜像（坏）** — `excalidraw-diagram` 和 `ingest` 是 find-replace 产物，替换规则是 `Claude→Codex` / `CLAUDE.md→AGENTS.md` / `.claude→.Codex`：

- `.agents/skills/excalidraw-diagram/SKILL.md:464`、`:479`、`:531` — 三处 `cd .Codex/skills/excalidraw-diagram/references`。`.Codex/` 目录不存在（`ls` 已确认），这三处是**运行时命令，会直接失败**。渲染器实际躺在 `.agents/skills/excalidraw-diagram/references/render_excalidraw.py`。
- `.agents/skills/excalidraw-diagram/SKILL.md:210` — "Codex has a ~32,000 token output limit"。这是把 Claude Code 的输出上限贴到了 Codex 头上，数字未经核实（不确定 Codex 的真实上限）。
- `.agents/skills/ingest/SKILL.md:71` — "Try **Codex for Chrome**… use the `Codex-in-chrome` MCP tools"。不存在这个 MCP server；真实名字是 `claude-in-chrome`。
- `.agents/skills/ingest/SKILL.md:133` — 读 `.Codex/commands/learn-note.md`，路径不存在。而且 `.agents/` 下**根本没有 `commands/` 目录**（`ls .agents/` 只有 `skills/`），所以即便改成 `.agents/` 也修不好——这个文件只在 `.claude/commands/learn-note.md` 存在。
- `.agents/skills/source-command-lint/SKILL.md:43` — 检查项写着"every row has a matching `.Codex/commands/{name}.md` or `.Codex/skills/{name}/SKILL.md`"。一个用来查漂移的 linter，自己指向不存在的路径。

> 讽刺点：README.md:145-148 的 v0.6 changelog 写的是「**Removed the Codex mirror layer**: deleted `AGENTS.md` (find-replace-damaged mirror pointing at nonexistent `.Codex/` paths), `.codex/`, and `.agents/`」。同一类损坏在 2026-07-22（`e72001a chore: prepare project for Codex`）和 2026-07-23（`d882fa2`）被原样重新引入，且 changelog 从未更新。

**（b）真实的前向设计（有意）** — `research` / `topic` / `draft` 三件套是 2026-07-29 一天内 7 个 commit 做出来的一次流水线重构，不是镜像：

- `.claude/skills/research/SKILL.md` 是**单阶段**：8 步，`mode:report` / `mode:guide` 双模，末尾 Gate-1 角度闸，产 `research-plan.md` + `report.md` + `ingest-candidates.md` + `meta.json`，角度选定后再跑 outline 细化模式（`SKILL.md:186-232`、`:313`）。
- `.agents/skills/research/SKILL.md` 是**三阶段中的第一段**：7 步，只负责"理解话题"，明确不产角度，产物多了 `source-ledger.md`（claim 级证据台账），角度决策被拆给 `/topic`（`.agents/skills/research/SKILL.md:49-66`、`:215`）。
- `.agents/skills/topic/SKILL.md` 是新增能力：market-scan → topic-options → 人选角度 → topic-brief + outline。`.claude/` 侧没有对应物。
- `.agents/skills/{draft,research,topic}/agents/openai.yaml` 存在（各 4 行 `interface:` 声明），`excalidraw-diagram` / `ingest` / `source-command-lint` 没有。这条线把「哪三个是认真写的」标得很清楚——只有新三件套走了 agentskills.io 的 interface 契约。

**（c）已经落地的事实：`.agents/` 是在用的那一套。** 这是本节最重要的一条，证据来自 `research/` 目录的实际产物形状：

| 工作区 | 特征产物 | 属于 | git 日期 |
|---|---|---|---|
| `loop-engineering/` | `meta.json` | `.claude` | 2026-06-27 |
| `best-practices-for-claude-fable-5/` | `meta.json` + `outline.md` | `.claude` | 2026-07-10 |
| `cost-effective-fable-harness/` | `meta.json` | `.claude` | 2026-07-13 |
| `codex/` | `facts.md` + overview/advanced | `.claude` (`mode:guide`) | 2026-07-17 |
| `graph-engineering/` | `source-ledger.md` | **`.agents`** | 2026-07-29 |
| `graph-engineering-rerun-1/` | `source-ledger.md` | **`.agents`** | 2026-07-29 |
| `claude-opus-5-best-practice/` | `source-ledger.md` | **`.agents`** | 2026-07-29 |
| `claude-opus-5-best-practice-rerun-1/` | `source-ledger.md` + `reference-comparison.md` | **`.agents`** | 2026-07-29 |

`source-ledger.md` 只由 `.agents/skills/research/SKILL.md:58-61` 定义；`meta.json` 只由 `.claude/skills/research/SKILL.md:232` 定义。**2026-07-17 之后 `.claude/` 的 research 没有产出过任何一个工作区。**

### 1.2 后果：今天跑 `/research` 拿到的不是你上次用的那套

Claude Code 只加载 `.claude/`（commands + skills + rules）；`.agents/skills/` 是 agentskills.io / Codex 的约定路径。本次会话的技能清单可直接观测到这一点（运行时证据，非 file:line）：清单里的 `research` 描述是 `.claude/skills/research/SKILL.md:3` 那一版（Gate-1 / mode:guide），`draft` 描述是 `.claude/commands/draft.md:3` 那一版，**没有 `topic`，没有 `source-command-lint`**。

所以当前状态是：
- 你最近 4 次调研的方法论（证据台账 + 对抗性检验 + 角度外置）在 Claude Code 里不可达。
- `research/README.md:26-27` 指导读者用 `/topic research/<slug>/`，这个命令在 Claude Code 下不存在。
- `research/README.md:44` 明写「当前契约以 `.agents/skills/research/SKILL.md` 和其 `references/` 为准」，而 `CLAUDE.md:18` 描述的仍是 `.claude/` 的 §1-7 报告形状。两个根级文档互相矛盾。

### 1.3 可选目标态

**选项 A — 合并回 `.claude/`，弃用 `.agents/`**

把 `.agents/{research,topic,draft}` 移植进 `.claude/skills/`（`topic` 是新增目录，`research` 覆盖，`draft` 从 `commands/` 升级为 skill 文件夹），删除 `.agents/`。

- 代价：要修 `.agents/skills/*/SKILL.md` 里 `AGENTS.md` → `CLAUDE.md` 的引用（`ingest:8,121`、`draft:8`、`research:8`、`topic:8`）；要在 `.claude/` 侧重建 `.claude/rules/` 与新技能的配合；`research/README.md:44` 要改指向。`.claude/skills/research/SKILL.md` 的 `mode:guide`（产出了 `research/codex/`）在 `.agents/` 版里**没有对应物**，直接覆盖会丢掉这个模式——需要先决定是保留、移植还是承认它已被 `/topic` 取代。
- 不可逆点：无。所有内容都在 git 里，`.agents/` 删除后可 `git revert`。
- 前提：你不再用 Codex。

**选项 B — 以 `.agents/` 为准，`.claude/` 降级为薄壳**

`.claude/skills/` 只留 Claude-Code-专属的东西（`excalidraw-diagram` 因为 `.claude/commands/visualize.md:6` 依赖它），research/topic/draft 全部指向 `.agents/`。

- 代价：Claude Code **不会**自动加载 `.agents/skills/`——需要在 `.claude/` 侧放转发桩（每个技能一个 SKILL.md，正文写"读 `.agents/skills/<name>/SKILL.md` 并照做"），否则 Claude Code 侧完全失能。转发桩本身是新的漂移面。`.agents/` 缺 `rules/`（`ls .agents/` 只有 `skills/`），所以 `.claude/rules/wiki-page-format.md:2` 和 `log-format.md:2` 的 `paths:` 自动加载在 Codex 下**完全不生效**——wiki 页格式与 log 格式在 Codex 侧只是口头约定。要么接受，要么在 `.agents/skills/ingest/SKILL.md` 里内联这两份格式。
- 不可逆点：无（同上）。
- 前提：你主力在 Codex。

**选项 C — 生成式镜像（单源 + 构建脚本）**

一棵源树（比如 `skills/`），一个脚本按 harness 生成 `.claude/` 和 `.agents/`，替换表显式声明（`CLAUDE.md`↔`AGENTS.md`、`.claude`↔`.agents`、`claude-in-chrome` 保持不变等）。

- 代价：要写并维护生成脚本 + 校验（`.Codex` 这类幽灵路径应当在生成时报错）；`tests/` 里要加一个「生成产物与源一致」的检查，否则手改镜像会静默漂移，就是现在这个状态。前期一次性成本明显高于 A/B。
- 不可逆点：**这是唯一有不可逆成分的选项**——一旦 `.claude/` 与 `.agents/` 变成构建产物，就不能再直接手改它们（手改会被下次生成覆盖）。要么把它们加进 `.gitignore`（会破坏 Claude Code 在新克隆里开箱可用），要么保持提交并接受"提交产物"的约定。
- 前提：两边都要长期用。

> 我不替你选：这取决于你是否还在用 Codex。可判定的事实是——**目前只有 `.agents/` 里的方法论在产出真实成果，而只有 `.claude/` 在被 Claude Code 加载**。这个交叉是当前架构最大的单点问题。

---

## 2. 注册表 vs 磁盘

### 2.1 CLAUDE.md

| 位置 | 声明 | 磁盘事实 | 判定 |
|---|---|---|---|
| `CLAUDE.md:57` | "Eight slash commands" | 表格 8 行；磁盘 `.claude/commands/` **7 个文件** + `.claude/skills/` 3 个 | 数字对得上表格，对不上磁盘 |
| `CLAUDE.md:59-68` 表格 | 8 行：ingest / ingest-anthropic-daily / research / query / lint / visualize / draft / learn | `.claude/commands/learn-note.md` **无对应行** | **漏登记** |
| `CLAUDE.md:57` | 重量级 = `/ingest`、`/research` | `.claude/skills/` = ingest、research、excalidraw-diagram | 一致 |
| `CLAUDE.md:72-76` Skills 表 | excalidraw-diagram + obsidian:obsidian-markdown + obsidian:defuddle | `.claude/skills/excalidraw-diagram/` 存在；两个 `obsidian:*` 来自插件，白名单内无法核实 | **不确定**（插件侧） |
| `CLAUDE.md:9-15` | "Five layers"：raw / wiki / drafts / learn / references + CLAUDE.md | 列了 5 个目录 + CLAUDE.md，共 6 个 bullet；`learn/` 与 `references/` 都在，`archive/`、`events/`、`visuals/`、`prompts/` 未列入分层模型 | 计数含糊但不算错 |
| `CLAUDE.md:18` | research 产物 = research-plan + report(§1-7) + ingest-candidates | 最近 4 个工作区产的是 research-plan + report + **source-ledger** + ingest-candidates | **过期**（见 §1.2） |
| 全文 | 无任何一处提到 `.agents/` | 6 个技能、7 个 commit、当前唯一在用的 research 流水线 | **重大缺失** |

### 2.2 README.md

| 位置 | 声明 | 磁盘事实 | 判定 |
|---|---|---|---|
| `README.md:110` | `.claude/commands/` = query, lint, visualize, draft, learn, ingest-anthropic-daily（6 个） | 7 个文件，缺 `learn-note.md` | **漏登记** |
| `README.md:111` | `.claude/skills/` = ingest, research + excalidraw-diagram | 一致 | ✅ |
| `README.md:60-69` Commands 表 | 8 行，与 CLAUDE.md 表一致 | 同上，`learn-note` 缺席 | **漏登记** |
| `README.md:36-49` 架构图 | `research/<slug>/ (report + outline + ingest-candidates)` | 最近工作区无 `outline.md`，有 `source-ledger.md` | **过期** |
| `README.md:145-148` | v0.6 声称删除了 `.agents/`、`.codex/`、`AGENTS.md`（"find-replace-damaged mirror pointing at nonexistent `.Codex/` paths"） | `.agents/`（6 技能）与 `AGENTS.md`（55 行）都在，且 `.Codex/` 幽灵引用重现于 4 处 | **与事实相反** |
| `README.md:118-232` Changelog | 最新条目 v0.8（2026-07-17） | 此后有 15 个 commit，含整条 Codex 迁移 + research 重构 | **停更**（`.claude/commands/lint.md:41` 恰好把这条列为检查项） |
| `README.md:181-182` | CLI 动词 5 个：list-ingests / export-source / mark-routed / record-ingest / backfill-from-log | `scripts/obsidian_content.py` 有 **6 个**（多 `export-learn`，`:562-569`） | **漏登记** |
| `README.md:103-104` | `research/<topic-slug>/` 含 `meta.json` | 4 个新工作区无 `meta.json` | **过期** |
| `README.md:112` | `prompts/` = skill-audit, research dispatch, … | `prompts/` 实有 4 个文件，含 `fable5-pipeline-audit-prompt.md`、`research-prompt.md` | 模糊但不算错 |
| 全文 | 无 `.agents/` | 同上 | **重大缺失** |

### 2.3 AGENTS.md

| 位置 | 声明 | 磁盘事实 | 判定 |
|---|---|---|---|
| `AGENTS.md:21` | "`.claude/` — slash commands (`/draft`, `/learn`, `/ingest`, `/query`, `/visualize`, …), `rules/`, `skills/`" | `/ingest` 是 skill 不是 command；未提 `/lint`、`/learn-note`、`/ingest-anthropic-daily` | 粗略但方向对 |
| `AGENTS.md:13` | "`learn/`, `references/`, `research/`" 三者并列为 vault 内容 | `CLAUDE.md:17` 明确 `research/` 是**非 vault**、Tier-4 | **矛盾** |
| `AGENTS.md:16` | `logs/` 未在本 clone 落盘（sparse-checkout, ~91 MB） | ✅ 已核实：`git ls-files logs/` = 1 个路径 `logs/claude-remote.log`，blob 89.5 MB，`git sparse-checkout list` 含 `!/logs/` | ✅ |
| `AGENTS.md:19` | `scripts/` = ingest_url / learn_note / content_agent / obsidian_content + `*-claude-remote.sh` | ✅ 完全一致 | ✅ |
| `AGENTS.md:24` | Python ≥ 3.12；依赖 claude-agent-sdk / python-dotenv / tzdata | 依赖声明属实（`pyproject.toml:6-10`），但三者在代码里**零引用**（见 §4.3） | **误导** |
| `AGENTS.md:28` | Lint：`ruff check` | `ruff` 在 `.venv/bin/` 和 PATH 上都不存在（已核实），且未在 `pyproject.toml` 声明为依赖 | **不可执行** |
| `AGENTS.md:29-33` | 两个离线测试 | ✅ 已跑：`test_ingest_url.py` 10 passed、`test_learn_note.py` 13 passed | ✅ |
| 全文 | 无 `.agents/`——这份**给 Codex 看的**文档没提 Codex 的技能树 | 6 个技能 | **重大缺失** |

### 2.4 交叉矛盾汇总

1. `research/README.md:44`（"以 `.agents/` 为准"）vs `CLAUDE.md:18` + `README.md:36-49`（描述 `.claude/` 形状）。
2. `research/README.md:26-27`（用 `/topic`）vs Claude Code 无 `/topic`。
3. `AGENTS.md:13`（research 是 vault 层）vs `CLAUDE.md:17,43`（非 vault、Tier-4）。
4. `README.md:145-148`（`.agents/` 已删）vs `.agents/` 是当前唯一在用的流水线。
5. `.claude/commands/lint.md:36-41` 与 `.agents/skills/source-command-lint/SKILL.md:39-44` 是同一份 docs-drift 检查器的两个副本，各自指向 CLAUDE.md/`.claude` 和 AGENTS.md/`.Codex`——**其中一份指向的路径不存在**，而以上 4 条矛盾正是它们本该抓到的。

---

## 3. 分层模型是否可执行

**真正的机制只有一个半。**

**（1）`.claude/rules/` 的 `paths:` glob — 唯一的自动机制。**
- `.claude/rules/wiki-page-format.md:2` → `paths: ["wiki/**"]`
- `.claude/rules/log-format.md:2` → `paths: ["wiki/log.md"]`

这是全仓唯一由 harness 自动注入的约束。局限：(a) 只在 `.claude/` 下存在，`.agents/` 没有 `rules/` 目录，所以 Codex 侧零覆盖；(b) 它注入的是**格式模板**，不是边界——它不能阻止写入 `raw/`，也不检查 `index.md` 是否同步。

**（2）`scripts/obsidian_content.py` 的仓内路径校验 — 半个机制。**
`:169-172` 强制 `--source` 必须落在 repo 内，`:249` 只读不写 `raw/`。这是唯一被代码强制的不变量，但作用域只覆盖 CLI 这一条路径。

**（3）其余全是口头约定。** `CLAUDE.md:35-43` 的 8 条 NEVER 里：

| NEVER | 有无机制 | 实测 |
|---|---|---|
| 不改 `raw/` | 无（仅 prompt） | 未测 |
| `wiki/` 不建子目录 | 无 | 磁盘上确实是平的（211 个 `.md`） |
| 不建页而不更新 `index.md` | 无 | **已违反：7 个页面不在 index 里** |
| 每条 claim 可溯源到 `raw/` | 无 | 白名单内无法核实（**不确定**） |
| 不 link 泛词 | 无 | 未测 |
| 不自动 ingest research 候选 | 无 | 未测 |
| 不自动 ingest `references/` | 无 | `references/` 目前只有 README，无条目（`references/README.md:54`） |
| research 不当 Tier-1 | 部分：`research/README.md:38-39` 明说排除配置在 **gbrain 侧**、本仓无法保证 | 结构性外部依赖 |

**索引漂移的具体清单**（磁盘 211 页 vs index 208 条唯一条目，逐项 diff）：

不在 `wiki/index.md` 里的 7 个页面：
`Dispatch.md`、`Tracker.md`、`source-building-effective-agents.md`、`source-cost-effective-harnesses-with-fable.md`、`source-fable-finding-your-unknowns.md`、`source-founder-mode.md`、`source-having-kids.md`

其中 5 个 `source-*` 页的成因是**设计内建的**，不是疏忽：`.claude/commands/learn-note.md:4` 的「Headless 铁律」明确写着「只写本作业书列出的文件——**不更新 index/log**、不调 record-ingest」，而 `:9` 的示例正是 `raw/2026-07-05-founder-mode.md founder-mode` → `wiki/source-founder-mode.md`。也就是说 `/learn-note`（由 `scripts/learn_note.py:166` 无头 spawn）**每跑一次就结构性地制造一次 `CLAUDE.md:38` 违规**，且没有任何补偿步骤。

`Dispatch.md` / `Tracker.md` 是首字母大写，违反 `CLAUDE.md:46` 的 kebab-case 约定；来源**不确定**（未读其内容）。

另有 `wiki/index.md:34-37` 存在**完全重复的两条**：`[[george-nurijanian]]`（34 与 36 行）、`[[pm-os]]`（35 与 37 行）——同一段文字连续贴了两遍。

`/lint`（`.claude/commands/lint.md:28`）确实把 index drift 列为检查项，但它是**人工触发**的；`wiki/log.md` 最后一条是 2026-07-15 的 ingest，之后无 lint 记录——即三周未跑。

**结论**：分层模型在 `.claude/` 下有 1 个自动机制（格式模板注入）+ 1 个人工闸（`/lint`）+ 1 个代码级路径校验（CLI）。边界本身（谁能写哪层）**没有任何执行机制**，全靠 prompt 遵守；而 `/learn-note` 证明只要有一条绕过主流程的写入路径，约定就会被静默破坏。

---

## 4. Python 层

`scripts/` 4 个模块 1247 行 + 3 个 shell + `tests/` 425 行。

### 4.1 契约面风险 —— 核心结论

`scripts/obsidian_content.py`（593 行）暴露 6 个动词。测试覆盖如下：

| 动词 | 定义 | 直接测试 | 间接测试 | Hermes 是否调用 |
|---|---|---|---|---|
| `record-ingest` | `:151-197` | 无 | ✅ 有（`scripts/ingest_url.py:134` 以子进程调用，被 `tests/test_ingest_url.py:104-156` 覆盖到事件写入与幂等） | 否（`/ingest` 内部用） |
| `export-learn` | `:278-351` | ✅ 3 个（`tests/test_learn_note.py:193-219`） | — | 否（b2v 用） |
| `list-ingests` | `:202-224` | **无** | **无** | ✅ **是**（`README.md:78`） |
| `export-source` | `:229-273` | **无** | **无** | ✅ **是**（`README.md:79`） |
| `mark-routed` | `:356-388` | **无** | **无** | ✅ **是**（`README.md:80`） |
| `backfill-from-log` | `:467-523` | **无** | **无** | 否（一次性 seed） |

**风险判定：覆盖率恰好与风险倒挂。** 有测试的两个动词是内部消费者（`/ingest`、blog2video）；**Hermes 契约面的三个动词全部零测试**。具体暴露的面：

- **状态折叠（`fold_state`，`:91-130`）零直接测试。** `list-ingests` 的全部正确性建立在它之上——`routed` 先于 `ingest` 到达时会建 stub（`:122-125`），`ingest` 记录会 `update()` 覆盖但用 `setdefault` 保留 routed 状态（`:115-118`）。这个「重放顺序无关」的不变量是 `docs/obsidian-content-cli.md:114-121` 明确承诺给 Hermes 的，却没有一个测试钉住它。真实事件日志 `events/ingest-events.jsonl` 已 27 KB，回归只会靠人眼。
- **过滤/分页语义零测试。** `:212-217` 的 `--since` 是字符串比较（`(r.get("ts") or "") >= args.since`）。传 `--since 2026-06-01` 与 ISO 时间戳 `2026-06-01T00:00:00+00:00` 做字典序比较——这个例子恰好能工作，但语义脆弱；`docs/obsidian-content-cli.md:131` 就是这么示范的。`--limit` + `--newest` 的取头/取尾（`:217`）同样无覆盖。
- **`export-source` 的写盘分支零测试。** `:259-269` 的 `--out` 相对路径解析到 repo 根、`--dry-run` 只报 `would_write_to`——这是 Hermes 落盘的实际路径，也是最容易被后续重构改坏的地方。
- **契约版本没有守卫。** `CONTRACT_VERSION = "1.0"`（`:31`）与 `docs/obsidian-content-cli.md:36` 承诺「破坏性变更时 bump」，但没有任何测试断言 envelope 的键集合（`contract_version/ok/verb/artifacts/warnings/errors`，`:138-145`）。删掉或改名一个键，测试全绿。

**缓解因素（不要高估风险）**：纯 stdlib、纯本地文件 IO、append-only、无网络无 LLM（`:14-16` 的设计约束在代码里是真的成立的），失败模式基本是「返回 `ok:false`」而非静默损坏；且 `emit()` 保证 exit∈{0,1} 时永远有合法 JSON。所以风险的形状是**回归风险**（改动时无人发现语义变了），不是运行时爆炸风险。补 3 个动词各 2-3 个测试就能封住，成本很低——测试骨架已经现成（`tests/test_learn_note.py:104-108` 的 `run_oc()` 直接可复用）。

### 4.2 文档 vs 代码

- `docs/obsidian-content-cli.md:49-112` 只记了 5 个动词，**`export-learn` 完全缺席**——而它写盘（`:343-349`，含 `shutil.rmtree(dest)`）、跨仓交付给 blog2video，是最需要写清楚契约的一个。
- `bin/obsidian-content:9-16` 额外路由了两个动词 `ingest-url` → `scripts/ingest_url.py`、`learn` → `scripts/learn_note.py`。这两个**不在** `obsidian_content.py` 的 argparse 里，所以 `bin/obsidian-content --help` 不会列出它们，`docs/obsidian-content-cli.md` 也没写。`README.md:108` 把 `bin/obsidian-content` 描述为「thin shim → scripts/obsidian_content.py」，实际上它是个三路分发器。

### 4.3 依赖声明

`pyproject.toml:6-10` 声明 `claude-agent-sdk>=0.1.29`、`python-dotenv>=1.0.0`、`tzdata>=2024.1`。全仓 `scripts/` + `tests/` + `bin/` 对这三个包的引用数：**0**（已 grep 核实，含 `zoneinfo`）。

而唯一的第三方 import 是 `scripts/content_agent.py:23` 的 `from anthropic import Anthropic`——`anthropic` **未在 pyproject 声明**。当前能跑只是因为宿主 python3 恰好装了 0.58.2。

即：`pip install -e .` 装的三个包一个都用不到，真正需要的那个装不上。

### 4.4 环境不一致

- `pyproject.toml:5` 要求 `>=3.12`；`scripts/obsidian_content.py:18` 文档说「runs on Python 3.11+」；当前 `python3` 是 **3.11.0**。测试在 3.11 下全绿（23 passed），所以 3.12 的门槛是名义上的。`CODEX_MIGRATION.md:50` 已经记过这个不一致，未修。
- `AGENTS.md:28` 的 `ruff check` 无法执行（未安装、未声明）。`CODEX_MIGRATION.md:46` 记录当时有「7 个既存 style findings」，现在无法复核。

---

## 5. 死配置与卫生

**失效引用**

| 位置 | 引用 | 状态 |
|---|---|---|
| `.agents/skills/excalidraw-diagram/SKILL.md:464,479,531` | `cd .Codex/skills/…` | 目录不存在，**运行时命令会失败** |
| `.agents/skills/ingest/SKILL.md:133` | `.Codex/commands/learn-note.md` | 双重失效：`.Codex/` 不存在，且 `.agents/` 下无 `commands/` |
| `.agents/skills/source-command-lint/SKILL.md:43` | `.Codex/commands/`、`.Codex/skills/` | linter 自身的检查基准指向虚空 |
| `.agents/skills/ingest/SKILL.md:71` | `Codex-in-chrome` MCP tools | 无此 server（真实名 `claude-in-chrome`） |
| `.claude/commands/ingest-anthropic-daily.md:14,27,127` | `.claude/state/anthropic-daily-last-run.json` | `.claude/state/` 不存在。`:27` 写了「create dir if missing」所以是软失效——但意味着这条命令**从未成功跑完过一次**（否则目录会在），或跑过但状态文件未提交（**不确定**，`.gitignore` 只忽略 `.claude/settings.local.json`，不忽略 `state/`） |

**重复资产**

- 26 MB 字体 vendor 在两棵树各一份（`.claude/…/references/vendor`、`.agents/…/references/vendor`），`diff -rq` 确认**逐字节相同**，各 236 个文件被 git 跟踪。
  - 磁盘成本：52 MB（2×）。
  - **git 成本：≈1×**——内容相同 ⇒ 同一批 blob，只多了 tree 条目。所以「26 MB × 2 进了历史」这个直觉是错的，实际历史膨胀可忽略；`.git` 总共 38 MB。真正的成本是**工作树体积 + 每次 glob/搜索被扫两遍**。
- `.claude/commands/lint.md` 与 `.agents/skills/source-command-lint/SKILL.md` 是同一份 68 行 workflow 的两个副本，已开始分歧（后者的 `:43` 指向 `.Codex`）。
- `.claude/skills/excalidraw-diagram/` 与 `.agents/…` 除 SKILL.md 4 行外全部相同，包括 `README.md`、`render_excalidraw.py`、`render_template.html`、golden fixture。

**大文件**

- `logs/claude-remote.log` 作为**单个 89.5 MB blob 永久存在于 git 历史中**（`git cat-file -s` 实测）。sparse-checkout（`!/logs/`）只是让它不落盘，`git clone` 仍要传输。`.gitignore` 全 22 行**不包含 `logs/`**，所以新产生的日志随时可能再次被提交。这是全仓最大的单点体积问题，也是唯一有**不可逆成分**的卫生问题（清除需要改写历史）。

**未被任何入口触及的文件**

| 文件 | 状态 | 依据 |
|---|---|---|
| `scripts/content_agent.py`（280 行） | **孤立**。全仓唯一提及它的地方是 `AGENTS.md:19` 的目录清单。无测试、无 shell 入口、`bin/obsidian-content` 不路由它，功能（Research→Outline→Write）与 `/research`+`/draft` 完全重叠。依赖 `anthropic` 未声明。 | grep 全仓 |
| `.claude/skills/.gitkeep` | 残留占位符（该目录已有 3 个真实子目录），仍被 git 跟踪 | `git ls-files` |
| `.claude/commands/learn-note.md` | **活跃但零注册**。被 `scripts/learn_note.py:166` 以 `claude -p "/learn-note …"` 无头调用，是唯一没有 YAML frontmatter 的 command 文件（`:1` 直接是 `#` 标题）。不在 CLAUDE.md、README.md、AGENTS.md 任何一张表里。 | §2 |
| `research/_reference/`（2 文件） | 由 `research/README.md:41-44` 明确降级为「仅用于审计旧产物，不定义当前结构」。可归档。 | — |
| `prompts/`（4 文件） | `README.md:112` 提及但无命令/脚本引用。**不确定**是否仍在手工使用。 | grep |
| `docs/obsidian-remote-control-setup-report.md`（220 行）、`docs/claude-remote-ops.md`（136 行） | 描述一台 VPS（`/home/ubuntu/…`）上的远程 Claude 部署，配套 3 个 `*-claude-remote.sh`。是否仍在运行**不确定**（白名单内无法核实）。若已停用，它们和那个 89.5 MB 日志是同一件事的两半。 | — |

---

## 建议动作

按依赖关系排序。「依赖哪个决策」= 该动作必须等哪个判断落定。

| # | 动作 | 影响面 | 可逆性 | 依赖哪个决策 |
|---|---|---|---|---|
| 1 | **决定 harness 目标态（A/B/C）** | 全仓 | — | **你是否还在用 Codex**（前置于 2、3、4、6） |
| 2 | 按目标态收敛 `research`/`topic`/`draft`：或移植进 `.claude/`（A），或在 `.claude/` 加转发桩（B），或建生成脚本（C） | `.claude/skills/`、`.agents/skills/` | 完全可逆（A/B）；C 引入「不可手改镜像」的单向约定 | #1 |
| 3 | 修 4 处 `.Codex/` 幽灵引用（`excalidraw:464,479,531`、`ingest:133`、`source-command-lint:43`）；`ingest:71` 的 `Codex-in-chrome` → `claude-in-chrome` | `.agents/` 5 个文件 | 完全可逆 | #1（若选 A 则整棵删除，此项作废） |
| 4 | 决定 `.claude/skills/research` 的 `mode:guide` 去留（`.agents/` 侧无对应物，`research/codex/` 是其唯一产物） | `research` 技能 | 完全可逆（git 留底） | #1 + 你是否还要产「常青指南」 |
| 5 | **补 Hermes 三动词测试**（`list-ingests`/`export-source`/`mark-routed`）+ 一个 envelope 键集合断言 + `fold_state` 乱序重放断言 | `tests/`（新增，不改生产代码） | 完全可逆 | 无依赖，**可立即做**；`run_oc()` 骨架现成 |
| 6 | 三张注册表对齐磁盘：补 `learn-note` 行、补 `.agents/` 章节、修 `README.md:145-148` 的反事实 changelog、`README.md:181` 补 `export-learn`、`AGENTS.md:13` 修 research 层级、`research/README.md:44` 与 `CLAUDE.md:18` 二选一 | 4 个根级 md | 完全可逆 | #1（`.agents/` 怎么写取决于目标态） |
| 7 | `docs/obsidian-content-cli.md` 补 `export-learn`；`README.md:108` 更正 `bin/obsidian-content` 为三路分发器 | 2 个 doc | 完全可逆 | 无 |
| 8 | `pyproject.toml`：删 3 个未使用依赖，加 `anthropic`（或连同 #12 一起删 `content_agent.py`）；加 `ruff` 到 dev 依赖或从 `AGENTS.md:28` 移除该指令 | `pyproject.toml`、`AGENTS.md` | 完全可逆 | #12 |
| 9 | 修 `wiki/index.md:34-37` 的两条重复条目；补录 7 个缺席页面（先看 `Dispatch.md`/`Tracker.md` 是否该留） | `wiki/index.md` | 完全可逆 | 无 |
| 10 | 给 `/learn-note` 加索引补偿：或在 `learn_note.py` 落盘后追加 index 条目，或在 `.claude/commands/learn-note.md:4` 放宽铁律允许写 index | `scripts/learn_note.py` 或该 command | 完全可逆 | 无（这是 §3 里唯一的结构性违规源） |
| 11 | `.gitignore` 加 `logs/`；决定是否改写历史移除 89.5 MB blob | 全仓 clone 体积 | **改写历史不可逆**（需 force-push，所有克隆失效）；只加 `.gitignore` 完全可逆 | 你是否还在跑 VPS remote（同 #13） |
| 12 | 删除或归档 `scripts/content_agent.py`（孤立、功能重叠、依赖未声明） | `scripts/` | 完全可逆（git 留底） | 你是否还打算用 Managed Agents 那条路 |
| 13 | 确认 VPS remote 是否仍在运行；若否，归档 `docs/{claude-remote-ops,obsidian-remote-control-setup-report}.md` + 3 个 `*-claude-remote.sh` | `docs/`、`scripts/` | 完全可逆 | 需要你回答（白名单内无法核实） |
| 14 | vendor 去重（若选 C 或 B，只留一棵） | 工作树 -26 MB；git 历史无变化 | 完全可逆 | #1 |
| 15 | 删 `.claude/skills/.gitkeep`；归档 `research/_reference/` | 2 处 | 完全可逆 | 无 |

**若只做三件事**：#1（定 harness 方向，它锁着 6 个下游动作）、#5（Hermes 契约测试，无依赖、成本最低、风险最实）、#10（堵住唯一在持续制造违规的写入路径）。
