# Codex 完全使用指南（进阶续集）深度调研报告

> depth: standard · generated: 2026-07-17 · tools: **deep-research（5-angle fan-out，5/5 返回）** · WebSearch · WebFetch | skipped: bird · last30days · summarize · defuddle
> ⚠️ 互动数据：X/YouTube 全部「推断·未实测」（本机无 bird/last30days/summarize），已逐条标注。Web/官方为实测主力。
> ⚠️ 本报告承接已发 `drafts/openai-codex-getting-started`（上手篇），只覆盖**进阶面**；假设读者已装好、会跑第一个任务。
> 溯源纪律：每论断标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游 writer 只穿透引用**原始出处**，不引本报告。

## TL;DR

- **进阶指南真正的护城河 = 一手「可复制语法」+ 诚实纠偏。** 上手篇留了 TODO 的 **MCP 精确 TOML** 这次抓到逐字（是 `[mcp_servers.<name>]` 表，**不是** `[mcp]` 块）；hooks 是 **10 个生命周期事件**（不是坊间传的 6 个）；subagents 靠 `[features] multi_agent = true` 开关 + `[agents]` 默认值（`max_threads=6`/`max_depth=1`/`job_max_runtime_seconds=1800`）。这些逐字块（§6）= 全稿最硬的差异化弹药。
- **⚠️ 世界在 11 天内变了三件大事，旧调研已过时**：① **默认模型不再是 GPT-5.5** —— OpenAI 发 **GPT-5.6 家族（Sol/Terra/Luna）**，Codex 当前默认 = **`gpt-5.6-sol` @ medium**，`gpt-5.2`/`gpt-5.3-codex` 已弃用；② **官方文档搬家**：`developers.openai.com/codex/*` → **`learn.chatgpt.com/docs/*`**（308 永久重定向）；③ **"Automations" 官方改名 "Scheduled tasks"**，且调度是 **RRULE（RFC 5545）不是 cron**（cron 只在 CLI `codex exec` headless 路径）。任何沿用旧事实的段落都要改写。
- **进阶面的分层**：**配置层金料**（MCP/hooks/subagents/`approval_policy="never"`，§6 逐字）· **方法论层**（长时任务**四文件法**——博客非 cookbook · `/goal` 三部曲 cookbook · Codex Remote 手机控主机）· **纠偏层**（默认模型、文档域名、Scheduled tasks 术语）。
- **切法**：这是给「已上手、想把 Codex 当自主 agent 平台压榨」的读者的**进阶手册**，中文世界空白；GEO 弹药足（每个 claim 挂 `learn.chatgpt.com` 官方链 + 硬数字：12h 缓存 / max_threads=6 / 精简 prompt 省 41–66% token）。

## 0. Vault 已有锚点（查内）

> ⚠️ 内部存量**只塑造 outline 与本节**，不填充正文（plan §11.6 自我重复陷阱）。vault 在 Codex **方法论**上已是 Tier-1，本报告补**进阶产品面 + 当前状态**这一缺口。

> [!warning] 你已写过上手篇 —— 本稿是进阶续集，不是重写
> `drafts/openai-codex-getting-started.zh.md` / `.en.md`（2026-07-06）已覆盖：四 surface · 安装登录 · 第一个任务 · 基础 AGENTS.md · 基础 config · 模型命名 · MCP/hooks **一瞥** · 给 Claude Code 用户对照。**本稿继承其读者、专攻它只是「一瞥」的进阶面，零重复。** 上手篇里过时的模型/术语（GPT-5.5 默认、Automations、`[mcp]`）需回头随本报告修订。

**已表达角度（勿重复）：**
- [[claude-code-goal]] / [[source-openai-codex-cookbook-trilogy]] — `/goal` + 三层嵌套 loop 方法论已讲透。[内部/Tier-1]
- [[chris-hayduk]] / [[source-chrishayduk-codex-goals-effectively]] — `/goal` practitioner 三招。[内部/Tier-1]
- [[iterative-repair-loop]] · [[agent-improvement-flywheel]] · [[agentic-loop-tracking-files]] — loop 内部机制。[内部/Tier-1]

**进阶面 vault 锚点（各有源页，但都是分散 source-summary，无消费者向进阶指南）：**
- [[source-openai-codex-skills-docs]]（agentskills.io）· [[source-openai-codex-subagents-docs]]（max_threads=6/max_depth=1）· [[source-openai-codex-automations-docs]] · [[source-openai-codex-cloud-environments-docs]]（12h 缓存）· [[source-openai-codex-hooks-docs]]（hooks 事件/exit 2）· [[source-openai-long-horizon-tasks-codex]]（长时任务）· [[source-openai-cookbook-plans-md]]（PLANS.md）。[内部/Tier-1]

