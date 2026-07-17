# 上手 Codex：从 Claude Code 迁过来，一天摸清全貌

> 版本日期：2026-07-17 · Codex 常青报告 · 基础/概览篇
> 适用对象：你已经会用 Claude Code / Cursor / API，能跑通脚本、读得懂 config，但不是资深 systems engineer。读完这一篇，你能说清 Codex 是什么系统、四个入口各管什么、跑通第一个真实任务，并知道每个功能大致怎么配。想把它压榨成能并行、能无人值守、能跑几十小时的自主 agent 平台，看姊妹篇《[压榨 Codex](codex-advanced.md)》。
> 信息基础：以 OpenAI 官方 `learn.chatgpt.com/docs/*` 为准（Codex 文档已并入 ChatGPT Learn）。能力与套餐变动很快，以文末官方索引为准。核验细节见同目录 `facts.md`。

**一句话：** Codex 是 OpenAI 的**智能编码 agent（agentic coding agent）**——它读、改、跑你机器上的代码，开源、用 Rust 写。它不是「IDE 里更聪明的补全」，而是一个能自己动手、能并行、能无人值守长跑的 agent。

---

## 1. 先建立心智模型：Codex 是一套系统，不是一个 CLI

理解 Codex 的第一步，是别把它想成一个命令行工具。它是一套**共享同一份配置、在多个运行表面上工作**的编码 agent 系统。你在 `AGENTS.md` 和 `config.toml` 上花的功夫，四个主要入口通吃——不管你从终端、编辑器、桌面 App 还是云端调它，读的是同一套 approval policy、MCP 配置和项目指令。

四个主入口按「你是谁、在干什么」来选，而不是按功能强弱来选：

- **CLI（终端）** 是干真活的主力，可脚本化，适合活在 shell / Git / tmux / SSH 里的独立 builder。
- **IDE 扩展**（VS Code、JetBrains，也能在 Cursor / Windsurf 里跑）适合边看代码边让 agent 改、贴着编辑器上下文迭代的人。
- **桌面 App**（2026-07-09 起并入 ChatGPT 桌面 App）更像一个任务控制台而非聊天窗口：并行多条 thread、worktree 隔离、diff 审阅、Scheduled tasks、手机远程，适合想同时开多条任务线的人。
- **Codex Cloud** 对 GitHub repo 跑后台/长任务，本地关机也不影响，适合团队和长耗时活。

要记住的边界是：这些入口**共享本机配置，但不共享执行环境**。本地、云端、远程主机的文件、凭证和工具不会凭空同步——「项目已经出现在 Codex 里」不等于「本地未提交的改动已经到了云端」。

**需求 → 入口决策表**（拿不准用哪个时，查这张）：

| 你要干的活 | 优先用 |
|---|---|
| 当前仓库里连续编码 | CLI 或 IDE 扩展 |
| 多项目、多任务、频繁 diff 审查 | 桌面 App |
| 手机上启动、查看、批准任务 | ChatGPT Mobile Remote |
| 托管的并行任务、GitHub 工作流 | Codex Cloud |
| CI、脚本、VPS 后台任务 | `codex exec` |
| 自建控制器 / Telegram bot / dashboard | Codex SDK |
| 深度集成自有客户端 | App Server |

## 2. 从你已知的 Claude Code 映射过来

好消息是 hooks / skills / subagents / cloud 这些概念已经跨厂商收敛，几乎一一对位。别陷进 benchmark 口水战，平视着用——你只是换一套命令，不是换一套心智。

**能力映射表**（Claude Code → Codex）：

