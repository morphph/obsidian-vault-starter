# Outline: OpenAI Codex 上手指南 —— 从装到跑第一个任务，全部按官方核验

> 基于角度: report §7 角度1（推荐）· 目标渠道/形式: 博客长文（中文为主体，GEO 主场）→ 切 X 中文 thread + 中文 YouTube 实操

## prior_coverage（强制字段 —— 对「已表达角度清单」逐条声明关系）

- **[[claude-code-goal]] / [[source-openai-codex-cookbook-trilogy]]（Codex `/goal` + 三层 loop 方法论）** → **不同角度**：本稿是**产品上手指南**（装/surface/AGENTS.md/模型），不重复 loop 方法论；`/goal` 仅在「跑第一个任务」一节一句带过并链回旧稿。
- **[[chris-hayduk]] / [[source-chrishayduk-codex-goals-effectively]]（`/goal` 三招 practitioner）** → **不同角度**：本稿不讲 goal 写法，只在延伸阅读处指向。
- **[[source-openai-codex-hooks-docs]] · [[source-openai-codex-skills-docs]] · [[source-openai-codex-subagents-docs]] · [[source-openai-codex-cloud-environments-docs]]（各工具面源页）** → **新证据推进 + 收编**：这些是**分散的 source-summary**，本稿**首次把它们收编成一份消费者向上手指南**（读者不会去读五个 source 页）。增量 = 入口整合 + 安装/config/模型这些源页没覆盖的「起手」内容。
- **[[source-openai-long-horizon-tasks-codex]] · [[source-openai-cookbook-plans-md]]（Prompt/Plan/Implement · AGENTS.md+PLANS.md）** → **穿透引用**：AGENTS.md 一节引其原始出处，不引 vault 页。
- 结论：**vault 有 Codex 方法论、无 Codex 上手指南 —— 本稿是首次覆盖「产品入口」这个面，不与任何已表达角度重合。**

## take 占位（Gate 1 由作者填，3–5 句）
> **作者 take（2026-07-06，Gate 1）：**
> 1. **Thesis**：Codex 上手的真门槛不是装，而是心智模型。
> 2. **不同意主流叙事**：大家把它当 IDE 补全来讲，讲浅了。
> 3. **对 AI builder 的含义**：先配 AGENTS.md，再跑第一个任务。
> 〔researcher 建议稿——已被上方作者 take 取代，仅存档，writer 勿采〕原建议：**「Codex 的门槛不在模型、在配置层：装只要一行，真正拉开差距的是 AGENTS.md + config.toml 那几十行。这份指南按官方逐条核验，顺带把没人讲清的模型命名（GPT-5.5 vs 弃用的 -Codex 后缀）理顺。」** 不同意主流叙事哪点：反对「Codex vs Claude Code 谁更强」的 benchmark 口水，主张对已有 Claude Code 用户是「一套心智换个 CLI」。对 AI builder 的含义：上手成本被高估，配置素养被低估。

## 结构（逐节：论点 + 挂哪些 report 论断/出处 + 预估篇幅占比）

1. **一句话价值 + 谁该读**（前置结论，倒金字塔）— 论点：Codex 是能读改跑代码的开源 agent，门槛在配置不在装。— 证据：[外部: developers.openai.com/codex/cli] — ~5%
   - GEO：开篇给一句干净定义「Codex 是……」。

2. **是什么 + 四个 surface**（角色化入口：独立 builder 用 CLI/App，团队用 Cloud）— 论点：一个产品四个入口，共享同一套配置。— 证据：[外部: /codex/cli · /codex/ide] report §1 — ~12%
   - GEO：四 surface 用对比表（可扫描）。

3. **装 & 登录**（可复制命令块）— 论点：一行装完。— 证据：`curl … install.sh | sh` / `npm i -g @openai/codex`（Node≥22）/ ChatGPT 账号或 API key [外部: /codex/cli] report §1 — ~10%

4. **跑第一个任务** — 论点：AGENTS.md 先写，再让它动手。`/goal` 一句带过 + 链回 [[claude-code-goal]]。— 证据：report §6 最佳实践 1 — ~10%

5. **AGENTS.md：真正的杠杆**（自包含段落）— 论点：三级优先级 + 「30 行 AGENTS.md > 换模型」。— 证据：[外部: /codex/guides/agents-md] report §1 + §6 洞察二 + §4 实操派 meme — ~15%
   - GEO：给一个可复制的 AGENTS.md 最小模板。

6. **config.toml：approval / sandbox / model** — 论点：起步用 workspace-write + on-request，别一上来 full-access。— 证据：[外部: /codex/config-basic] report §1 + §6 实践 2–3 — ~13%

7. **用哪个模型**（收编 report §2 焦点）— 论点：默认 GPT-5.5（省 40% token），分清 frontier 线 vs 弃用的 -Codex 后缀。— 证据：[外部: /codex/models · openai.com/index/introducing-gpt-5-5 · /codex/changelog] report §2 — ~12%
   - GEO：模型对照表 + 「省 40% 输出 token」数字。

8. **MCP / hooks / 2026 有什么新**（进阶一瞥）— 论点：spec 里的「不要动」用 hooks 变「动不了」；列 2026 关键更新。— 证据：[外部: /codex/mcp · /codex/changelog] [内部/Tier-1: source-openai-codex-hooks-docs] report §1 更新 + 附录时间线 — ~10%

9. **给 Claude Code 用户：一套心智换个 CLI**（角色化入口 + 平视对比）— 论点：概念一一对位，10 分钟平移。— 证据：report §0 旧判断①② + §7 角度3 依赖 — ~8%
   - GEO：Claude Code→Codex 概念对照表。

10. **收尾 + 延伸**（延伸阅读指回 vault 方法论稿：`/goal`、cookbook 三层 loop）— ~5%

> **GEO 落地提醒（给 /draft）**：outline 标了「此处对照表 / 此处官方链接 / 此处数字」的地方，正文**必须真填**对应链接（developers.openai.com/codex/*）和数字（省 40% token、定价档、Node≥22），否则 GEO 规则等于没生效。
> **溯源提醒**：writer 只穿透引用官方原始 URL，**不引用本报告**。定价/模型数字发稿前重核 changelog 当前状态。