**旧判断回收（写新 take 时参照/推翻）：**
- 旧判断①「Codex 与 Claude Code 跨厂商功能收敛」→ **继承**：进阶面（subagents/hooks/skills/scheduled）仍一一对位，可平视。
- 旧判断②「配置层是杠杆，不是模型层」[内部/Tier-1: source-openai-codex-cookbook-trilogy] → **强化**：本轮抓到的逐字 MCP/hooks/subagents TOML 正是「30 行配置 > 换模型」的实证弹药。
- ⚠️ **需推翻的旧内部事实**：source-summary 里写的「hooks 6 事件」「MCP `[mcp]` 块」「long-horizon triad 三文件」等，本轮外扫已证伪（见 §2 纠偏清单）——修订 vault 页时一并纠正。

## 1. 进阶功能是什么 — 事实轴

> 全部对 `learn.chatgpt.com/docs/*`（官方文档新家）/ `developers.openai.com/{blog,cookbook}` 逐条核验。

### Skills（技能）
- **遵循 Agent Skills 开放标准**（agentskills.io；Anthropic 起草后开源，30+ 工具采纳，Codex 为官方 adopter）。目录：`SKILL.md`（必需）+ `scripts/`/`references/`/`assets/`（可选）+ **`agents/openai.yaml`（Codex 专属**，放外观与 `policy`）。目录 `name` 须与 SKILL.md `name` 一致。— [外部: learn.chatgpt.com/docs/build-skills · agentskills.io/specification] — ✅
- **调用**：`/skills` 或输入 **`$`** 提及；官方例 `$skill-installer linear`、`$skill-creator`。— ✅
- **两个别混的数字**：① 发现清单预算 = **「上下文 2%，未知时 8,000 字符」**（针对始终加载的 name+description 索引，这才是那个 ~8K cap）；② 单个 skill 正文建议 **< 5000 tokens** / SKILL.md < 500 行。渐进披露三段：元数据(~100 tokens 启动加载)→ 指令(激活加载)→ 资源(按需)。— ✅
  > [!warning] 别写「Skills is GA」
  > 官方页**未给 Skills 打 GA/preview 标签** —— 是「已发布未标注」。

### Subagents（子智能体）
- 靠 **`[features] multi_agent = true`** 开关（**stable，默认开**）；**没有单独 `subagents` flag**。多智能体工具：`spawn_agent`/`send_input`/`resume_agent`/`wait_agent`/`close_agent`。— [外部: learn.chatgpt.com/docs/agent-configuration/subagents] — ✅
- `[agents]` **确切默认值**：`max_threads=6` · `max_depth=1`（root=depth 0，允许一层子 agent）· `job_max_runtime_seconds=1800` · `interrupt_message=true`。— ✅
- 内置三类：**`default`**（兜底）· **`worker`**（执行/修复）· **`explorer`**（只读探索）。自定义 agent 每个一个 TOML，`~/.codex/agents/`（个人）或 `.codex/agents/`（项目）。— ✅
- **`spawn_agents_on_csv`** = **experimental**：读 CSV → 每行 spawn worker → 全批等待 → 导出 CSV；每 worker 须调一次 `report_agent_job_result`（否则该行 `status: error`）。— ✅

### Scheduled tasks（原 "Automations"，官方已改名）
- H1 就是 "Scheduled tasks"。两型：① **Standalone**（每次起新 chat，可跨多 project）；② **chat 内 scheduled task**（复用该 chat 上下文，支持**分钟级**间隔做主动跟进循环）。— [外部: learn.chatgpt.com/docs/automations] — ✅
- **project-scoped worktree** ✅：Git 仓库可选跑在 local project 或新 **worktree**（隔离定时任务改动与手头工作）；需机器开机 + 桌面 App 运行。
  > [!warning] 不是 cron，是 RRULE
  > App 内调度用 **RRULE（RFC 5545）**，例 `RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`。**cron 只在 CLI headless**（`codex exec` 适合被你自己的 cron/GitHub Actions 调度）。"在 UI 填 cron 表达式"是错的。
  > ⚠️ **"heartbeat"/"Triage automations" 非官方术语**（heartbeat 只在 GitHub issues；Triage 未证实为独立功能，只有一个 "Scheduled" 收件箱视图）。别当官方分类写。

### Cloud / Cloud environments
- 云面 **`chatgpt.com/codex`**；环境配置 `chatgpt.com/codex/settings/environments`；可从 GitHub PR / Linear / Slack 启动；无人值守后台跑是核心卖点。— [外部: learn.chatgpt.com/docs/cloud · /environments/cloud-environment] — ✅
- **12 小时容器缓存** ✅（"Containers cache for up to 12 hours"；改 setup/maintenance script / env / secrets 会失效）。默认镜像 `universal`（`openai/codex-universal`）。
- **setup 有网 / agent 默认无网** ✅；**secrets 只给 setup，agent 阶段前移除**，env vars 全程保留。
- **`@codex` GitHub** ✅：`@codex review`（👀 + 行内发现 + PR 级总结）· `@codex review for security regressions`（一次性聚焦）· `@codex fix the P1 issue`；非 review 的 `@codex` 提及以该 PR 为上下文起云 chat；设置有 "Automatic reviews" 开关；评审规则用最近的 `AGENTS.md` 定制。

