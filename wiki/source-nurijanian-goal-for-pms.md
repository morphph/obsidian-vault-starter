---
type: source-summary
created: 2026-05-18
last-updated: 2026-05-18
sources:
  - raw/2026-05-17-nurijanian-goal-for-product-managers.md
tags: [wiki, source, claude-code-goal, ralph, product-management, pm-os]
---

# Source: George (@nurijanian) — /goal for Product Managers

## Summary
Long-form X article by [[george-nurijanian|George]], 创始人 of [[pm-os|PM OS]] (prodmgmt.world), 2026-05-17. **27.9K views, 591 bookmarks, 208 likes, 18 RT. Bookmark-to-like ratio 2.84×** (high reference-saving intent). 第一篇明确从 **Product Manager 视角**讨论 Claude Code `/goal` 命令的方法论文章。核心论点：`/goal` 不是新魔法，**是 [[ralph-wiggum|Ralph Wiggum loop]] + 产品设计层**——loop 的质量取决于 spec / 测试 / 接受标准 / 证据的质量，而这些都是 PM craft。Agentic coding **不消除产品思考，只是更快地惩罚模糊的产品思考**。

## Source Metadata
- **URL:** https://x.com/nurijanian/status/2055927283991654775
- **Posted:** 2026-05-17 16:23
- **Engagement (at fetch, 2026-05-18):** 27,991 views · 591 bookmarks · 208 likes · 18 RT · 2 replies
- **Bookmark-to-like ratio:** ~2.84×
- **Format:** X Long-form Article
- **Fetch method:** Playwright MCP

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息

- **作者**：George (@nurijanian) —— Verified X 账号
  - 显示名："George from 🕹 prodmgmt.world"
  - Bio："Can I make everyone a great product manager? I will do my best | Get my AI PM OS ⬇️"
  - 身份定位：**他不是工程师，是 product manager + 产品创始人**。运营 prodmgmt.world 教育站，做 PM OS 产品（一个给 PM 用的 AI operating system）。这是 wiki 里**第一个 PM-native 视角的声音**——其他作者要么是 engineer（Matt Pocock / Tw93），要么是 founder/operator（Khairallah / Garry Tan），要么是 VC（Steph Zhang）。**他从 PM craft 角度切入 agent 话题，提供了独特角度**
- **来源**：X 长文（X Long-form Article）
- **发表时间**：2026-05-17 16:23
- **影响力指标**：
  - 27,991 views（27.9K 阅读）—— **比 mass-market 文章（Khairallah 几百 K-几 M）小一个数量级**
  - 591 bookmarks
  - 208 likes
  - 18 reposts
  - 2 replies
  - **Bookmark-to-like ratio: 2.84×** —— 高 retention，读者把它当 reference manual
- **在他整体输出中的位置**：是他 PM OS 推广系列的一部分
  - **5/10**：PM OS v2: The Memory Loop（24K views）—— PM OS 产品演进
  - **5/16**：write requirements with AI（46K views）—— 推荐 Matt Pocock /grill-me + Ryan Singer /shaping
  - **5/17（本篇）**：/goal for Product Managers（28K views）—— **把 /goal 翻译给 PM 受众**
  - 三篇 8 天连发；本篇是上述方法论的应用层
  - **配套关系**：写需求（5/16）→ 用 /goal 跑（5/17）→ 用 PM OS 系统化（持续 sell）

### 2. 核心论点（Thesis）

**作者主张**：Claude Code 的 `/goal` 命令看起来像"自主 agent 的新时代"，**实际是 [[ralph-wiggum|Ralph Wiggum loop]] 加了产品设计层**——loop 本身没有变魔术，关键是它能反复重读 spec / plan / 测试 / 验收标准。**因为**这些 durable files 是 loop 真正的"目标"，**所以** PM 工作的瓶颈从"让工程师能理解"升级到"让 agent 能反复执行 + harness 能验证 + 人能判定是否产品正确"——一个**远高于普通 ticket** 的标准。

简化压缩包：**"/goal 不是新魔法，是 Ralph + 产品设计层。agentic coding 不消除产品思考，只是更快地惩罚模糊的产品思考。"**

### 3. 论证结构

文章的逻辑骨架（这是好分析类文章的典范）：

