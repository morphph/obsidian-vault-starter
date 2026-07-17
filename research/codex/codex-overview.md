# 一文了解 Codex

> Codex 常青报告 · 基础/概览篇 · 最后更新 2026-07-17
> 定位:读完这一篇,你知道 **Codex 有哪些功能、各是什么、大致怎么用**。想把它压榨成自主 agent 平台,看姊妹篇《Codex 进阶实战》(`codex-advanced.md`)。
> 官方文档:`learn.chatgpt.com/docs/*`(Codex 文档已并入 ChatGPT Learn)。

**一句话:** Codex 是 OpenAI 的**智能编码 agent(agentic coding agent)**——「读、改、跑你机器上的代码」,**开源、用 Rust 写的**。它不是"IDE 里的高级补全",而是一个能自己动手、能并行、能无人值守长跑的 agent。[官方](https://learn.chatgpt.com/docs/cli)

**谁该读:** 已经会用 Claude Code / Cursor / API,想快速摸清 Codex 全貌的 AI builder。

---

## 1. 四个 surface:一个产品,四个入口,共享同一套配置

Codex 不是单一 CLI,而是**四个入口共享同一套 approval policy / MCP / AGENTS.md / 模型偏好**。选哪个取决于你是谁:

| Surface | 是什么 | 适合谁 |
|---|---|---|
| **CLI**(终端) | 干真活的主力入口,可脚本化 | 独立 builder |
| **IDE 扩展** | VS Code + JetBrains;也能在 Cursor / Windsurf 里跑 | 活在编辑器里的人 |
| **桌面 App** | 现已并入 **ChatGPT 桌面 App**(2026-07-09 起);并行 thread + worktree + diff 审阅 + Scheduled tasks | 想同时开多条任务线的人 |
| **Codex Cloud** | 对 GitHub repo 跑后台/长任务,本地关机不影响 | 团队、长耗时任务 |

> 你在 AGENTS.md 和 config.toml 上花的功夫,四个 surface 通吃。[官方 · IDE](https://learn.chatgpt.com/docs/ide)

---

## 2. 装 & 登录:一行搞定

macOS / Linux,二选一:

```bash
# 方式 A:官方 installer(推荐)。无人值守/CI 加 CODEX_NON_INTERACTIVE=1
curl -fsSL https://chatgpt.com/codex/install.sh | sh
# 方式 B:npm(需 Node ≥ 22)
npm i -g @openai/codex
```

装完终端敲 `codex` 起。**首次运行**会让你选:用 **ChatGPT 账号**登录,**或**填 **API key**。[官方 · CLI](https://learn.chatgpt.com/docs/cli)

---

## 3. 配置基础:AGENTS.md + config.toml

Codex 的杠杆在配置层,不在模型层。两份文件先懂:

### AGENTS.md —— 告诉 Codex "项目长什么样"
Codex 动手前先读的 markdown 指令文件,**三级优先级**从远到近层层拼接、近的覆盖远的:
1. **Global** —— `~/.codex/AGENTS.md`(所有项目通用偏好)
2. **Project** —— repo 根一路往下到当前工作目录
3. **拼接** —— 从 root 向下逐层合并,离 cwd 越近优先级越高

旋钮:`project_doc_max_bytes`、`project_doc_fallback_filenames`(fallback 顺序 `AGENTS.override.md → AGENTS.md → TEAM_GUIDE.md → .agents.md`)。[官方 · AGENTS.md](https://learn.chatgpt.com/docs/agents-md)

### config.toml —— 告诉 Codex "你允许它干到什么程度"
- **用户级** `~/.codex/config.toml` · **项目级** `.codex/config.toml`(覆盖) · 状态目录 `CODEX_HOME`(默认 `~/.codex`) · CLI `-c key=value` 单次覆盖。

三个最该懂的键:

```toml
model = "gpt-5.6-sol"            # 默认模型(见 §4)
approval_policy = "on-request"   # untrusted / on-request / never
sandbox_mode = "workspace-write" # read-only / workspace-write / danger-full-access
```

> [!tip] 起步别一上来 full-access
> 新手先用 `sandbox_mode = workspace-write` + `approval_policy = on-request`(能改工作区、但每步问你一句),摸清脾气再放宽。[官方 · config](https://learn.chatgpt.com/docs/config-file/config-reference)

---

## 4. 用哪个模型:GPT-5.6 家族

**当前默认 = `gpt-5.6-sol` @ medium reasoning。** GPT-5.6 是 Sol / Terra / Luna 家族(2026-07 起为 Codex 默认线)。

| 模型 | 定位 | 什么时候用 |
|---|---|---|
| **gpt-5.6-sol** | 当前默认 | 大多数任务 |
| **gpt-5.6** | frontier | 要求最高的 agent 活 |
| **gpt-5.6-terra** | 更快更便宜 | 较轻的 subagent / 并行 worker |
| **gpt-5.4 / gpt-5.4-mini** | 上一代 / 便宜快 | 回退 / 无聊批量活 |
| **gpt-5.3-codex-spark** | 更快变体 | research preview(Pro) |
| ~~gpt-5.2 / gpt-5.3-codex~~ | **已弃用** | 对 ChatGPT 登录用户已下架 |

> **命名分两条线**:通用 frontier 线(gpt-5.4 / 5.6,现在驱动 Codex)vs 旧的「-Codex」后缀模型(5.2/5.3-Codex,退场中)。方向是统一到 frontier 模型,专用后缀退场。默认选 gpt-5.6-sol 就对了。[官方 · models](https://learn.chatgpt.com/docs/models)

---

## 5. 功能一览:Codex 有哪些能力

> 每个功能给"是什么 + 能干嘛 + 最小例"。**怎么深配、逐字 TOML、组合成自主流水线 → 看《Codex 进阶实战》。**

### Subagents(子智能体)—— 并行拆活、保持主上下文干净
**是什么:** 让主 agent 派生出多个子 agent 并行干活(执行/探索),互不污染上下文。靠 `[features] multi_agent = true` 开(**默认已开**)。
**能干嘛:** 把一个大任务拆成几路并行;内置三类 `default`(兜底)/`worker`(执行修复)/`explorer`(只读探索)。
**最小例:** config 里控并行度——

```toml
[agents]
max_threads = 6     # 默认 6
max_depth = 1       # 默认 1(允许一层子 agent)
```
[官方 · subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

### MCP —— 接外部工具
**是什么:** Codex 支持 MCP(Model Context Protocol),把外部工具/数据源接进来。
**能干嘛:** 接 Context7、Figma、你自建的 MCP server 等,给 Codex 额外能力。
**最小例:** 一条命令接一个 stdio server——

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp
```
配置写在 `~/.codex/config.toml` 的 `[mcp_servers.<name>]` 表(**不是** `[mcp]` 块;逐字语法见进阶篇)。[官方 · MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

### Hooks —— 把"约定"变"强制"
**是什么:** 在 agent 生命周期的关键时刻(**共 10 个事件**,如 `PreToolUse`/`PostToolUse`/`Stop`)插入你的脚本。
**能干嘛:** 把 AGENTS.md 里那句"不要动 `migrations/`"从**约定**变**强制**——hook 脚本 `exit 2` 直接拦下动作。
**最小例:** 在 Bash 命令执行前跑一个策略检查脚本(逐字 TOML 见进阶篇)。企业可用 `requirements.toml` 托管。[官方 · hooks](https://learn.chatgpt.com/docs/hooks)

### Skills(技能)—— 可复用、可移植的能力包
**是什么:** 遵循 **Agent Skills 开放标准**(agentskills.io,与 Anthropic Skills 同标准)的能力包:一个含 `SKILL.md` 的目录(+ `scripts/`/`references/` + Codex 专属 `agents/openai.yaml`)。
**能干嘛:** 把一套流程/知识封装成可 `$skill` 显式调用的技能;渐进披露(元数据启动加载 → 指令激活加载 → 资源按需)。
**最小例:** 输入 `$skill-creator` 造新技能,或 `/skills` 管理。[官方 · skills](https://learn.chatgpt.com/docs/build-skills)
> ⚠️ Skills 官方未打 "GA" 标签(已发布未标注)。

### Scheduled tasks(定时任务)—— 无人值守跑
**是什么:** 让 Codex 按计划自动跑(旧称 "Automations",官方已改名)。两型:**standalone**(每次起新 chat)/**chat 内**(复用上下文,支持分钟级跟进)。
**能干嘛:** 定时评审、定时同步、主动跟进循环;可跑在隔离的 **worktree** 里、组织策略允许时自动用 `approval_policy = "never"`。
**最小例:** App 内用 **RRULE(RFC 5545)** 排期,如每月 1 号 9 点 `RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`;CLI headless 则用 `codex exec` 接你自己的 cron/GitHub Actions。[官方 · scheduled tasks](https://learn.chatgpt.com/docs/automations)
> ⚠️ App 内调度是 **RRULE 不是 cron**;cron 只在 CLI 路径。

### Codex Cloud —— 后台/长任务
**是什么:** 在 `chatgpt.com/codex` 对 GitHub repo 跑并行云环境任务,本地关机不影响。
**能干嘛:** 无人值守后台跑;从 GitHub PR / Linear / Slack 启动;`@codex review` / `@codex fix` 直接在 PR 上用。容器缓存 **最长 12 小时**;setup 阶段有网、agent 阶段默认无网,secrets 只给 setup。
**最小例:** GitHub PR 里评论 `@codex review` → 拿到 👀 + 行内发现 + PR 级总结。[官方 · cloud](https://learn.chatgpt.com/docs/cloud) · [GitHub](https://learn.chatgpt.com/docs/third-party/github)

### Codex Remote —— 手机控主机
**是什么:** 用手机上的 ChatGPT 控制你主机上的 Codex(**2026-06-25 GA**)。手机是**控制面,不是第二个 Codex**——主机提供环境,手机发 prompt/审批/后续。
**能干嘛:** 长任务远程盯梢、随手审批。二维码配对(桌面 App 生成 QR,扫码连接,认证一对一),secure relay 不把主机暴露公网。
**最小例:** 桌面 App 生成 QR → 手机 ChatGPT 扫码 → 手机上盯长任务。[官方 · remote](https://learn.chatgpt.com/docs/remote-connections)

---

## 6. 给 Claude Code 用户:一套心智,换个 CLI

hooks / skills / subagents / cloud 这些概念已跨厂商收敛,几乎一一对位。别打 benchmark 口水战,平视用:

| Claude Code | Codex |
|---|---|
| CLAUDE.md | **AGENTS.md**(三级优先级) |
| 权限/审批模式 | **approval_policy**(untrusted/on-request/never) |
| 沙箱 | **sandbox_mode**(read-only/workspace-write/danger-full-access) |
| hooks | **hooks**(10 事件, exit 2 拦截) |
| skills / subagents | **Codex skills / subagents**(同 agentskills.io 标准) |
| 后台/云端任务 | **Codex Cloud** + **Remote** |

把 CLAUDE.md 心智搬进 AGENTS.md,权限直觉映射到 approval_policy + sandbox_mode,剩下的就是换套命令。

---

## 7. 延伸

- **想榨干 Codex** → 姊妹篇《Codex 进阶实战:当自主 agent 平台压榨》(`codex-advanced.md`):subagents 并行深配、无人值守、长时任务四文件法、逐字 TOML 金料、`/goal` loop 方法论。
- **方法论层**(vault 已有):`/goal` + 三层嵌套 loop、Chris Hayduk 的 `/goal` 三招、PLANS.md 多小时长任务。
- **追新唯一权威**:[learn.chatgpt.com/docs/changelog](https://learn.chatgpt.com/docs/changelog)。

---

## 更新记录

| 日期 | 变更 | 官方来源 |
|---|---|---|
| 2026-07-17 | **初版**:合并旧(`research/openai-codex`)+新(`research/codex-advanced-guide`)调研,校准到当前状态——默认模型 `gpt-5.6-sol`、文档迁 `learn.chatgpt.com/docs/*`、"Automations"改名"Scheduled tasks"(RRULE)、hooks 10 事件、MCP `[mcp_servers]` 表、桌面 App 并入 ChatGPT App、Codex Remote GA(06-25) | learn.chatgpt.com/docs/{models,changelog,automations,hooks,extend/mcp} |
