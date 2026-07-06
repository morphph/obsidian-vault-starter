# OpenAI Codex 指南 深度调研报告

> depth: standard · generated: 2026-07-06 · tools: WebSearch · WebFetch | skipped: bird · last30days · summarize
> ⚠️ 互动数据：X/YouTube 全部为「推断·未实测」（本机无 scanner），已逐条标注。Web/官方为实测主力。
> ⚠️ headless 运行：plan checkpoint 已跳过；消歧「Codex=2025→2026 agentic 产品」已按证据定（见 research-plan.md）。
> 溯源纪律：每论断标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游 writer 只穿透引用**原始出处**，不引本报告。

## TL;DR

- **我们对 Codex 的「深」是错位的深。** vault 已经把 Codex 的**方法论层**（`/goal`、cookbook 三层 loop、hooks/skills/subagents/cloud 的跨厂商对位）啃穿了，但**缺一份「怎么装、怎么起手、四个 surface 各干嘛、AGENTS.md 怎么写、用哪个模型」的上手指南**——恰恰是「指南/guide」这个词要的东西。这是明确的空白，可安全立新选题。
- **最硬的一手事实全在 `developers.openai.com/codex`**：Rust 写的开源 agent、四大 surface（CLI/IDE/App/Cloud）、`curl … install.sh` 或 `npm i -g @openai/codex`、AGENTS.md 三级优先级、`config.toml` 的 `approval_policy`/`sandbox_mode`/`model`、默认模型 **GPT-5.5**（2026-04 起 ~省 40% 输出 token）。[外部: developers.openai.com/codex/cli] ✅
- **两个写作差异化钩子**：① 中文世界几乎没有一份诚实、按官方核验的 Codex 上手指南（英文 handbook 有 freeCodeCamp，中文空白）；② **模型命名陷阱**（GPT-5.5 frontier 线 vs 已弃用的「-Codex」后缀模型）没人讲清——诚实核验 = 我们的护城河。

## 0. Vault 已有锚点（查内）

> ⚠️ 内部存量**只塑造 outline 与本节**，不填充正文（避免自我重复）。vault 在 Codex **方法论**上已是 Tier-1，本报告只补**产品/上手**这一缺口。

**已表达角度（drafts/ 与 wiki 已覆盖，勿重复）：**
- [[claude-code-goal]] / [[source-openai-codex-cookbook-trilogy]] — Codex `/goal` + 三层嵌套 loop（Goal→完成 / Repair→质量 / Improvement→演化）已讲透。[内部/Tier-1]
- [[chris-hayduk]] / [[source-chrishayduk-codex-goals-effectively]] — Codex `/goal` 的 practitioner 三招（量化目标 + 紧反馈 + 三文件）。[内部/Tier-1]
- [[iterative-repair-loop]] · [[agent-improvement-flywheel]] · [[agentic-loop-tracking-files]] — loop 内部机制。[内部/Tier-1]
- Codex **工具面**各有源页但**无消费者向指南**：[[source-openai-codex-hooks-docs]]（hooks GA 5/14）· [[source-openai-codex-skills-docs]]（agentskills.io）· [[source-openai-codex-subagents-docs]]（max_threads=6/max_depth=1）· [[source-openai-codex-cloud-environments-docs]]（12h 缓存）· [[source-openai-codex-automations-docs]] · [[source-openai-long-horizon-tasks-codex]]（Prompt/Plan/Implement 三件套）· [[source-openai-cookbook-plans-md]]（AGENTS.md + PLANS.md）。[内部/Tier-1]

> [!note] drafts/ 无 Codex 成稿
> `drafts/` 里命中「codex」的都是 PM long-horizon / Ralph 稿的顺带提及，**没有任何 Codex 上手/指南成稿**。**可安全立新选题。**