```
1. Reframe 新工具的本质（颠覆 hype）
   → "/goal 看起来是 autonomy，实际是 Ralph + 产品设计层"
2. 揭示根本机制（什么真正有效）
   → "Fresh context + durable files outside conversation"
3. Push 推论到读者身上（这对你意味着什么）
   → "Requirements act more like target states than prose"
4. 量化 risk（不做的代价）
   → "A loop can spend 40 turns making the wrong thing more internally consistent"
5. 对比 weak vs strong（让差异具体）
   → "improve onboarding" vs detailed acceptance criteria + validation
6. 给操作指南（怎么做）
   → Practical goal template (6 sections)
7. 反面教材（不要这样做）
   → Adjectives, vibes, disguised implementation
8. Closing reframe + 产品 plug
   → "Define done, prove done, keep the proof outside the chat"
```

**骨架的关键洞察**：他用"reframe → 机制 → 推论 → 风险 → 对比 → 操作 → 反面 → 产品"这个结构，每一步都让读者更深一层。**这适合任何"重新解读流行工具"的文章**——你写中文版可以套用这个骨架。

### 4. 关键概念字典

> **/goal 的本质 = Ralph + Product Design Layer（/goal 本质 = Ralph + 产品设计层）**
> - **是什么**：`/goal` 不是新发明，是把 [[ralph-wiggum|Ralph Wiggum loop]] 标准化成 IDE 原生命令，加上一个 evaluator + acceptance criteria 的产品层
> - **为什么重要**：reframe 是文章的根基。如果你以为 `/goal` 是 "agent autonomy"，你会忽略真正的 leverage point（spec / 测试 / 验证证据）；理解为"Ralph + 产品层"，你立刻知道 PM 的工作就是建好那个"产品层"
> - **直觉类比**：像汽车工业 —— 自动驾驶不是车更聪明了，是**路标 / 车道线 / 信号灯**这些基础设施做好了车才能开。`/goal` 是车，spec / tests / criteria 是基础设施
> - **适用场景**：评估任何"agent autonomy" claim 时
> - **反面/失败模式**：把 `/goal` 当成"魔法盒子"→ 写模糊 spec → loop 在错的方向上花 40 turns 推进

> **Externalised Intent / Durable Files（外部化意图 / 持久化文件）**
> - **是什么**：把项目的真实意图（spec / plan / test / acceptance criteria / status notes）放在**对话之外**的文件里，loop 每次新 turn 都重新加载
> - **为什么重要**：解决 context rot 问题。"The conversation could rot, but the source of truth stayed outside the conversation."
> - **直觉类比**：像公司有官方文档库 vs 全靠员工记忆 —— 员工会换 / 会忘 / 会记错，文档库是 source of truth
> - **适用场景**：任何长跑 agent loop
> - **反面/失败模式**：把所有 context 塞在 prompt 里 → token 膨胀；compaction 时丢关键信息；新 agent 起来不知道项目是什么
> - **wiki 对应**：[[agentic-loop-tracking-files]] 描述的 PLAN.md + EXPERIMENTS.md + SCRATCHPAD.md 模式

> **Spec as Product Surface（spec 作为产品界面）**
> - **是什么**：当你 step away 让 agent 独立跑，spec 文件就变成了**真正的产品界面**——agent 的所有行为来自它读到的 spec
> - **为什么重要**：这是 PM 工作的范式转变。以前 spec 是给 engineer 看的"沟通文档"；现在 spec 是 agent 的"执行接口"
> - **直觉类比**：像写函数签名 vs 写函数说明 —— 写说明给同事看；写签名给编译器执行。Spec 现在两者都要兼顾
> - **适用场景**：你要做任何 AFK agent run 之前
> - **反面/失败模式**：用写传统 ticket 的标准写 spec → agent 把模糊的部分填成自己以为的样子

> **Weak Goal vs Strong Goal（弱目标 vs 强目标）**
> - **是什么**：
>   - **Weak**：愿望式（"improve onboarding"）—— agent 优化任何容易证明的指标
>   - **Strong**：finish line + proof method + boundary（"implement spec X, all criteria pass, npm test exits 0, no files outside paths Y are changed, stop after 20 turns"）
> - **为什么重要**：是文章的核心实操对比。差异不在 prompt 长度，**在是否给 loop 一个"可检验的退出条件"**
> - **直觉类比**：weak goal 像"做个好菜"——厨师做什么都说"是好菜"；strong goal 像"鲈鱼 + 200ml 酱汁 + 75°C 鱼肉中心温度"——做完了一目了然
> - **适用场景**：每次写 `/goal` 命令 / agent 任务
> - **反面/失败模式**：把"strong"理解成"长"—— strong 的关键不是字多，是**是否包含可检验的退出条件**