### MCP（深配）
- 关键：是 **`[mcp_servers.<name>]` 表**，**不是** `[mcp]` 块（上手篇 TODO 的正解）。配置在 `~/.codex/config.toml`（项目 `.codex/config.toml` 覆盖）；传输由存在的键决定（`command`=stdio，`url`=streamable HTTP，二者互斥）；有 `codex mcp add` CLI。逐字块见 §6。— [外部: learn.chatgpt.com/docs/extend/mcp?surface=cli] — ✅

### Hooks（实战）
- **10 个生命周期事件，不是 6 个**：turn 级 8 个（`PreToolUse`/`PermissionRequest`/`PostToolUse`/`PreCompact`/`PostCompact`/`UserPromptSubmit`/`SubagentStop`/`Stop`）+ 会话/子 agent 启动级 2 个（`SessionStart`/`SubagentStart`）。— [外部: learn.chatgpt.com/docs/hooks] — ✅
- **阻断约定 = exit code 2 + 原因写 stderr**。企业管控用 `requirements.toml`（`allow_managed_hooks_only` · `[features] hooks = true` · `[hooks] managed_dir`）。逐字块见 §6。— ✅
  - ⚠️ 官方 hooks 页**未标 GA 日期**；第三方称 GA=2026-05-14（byteiota 等），另有第三方称 hooks engine 于 v0.124.0（2026-04-23）稳定 —— 均**第三方**，官方未逐字确认，正文标注。

### Worktree 并行
- ❌ **不是"自动 per-thread"**：桌面 App 新建 chat 时**手动选 "Worktree" / "Local"**；每个托管 worktree 通常专属一个 chat，resume 回同一 worktree。— [外部: learn.chatgpt.com/docs/environments/git-worktrees] — ✅
- ✅ **"Hand off"** 在 Local(前台)↔ Worktree(后台)间移动 chat = 官方并行范式（"排队后台工作，同时前台专注"）。
- ⚠️ worktree root 默认 `$CODEX_HOME/worktrees`、自动清理保留**最近 15 个** —— 是 **App 设置**(Settings > Worktrees)的 prose，**config.toml 无专门 worktree 键**，别当配置键写。`projects.<path>.trust_level` 可标 trusted/untrusted。
- ⚠️ **CLI 无原生 `--worktree` flag** / `codex --resume --all` 跨 worktree —— 纯第三方，官方未证实。

### 长时 / 自主运行任务（第一类工作流）
- **四文件法在博客，不在 cookbook**："Run long horizon tasks with Codex"，**Derrick Choi，2026-02-23**。`Prompt.md`(冻结目标) · `Plan.md`(里程碑+验证命令+"stop-and-fix") · `Implement.md`(执行手册，plan 为 single source of truth) · `Documentation.md`(状态/审计日志)。"**Freeze the target**" = 用稳定 markdown 记忆"做完的定义"，防 scope drift。硬指标 **~25h 不间断 / ~13M tokens / ~30k 行**（GPT-5.3-Codex, Extra High）。— [外部: developers.openai.com/blog/run-long-horizon-tasks-with-codex] — ✅
  - ⚠️ 该博客用 **`/plan`** 命令，**不含** `approval_policy`/cron/云配置 —— 是**提示工程纪律，不是配置菜谱**。`openai-cookbook/.../long_horizon_tasks.md` **404 不存在** —— 别引 cookbook。
- **PLANS.md 多小时任务 = 另一篇真 cookbook**："Using PLANS.md for multi-hour problem solving"，**Aaron Friel，2025-10-07**。PLANS.md 定义 **ExecPlans**（自包含活文档）；与 **AGENTS.md 配合**（AGENTS.md 放触发短语）；四必需活文档小节 **Progress · Surprises & Discoveries · Decision Log · Outcomes & Retrospective**；实证"单条 prompt 工作 **7+ 小时**"。— [外部: developers.openai.com/cookbook/articles/codex_exec_plans] — ✅

### Codex Remote（手机控主机）
- **GA = 2026-06-25**（官方 changelog 逐字："Codex Remote has reached general availability"）。手机发 prompt/审批/后续，**主机提供环境**；手机是**控制面，不是第二个 Codex**。**二维码配对**（桌面 App 生 QR，扫码进 ChatGPT，认证一对一，绑当前登录会话）；**secure relay 不把主机暴露公网**。随 GA 附 DigitalOcean 插件（`@DigitalOcean` 起 Droplet 当主机）。— [外部: learn.chatgpt.com/docs/remote-connections · /changelog] — ✅

### `/goal` 循环方法论（落地）
- **`/goal` 是真官方 CLI slash 命令**（"Set, edit, pause, resume, view, or clear a task goal"）；`/plan` 亦真。— [外部: learn.chatgpt.com/docs/developer-commands?surface=cli] — ✅
- **Cookbook 三部曲都真，但标题与旧内部记录不同**（见 §3 W16–W18）；**没有一篇叫 "Agent Improvement Flywheel"** —— 第三篇是 "Build an Agent Improvement **Loop**"，flywheel 只是图里的标签。⚠️ 修订 vault 页时纠正。

