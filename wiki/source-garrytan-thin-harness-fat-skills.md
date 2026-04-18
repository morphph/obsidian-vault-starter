---
type: source-summary
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, source, garry-tan, agentic, viral]
---

# Source: Garry Tan — "Thin Harness, Fat Skills"

## Summary
X long-form Article by [[garry-tan|Garry Tan]] (President & CEO, Y Combinator), published 2026-04-11. 1.3M views · 10.7K bookmarks · 537 reposts · 3.8K likes — one of the most-shared agentic-AI essays of 2026. Triggered by [[claude-code]]'s accidental 2026-03-31 npm publish (512K LOC). Crystallizes the post-leak architectural consensus into a 5-definition framework: skill files, harness, resolvers, latent vs. deterministic, diarization.

## Citation
- **Source URL**: https://x.com/garrytan/status/2042925773300908103
- **Format**: X Article (long-form post, ~2,400 words)
- **Published**: 2026-04-11 7:20 PM
- **Fetched**: 2026-04-18 via Playwright MCP (WebFetch fails on X with HTTP 402)
- **Raw**: `raw/2026-04-18-garrytan-thin-harness-fat-skills.md`

## 要点解读

### 1. 100倍生产力差距来自架构，不是模型
Steve Yegge 说用 AI coding agent 的人比 Cursor 用户高 10-100 倍生产力，比 2005 年 Google 工程师高 1000 倍。Garry 强调**这是真实数字**，但解释错了方向——大家以为是「模型更聪明」，但 2x 和 100x 的人用的是同一个 Claude。差距是 **harness（外壳）的架构**。

> Anthropic 在 2026-03-31 意外把 Claude Code 的 51.2 万行源码 push 到 npm，Garry 读完后印证了他在 YC 教的所有东西：**模型不是产品，包模型的那层东西才是产品**。

**实操启发**：评估自己工作流时不要问"Claude 够不够聪明"，要问"我有没有给它正确的上下文、工具、流程"。

### 2. Skill files 当作"方法调用"
Skill = markdown 文档教模型**怎么做**（process），用户提供**做什么**（input）。关键洞察：**skill 是带参数的方法调用**。同一个 `/investigate` skill，传入「安全科学家 + 210 万邮件」就变成医学调查员；传入「壳公司 + FEC 文件」就变成金融取证员。同样七步、同样 markdown 文件、完全不同的能力。

> "这不是 prompt engineering，这是软件设计——markdown 是编程语言，人类判断是 runtime。markdown 比源代码更适合封装能力，因为它用模型本来就在思考的语言来描述 process、judgment 和 context。"

详见 [[skill-as-method-call]]。

### 3. Thin harness（薄外壳）只做四件事
Harness 只做四件事：跑模型循环、读写文件、管 context、强制安全。**就这四件，这就是"thin"**。

反模式："fat harness + thin skills" → 40+ 工具定义吃掉一半 context、MCP 工具每次往返 2-5 秒、REST API 每个 endpoint 包一个工具 → token 三倍、延迟三倍、失败率三倍。

> 例子：Playwright CLI 每个浏览器操作 100ms，Chrome MCP 完成截图-找元素-点击-等待-读取要 15 秒——**75 倍差距**。

### 4. Resolvers（路由表）解决 CLAUDE.md 膨胀问题
Resolver = "当任务类型 X 出现时，先加载文档 Y"的路由表。Skills 告诉模型"怎么做"，resolver 告诉它"现在该读什么"。

**Garry 的忏悔**：他的 CLAUDE.md 曾经写到 **2 万行**，每个 quirk、每个 pattern 全塞进去。Claude Code 自己跟他说"切短点"。最后改成 **200 行 + 指针指向其他文档**。模型注意力恢复正常，2 万行知识依然可调用，不污染 context window。

> Claude Code 内置 resolver——每个 skill 的 description 字段就是 resolver。模型自动匹配用户意图到 skill description。

详见 [[resolvers]]。

### 5. Latent vs Deterministic：Agent 设计最常见的错误
**Agent 设计最常见的错误**：把活儿放错边。

- **Latent space**（智能在这里）：判断、综合、模式识别。
- **Deterministic**（信任在这里）：同样输入→同样输出。SQL、编译、算术。