> **Agent-Ready Requirements（agent-ready 需求）**
> - **是什么**：PM 写需求的新标准——包含 7 件东西：observable behavior / negative cases / scope boundaries / validation evidence / stop conditions / status-report expectations / customer-facing success criteria
> - **为什么重要**：这是 PM craft 的 evolved version。从"够 engineer 懂"升级到"够 agent 反复执行 + harness 验证 + 人判定产品正确"
> - **直觉类比**：像合同 vs 邀约 —— 邀约说"我们想做这个事"；合同说"在 X 条件下做 Y 事，达成 Z 标准时算完成"
> - **适用场景**：写所有给 agent 跑的需求
> - **反面/失败模式**：只写正面行为，不写 negative cases → agent 把所有不该改的也改了
> - **wiki**：见 [[agent-ready-requirements]]

> **Calibration Loops（校准 loops / 看头几轮）**
> - **是什么**：开始 long-running agent 前，先**看头几次迭代** —— 不是"不信任 agent"，是**让 spec 经历模型考验后再放手**
> - **为什么重要**：避免"写完巨大 spec → 关电脑 → 醒来发现 agent 做了 40 turns 错事"。Calibration phase 是让 spec 和 agent 互相磨合
> - **直觉类比**：像新员工 onboarding —— 第一周必须坐在旁边看他怎么做，不是不信任，是知道你的工作指令需要被实际工作场景检验
> - **适用场景**：每次开新 agent loop
> - **反面/失败模式**：跳过 calibration → 后面 unattended 跑全是反复犯同样误解

> **Delegating Effort vs Delegating Outcome（委托劳动 vs 委托结果）**
> - **是什么**：传统 prompt 是"让 agent 努力做 X"；agent-ready spec 是"让 agent 做到 Y 状态停止"
> - **为什么重要**：作者用一句话总结整个文章的差异 —— "A prompt asks for effort, while a contract defines the condition where effort stops"
> - **直觉类比**：像雇佣 vs 承包 —— 雇佣是"你来工作 8 小时"；承包是"完成这个任务你拿钱"。前者付 effort，后者付 outcome
> - **适用场景**：所有 agent task definition
> - **反面/失败模式**：用 effort framing 跑 unattended loop → agent 可以无限"努力"但永远不"完成"

### 5. 框架与心智模型

**核心框架：Practical Goal Template（实操目标模板）**—— 6 个 section：

```
/goal [specific target state]

Source of truth:
- read [spec file]
- follow [implementation plan]
- update [status file]

Acceptance criteria:
- [observable behavior 1]
- [observable behavior 2]
- [negative case]
- [non-regression condition]

Validation:
- [test command]
- [lint/typecheck/build command]
- [browser/visual/manual evidence if needed]

Boundaries:
- only edit [paths]
- do not change [systems]
- preserve [contract/data/API behavior]

Loop behavior:
- after each meaningful change, run the relevant validation
- update the status file with changed files, result, and remaining risk
- stop after [N turns/time] if blocked and report the blocker
```

**怎么套用（举例：你做 blog2video 的 chapter generator）**：

```
/goal 给 raw/2026-05-18-source-article.md 生成 chapter markers，符合 docs/chapter-spec.md

Source of truth:
- read docs/chapter-spec.md
- follow docs/chapter-implementation-plan.md
- update docs/status-chapters.md

Acceptance criteria:
- 每个 chapter 30-60 秒内容覆盖
- 每个 chapter 有 hook + 论点 + 例证三段结构
- 最后一个 chapter 必须以 CTA 结尾
- 整篇 chapter markers 总长不超过文章总长 1/3
- negative case: 不允许出现"summary" / "overview" 这类元描述

Validation:
- npm run test:chapter-format（检查格式）
- 人工抽查 3 段（confirm 论点完整）

Boundaries:
- 只输出 chapter markers 到 docs/output/chapters.md
- 不修改 raw/ 任何文件
- 不修改 docs/chapter-spec.md（这是 spec 不是工作产物）

Loop behavior:
- 每生成一段验证一次（npm run validate-chapter）
- 失败时记录到 status file 并 retry 一次
- 5 个 chapter 全过后 emit COMPLETE signal
```