## 2. 焦点：自 2026-07-06 旧调研以来的事实漂移（进阶指南最易踩坑处）

> 消歧无需（实体已锚定）；真正的焦点是**当前状态**。这些是写稿前必须内化的纠偏。

**变了的事实（务必更新）：**
- **默认模型 GPT-5.5 → `gpt-5.6-sol` (medium)**。GPT-5.6 家族（**Sol/Terra/Luna**）限量预览 2026-06-26、公开 ~2026-07-09；GPT-5.5 降级为"上一代"；**`gpt-5.2`、`gpt-5.3-codex` 在 ChatGPT 登录态弃用**。orchestrator+worker 模式的模型名迁到 **`gpt-5.6`（难活）+ `gpt-5.6-terra`/`gpt-5.4-mini`（并行 worker/杂活）**——旧的 "5.5-thinking + 5.4-mini" 逐字组合在当前官方文档已不存在。— [外部: learn.chatgpt.com/docs/models] — ✅
- **官方文档搬家**：`developers.openai.com/codex/*` **308 永久重定向到 `learn.chatgpt.com/docs/*`**（Codex 文档并入 ChatGPT Learn）。旧 URL 非死链，但引用给规范新 URL。— ✅
- **Codex 并入 ChatGPT 桌面 App**（2026-07-09，Desktop 26.707）—— 独立 "Codex App" 说法过时；worktree/scheduled-tasks UI 都在桌面 App 里。— ✅
- **"Automations" → "Scheduled tasks"**（术语换）+ **RRULE 非 cron**（§1）。
- **Codex Remote GA 2026-06-25**（§1）。
- changelog 后续：07-13 iOS 1.2026.188 · 07-14 CLI 0.144.4 · 07-16 CLI 0.144.5（危险命令检测）。— ✅

**必须纠偏的旧假设清单（写稿 checklist）：**
| 旧说法 | 实际 | 证据 |
|---|---|---|
| hooks「6 生命周期事件」 | **10 个** | [外部: /docs/hooks] ✅ |
| MCP `[mcp]` 块 | **`[mcp_servers.<name>]` 表** | [外部: /docs/extend/mcp] ✅ |
| long-horizon「三文件 triad」且在 cookbook | 博客里**四文件**(+Documentation.md)，cookbook 同名 **404** | [外部: blog] ✅ |
| 用 `/goal` 跑长任务 | 长任务博客用 **`/plan`** | [外部: blog] ✅ |
| "Agent Improvement Flywheel"(文章名) | 真名 "Build an Agent Improvement **Loop**" | [外部: cookbook] ✅ |
| "heartbeat / Triage automations"(官方分类) | 非官方术语/未证实 | ⚠️ |
| worktree「自动 per-thread」 | **手动 Local/Worktree 选 + Hand off** | [外部: /docs/environments/git-worktrees] ✅ |
| 默认 GPT-5.5 | **gpt-5.6-sol medium** | [外部: /docs/models] ✅ |

## 3. Web / 官方 — Top 10（增长轴 · 渠道层 · 实测主力）

> 官方页无互动数属正常（= 事实锚定）；第三方阅读量「推断·未实测」。完整 21 条候选见 `ingest-candidates.md`。

### #1 官方「MCP (extend)」— 进阶指南的金块
- `learn.chatgpt.com/docs/extend/mcp?surface=cli` · OpenAI 官方 · live
- 核心：**`[mcp_servers.<name>]` TOML（stdio + HTTP 两块对照）** + `codex mcp add`。上手篇 TODO 的正解。
- **写作风格拆解：两块对照 + 传输选择规则，一看就能抄 —— 直接偷它的"stdio/HTTP 并列"骨架。**

### #2 官方「Hooks」
- `learn.chatgpt.com/docs/hooks` · OpenAI 官方 · 未标 GA 日期
- 核心：10 事件、exit 2 阻断、`config.toml` + 企业 `requirements.toml` 两版逐字。
- **写作风格拆解：事件按 scope 分组 + 逐字 TOML + 企业/个人两版分栏。**

### #3 官方「Subagents」
- `learn.chatgpt.com/docs/agent-configuration/subagents` · OpenAI 官方 · 07-17 仍在更新
- 核心：`multi_agent` 开关、`[agents]` 默认值、三内置、自定义 TOML、`spawn_agents_on_csv` 批处理。
- **写作风格拆解：先给配置再给能跑实例；每键配默认值 —— 进阶配置章节的模板。**

### #4 官方「Scheduled tasks」（原 Automations）
- `learn.chatgpt.com/docs/automations` · OpenAI 官方 · 随 07-09 上线
- 核心：两型 · worktree 选项 · **RRULE** · `approval_policy=never` · `$skill` 定时。
- **写作风格拆解：每小节一句"何时用"开头 + 末尾可复制 Examples —— how-to 模板。**