| Claude Code | Codex | 主要用途 |
|---|---|---|
| `CLAUDE.md` | **`AGENTS.md`**（三级优先级） | 项目长期指令、命令、规范、完成标准 |
| `settings.json` | **`config.toml`** | 模型、推理强度、权限、MCP、Hooks、Agent 设置 |
| 权限 / 审批模式 | **approval_policy**（untrusted/on-request/never） | 何时向你请求授权 |
| 沙箱 | **sandbox_mode**（read-only/workspace-write/danger-full-access） | agent 实际能读改访问什么 |
| Skills | **Skills**（同 agentskills.io 标准） | 可复用、多步骤、带脚本/资源的工作流 |
| Subagents | **Subagents / Agent threads** | 并行探索、测试、审查、分析 |
| Custom agents | **Agent roles**（`.codex/agents/*.toml`） | 专门模型、推理级别、角色指令 |
| Hooks | **Hooks**（10 事件，`exit 2` 拦截） | 生命周期事件上跑脚本/检查 |
| Slash commands | **Custom Prompts 或 Skills** | 简单模板 or 完整工作流 |
| MCP | **MCP / Apps / Plugins** | 外部工具、实时数据、授权系统 |
| `claude -p` | **`codex exec`** | 非交互任务、CI、批处理 |
| Agent SDK | **Codex SDK / Agents SDK** | 程序化控制、多 agent 编排 |
| 后台任务 | **Goals / Scheduled tasks / Cloud tasks** | 长期、定时、托管执行 |

**职责边界清单**——最容易踩的坑不是不会某个功能，而是把东西放错层。用下面这套排他分配把它们各归各位：

- 当前任务的一次性要求：写在 **prompt** 里。
- 项目长期规范：写进 **`AGENTS.md`**。
- 个人或项目的运行默认值：写进 **`config.toml`**。
- 重复的多步骤方法：做成 **Skill**。
- 连接外部系统：用 **MCP** 或 **App connector**。
- 组合分发 Skills / MCP / Hooks：打成 **Plugin**。
- 机械性的安全拦截或生命周期动作：用 **Hook** 或 **Rule**。
- 可独立并行的工作：交给 **Subagents**。
- 固定时间重复执行：用 **Scheduled tasks**。
- 程序化、无人值守执行：用 **`codex exec`** 或 **SDK**。

> [!tip] 有现成的 Claude Code 配置？直接导入
> 桌面 App 的 `Settings > Import` 能从 Claude Code 导入：指令文件映射到 `AGENTS.md`、`settings.json` 映射到 `config.toml`，Skills、MCP、Hooks、Subagents、Slash commands 也一并搬过来。但这是**一次性导入，不是持续双向同步**——之后你在 Claude Code 新增的 Hook 或 Skill 不会自动出现在 Codex，且导入后要重点复查 Hook 脚本路径、MCP 认证、agent 工具权限这些副作用面。

## 3. 装 & 登录：一行搞定

macOS / Linux 二选一：

```bash
# 方式 A：官方 installer（推荐）。无人值守 / CI 加 CODEX_NON_INTERACTIVE=1
curl -fsSL https://chatgpt.com/codex/install.sh | sh
# 方式 B：npm（需 Node ≥ 22）
npm i -g @openai/codex
```

装完终端敲 `codex` 起。首次运行会让你选：用 **ChatGPT 账号**登录，或填 **API key**。

**处方：** 个人试验先用 ChatGPT 账号登录（走订阅额度、接入最简单）；CI 和服务端自动化才用 API key（按 API 用量计费）。判断规则：如果这是一台会长期无人值守跑任务的机器，用独立身份或 API project，别和你日常交互的登录共享额度。

## 4. 用哪个模型：GPT-5.6 家族

当前默认是 **`gpt-5.6-sol` @ medium reasoning**，大多数任务不用改。GPT-5.6 是 Sol / Terra / Luna 家族，2026-07 起成为 Codex 的默认线。选模型的核心判断是「难度 vs 成本」：

| 模型 | 什么时候用 |
|---|---|
| **gpt-5.6-sol** | 当前默认，大多数任务 |
| **gpt-5.6** | frontier，要求最高的 agent 活 |
| **gpt-5.6-terra** | 更快更便宜，适合并行 worker / 杂活 |
| **gpt-5.4 / gpt-5.4-mini** | 上一代 / 便宜快，回退或无聊批量活 |

> [!warning] 别再点名旧的 -Codex 模型
> `gpt-5.2` 和 `gpt-5.3-codex` **已弃用**，对 ChatGPT 登录用户已下架。命名正在从旧的「-Codex」后缀线统一到通用 frontier 线（gpt-5.4 / 5.6 现在就驱动 Codex）。默认选 `gpt-5.6-sol` 就对了，配置里别再写下架型号。

