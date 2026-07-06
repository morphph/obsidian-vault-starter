---
status: draft
lang: zh
sources:
  - raw/2026-05-14-openai-codex-hooks-docs.md
  - raw/2026-05-05-openai-blog-long-horizon-tasks-codex.md
  - raw/2025-10-07-openai-cookbook-plans-md-multi-hour.md
  - raw/2026-05-09-openai-cookbook-using-goals-in-codex.md
external-refs:
  - https://developers.openai.com/codex/cli
  - https://developers.openai.com/codex/ide
  - https://developers.openai.com/codex/guides/agents-md
  - https://developers.openai.com/codex/config-basic
  - https://developers.openai.com/codex/config-reference
  - https://developers.openai.com/codex/models
  - https://developers.openai.com/codex/mcp
  - https://developers.openai.com/codex/pricing
  - https://developers.openai.com/codex/changelog
  - https://openai.com/index/introducing-gpt-5-5/
research: research/openai-codex/
platform: blog
created: 2026-07-06
last-updated: 2026-07-06
tags: [draft]
---

<!-- HOOK: [placeholder for opening hook —— 建议用「装 Codex 只要一行，可我第一次跑它照样翻车」的反差开场] -->

# OpenAI Codex 上手指南：从装到跑第一个任务，全部按官方核验

**先给结论（谁该读、读完能干嘛）：** 如果你已经会用 Claude Code / Cursor，想把 OpenAI Codex 加进工作流，这篇按官方文档逐条核验的中文指南能带你从「装」走到「跑通第一个任务」。但真正想传给你的一句话是——

> **Codex 上手的真门槛不是装，而是心智模型。** 装只要一行命令；大多数人第一次用不顺，是因为把它当成「IDE 里的高级补全」，讲浅了、也用浅了。Codex 是一个**能读、能改、能在你机器上跑代码的 agent**——你要做的第一件事不是敲提示词，而是**先给它写一份 AGENTS.md，再让它动手**。这份指南所有的重量，都压在「配置层」这三个字上。