### #5 官方「Cloud environment」
- `learn.chatgpt.com/docs/environments/cloud-environment` · OpenAI 官方 · live
- 核心：**12h 缓存** · setup 有网/agent 无网 · secrets 时序。
- **写作风格拆解：编号"执行流" + 隐含默认值表，安全/时序事实密度最高。**

### #6 官方「GitHub (@codex)」
- `learn.chatgpt.com/docs/third-party/github` · OpenAI 官方 · live
- 核心：`@codex review / fix` 全部触发串 · 自动评审 · AGENTS.md 定制评审规则。
- **写作风格拆解：手动 vs 自动分栏 + 触发串放 backtick —— "确切命令内联"范式。**

### #7 官方博客「Run long-horizon tasks with Codex」（方法论一等公民）
- `developers.openai.com/blog/run-long-horizon-tasks-with-codex` · Derrick Choi · 2026-02-23
- 核心：**四文件法** · freeze the target · 25h/13M/30k 硬指标。
- **写作风格拆解：用"制品"教学——直接给三个可抄文件骨架；先失败模式后解法，极易模仿。**

### #8 官方 Cookbook「Using PLANS.md for multi-hour」
- `developers.openai.com/cookbook/articles/codex_exec_plans` · Aaron Friel · 2025-10-07
- 核心：**ExecPlans 四小节** · 与 AGENTS.md 配合 · 7h 实证。
- **写作风格拆解：spec-doc 即课程；强制命名活文档小节 + 一个英雄指标。**

### #9 官方「GPT-5.6 prompting guidance」
- `developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6` · OpenAI 官方 · live
- 核心：**精简 prompt 提分 10–15% 且省 token 41–66%** · medium 起步 · `reasoning.mode:"pro"`。
- **写作风格拆解：带硬百分比的 do/don't，数字即论据 —— GEO 金矿。**

### #10 官方「Remote connections」
- `learn.chatgpt.com/docs/remote-connections` · OpenAI 官方 · 06-25 GA
- 核心：手机控主机 · QR 配对 · secure relay。
- **写作风格拆解："control surface, not a second Codex" 一句心智模型可直接偷。**

> [!note] 第三方结构范本（次要 · 阅读量「推断·未实测」）
> `codex.danielvaughan.com`（Daniel Vaughan "Codex Knowledge Base"）镜像官方结构 + 补可跑 config 块与 gotcha；subagents 篇今日(07-17)更新；"Loop Engineering…autonomous loops that run while you sleep"(06-11) 是"无人值守循环"最完整第三方叙事 —— **但其 `[goals]` TOML 官方无法证实（`o4-mini`/`max_turns` 存疑），别抄进正文**。freeCodeCamp "Codex Handbook"、Simon Willison `/tags/codex` 作 leads。

## 4. X / Twitter — Top 2（增长轴 · 渠道层）

> [!warning] 本节互动全「推断·未实测」（本机无 bird）；X Article/post 登录墙（memory: 需登录态 Chrome）。只 @OpenAIDevs 一条硬锚，未对任何主张绑定未亲验 handle。

### #1 @OpenAIDevs — Subagents 官宣
- `x.com/OpenAIDevs/status/2033636701848174967` · OpenAI 官方 · 短推 · 互动**推断·未实测**（官方，反推高）
- 核心：*"Subagents are now available in Codex"* —— 保持主上下文干净 / 并行拆任务 / 边跑边操控。✅ 帖存在且官方口径，可作 subagents 官宣锚点。
- **写作风格拆解：官方公告短推，收益导向。**

### #2 @therobertta（Threads，非 X）— repair loop 转述
- `threads.com/@therobertta/...` · 短帖串 · 互动**推断·未实测**
- 核心：转述 OpenAI iterative-repair cookbook（review-repair-validate、`repair_until_done` 停止条件）；自称 "70 MCP tools + 8 cron jobs 生产跑"。
- **写作风格拆解：practitioner 生产叙事。** ⚠️ 其"4 个停止条件"是第三方演绎（官方页只 2 个），引用需纠偏；平台是 Threads 非 X。

> [!note] X 深度缺口
> bird 缺失 + 登录墙 → 进阶工作流长贴（AGENTS.md 杠杆 / worktree 并行 / overnight cron）未能深挖。若要补 X growth 信号，须用登录态 claude-in-chrome。

## 5. YouTube — Top 3（增长轴 · 渠道层）

> [!warning] 观看全「推断·未实测」（本机无 summarize/last30days）。均 WebSearch 命中的标题/日期，作 leads。

### #1「How to Setup MCP in Codex CLI (Step-by-Step)」
- `youtube.com/watch?v=gaSLGiaq5nk` · ~2026-06-14 · 观看**推断·未实测** · 实操
- **写作风格拆解：与 §6 MCP TOML 互为视频版 —— 配文可交叉引。**

