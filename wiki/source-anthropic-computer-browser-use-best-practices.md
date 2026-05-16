---
type: source-summary
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md
tags: [wiki, source, anthropic, computer-use, browser, agents]
---

# Source: Anthropic — Best Practices for Computer and Browser Use with Claude

## Summary
Anthropic engineering blog post by **Lucas Gonzalez** and **Luca Weihs**, 2026-05-13. ~5-minute read. **The first production playbook for Claude's `computer_20251124` tool.** Compresses a year of internal learnings: the #1 issue is screenshot resolution mismatch, the prompt-injection classifier runs free with the official tool, and demonstration-based teaching is a quietly important new pattern. Closes a gap in our wiki — we had nothing on computer-use, and this is now Claude's most agentic API surface.

## Source
- **URL:** https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
- **Posted:** 2026-05-13
- **Authors:** Lucas Gonzalez, Luca Weihs (Anthropic)
- **Format:** Engineering blog post (~5 min read)
- **Fetch method:** WebFetch (static, no fallback needed)

## 要点解读

### 1. **核心发现 —— 80% 的 computer-use 失败都因为一件事：screenshot resolution mismatch ⭐**
开篇 Anthropic 团队就把矛头指向一个看似最 boring 的问题：**截图发到 API 之前必须先 downscale**。如果不 downscale，模型给出的点击坐标就会系统性偏移。

**两套硬性极限：**
| Model | Max 长边 | Max 总像素 |
|-------|---------|-----------|
| **Claude 4.6 系列** | 1568 px | 1.15 MP |
| **Claude Opus 4.7** | 2576 px | 3.75 MP |

**实操默认：**
- 大多数场景 → **1280×720**（4.6/4.7 都吃得下）
- Opus 4.7 + 质量优先 → **1080p**（token 效率好，文字清晰）

**返回坐标必须重新映射回原始分辨率**：`screen_x = api_x * (native_w / display_w)`

这是个枯燥但 critical 的优化 —— **如果客户端没做这一步，所有后续优化都没意义。**

### 2. **零成本提升点击精度的窍门 —— text 放在 image 之前**
> "Place text instructions *before* images in the messages array to improve click accuracy. The model uses the instruction context while processing the screenshot."

简单到不可思议：**就调一下 messages array 里的顺序**。先 text 后 image。模型在"看"图的时候，指令已经在 context 里建好了上下文。

零新增 token，零新代码，纯顺序优化。

### 3. **反直觉的模型选择 —— Opus 4.7 在 click accuracy 上不比 Sonnet 4.6 强**
Anthropic 自己承认（这点值得记）：
> "Opus 4.7: Superior reasoning with **click precision matching Sonnet 4.6**"

也就是说 Opus 4.7 在 computer-use 任务上的优势**不是"点得更准"**，而是：
- 更强的**推理**（决定下一步该点什么）
- 更大的**分辨率预算**（3.75 MP vs 1.15 MP → 不需要 downscale 那么狠 → 间接更准）

实操选择：
- **Sonnet 4.6**：accuracy / reasoning / cost 平衡 —— **默认推荐**
- **Opus 4.7**：需要复杂推理 + 不想 downscale（dense UI）
- **Haiku 4.5**：延迟优先

### 4. **三层 context 管理 —— 解决长 session 的 screenshot 爆量 ⭐**
Computer-use session 每个 turn 都加一张图。100 turns 就有 100 张图。三层管理：

1. **Cache breakpoints（确定性层）：** 1 个 in stable prefix + 3 个 in recent tool results
2. **Rolling buffer（中期层）：** 留最近 3 张截图；**老的批量剪掉（不要一张一张剪）** —— 这是为了 cache 不每次都失效（呼应 [[prompt-cache-optimization]] 的 4-layer 原则）
3. **LLM compaction（长期层）：** 到 ~150K tokens 时用 custom prompt summarize history

**关键洞察（这条要记下）：** Rolling buffer 的"批量剪老图"细节，正是 [[prompt-cache-optimization]] 4-layer ordering 的具体应用 —— **你剪 N 张图就是 N 次 cache 失效；批量剪一次只失效一次。** 这是 production-grade 的 cache 经济学。