## 5. 配置基础：AGENTS.md + config.toml

Codex 的杠杆在配置层，不在模型层。两份文件先懂。

### AGENTS.md —— 告诉 Codex「项目长什么样」

`AGENTS.md` 就是面向 agent 的项目 README，是 `CLAUDE.md` 最直接的对应物。它**三级优先级从远到近层层拼接、近的覆盖远的**：全局 `~/.codex/AGENTS.md`（所有项目通用偏好）在最外层，repo 根一路往下到当前工作目录逐层合并，离 cwd 越近的优先级越高。

**什么时候写进 AGENTS.md：** 当某条要求是「这个项目永远该这么做」而不是「这次任务这么做」。写真实命令（`pnpm test`）而不是空泛要求（「确保质量」）；写完成标准而不只是编码风格；写不可违反的架构边界。当 Codex 反复犯同一种错，再加一条规则——不要一次性写一大本它读不进去的规范。

**处方：**
- ✅ 建议：项目级 `AGENTS.md` 纳入 Git（团队共享）；个人偏好放全局 `~/.codex/AGENTS.md`。
- ⛔ 不要：把 secrets 写进任何 `AGENTS.md`。
- 判断规则：文件太长时，用 `docs/testing.md`、`docs/architecture.md` 拆出去，在 `AGENTS.md` 里引用。

### config.toml —— 告诉 Codex「你允许它干到什么程度」

配置位置：用户级 `~/.codex/config.toml`、项目级 `.codex/config.toml`（覆盖用户级）。状态目录是 `CODEX_HOME`（默认 `~/.codex`）。临时改一次用 CLI 的 `-c key=value`。三个最该懂的键：

```toml
model = "gpt-5.6-sol"            # 默认模型
approval_policy = "on-request"   # untrusted / on-request / never
sandbox_mode = "workspace-write" # read-only / workspace-write / danger-full-access
```

> [!warning] 项目配置只在项目被信任时才生效
> 不可信项目里的项目级 Hooks、Rules 和 `config.toml` 会被**忽略**，只有用户级和系统级配置独立生效。所以别把关键安全设置只放在一个还没标 trusted 的项目里——它可能根本没加载。

**处方：**
- ✅ 建议：起步别一上来 full-access。新手用 `sandbox_mode = workspace-write` + `approval_policy = on-request`（能改工作区、但每步问你一句），摸清脾气再放宽。
- ⛔ 不要：为了「省得点确认」把边界全局关掉。
- 判断规则：个人跨项目偏好放 `~/.codex/`，仓库专属行为放 `repo/.codex/`，临时变化用 CLI 参数或当前 prompt。

## 6. 权限三件套：Sandbox、Approval policy、Rules 别混

这三个经常被搅在一起，但各管一件事：

- **Sandbox** 决定 agent **实际能读、改、访问什么**（read-only / workspace-write / danger-full-access）。
- **Approval policy** 决定**什么时候向你请求授权**（untrusted / on-request / never）。
- **Rules** 决定**某类命令在请求离开 sandbox 时**是 allow、prompt 还是 forbidden，适合表达命令级权限，不适合表达完整开发流程。

Rules 用一个 `prefix_rule()` 声明，比如「push 前先问我」：

```python
prefix_rule(
    pattern = ["git", "push"],
    decision = "prompt",           # allow / prompt / forbidden
    justification = "Confirm target branch before pushing",
)
```

> [!warning] 不要混淆这四层
> - 「所有修改都必须 typecheck」属于 **AGENTS.md**（工作方法）；
> - 「完成一次版本发布」属于 **Skill**（可复用流程）；
> - 「禁止执行危险命令」属于 **Rule**（命令权限）；
> - 「停止前运行验证脚本」属于 **Hook**（生命周期动作）。
> 放错层是新手最常见的坑：把流程塞进 Rule、把一次性要求写进 AGENTS.md，都会让 Codex 行为难以预测。

## 7. 功能一览：Codex 有哪些能力