### #2「Codex Multi-Agent Workflow with Git Worktrees」
- `youtube.com/watch?v=fVdBEgVE0wI` · ~2026 · 观看**推断·未实测** · 实操
- **写作风格拆解：worktree 并行多 agent 不互踩，对应 §1 worktree 一节的演示。**

### #3「OpenAI Codex now lets you schedule automations…」(short)
- `youtube.com/shorts/CHyNt5dmAoo` · ~2026-02-05 · 观看**推断·未实测** · 概念 short
- **写作风格拆解：早期 short，术语已改"Scheduled tasks"，引用需更新。**

> [!note] 渠道洞察
> 进阶实操视频**英文中腰部零散、中文近乎空白**；"按官方核验 + 逐字 TOML"的中文进阶实操位无人占。

## 6. 核心洞察 + 最佳实践 + 可复制语法金料

**洞察一：进阶指南的价值 = 逐字语法 + 诚实纠偏，不是概念科普。** 读者已上手，缺的是"MCP 那块 TOML 到底怎么写""hooks 有哪些事件""subagents 默认几个线程"。本轮抓到的逐字块（下方）+ §2 纠偏表 = 别处（尤其中文）没有的硬料。[外部: learn.chatgpt.com/docs/extend/mcp · /hooks · /agent-configuration/subagents]

**洞察二：Codex 进阶的主线是「把它当自主 agent 平台」，不是"更会补全"。** subagents（并行）+ scheduled tasks（`approval_policy=never` 无人值守）+ cloud（后台）+ Remote（手机盯）+ 长时任务四文件法 = 一条"排队 → 后台自动跑 → 远程盯梢"的自主流水线。这是进阶稿该立的骨架。[外部: /docs/automations · /docs/cloud · blog long-horizon]

**洞察三：配置层是杠杆的实证被本轮坐实。** hooks 把 AGENTS.md 的"不要动"从约定变强制（exit 2）；`requirements.toml` 做企业托管；subagents `[agents]` 旋钮控并行度 —— 全是"几十行 TOML > 换模型"。[外部: /docs/hooks · /docs/agent-configuration/subagents]

**洞察四：事实漂移快到"11 天即过时"，诚实核验就是护城河。** 默认模型、文档域名、功能改名在两周内全变 —— 中文二创普遍抄旧料；本稿逐条挂官方新 URL + 标注纠偏 = 差异化。[外部: /docs/models · /docs/changelog]

**最佳实践清单（可进正文/角度）：**
1. MCP 用 `[mcp_servers.<name>]` 表，`command`=stdio / `url`=HTTP 二选一；能用 `codex mcp add` 就别手写。
2. 并行任务先 `[features] multi_agent = true`（默认已开）+ 控 `max_threads`/`max_depth`；批处理走 `spawn_agents_on_csv`（experimental，注意每 worker 回 `report_agent_job_result`）。
3. 无人值守：Scheduled task + `approval_policy="never"` + 跑在 **worktree**（隔离改动）；App 内用 **RRULE**，CLI headless 用 `codex exec` 接你自己的 cron/Actions。
4. 把 spec 里的"不要动"用 **hooks（exit 2）** 变"动不了"；企业用 `requirements.toml` 托管。
5. 长时任务用**四文件法**（Prompt/Plan/Implement/Documentation）冻结目标；或 **PLANS.md/ExecPlan** 四小节。别把它跟 `/goal` 混——长任务博客用 `/plan`。
6. 模型分工：难活 `gpt-5.6`（默认 sol medium）、并行 worker/杂活 `gpt-5.6-terra`/`gpt-5.4-mini`；prompt 精简可省 41–66% token。
7. 远程盯长任务用 **Codex Remote**（手机控主机 + QR），手机是控制面不是第二个 Codex。
8. 所有数字/术语发稿前重核 `learn.chatgpt.com/docs/{models,changelog}` 当前状态（漂移极快）。

---

### 可复制语法金料（写稿直接搬 · 每块标 ✅ 官方 / ⚠️ 存疑）

**① MCP — stdio 服务器** ✅ `learn.chatgpt.com/docs/extend/mcp?surface=cli`
```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]
startup_timeout_sec = 10
tool_timeout_sec = 60

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"
```
**MCP — streamable HTTP / 远程** ✅（同页）
```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
auth = "oauth"

[mcp_servers.figma.http_headers]
"X-Figma-Region" = "us-east-1"
```
**MCP CLI** ✅：`codex mcp add context7 -- npx -y @upstash/context7-mcp`
> `~/.codex/config.toml`（项目 `.codex/config.toml` 覆盖）；`command`↔stdio、`url`↔HTTP 互斥；`startup_timeout_sec` 默认 10、`tool_timeout_sec` 默认 60。

**② Hooks — config.toml** ✅ `learn.chatgpt.com/docs/hooks`
```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"
```
**Hooks — requirements.toml（企业托管）** ✅（同页）
```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
timeout = 30
```
> 阻断 = handler `exit 2` + 原因写 stderr。10 事件见 §1。