**旧判断回收（写新 take 时参照/推翻）：**
- 旧判断①：**「Codex 与 Claude Code 是跨厂商功能收敛」**——vault 反复强调 hooks/skills/subagents/cloud/`/goal` 几乎一一对位。→ 新指南可**继承**这条，但把它从「方法论对位」落到「一个 Claude Code 用户怎么 10 分钟上手 Codex」。
- 旧判断②：**「hooks GA 5/14 让『Anthropic stack 更厚』的说法过期」**[内部/Tier-1: source-openai-codex-hooks-docs]。→ 新指南应据此给出**平视**而非「谁更强」的对比。

## 1. 这个话题是什么 — 事实轴

> 全部对 `developers.openai.com/codex` / `openai.com` 逐条核验。

- **Codex 是什么** — OpenAI 的 **agentic 编码 agent**，「读、改、跑你机器上的代码」，**开源、Rust 写的**。— [外部: developers.openai.com/codex/cli] — ✅ verified
  > [!warning] 版本消歧
  > 部分第三方页仍把 Codex 描述成「2025-05 上线的云端自主 agent、GPT-5 家族驱动」——那是**旧的 2025 云端-only Codex**。2026 的产品是 **CLI-first 的四 surface 平台**。「云端-only / 2025-05 launched」对当前产品 ❌ contradicted。
- **四大 surface** — ① **CLI**（终端，干真活的主力）② **IDE 扩展**（VS Code + JetBrains，也能在 Cursor/Windsurf 里跑）③ **Desktop App**（macOS/Windows；并行 thread + 每 thread worktree + diff 审阅 + automations）④ **Codex Cloud**（对 GitHub repo 跑后台/长任务）。四者共享 approval policy / MCP / AGENTS.md / 模型偏好。— [外部: developers.openai.com/codex/ide · /codex/cli] — ✅ verified
- **安装（macOS/Linux）** — `curl -fsSL https://chatgpt.com/codex/install.sh | sh`（无人值守加 `CODEX_NON_INTERACTIVE=1`）；或 `npm i -g @openai/codex`（Node ≥ 22），然后 `codex` 起。— [外部: developers.openai.com/codex/cli] — ✅ verified（npm 形式广泛引用，官方页强调 curl installer）
- **登录** — 首次运行提示：ChatGPT 账号 **或** API key。— [外部: developers.openai.com/codex/cli] — ✅ verified
- **AGENTS.md** — Codex 动手前先读的 markdown 指令文件；**三级优先级**：global（`~/.codex/AGENTS.md`）→ project（repo root 往下到 cwd）→ 自 root 向下拼接、近的覆盖远的。旋钮：`project_doc_max_bytes`、`project_doc_fallback_filenames`；fallback 顺序 `AGENTS.override.md → AGENTS.md → TEAM_GUIDE.md → .agents.md`。— [外部: developers.openai.com/codex/guides/agents-md] — ✅ verified
  - ⚠️ 「AGENTS.md 是跨工具行业标准」——官方只把它当 Codex 特性讲（提到有 agents.md 站点，但不宣称全行业采用）→ 「行业标准」status: unconfirmed，勿写死。
- **config.toml** — 用户级 `~/.codex/config.toml`；项目级 `.codex/config.toml`；状态在 `CODEX_HOME`（默认 `~/.codex`）；CLI `-c key=value` 单次覆盖。默认模型 `model = "gpt-5.5"`。— [外部: developers.openai.com/codex/config-basic] — ✅ verified
- **approval_policy** — `untrusted` / `on-request` / `never`。— [外部: developers.openai.com/codex/config-basic] — ✅ verified（key 名）
- **sandbox_mode** — `read-only` / `workspace-write` / `danger-full-access`。— [外部: 同上] — ✅ verified
- **MCP 支持** — 有，`config.toml` 里 `[mcp]` 配置，专门文档 `/codex/mcp`。— [外部: developers.openai.com/codex/mcp] — ✅ verified（存在性）；⚠️ 精确 TOML 语法未在本轮引出，写稿前需一手确认。
- **定价 / plan 接入** — 随 ChatGPT plan 附带：Free $0 · **Go $8** · **Plus $20** · **Pro 起 $100**（比 Plus 高 5×/20× rate limit）· Business $20/座 · Enterprise/Edu 定制。也支持 API-key 用量计费。— [外部: developers.openai.com/codex/pricing] — ✅ verified
  - ⚠️ 「Pro 5× $100 档 4/9 加入」「4/2 从 per-message 转 token/credit 计费」「Plus ≈ 每 5h 窗口 10–60 个 cloud 任务」——均**第三方（eesel/uibakery）**，官方页未逐字确认，写稿前核。