这个模板**直接套用 Khairallah 4-component agent contract 的兄弟模式**——一个是 agent build-time spec（Khairallah），一个是 agent run-time goal（George）。**两者配合使用**：用 Khairallah 定义 agent 是什么，用 George 定义这次任务要做什么。

### 6. 关键数据与例证

按重要性排序：

| 数据 | 支撑什么观点 | 用途 |
|---|---|---|
| **"A loop can spend 40 turns making the wrong thing more internally consistent"** | 量化模糊 goal 的真实代价 | 这是文章最有冲击力的"恐吓数字"，可以做博客 hook |
| **27.9K views / 591 bookmarks（2.84× B/L）** | mass-market 之下，**niche-but-deep** 受众 | 验证选题：PM 视角的中文版几乎没人做 |
| **5 个"natural fit" 场景**（migration / backlog clearing / file splitting / brute-force testing / exploration） | 锚定 /goal 真正的甜区 | 直接给实操参考清单 |
| **6-section goal template** | 把抽象 idea 变成模板 | 可立即抄走用 |
| **PM OS v2 即将发布** | 间接证明这套方法他在自己产品里实践 | 信号：这不是纯理论 |

**注意**：作者**全文没给具体 case study**（"我用这套方法 build 了 X，省了 Y 时间"）—— 全是抽象方法论 + 模板 + 反例。这是他这类文章的常见弱点。**你写中文版可以补 case study**（用 blog2video chapter generator 或 LoreAI FAQ 扩展实例）。

### 7. 关键引语

> **"/goal is better understood as the Ralph Wiggum loop with product design around it."**
> /goal 更应该被理解为：Ralph Wiggum loop + 围绕它的产品设计层。
> ⭐ 文章 thesis 一句话版。可直接做标题。

> **"The useful part was not a smarter model. It was the fresh context at the start of each run."**
> 有用的部分不是更聪明的模型，是每次循环开始时的新鲜 context。
> ⭐ Ralph 真正的洞察一句话，反对"model autonomy" 叙事。

> **"The conversation could rot, but the source of truth stayed outside the conversation."**
> 对话可以腐烂，但 source of truth 留在对话之外。
> ⭐ Externalised intent 的最强 framing。

> **"The further out of the loop you go, the more leverage you get. But the more important your setup and planning becomes."**
> 你离 loop 越远，杠杆越大；但你的 setup 和 planning 也越关键。
> ⭐ AFK 的核心 trade-off 一句话。

> **"A one-shot mistake is annoying. A loop can spend 40 turns making the wrong thing more internally consistent."**
> 一次性的错误是 annoying；loop 可以花 40 turns 让错的东西变得更加内部一致。
> ⭐ 量化模糊 goal 的真实代价。

> **"A prompt asks for effort, while a contract defines the condition where effort stops."**
> Prompt 要求努力；contract 定义努力停止的条件。
> ⭐ Delegating effort vs outcome 的最强对照。

> **"Agentic coding does not remove product thinking. It punishes vague product thinking faster."**
> Agentic coding 不消除产品思考，只是更快地惩罚模糊的产品思考。
> ⭐ 给 PM 受众的"震撼一句"，反 hype 又 motivating。

> **"The loop becomes useful after the spec survives contact with the model."**
> Loop 在 spec 经历了与模型的接触并幸存之后才变得有用。
> ⭐ Calibration 的诗意表达。

> **"Define done, prove done, and keep the proof outside the chat."**
> 定义完成，证明完成，把证据留在对话之外。
> ⭐ 文章 closing 的 operational rule，可作为标题或 closing 引用。

### 8. 实操指南

**写 strong goal 的 7 个组件 checklist**（这是文章的 take-home）：
- [ ] **Observable behavior**：用户实际看到/做到的行为（不是抽象状态）
- [ ] **Negative cases**：什么不能发生（往往比 positive case 更重要）
- [ ] **Scope boundaries**：哪些文件/系统不能动
- [ ] **Validation evidence**：用什么命令/检查证明完成
- [ ] **Stop conditions**：N turns 或 时间上限
- [ ] **Status-report expectations**：失败时记什么 / 成功时记什么
- [ ] **Customer-facing success criteria**：对最终用户有什么意义