**③ Subagents — 配置 + 自定义 agent** ✅ config-reference / subagents
```toml
[features]
multi_agent = true          # stable, 默认开

[agents]
max_threads = 6             # 默认 6
max_depth = 1               # 默认 1 (root=depth 0)
job_max_runtime_seconds = 1800
interrupt_message = true
```
自定义 agent（`~/.codex/agents/reviewer.toml` 或 `.codex/agents/`）✅
```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
"""
nickname_candidates = ["Atlas", "Delta", "Echo"]
# 可选继承键: model, model_reasoning_effort, sandbox_mode, mcp_servers, skills.config
```

**④ 无人值守 / autonomous** ✅ config-reference / automations
```toml
approval_policy = "never"          # untrusted | on-request | never
sandbox_mode = "workspace-write"   # read-only | workspace-write | danger-full-access
```
CLI 等价 ✅：`codex -a never -s workspace-write exec "…prompt…"`
> Scheduled tasks 在组织策略允许时自动用 `approval_policy="never"`；被 `requirements.toml` 禁止时回退所选权限模式。App 内定时用 **RRULE 不是 cron**。
> ⚠️ **别抄**：第三方(Vaughan) `[goals] max_turns / check_model="o4-mini" / timeout_minutes` 块官方无法证实。

**⑤ Skills — SKILL.md frontmatter** ✅ agentskills.io / build-skills
```markdown
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Bash(jq:*) Read   # Experimental
---
```
> 关闭隐式调用（仍可 `$skill` 显式调）：skill 内 `agents/openai.yaml` 写 `policy: { allow_implicit_invocation: false }`。

**⑥ 长时任务四文件法** ✅（博客，结构逐字）：`Prompt.md`(Goals/非目标/硬约束/"Done when") · `Plan.md`(里程碑+验证命令+"Stop-and-fix rule") · `Implement.md`("Plans markdown 是 source of truth") · `Documentation.md`(状态+审计)。PLANS.md/ExecPlan 四小节：`Progress · Surprises & Discoveries · Decision Log · Outcomes & Retrospective`。

> **溯源标注纪律（plan §11.7，全报告适用）**：每论断标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游 writer 只穿透引用**原始出处**，绝不引本报告。

## 7. 对内容创作的启示 — 增长轴 → 排序的内容角度

> 锚 audience-profile：全背景 AI builder（能上手非资深）· 中文为主体 · 具体压笼统 · 分层深度 + 角色化入口 · GEO 规则（官方引用 +40%、数字 +37%、前置定义、可扫描）。

### 时机窗口
- Codex 2026 上半年功能井喷 + **两周内三处大变**（GPT-5.6 默认 ~7/9、文档搬家、Automations 改名）—— 英文进阶教程零散、中文进阶指南**空白**，且**现有二创普遍抄旧料**。现在（7/17）是"按官方新状态核验的中文 Codex 进阶指南"**首发+纠偏双窗口**。
- ⚠️ 漂移极快：发稿前重核 `learn.chatgpt.com/docs/{models,changelog,automations}` 当前状态。

### 排序的内容角度（角度闸 · 每个 = 一个内容赌注）

#### 角度1（推荐）「Codex 进阶实战：把它当自主 agent 平台压榨——subagents / 无人值守 / 长时任务，全部按官方逐字核验」
- **① 标题候选**：《Codex 进阶完全指南：从"会用"到"让它替你通宵干活"》/《Codex 自主 agent 实战：subagents·Scheduled tasks·长时任务（2026-07 官方核验版）》
- **② thesis**：Codex 进阶的分水岭不是"更会写代码"，而是**把它从助手升级成能并行、能无人值守、能跑几十小时的自主 agent 平台**——而这套能力的开关，全在几十行 TOML 和四个 markdown 文件里。
- **③ 为什么我们/为什么现在**：中文无一份进阶指南；现有二创普遍抄旧料（GPT-5.5 默认、`[mcp]`、Automations）——**诚实核验 + 逐字语法**是我们的护城河；两周内三处大变给了"首发+纠偏"双窗口。
- **④ prior_coverage 关系**：**不同角度**——上手篇讲装/第一个任务；本稿专攻上手篇只"一瞥"的 subagents/hooks/scheduled/cloud/长时任务；`/goal` 一句带过链回 [[claude-code-goal]]。零重复。
- **⑤ 骨架（3–5 行）**：一句价值+谁该读 → **自主 agent 流水线全景**（subagents 并行 → scheduled 无人值守 → cloud 后台 → Remote 手机盯）→ **配置层金料**（MCP/hooks/subagents 逐字 TOML）→ **长时任务四文件法** → **纠偏盒**（默认模型/文档域名/改名）→ Claude Code 用户平移 → 收尾。
- **⑥ 渠道建议**：博客长文（GEO 主场，逐字 TOML + 官方链 + 硬数字）→ 切中文 X thread（"11 天内 Codex 变了 3 件事" 纠偏钩子）+ 中文 YouTube 实操（MCP/worktree 演示，视频位空）。