下面每个功能给「是什么 + 什么时候用 + 最小例」。逐字 TOML、深配和组合成流水线的部分，全在《[压榨 Codex](codex-advanced.md)》进阶篇。

### Subagents（子智能体）—— 并行拆活、保持主上下文干净
**是什么：** 让主 agent 派生出多个子 agent 并行干活（执行或只读探索），互不污染上下文。并行能力默认已开，你不用额外打开它。
**什么时候用：** 大型代码库探索、安全/测试/可维护性三路并行审查、独立方案比较、monorepo 分区调查。
**最小例：** 一句 prompt 就能触发，比如「用三个只读 subagent 分别查安全风险、测试缺口、可维护性问题，此阶段都不改代码，全部完成后按严重性汇总并给出文件位置」。
**处方：** 优先把只读、独立的探索/审查交给它；写入型并行任务要各自用独立 worktree，避免两个 agent 同时改一个文件。

### MCP —— 接外部工具
**是什么：** Codex 支持 MCP（Model Context Protocol），把外部工具和数据源接进来，比如 Context7、Figma、你自建的 server。
**什么时候用：** 需要开发文档、设计稿、数据库或自建服务的实时上下文时。
**最小例：** 一条命令接一个 stdio server——

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

**处方：** 能 `codex mcp add` 就别手写配置。要连已授权的 SaaS 工作区（GitHub / Google Drive / Slack）优先用 App connector；结构化 connector / API / MCP 永远优先于 UI 操作（Browser / Computer Use），前者更快、更可靠、更好审计。

### Hooks —— 把「约定」变「强制」
**是什么：** 在 agent 生命周期的关键时刻插入你的脚本。
**什么时候用：** 当 `AGENTS.md` 里那句「不要动 `migrations/`」需要从约定升级成强制时——hook 脚本让越界动作直接被拦。
**最小例：** 在 Bash 命令执行前跑一个策略检查脚本。阻断的方式是 handler `exit 2` 并把原因写进 stderr。
**处方：** 项目 Hook 只在可信项目加载，改动后需要重新审查信任；企业可用 `requirements.toml` 托管。逐字 TOML 见进阶篇。

### Skills（技能）—— 可复用、可移植的能力包
**是什么：** 遵循 Agent Skills 开放标准（agentskills.io，与 Anthropic Skills 同标准）的能力包：一个含 `SKILL.md` 的目录，可带 `scripts/`、`references/` 和 Codex 专属的 `agents/openai.yaml`。
**什么时候用：** 一套流程重复出现、每次都有相同步骤/参考资料/验证要求时。
**最小例：** 输入 `$skill-creator` 造新技能，或用 `/skills` 管理。
**处方：** 判断规则——同一类 prompt 已经重复三次、且每次步骤相同，通常就值得做成 Skill。还在单个项目里迭代就先做 local Skill；要跨团队/机器分发再打成 Plugin。

### Scheduled tasks（定时任务）—— 无人值守跑
**是什么：** 让 Codex 按计划自动跑（旧称 "Automations"，官方已改名）。两型：standalone（每次起新 chat）和 chat 内（复用上下文，支持分钟级跟进）。
**什么时候用：** 定时评审、每周依赖审计、周期性生成项目状态这类循环。
**最小例：** App 内用 RRULE 排期，比如每周一 9 点 `RRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9`。
**处方：** 可以让它跑在隔离 worktree 里，把定时改动和你手头的活分开。

> [!warning] App 内调度是 RRULE，不是 cron
> 桌面 App 的调度用 **RRULE（RFC 5545）**，UI 里填不了 cron 表达式。**cron 只在 CLI headless 路径**——要用 cron，走 `codex exec` 接你自己的 crontab 或 GitHub Actions。

### Codex Cloud —— 后台 / 长任务
**是什么：** 在 `chatgpt.com/codex` 对 GitHub repo 跑并行云环境任务，本地关机不影响。
**什么时候用：** 无人值守后台跑、GitHub PR 上的 code review、独立并行任务。
**最小例：** GitHub PR 里评论 `@codex review`，拿到 👀 + 行内发现 + PR 级总结；`@codex fix the P1 issue` 会起一个云 chat 去修。
**处方：** 记住云端看不到你未 push 的本地改动，也不会自动继承本机 `~/.codex/config.toml`——重大变化后开新 task 或要求它重读当前文件和 `git status`。