- **最近更新（2026-05~07）** — Codex Remote GA（ChatGPT 手机端控主机、QR 一对一配对，~6/25）· Windows 上 Computer Use（~5/29）· Sites 插件（~6/2）· Record & Replay → 演示即可复用 skill（macOS，~6/18，排除 EEA/UK/CH）· Appshots（双击 Command 把前台窗口发给 Codex）· 应用内浏览器控制 · DigitalOcean 插件。— [外部: developers.openai.com/codex/changelog] — ✅ verified

## 2. 焦点实体深挖 — Codex 背后的模型（最易踩坑的事实）

> 消歧块确认的焦点：读者最容易搞混「Codex 用哪个模型」。逐条同 §1 核验纪律。

- **当前默认 = GPT-5.5** — 2026-07 Codex 大多数任务的推荐默认；~2026-04-23 起进入 Codex；同任务比 GPT-5.4 **少约 40% 输出 token**。— [外部: developers.openai.com/codex/models · openai.com/index/introducing-gpt-5-5] — ✅ verified
- **可选**：GPT-5.4、GPT-5.4 mini（便宜快，适合无聊活）；**GPT-5.3-Codex-Spark** = 更快变体，research preview（Pro）。— [外部: developers.openai.com/codex/models] — ✅ verified
- **已弃用**：对 ChatGPT 登录用户，**GPT-5.3-Codex 与 GPT-5.2 已从可选模型下架**。— [外部: developers.openai.com/codex/changelog] — ✅ verified
- **命名陷阱（写作弹药）** — 要分清**通用 frontier 线**（GPT-5.4 / **5.5**，现在驱动 Codex）与**旧的「-Codex」后缀模型**（GPT-5.2-Codex / 5.3-Codex，正被弃用/取代）。2026 的方向是**统一 frontier 模型（5.5）**，专用「-Codex」后缀退场。— [外部: developers.openai.com/codex/models] — ✅ verified

## 3. Web / 博客 — Top 7（增长轴 · 渠道层 · 实测主力）

> Web 有实测发布/作者，通常无互动数属正常。官方 5 页 = 事实锚定；第三方 = 结构范本与外部视角。

### #1 OpenAI 官方「CLI — Codex」— 起手锚点
- `developers.openai.com/codex/cli` · OpenAI 官方 · 活文档
- 核心：安装 / 登录 / Codex 是什么，任何上手指南的脊柱。
- **写作风格拆解：reference tutorial，祈使句 + 可复制命令块。** 学它的「命令块骨架」，但补中文解释。

### #2 官方「Custom instructions with AGENTS.md」
- `developers.openai.com/codex/guides/agents-md` · OpenAI 官方
- 核心：三级优先级 + 旋钮。
- **写作风格拆解：how-to，先概念后配置、分层示例。** 中文指南可直接对标这个结构。

### #3 官方 Configuration Reference / Config basics
- `developers.openai.com/codex/config-basic`（+ `/config-reference` `/config-advanced`）· OpenAI 官方
- 核心：`approval_policy` / `sandbox_mode` / `model` / MCP。
- **写作风格拆解：干枯穷举 reference —— 挖数据，别学它的声音。**