> 例子：让 LLM 安排 8 个人的晚餐桌位（考虑性格社交）——可以。让它安排 800 人——它会幻觉出"看起来合理但完全错"的座位表。这是组合优化的确定性问题，被错误地塞进 latent space。

**实操启发**：审视我们的 pipeline——比如 `scripts/compile.py` 是确定性的（应该是）；wiki 的"找连接 / 推理"是 latent 的（应该是）。不要让 LLM 做 SQL 能做的事。

详见 [[latent-vs-deterministic]]。

### 6. Diarization：让 AI 真正能做知识工作的关键步骤
不是 RAG、不是 embedding 搜索、不是 SQL 查询。**模型实际读所有材料、记住矛盾、注意时间线变化、综合出一页结构化判断**——像分析师简报，不像数据库查询。

> Garry 的实例（YC Startup School 6000 创始人）：
> "Maria Santos 公司 Contrail，**SAYS**: 'Datadog for AI agents'。**ACTUALLY BUILDING**: 80% commits 在 billing 模块。她其实在做伪装成 observability 的 FinOps 工具。"
>
> 这种 "say vs. actually building" 的差距，**embedding 搜索找不到、关键词过滤找不到**。必须模型读完应用 + GitHub + 1:1 录音再做判断。

**实操启发**：blog2video 的"AI 精读"本质就是 diarization。可以更结构化——不止总结观点，还要标注"作者说什么 vs 真正传达什么"。

详见 [[diarization]]。

### 7. 三层架构（这是这篇文章的"index card"）

```
┌─────────────────────────────────────┐
│  Fat Skills（90% 价值）              │ ← markdown 流程，编码判断
├─────────────────────────────────────┤
│  Thin CLI Harness（~200 行代码）     │ ← JSON in, text out, 默认只读
├─────────────────────────────────────┤
│  Your Application（确定性基础）       │ ← QueryDB, ReadDoc, Search
└─────────────────────────────────────┘
```

**方向性原则**：智能往**上**推进 skills；执行往**下**推进 deterministic 工具；harness 保持**薄**。

> 这样做的好处：**模型每次升级，所有 skill 自动变好；deterministic 层永远稳定**。

详见 [[thin-harness-fat-skills]]。

### 8. Skills 是"永久升级"——不允许做一次性工作
Garry 给他的 OpenClaw 的指令（已被千赞、2.5K 收藏）：

> "你不允许做一次性工作。如果我让你做的事将来会再发生，你必须：
> 1. 先手动做 3-10 次
> 2. 给我看输出
> 3. 我同意后，写成 skill file
> 4. 如果该自动跑，就放到 cron
>
> **测试标准：如果同一件事我得让你做两次，你就失败了。**"

> "每写一个 skill 都是系统的永久升级。它不会退化、不会遗忘、凌晨 3 点你睡觉时它在跑。下一个模型发布时，所有 skill 自动变好——latent 步骤的判断力升级，deterministic 步骤完美稳定。
>
> 这才是 Yegge 100x 的来源。不是更聪明的模型。是 fat skills、thin harness、以及把所有事情都 codify 的纪律。
>
> **系统会复利。Build once. Runs forever.**"

**实操启发（针对我们的工作流）**：
- 你已经在做这事——5 个 slash command 就是 skills
- 下一步：每次发现新的"重复模式"立刻问"这能不能写成 skill？"
- 例子：今天的"X 账号验证 via Playwright"如果再做一次，应该 codify 成 `/verify-x-handle` skill

## Pages this source spawned
- [[garry-tan]] — entity (new)
- [[thin-harness-fat-skills]] — concept (new, central)
- [[skill-as-method-call]] — concept (new)
- [[latent-vs-deterministic]] — concept (new)
- [[diarization]] — concept (new)
- [[resolvers]] — concept (new)

## Pages updated
- [[harness-design]] — added "thin harness" sub-thesis + Garry attribution
- [[claude-code]] — added 2026-03-31 npm-leak event + Garry's read

## Connections
- Related: [[garry-tan]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[latent-vs-deterministic]], [[diarization]], [[resolvers]], [[harness-design]], [[claude-code]], [[ralph-wiggum]], [[boris-cherny]]