### Codex Remote —— 手机控主机
**是什么：** 用手机上的 ChatGPT 控制你主机上的 Codex（2026-06-25 GA）。手机是**控制面，不是第二个 Codex**——主机提供环境，手机发 prompt / 审批 / 后续。
**什么时候用：** 长任务远程盯梢、随手审批。
**最小例：** 桌面 App 生成二维码 → 手机 ChatGPT 扫码配对 → 在手机上盯长任务、看 diff、批准动作。
**处方：** 手机连接依赖已配对且在线的 host——主机睡眠、断网或关 App 时 Remote 会中断。要真正 24/7，需要 always-on host 或改用 `codex exec` / SDK 自建持久服务（见进阶篇）。

## 8. 端到端工作流：一次完整的活长什么样

别把「代码已经生成」当作完成。推荐的默认闭环是：

```
理解 → 探索 → 计划 → 实施 → 测试 → Review → 修复 → 再验证
```

具体到一个真实场景——你要给项目加一个登录后的 onboarding flow：先让 Codex 读 `AGENTS.md`、认证模块和相关测试（理解 + 探索）；复杂或含歧义时先进 Plan mode，让它标出未知信息、提出可验证的计划、明确完成标准，你确认后再进实施；实施时约束它「不新增状态管理库、不改数据库 schema、不动无关文件」；跑完相关测试、typecheck 和 build（测试）；让它审查最终 diff、自己发现问题自己修（Review + 修复）；最后要它总结改了什么、验证证据和残余风险（再验证）。清晰的小改动不必套这一整套——直接要求实现、测试、review 即可。

## 9. 七天上手计划

一天摸清全貌，一周把每个功能真跑一遍。每天都有明确动作和验收。

### 第 1 天：项目和配置
- 动作：装 App、CLI、IDE 扩展；连一个活跃项目；从 Claude Code 导入设置；检查 `AGENTS.md` 和 `config.toml`。
- 验收：`codex` 能起、能读到你的 `AGENTS.md`，`git status`/分支/工作树确认无误。

### 第 2 天：一个真实小功能
- 动作：用 Plan mode 做一次小功能，要求测试、build、review。
- 验收：功能可用、验证通过，且你记下了该补进 `AGENTS.md` 的规则。

### 第 3 天：Subagents
- 动作：用三个只读 agent 做安全 / 测试 / 可维护性审查，学会查看 agent threads。
- 验收：拿到三份汇总，并对「并行收益 vs 额度消耗」有了体感。

### 第 4 天：Skills 与 MCP
- 动作：迁一个常用 Skill，连一个必要 MCP，用真实任务验证。
- 验收：Skill/MCP 在一个真任务里真的被用上了，而不只是「已安装」。

### 第 5 天：Hooks 和权限
- 动作：加一个低风险的 Stop 或 PostToolUse Hook，加一条命令 Rule。
- 验收：验证 trust、sandbox 和 approval 行为符合预期。

### 第 6 天：Worktrees
- 动作：并行实现两个方案，分别测试。
- 验收：由主 task 比较两份 diff 和风险，选出合并哪个。

### 第 7 天：远程或自动化
- 动作：配一次 Mobile Remote，或建一个低风险的 `codex exec` 任务。
- 验收：观察到稳定性、恢复行为和消耗——但别第一天就自动化生产部署。

## 10. 可复制模板

### 模板 A：日常任务 prompt（四段式）

```text
目标：
[描述最终结果]

上下文：
先阅读 AGENTS.md、相关模块、测试和最近改动。

工作方式：
1. 对复杂或不明确的问题先计划。
2. 只把独立、只读或隔离良好的工作交给 subagents。
3. 实施最小且符合现有架构的修改。
4. 运行相关测试、lint、typecheck 和 build。
5. 审查最终 diff，发现问题自行修复并重新验证。

约束：
- 不修改无关文件；
- 不覆盖已有本地修改；
- 不执行生产部署或数据库写入，除非明确授权。

完成条件：
- 功能符合要求；
- 验证通过；
- 总结修改、证据和残余风险。
```