### #4 官方 Changelog
- `developers.openai.com/codex/changelog` · OpenAI 官方 · 持续更新
- 核心：带日期的功能投放。
- **写作风格拆解：倒序 release notes，一段一功能 —— 「2026 有什么新」章节的完美来源。**

### #5 freeCodeCamp「The Codex Handbook」（第三方 · 最佳结构范本）
- `freecodecamp.org/news/the-codex-handbook-a-practical-guide-to-openai-s-coding-platform/` · 2026
- 核心：跨 surface 端到端实操。
- **写作风格拆解：长篇结构化 handbook —— 最接近 vfan 要写的形态，重点研究它的章节排序。**

### #6 Simon Willison — /tags/codex（第三方 · 高信号独立视角）
- `simonwillison.net/tags/codex/` · 2026 持续
- 核心：**公开从 Claude Code 切换到 Codex 当日常主力**；犀利 practitioner 观点。
- **写作风格拆解：观点 + 亲手 micro-benchmark，怀疑派、金句多 —— 引一个可信外部声音的最佳来源。**

### #7 Codex vs Claude Code 2026（第三方 · 对比范本）
- `blakecrosley.com/blog/codex-vs-claude-code-2026`（+ mindstudio.ai · morphllm.com）· 2026
- 核心：架构/定价/benchmark 对比（SWE-bench vs Terminal-Bench 框架）。
- **写作风格拆解：comparison/benchmark listicle —— 「vs Claude Code」表的好底子，但所有数字都要核。**

## 4. X / Twitter — Top 3（增长轴 · 渠道层）

> [!warning] 本节互动全「推断·未实测」（本机无 bird）。仅 @OpenAIDevs 一条 URL 直接核实；其余 handle/URL best-effort，勿在正文归因具体 handle 前不核。

### #1 @OpenAIDevs — 官方 GPT-5.5×Codex 发布
- `x.com/OpenAIDevs/status/2047381283358355706` · ~2026-04-23 · thread · 互动**推断·未实测**（官方发布，反推高）
- 核心：*"With GPT-5.5, Codex now gets more of the job done across the browser, files, docs, and your computer…"* 扩展 browser use。
- **写作风格拆解：官方公告 thread，收益导向 + 截图/视频。**

### #2 @simonw（Simon Willison）
- handle `x.com/simonw`（具体贴 URL best-effort/未核）· 2026 · 单帖 + 博客交叉链
- 核心：公开 Claude Code → Codex 迁移；对 Anthropic 定价的批评。
- **写作风格拆解：简短 practitioner hot-take，回链长博客 —— dev 受众可信度高。**

### #3 「AGENTS.md 才是杠杆」实操派（聚合观点，handle 未核）
- 经第三方博客（ofox.ai/webscraft 等）转述 · 2026 · thread · 互动**推断·未实测**
- 核心：反复出现的 meme——*"杠杆不是模型，是那 30 行 AGENTS.md"* + *"并行开 3–4 个 worktree，GPT-5.5 思考、5.4-mini 干无聊活"*。
- **写作风格拆解：观点型 workflow thread。** ⚠️ 原帖作者/URL 未核实，勿归因具体 handle。

## 5. YouTube — Top 3（增长轴 · 渠道层）

> [!warning] 观看全「推断·未实测」（本机无 summarize/last30days）。**诚实说：YouTube 量大但无单一权威视频**，全是中腰部教程，日期/频道/观看均未核，仅作 leads。

### #1「The ULTIMATE Beginner's Guide to OpenAI Codex（3-Hour Course）」
- `youtube.com/watch?v=lmGX79cumyw` · 频道未核 · ~2026-05-15 · 观看**推断·未实测** · **实操重**
- **写作风格拆解：长篇完整课程，屏幕共享 build-along —— 综合指南的结构参考。**

### #2「How to Install OpenAI Codex — Desktop App, CLI, and Extensions」
- `youtube.com/watch?v=KkUmD1TH3UQ` · ~2026-06 · 观看**推断·未实测** · **实操（装/配为主）**
- **写作风格拆解：逐步 setup 录屏，覆盖全 surface —— 对应「安装&起手」读者需求。**