**开 goal loop 前的 calibration checklist**：
- [ ] 写完 spec 后不要立刻 close laptop
- [ ] 启动 loop，**坐着看头 3-5 个 iteration**
- [ ] 如果 agent **misunderstand target** → stop, edit spec, restart
- [ ] 如果 agent **写错的 test 来 bless 错的行为** → stop, fix validation protocol, restart
- [ ] 如果 agent **碰了不相关文件** → stop, add scope boundaries, restart
- [ ] 如果 agent **反复问同样问题** → stop, spec 有 ambiguity，明确化
- [ ] 当 spec 通过 calibration 后再放心 AFK

**weak → strong 重写 checklist**（把任何 weak goal 都过一遍）：
- [ ] 把所有形容词（better / cleaner / easier / smarter）替换成 observable states
- [ ] 把所有"vibe"（"polish the flow"）替换成 named product behavior
- [ ] 把所有 implementation preference（"refactor into cleaner architecture"）替换成 the pain the refactor must relieve

**用 status file 做 durable memory checklist**：
- [ ] 创建专门的 status file（如 `docs/status-{feature}.md`）
- [ ] 每个 agent iteration 必须更新它
- [ ] Status file 必须记录：what changed / which checks passed / which failed / what decision / what remains risky / what human should inspect next

### 9. 对比与反对意见

| 对比对象 | 作者立场 | 隐含信念 |
|---|---|---|
| **vs "agent autonomy" hype** | 强烈反对 | autonomy 不是从天上掉下来；是 spec + tests + criteria 撑起来的 |
| **vs Vibe-style prompts**（"improve onboarding"） | 强烈反对 | 模糊 prompt = 优化剧场，agent 优化任何容易证明的指标 |
| **vs 写完 spec 立刻 close laptop** | 强烈反对 | 必须 calibrate; spec 必须经历模型考验 |
| **vs 把所有 context 塞 prompt** | 反对 | Externalise to durable files; let conversation rot |
| **vs 用 effort framing 跑 unattended loop** | 反对 | Use contract framing; define stop condition |

**作者明确反对**：
1. 把 `/goal` 当魔法 —— 它只是 Ralph + 产品层
2. 用 adjectives / vibes 给 agent 任务
3. 跳过 calibration phase
4. 把实现偏好包装成产品目标（"refactor into cleaner architecture"）
5. 用 exploration loop 偷偷跑 production work（"the dangerous version is asking an exploratory loop to silently become a production loop"）

**作者隐含承认的限制**（他没明说但能推断）：
- **写 strong goal 的成本高** —— 每个任务都按 6-section template 写，PM 工作量增加 2-5×
- **不是所有任务都适合 AFK** —— 他给了 5 个"natural fit"，言下之意其他场景未必 fit
- **依赖好的测试 / lint / typecheck 基础设施** —— 没有这些 evaluator 无法工作
- **vibe-coding 文化 vs 严谨 spec 文化的冲突** —— 公司文化决定能不能用上
- **没讨论团队协作** —— 全是单 PM 视角；多 PM 怎么共享 spec library / status file 没说

### 10. 与 wiki 知识的连接

**强连接**：
- [[claude-code-goal]] —— /goal 命令本身的官方文档。**本文给它加了 PM 角度的方法论**
- [[ralph-wiggum]] —— /goal 本质就是 Ralph，本文是 reframe 的最强一句证据
- [[agent-ready-requirements]] —— 本文创造的核心概念（新建 wiki 页）
- [[goal-template]] —— 本文给的实操模板（新建 wiki 页）
- [[george-nurijanian]] —— 作者实体（新建 wiki 页）
- [[pm-os]] —— 他的产品（新建 wiki 页）

**强化已有概念**：
- 强化 [[ralph-wiggum]]：之前我们的 Ralph 页主要讲 engineering 视角，本文加了 PM design 视角
- 强化 [[claude-code-goal]]：之前只有官方文档信息，本文加了 PM 实操方法论
- 强化 [[agentic-loop-tracking-files]]：本文的 "status file as durable memory" 跟 PLAN.md/EXPERIMENTS.md/SCRATCHPAD.md 是同一模式
- 强化 [[sprint-contracts]]：本文的"6-section goal template"是 sprint-contract 在 /goal 命令上的具体化
- 强化 [[grill-with-docs]]：本文的 calibration phase（"watch first loops"）跟 grill-with-docs 的 interactive discovery 是兄弟概念