#### 角度2「Codex 的 MCP / hooks / subagents 到底怎么配——一份可直接抄的 TOML 速查」
- **① 标题候选**：《Codex 配置速查：MCP·hooks·subagents 逐字 TOML（复制即用）》
- **② thesis**：进阶卡点 90% 是"那块 TOML 到底怎么写"——把官方逐字配置整理成一页可抄速查，比任何概念讲解都值钱。
- **③ 为什么我们/为什么现在**：上手篇明确留了 MCP TOML 的 TODO；坊间"`[mcp]` 块""hooks 6 事件"错料流传——一手逐字 = 纠错型高引用内容。
- **④ prior_coverage 关系**：**新证据推进**——把上手篇的"一瞥"升级为可抄速查；与角度1 是"速查卡 vs 实战全景"的关系，可作角度1 的抽出物或独立短篇。
- **⑤ 骨架**：MCP（stdio/HTTP 两块）→ hooks（10 事件 + exit 2 + requirements.toml）→ subagents（`[agents]` 默认值 + 自定义 agent + CSV 批）→ `approval_policy=never` 无人值守 → 每块附"常见错法 vs 正解"。
- **⑥ 渠道建议**：博客中篇 + 一张速查表（可扫描、GEO 友好）；X carousel/图。

#### 角度3「11 天，Codex 变了 3 件大事：默认模型、文档搬家、Automations 改名——你抄的教程可能全过时了」
- **① 标题候选**：《你收藏的 Codex 教程可能已过时：2026-07 三处关键变更核对》
- **② thesis**：AI 工具的事实漂移快到"两周即过时"，而中文二创普遍滞后——一份"纠偏 + 当前状态核对"本身就是高价值内容。
- **③ 为什么我们/为什么现在**：时效性钩子极强（"11 天"具体数字）；诚实核验是 vault 一贯品牌；可复用为"Codex 变更追踪"系列的第一期。
- **④ prior_coverage 关系**：**旧判断回收/推翻**——公开修订我们自己上手篇里的过时事实（GPT-5.5/`[mcp]`），可信度加分；与角度1 互补（角度1 是完整指南，本角度是短平快时效号）。
- **⑤ 骨架**：三处大变逐条（旧→新→官方链）→ 附"你该改哪些认知"checklist（§2 纠偏表）→ 一句"以后怎么追新（changelog 唯一权威）"。
- **⑥ 渠道建议**：X 中文 thread（时效号主场）+ 博客短文；蹭"model/docs 变更"搜索窗口。

### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
|---|---|---|
| @OpenAIDevs | OpenAI 官方 | 进阶功能发布一手源（subagents 官宣已锚） |
| Simon Willison | 独立高信号 practitioner | Codex 日常主力叙事 + 亲测 |
| Aaron Friel / Derrick Choi | OpenAI cookbook/blog 作者 | 长时任务 PLANS.md / 四文件法原始出处 |
| Daniel Vaughan | 第三方 KB 作者 | 无人值守循环最完整第三方叙事（TOML 需存疑） |

### 内容形式参考库
- **进阶 how-to / 逐字配置** → 学官方 MCP/hooks 页（stdio/HTTP 两块对照 + 企业/个人分栏）
- **方法论"制品"教学** → 学 long-horizon 博客（直接给可抄文件骨架 + 先失败后解法）
- **数字即论据** → 学 GPT-5.6 prompting 页（带硬百分比 do/don't，GEO 金矿）
- **官方公告** → 学 @OpenAIDevs（收益导向短推）

## 附录：关键时间线

| 日期 | 事件 |
|---|---|
| 2025-10-07 | Cookbook「Using PLANS.md for multi-hour」(Aaron Friel) —— ExecPlans 四小节 |
| 2026-02-23 | 博客「Run long-horizon tasks with Codex」(Derrick Choi) —— 四文件法 + freeze the target |
| 2026-05-09~12 | Cookbook `/goal` 三部曲（Using Goals / Iterative Repair Loops / Agent Improvement Loop）|
| ~2026-05-14 | （第三方）Codex Hooks GA —— ⚠️ 官方页未标日期 |
| **2026-06-25** | **Codex Remote GA**（手机控主机 + QR 配对）[外部: /docs/changelog] |
| 2026-06-26 | GPT-5.6 家族（Sol/Terra/Luna）限量预览 |
| **2026-07-09** | **GPT-5.6 公开 + 默认切 `gpt-5.6-sol`；Codex 并入 ChatGPT 桌面 App（26.707）** |
| ~2026-07（同期）| 官方文档 developers.openai.com/codex/* → learn.chatgpt.com/docs/*；Automations 改名 Scheduled tasks |
| 2026-07-14~16 | CLI 0.144.4 → 0.144.5（危险命令检测）|
| 2026-07-17 | 本报告生成 |