### #3「The Ultimate Codex Tutorial: For Beginners 2026」
- `youtube.com/watch?v=0TitiOk7hbI` · ~2026-05-24 · 观看**推断·未实测** · **实操、中长度**
- **写作风格拆解：新手教程，任务驱动 demo。**

> [!note] 渠道洞察
> **中文实操视频近乎蓝海**：英文中腰部教程已饱和，但没人占「权威」位；中文的「按官方核验 + 诚实讲模型命名」视频几乎无人做。

## 6. 核心洞察 + 最佳实践

**洞察一：我们的深度错位——方法论满仓、上手空仓。** vault 把 `/goal`/loop/hooks/skills 讲穿了，但**没有一份「装好 Codex 干第一件事」的指南**。缺口不在深度，在**入口**。[内部/Tier-1: source-openai-codex-cookbook-trilogy]

**洞察二：Codex 的杠杆在配置层不在模型层。** 官方文档 + 实操派一致指向 **AGENTS.md + config.toml（approval/sandbox/model）+ worktree 并行** 才是真正拉开差距的地方——「30 行 AGENTS.md > 换模型」。[外部: developers.openai.com/codex/guides/agents-md]

**洞察三：模型命名是当前最大的读者困惑点。** GPT-5.5（frontier 默认）vs 弃用中的「-Codex」后缀模型——没人讲清，诚实梳理 = 差异化。[外部: developers.openai.com/codex/models]

**洞察四：平视而非「谁更强」。** hooks/skills/subagents/cloud 已跨厂商对位；对 Claude Code 用户，正确框架是「同一套心智，换个 CLI 10 分钟上手」，而非 benchmark 口水战。[内部/Tier-1: source-openai-codex-hooks-docs]

**最佳实践清单（可进正文/角度）：**
1. 先写 AGENTS.md（项目根），再让 Codex 动手——「agent 动前先读它」。
2. 起步用 `sandbox_mode = workspace-write` + `approval_policy = on-request`，别一上来 `danger-full-access`。
3. 默认 `model = gpt-5.5`；无聊批量活切 `gpt-5.4-mini` 省钱。
4. 长任务用 Cloud surface / worktree 并行，本地关机不影响。
5. 把 spec 里的「不要动」用 hooks 变成「动不了」（exit 2 拦截）。[内部/Tier-1: source-openai-codex-hooks-docs]
6. 数字类 claim（定价档位/计费变更日期）以 `developers.openai.com/codex/pricing` 为准，第三方数字先核。

## 7. 对内容创作的启示 — 增长轴 → 排序的内容角度

> 锚 audience-profile：全背景 AI builder（能上手非资深）· 中文为主体 · 具体压笼统 · GEO 规则（官方引用 +40%、数字 +37%、前置定义、可扫描）。

### 时机窗口
- Codex 2026 上半年**功能井喷**（GPT-5.5 4/23、hooks GA 5/14、Remote GA 6/25），英文教程已饱和但**中文权威上手指南仍空白**。现在（7/6）是**中文首发窗口正当时**——抢「按官方核验的中文 Codex 指南」这个位。
- ⚠️ 模型/定价变动快：发稿前核 `developers.openai.com/codex/{models,pricing,changelog}` 当前状态。

### 排序的内容角度（每个 = 一个内容赌注）