**挑战/补充已有观点**：
- 跟 [[idea-to-afk-agent-flow]] 高度互补：
  - idea-to-afk-flow 的 Phase 1（discovery）+ Phase 2（prompt prototyping）≈ 本文的 strong goal spec writing
  - idea-to-afk-flow 的 Phase 5（AFK handoff）≈ 本文的 /goal loop 启动
  - **本文填了 idea-to-afk-flow 缺的 PM 视角** —— Matt Pocock 是 engineer 视角；George 是 PM 视角，两者拼起来才完整

**与新 wiki 的关系**：
- [[mattpocock-skills-library]] —— George 在他另一条 tweet 推荐 Matt 的 `/grill-me`，证明两人在同一方法论 trajectory
- [[sandcastle]] —— George 描述的 6-section goal template 完美适配 Sandcastle 的 prompt file 格式

**扩展方向 / 可继续 ingest 的源**：
- [Ryan Singer's shaping skills](https://github.com/rjs/shaping-skill) —— George 推荐的另一个 PM 工具（ex-Basecamp 的 shaping 方法论 → Claude Skill）
- [PM OS](https://prodmgmt.world/ai-pm-os) —— George 的产品，值得 deep scan（如果有 GitHub repo）
- [Codex Using Goals cookbook](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) —— 已 ingest（[[source-openai-codex-cookbook-trilogy]]）

### 11. 对用户（vfan）的启示

基于 vfan 的情况（Singapore growth marketer + AI content builder，LoreAI + blog2video）：

#### 短期（本周）
1. **用 6-section goal template 重写你目前最频繁的 Claude 任务**。建议候选：
   - **blog2video**：chapter generator（前面已建议 build 这个 skill，现在加上正式的 goal template 规范）
   - **LoreAI**：FAQ 扩展 generator（每个 glossary 词条自动生成 5 个 FAQ）
   - **个人**：tweet → blog draft 转换器
2. **calibration practice**：下次启动新 agent loop 时，**强制坐着看头 3 个 iteration**，记下"agent misunderstand 了什么"，迭代 spec
3. **重写一个你常给 Claude 的"形容词式"prompt** —— grep 自己最近 prompt 里的 "better / cleaner / easier" → 改成 observable behavior

#### 中期（接下来 2-4 周）
1. **建一个 spec library**：把你常用的 agent task 都按 6-section template 写成 markdown 文件，存在 `wiki/specs/` 或单独 repo。每次 invoke 时直接 reference 文件路径，不要每次手敲
2. **建立 status file 习惯**：所有 AFK agent run 都强制有一个 status file。配合 `.ralph/guardrails.md`（Matt Pocock 方法）双轨记录
3. **跑一次真正的 AFK loop**（不只是 prototype）：选一个 backlog clearing 或 file splitting 任务，按 strong goal 规范跑，看实际效果

#### 长期（如果验证有效）
1. **中文版选题**："从 PM 视角看 Claude /goal —— 模糊需求的代价"
   - 在中文圈是空白 —— Matt Pocock 翻译版有人做（你之前已经在做了），George 这个 PM 视角的翻译版没人做
   - 加入你的 LoreAI / blog2video 真实 case study（spec 长什么样、loop 跑多少 turn、ROI）
2. **Productize**：参考 PM OS 模式，可以 build "Indie Content Creator's Spec Library" —— 一套给独立内容创作者用的 agent-ready spec templates（chapter generator / SEO content / newsletter / 等），可付费或引流
3. **跨文化角度**：George 默认西方 PM 文化（spec-driven, 测试驱动）；中文圈很多公司是 "vibe-driven" 文化。**你可以加一个 angle：怎么在 vibe-driven 公司引入 agent-ready requirements 文化**

### 12. 一句话总结

**"/goal 不是新魔法，是 Ralph + 产品设计层 —— agentic coding 不消除产品思考，只是更快地惩罚模糊的产品思考。"**

或更短：**"Prompt 要求努力，contract 定义努力停止的条件。"**

或最适合做标题：**"模糊的 ticket 在 agentic 时代要付的 token 税"**

---

## Connections
- Related: [[george-nurijanian]], [[pm-os]], [[claude-code-goal]], [[ralph-wiggum]], [[agent-ready-requirements]], [[goal-template]], [[agentic-loop-tracking-files]], [[idea-to-afk-agent-flow]], [[mattpocock-skills-library]], [[grill-with-docs]], [[sandcastle]], [[sprint-contracts]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-18 | raw/2026-05-17-nurijanian-goal-for-product-managers.md | Initial creation using 12-section comprehensive structure |