### 5. **Prompt injection classifier 内置免费 ⭐**
> "Built-in classifiers run automatically with the official `computer_20251124` tool type **at no extra cost**."

这是 Anthropic 在打"安全 + 易用"的双牌：用官方 `computer_20251124` 工具类型就自动有 prompt-injection 防御，不额外计费。自己写 computer-use 工具的就没有 —— 需要申请。

**对 builder 的启示：** 永远先用官方 tool type，不要自己造同名工具。除了功能完整，还能白嫖 prompt-injection 防御。

非依赖 classifier 的最佳实践（任何时候都该做）：
- High-stakes actions（付款、发送、删除）走 human-in-the-loop
- Agent 权限要严格 scoped
- 所有 action 都 log 并 monitor
- **Treat web content as untrusted** —— 网页内容可能注入指令，要当不可信源处理

### 6. **Demonstration-Based Teaching ⭐⭐ —— 新颖的教学范式**
这是文章里最有迁移价值的概念。普通的 record-and-replay（Selenium/RPA）失败的原因永远一样：**UI 微小变化就崩**。

Anthropic 的做法不一样：**录一次 demonstration（含截图 + 点击位置 + 选择器 + 描述 + 可选语音）**，然后让 Claude **基于当前 UI 状态自适应回放**，而不是盲目重放坐标。

每步捕获的数据：
- Action type（click/type/navigate/scroll/select）
- Human-readable description（用户在干嘛）
- CSS selector + 坐标
- 带标注的截图
- Viewport 尺寸
- 可选语音 narration

**为什么这比 RPA 强：** 坐标只是"线索"，不是命令。模型每次回放都用 description + selector + 视觉 context 重新识别目标元素。

**关键的设计哲学（这条特别值得记）：**
> 脚本告诉计算机"怎么做"。Demonstration 告诉模型"做什么" —— 模型当天 figure out "怎么做"。

跟 [[skill-as-method-call|skill]] 是平行概念：skill 是文字版的过程化知识，demonstration 是视觉版的。两者都可以 [[skillify-meta-skill|skillify]] —— 我新建了 [[demonstration-based-teaching]] 完整抓住这个模式。

### 7. **两个实验性技术值得跟踪**
- **Batch tools**：把多个非依赖的 action 合并到一个 tool call。**省 latency，但 error compounding 风险**（一个错全错）。用在已知安全的链路。
- **Advisor tool**：执行模型 + 高智能 advisor 模型搭对。Advisor 在同一个 API call 内给战略指导，不增加 round-trip。**长 horizon task 的便宜方案。**

### 8. **Anthropic 自己的失败案例目录（直接抄）**
| 症状 | 原因 | 修复 |
|------|------|------|
| 点击总偏移 | 尺寸不匹配或超 API 上限 | downscale 到 1280×720 或用 `compute_max_api_fit` |
| 点不中小目标 | 高分辨率源被压得太狠 | 开 zoom；增大目标尺寸 |
| 点错元素 | 指令模糊 / UI 复杂 | 给具体位置上下文；拆小步 |
| 全面精度差 | 截图超限 | 全部 pre-downscale |

这张表本身就是 [[silent-fallback-antipattern]] 的反例 —— **明确的失败 → 明确的诊断 → 明确的修复**。production blog 应该长这样。

## Pages created from this source
- [[computer-and-browser-use]] — concept (the full playbook)
- [[demonstration-based-teaching]] — concept (the novel record-and-adapt pattern)
- [[source-anthropic-computer-browser-use-best-practices]] — this page

## Pages updated from this source
- [[claude-opus-4-7]] — high-res vision (3.75 MP) as the concrete computer-use enabler
- [[anthropic]] — computer-use as a product surface
- [[prompt-cache-optimization]] — added "batch-prune screenshots" as a concrete don't-break-cache pattern
- [[index]], [[log]]

## Connections
- Related: [[computer-and-browser-use]], [[demonstration-based-teaching]], [[claude-opus-4-7]], [[anthropic]], [[prompt-cache-optimization]], [[plan-mode-as-tools]], [[verification-loops]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md | Initial creation |