### 模板 B：AGENTS.md 起步骨架

```md
# Repository Guide

## Architecture
- Web app: apps/web
- API: apps/api
- Shared packages: packages/
- Do not import server modules into client components

## Commands
- Install: pnpm install
- Test: pnpm test
- Typecheck: pnpm typecheck
- Build: pnpm build

## Engineering rules
- Reuse existing components before adding new ones
- Add tests for behavior changes
- Do not edit generated files

## Git workflow
- Inspect git status before editing
- Do not overwrite unrelated local changes
- Use a focused commit message

## Definition of done
- Relevant tests pass
- Typecheck and build pass
- Final diff is reviewed
- Remaining risks are reported
```

## 11. 上手检查清单

### 安装与登录
- [ ] `codex` 能起，`codex --version` 正常
- [ ] 登录方式选定（个人试验用 ChatGPT 账号；自动化用 API key）
- [ ] 默认模型确认为 `gpt-5.6-sol`（没在配置里点名下架型号）

### 配置
- [ ] 项目根有 `AGENTS.md`，写了真实命令 + 完成标准 + 架构边界
- [ ] `config.toml` 起步用 `workspace-write` + `on-request`
- [ ] secrets 没写进任何 `AGENTS.md` 或仓库配置

### 权限边界
- [ ] 分清 Sandbox / Approval policy / Rules 各管什么
- [ ] 高风险命令（push / deploy / DB 写入）走单独审批或 Rule

### 第一个任务
- [ ] 用四段式 prompt 跑通一个真实小功能
- [ ] 要求了测试 + review + 残余风险总结，而不是只看代码生成

## 12. 官方资料索引

- [Codex Best Practices](https://learn.chatgpt.com/guides/best-practices)
- [CLI](https://learn.chatgpt.com/docs/cli) · [IDE](https://learn.chatgpt.com/docs/ide)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Models](https://learn.chatgpt.com/docs/models)
- [Sandbox and approvals](https://learn.chatgpt.com/docs/agent-approvals-security) · [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules)
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) · [MCP](https://learn.chatgpt.com/docs/extend/mcp)
- [Hooks](https://learn.chatgpt.com/docs/hooks) · [Skills](https://learn.chatgpt.com/docs/build-skills) · [Plugins](https://learn.chatgpt.com/docs/build-plugins)
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations) · [Cloud](https://learn.chatgpt.com/docs/cloud) · [Remote connections](https://learn.chatgpt.com/docs/remote-connections)
- [Import from another agent](https://learn.chatgpt.com/docs/import)
- 追新唯一权威：[changelog](https://learn.chatgpt.com/docs/changelog)

---

## 更新记录

| 日期 | 变更 | 官方来源 |
|---|---|---|
| 2026-07-17 | 按 guide 模板 v1 重组为读者指南形状（心智模型 + 需求→入口决策表 + Claude Code 映射 + 职责边界 + 每功能处方 + 端到端工作流 + 七天上手计划 + 可复制模板 + 检查清单）；核验台账迁至 `facts.md`；补入已核验的 Import / Rules / Plugins。 | learn.chatgpt.com/docs/{cli,ide,models,agent-configuration/*,config-file,extend/mcp,hooks,build-skills,build-plugins,automations,cloud,remote-connections,import} |
| 2026-07-17 | 初版：合并旧（`research/openai-codex`）+ 新（`research/codex-advanced-guide`）调研，校准到当前状态——默认模型 `gpt-5.6-sol`、文档迁 `learn.chatgpt.com/docs/*`、"Automations" 改名 "Scheduled tasks"（RRULE）、hooks 10 事件、MCP `[mcp_servers]` 表、桌面 App 并入 ChatGPT App、Codex Remote GA（06-25）。 | learn.chatgpt.com/docs/{models,changelog,automations,hooks,extend/mcp} |