#### 角度1（推荐）「OpenAI Codex 上手指南：从装到跑第一个任务，全部按官方核验」
- **缺口**：中文世界没有一份**诚实、逐条对官方核验**的 Codex 上手指南；英文有 freeCodeCamp handbook，中文空白。vault 自己也只有方法论、没有入口。
- **受欢迎度证据**：YouTube 大量 beginner 教程（推断量大）+ freeCodeCamp handbook 存在 = 需求确凿；但都在英文/视频，中文长文位空。
- **参考写法**：骨架学 freeCodeCamp handbook 的章节排序（是什么 → 装 → 四 surface → AGENTS.md → config → 模型选择 → vs Claude Code），命令块学官方 CLI 页，但**每步补中文解释 + 踩坑**。
- **渠道 + 形式**：博客长文（GEO 主场）→ 切 X 中文 thread + 中文 YouTube 实操（视频位空）。
- **依赖**：§1 全部 ✅ 事实 · §2 模型命名 · 候选源官方 9 页 · `<!-- GEO: 每个 claim 挂 developers.openai.com 链接 + 定价/token 数字 -->`

#### 角度2「Codex 用哪个模型？GPT-5.5 与那些『-Codex』后缀模型，到底谁是谁」
- **缺口**：模型命名混乱（5.5 frontier vs 弃用的 5.2/5.3-Codex），**没人讲清**；这是读者第一个卡点。
- **受欢迎度证据**：命名困惑在评论区/第三方反复出现（推断）；「省 40% token」是可核验数字钩子。
- **参考写法**：学 Simon Willison 的「亲测 + 怀疑派」，以「哪些型号还能选、哪些没了、默认该用哪个」为一图流。
- **渠道 + 形式**：博客中篇 + 一张模型对照表（可扫描，GEO 友好）。
- **依赖**：§2 全部 ✅ · [外部: developers.openai.com/codex/models · changelog]

#### 角度3「Claude Code 用户 10 分钟上手 Codex：一套心智，换个 CLI」
- **缺口**：对已用 Claude Code 的人，没人写「同一套 hooks/skills/subagents/`/goal` 概念怎么平移」。
- **受欢迎度证据**：Simon Willison 公开切换叙事有传播力（推断）；vault 旧判断①「跨厂商收敛」正好背书。
- **参考写法**：对照表（Claude Code 概念 → Codex 对应），学 vs-Claude-Code listicle 但**平视不打架**。
- **依赖**：§0 旧判断①② · [内部/Tier-1: source-openai-codex-hooks-docs · source-openai-codex-skills-docs] · [外部: 官方 config/hooks 页]

### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
|---|---|---|
| Simon Willison | 独立高信号 practitioner | Claude Code→Codex 切换叙事 + 亲测 |
| @OpenAIDevs | OpenAI 官方 | 功能发布一手源 |
| Chris Hayduk | OpenAI FDE | Codex `/goal` insider（vault 已有页）|

### 内容形式参考库
- **长文/handbook** → 学 freeCodeCamp Codex Handbook（章节排序）
- **观点+亲测** → 学 Simon Willison（怀疑派 + micro-benchmark）
- **命令块骨架** → 学官方 CLI 页（祈使句 + 可复制）
- **对比表** → 学 codex-vs-claude-code listicle（但数字必核 + 平视）

## 附录：关键时间线

| 日期 | 事件 |
|---|---|
| 2025-05 | 旧「云端-only」Codex 上线（GPT-5 家族）—— 已被 2026 四-surface 产品取代 |
| ~2026-04-02 | （第三方）计费从 per-message 转 token/credit —— ⚠️ 待官方核 |
| ~2026-04-09 | （第三方）Pro 5× $100 档加入 —— ⚠️ 待官方核 |
| **2026-04-23** | **GPT-5.5 进入 Codex**（~省 40% 输出 token）[外部: openai.com/index/introducing-gpt-5-5] |
| **2026-05-14** | **Codex Hooks GA**（CLI 0.131 同期）[内部/Tier-1: source-openai-codex-hooks-docs] |
| ~2026-05-29 | Windows 上 Computer Use |
| ~2026-06-02 | Sites 插件 |
| ~2026-06-18 | Record & Replay → 演示即 skill（macOS，排除 EEA/UK/CH）|
| **~2026-06-25** | **Codex Remote GA**（手机端控主机 + QR 配对）|
| 2026-07-06 | 本报告生成 |