**Codex 是什么（一句话定义）：** Codex 是 OpenAI 的**智能编码 agent（agentic coding agent）**，官方定义是「读、改、跑你机器上的代码」，**开源、用 Rust 写的**。[官方 · developers.openai.com/codex/cli](https://developers.openai.com/codex/cli)

> [!warning] 别搞混版本
> 网上不少第三方页面还把 Codex 说成「2025 年 5 月上线的云端自主 agent、GPT-5 家族驱动」——那是**旧的、云端 only 的 2025 版 Codex**。2026 年的 Codex 是一个 **CLI 优先、四个入口** 的平台。看到「云端 only / 2025-05 launched」的描述，对当前产品是过时的。

---

## 一、四个 surface：一个产品，四个入口，共享同一套配置

Codex 不是单一 CLI，而是**四个 surface（入口）共享同一套 approval policy / MCP / AGENTS.md / 模型偏好**。选哪个取决于你是谁：

| Surface | 是什么 | 适合谁 |
|---|---|---|
| **CLI**（终端） | 干真活的主力入口 | 独立 builder、想要可脚本化的人 |
| **IDE 扩展** | VS Code + JetBrains；也能在 Cursor / Windsurf 里跑 | 已经活在编辑器里的人 |
| **Desktop App** | macOS / Windows；并行 thread + 每 thread 一个 worktree + diff 审阅 + automations | 想同时开多条任务线的人 |
| **Codex Cloud** | 对 GitHub repo 跑后台 / 长任务，本地关机不影响 | 团队、长耗时任务 |

[官方 · developers.openai.com/codex/ide](https://developers.openai.com/codex/ide) · [/codex/cli](https://developers.openai.com/codex/cli)

**角色化提示：** 如果你是**独立 builder**，CLI + App 就够了；如果你是**团队 lead**，Cloud 才是给你准备的（后台跑、审 diff、自动化）。但记住——**四个入口的配置是同一套**，你在 AGENTS.md 和 config.toml 上花的功夫，四个 surface 通吃。

---

## 二、装 & 登录：真的只要一行

macOS / Linux，二选一：

```bash
# 方式 A：官方 installer（推荐）
curl -fsSL https://chatgpt.com/codex/install.sh | sh
# 无人值守 / CI 里加环境变量：
CODEX_NON_INTERACTIVE=1 curl -fsSL https://chatgpt.com/codex/install.sh | sh

# 方式 B：npm（需要 Node ≥ 22）
npm i -g @openai/codex
```

装完，终端里敲一下就起：

```bash
codex
```

**登录：** 首次运行会让你选——用 **ChatGPT 账号** 登录，**或**填 **API key**。[官方 · developers.openai.com/codex/cli](https://developers.openai.com/codex/cli)

看到这里你可能想说「就这？」——对，装就是这么简单。**这恰恰是我要提醒你的：装完的你，离『会用』还差一份 AGENTS.md。** 下面才是正戏。

---

## 三、跑第一个任务：先写 AGENTS.md，再让它动手

新手最容易犯的错，是装完直接对着空 repo 敲一句「帮我加个登录功能」。Codex 会动手，但它对**你的项目约定一无所知**——命名、目录结构、哪些文件不能碰、用什么测试框架。

正确顺序是：

1. **先在项目根写一份 AGENTS.md**（下一节给最小模板）——这是 Codex 动手前会先读的说明书。
2. **再交任务。** 任务描述里给「量化的完成标准」而不是「感觉对就行」。
3. 复杂 / 长任务，用 `/goal` 把目标拆成可验证的 loop——这套「Goal → Repair → Improvement」三层循环的方法论 vault 里已经讲透，本文不重复，只提醒你：`/goal` 是把「一句话需求」变成「agent 能自我验证的闭环」的开关。（延伸阅读见文末）

一句话：**Codex 不缺执行力，缺的是你把项目上下文喂给它。** 而喂上下文的标准动作，就是 AGENTS.md。

---

## 四、AGENTS.md：真正的杠杆

这一节是全文的重心。实操圈里流传一句 meme——**「杠杆不是模型，是那 30 行 AGENTS.md」**——它是对的。

**AGENTS.md 是什么：** Codex 动手前先读的 markdown 指令文件。它有**三级优先级**，从远到近层层拼接、近的覆盖远的：

1. **Global** —— `~/.codex/AGENTS.md`（你所有项目的通用偏好）
2. **Project** —— repo 根一路往下到当前工作目录
3. **拼接规则** —— 从 root 向下逐层合并，离 cwd 越近的指令优先级越高

几个旋钮值得知道：`project_doc_max_bytes`（读多大）、`project_doc_fallback_filenames`；fallback 文件名顺序是 `AGENTS.override.md → AGENTS.md → TEAM_GUIDE.md → .agents.md`。[官方 · developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)

> [!note] 别写死「行业标准」
> 有人说 AGENTS.md 是「跨工具行业标准」——官方只把它当 **Codex 的特性**讲（提到有个 agents.md 站点，但没宣称全行业采用）。所以别在文里写成「行业标准」，那是未坐实的说法。

**一份可复制的最小 AGENTS.md 模板：**

```markdown
# AGENTS.md

## 项目约定
- 语言 / 框架：<例如 TypeScript + Next.js>
- 目录结构：src/ 放业务，tests/ 放测试，别在根目录建新目录
- 命名：组件用 PascalCase，工具函数用 camelCase

## 动手前必读
- 改动后必须跑 `npm test`，全绿才算完成
- 不要碰 `migrations/` 和 `.env*`
- commit message 用祈使句，描述改了什么

## 完成标准
- 功能可跑通 + 测试通过 + 无 lint 报错
```

**为什么说它是杠杆：** 官方文档和实操派一致指向——**AGENTS.md + config.toml + worktree 并行**才是拉开差距的地方，而不是「换个更强的模型」。你花十分钟写清 30 行约定，比你纠结用 5.5 还是 5.4 的收益大得多。

---

## 五、config.toml：approval / sandbox / model 三个旋钮

如果 AGENTS.md 是「告诉 Codex 项目长什么样」，config.toml 就是「告诉 Codex 你允许它干到什么程度」。

配置文件位置：
- **用户级** —— `~/.codex/config.toml`
- **项目级** —— `.codex/config.toml`
- 状态目录在 `CODEX_HOME`（默认 `~/.codex`）
- CLI 里 `-c key=value` 单次覆盖

三个最该懂的键：

```toml
model = "gpt-5.5"              # 默认模型
approval_policy = "on-request" # untrusted / on-request / never
sandbox_mode = "workspace-write" # read-only / workspace-write / danger-full-access
```

[官方 · developers.openai.com/codex/config-basic](https://developers.openai.com/codex/config-basic) · [完整穷举见 /config-reference](https://developers.openai.com/codex/config-reference)

> [!tip] 起步别一上来 full-access
> 新手最该记的一条实践：**起步用 `sandbox_mode = workspace-write` + `approval_policy = on-request`**，别一上来就 `danger-full-access`。前者让 Codex 能改工作区、但每步动作前问你一句；等你摸清它的脾气，再放宽。

---

## 六、用哪个模型：GPT-5.5 与那些「-Codex」后缀，到底谁是谁

这是读者第一个真正会卡住的地方，也是我认为最值得诚实讲清的一节。

**当前默认 = GPT-5.5。** 2026-07 时点，Codex 大多数任务推荐用它；约 2026-04-23 起进入 Codex；同一个任务，比 GPT-5.4 **少约 40% 输出 token**——这不是玄学，是可核验的省钱数字。[官方 · developers.openai.com/codex/models](https://developers.openai.com/codex/models) · [GPT-5.5 发布](https://openai.com/index/introducing-gpt-5-5/)

**模型对照表：**

| 模型 | 定位 | 什么时候用 |
|---|---|---|
| **GPT-5.5** | 当前默认、frontier 线 | 大多数任务，省 token |
| **GPT-5.4** | 上一代 frontier | 需要时可回退 |
| **GPT-5.4 mini** | 便宜、快 | 无聊的批量活，省钱 |
| **GPT-5.3-Codex-Spark** | 更快变体 | research preview（Pro 专享） |
| ~~GPT-5.3-Codex / GPT-5.2~~ | **已弃用** | 对 ChatGPT 登录用户已下架 |

**命名陷阱（这才是重点）：** 你要分清两条线——
- **通用 frontier 线**：GPT-5.4 / **5.5**，现在驱动 Codex；
- **旧的「-Codex」后缀模型**：GPT-5.2-Codex / 5.3-Codex，**正在被弃用、取代**。

2026 的方向很清楚：**统一到通用 frontier 模型（5.5），专用的「-Codex」后缀退场。** 所以你在别处看到「5.3-Codex」之类的名字，多半是过时信息——默认选 GPT-5.5 就对了。[官方 · developers.openai.com/codex/models](https://developers.openai.com/codex/models) · [changelog](https://developers.openai.com/codex/changelog)

**顺带说定价**（随 ChatGPT plan 附带）：Free $0 · **Go $8** · **Plus $20** · **Pro 起 $100**（比 Plus 高 5× / 20× rate limit）· Business $20/座 · Enterprise / Edu 定制；也支持按 API key 用量计费。[官方 · developers.openai.com/codex/pricing](https://developers.openai.com/codex/pricing)（定价 / rate limit 变动快，下单前以官方页当前状态为准）

---

## 七、进阶一瞥：MCP / hooks / 2026 有什么新

摸熟了起手三件套（AGENTS.md + config + 模型），可以往这几个方向探：

- **MCP** —— Codex 支持 MCP，在 `config.toml` 里配 `[mcp]`，专门文档在 `/codex/mcp`。（精确 TOML 语法以官方页为准）[官方 · developers.openai.com/codex/mcp](https://developers.openai.com/codex/mcp)
- **Hooks** —— 把 AGENTS.md 里那句「不要动 `migrations/`」从**约定**变成**强制**：hooks 能在动作前拦截（exit 2 直接拦下），让「不要动」变成「动不了」。Codex Hooks 已于 **2026-05-14 GA**。[Tier-1 内部源 · raw/2026-05-14-openai-codex-hooks-docs.md]

**2026 上半年关键更新（时间线）：**

| 日期 | 事件 |
|---|---|
| **2026-04-23** | GPT-5.5 进入 Codex（约省 40% 输出 token） |
| **2026-05-14** | Codex Hooks GA |
| ~2026-05-29 | Windows 上 Computer Use |
| ~2026-06-02 | Sites 插件 |
| ~2026-06-18 | Record & Replay → 演示即可复用为 skill（macOS，排除 EEA/UK/CH） |
| **~2026-06-25** | Codex Remote GA（手机端控主机 + QR 一对一配对） |

[官方 · developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

---

## 八、给 Claude Code 用户：一套心智，换个 CLI

如果你已经是 Claude Code 老手，好消息是——**你不需要重学，只需要平移。** hooks / skills / subagents / cloud 这些概念已经跨厂商收敛，几乎一一对位。正确的框架不是「Codex vs Claude Code 谁更强」的 benchmark 口水战，而是「同一套心智，换个 CLI，10 分钟上手」。

| Claude Code 概念 | Codex 对应 |
|---|---|
| CLAUDE.md（项目说明） | **AGENTS.md**（三级优先级） |
| 权限 / 审批模式 | **approval_policy**（untrusted / on-request / never） |
| 沙箱 | **sandbox_mode**（read-only / workspace-write / danger-full-access） |
| hooks | **hooks**（2026-05-14 GA） |
| skills / subagents | Codex skills / subagents |
| 后台 / 云端任务 | **Codex Cloud** |

平移路径：把你的 CLAUDE.md 心智搬进 AGENTS.md，把权限直觉映射到 approval_policy + sandbox_mode，剩下的就是换套命令。**别打架，平视用。**

---

<!-- CTA: [placeholder for closing CTA —— 建议引导读者「先写好你的第一份 AGENTS.md，再回来跑任务」，并给 vault 方法论稿的延伸阅读入口] -->

## 收尾：门槛不在装，在你愿不愿意先配

回到开头那句话：**Codex 上手的真门槛不是装，而是心智模型。** 装是一行命令的事；把它当成能读改跑代码的 agent、先给它写 AGENTS.md 再让它动手——这才是把它用出杠杆的分水岭。

**延伸阅读（vault 方法论层，本文没展开的部分）：**
- `/goal` + 三层嵌套 loop（Goal → 完成 / Repair → 质量 / Improvement → 演化）——把「一句话需求」变成 agent 自我验证闭环的方法论。
- Chris Hayduk（OpenAI FDE）的 `/goal` 三招：量化目标 + 紧反馈 + 三文件。
- AGENTS.md + PLANS.md 组合，跑多小时长任务的实操。
