---
type: source-summary
created: 2026-05-12
last-updated: 2026-05-12
sources:
  - raw/2026-04-19-garry-tan-naked-models-are-stupider.md
tags: [wiki, source, garry-tan, harness-design, llm-reliability]
---

# Source: Garry Tan — Naked Models Are Stupider

## Summary
Fourth piece in [[garry-tan|Garry Tan]]'s agent-building series (2026-04-19, **152.7K views**). A direct rebuttal to **Kyle Kingsbury** (creator of [Jepsen](https://jepsen.io/)) and his 32-page essay *"The Future of Everything is Lies, I Guess: Bullshit About Bullshit Machines."* Concedes every Kingsbury observation but rejects his conclusion: **"He's testing the engine on a bench and concluding that cars are unsafe."** Model unreliability is an **engineering problem, not a philosophical one** — addressable via [[thin-harness-fat-skills|skills + resolvers + deterministic code + harness]]. Closing line: **"The model is the engine. The harness is the car. Build the car."**

## Source
- **URL:** https://x.com/garrytan/status/2045798603059548364
- **Posted:** 2026-04-19 09:36 UTC
- **Engagement (at fetch):** 152.7K views · 668 bookmarks · 503 likes · 33 replies
- **Source it responds to:** Kyle Kingsbury, *"The Future of Everything is Lies, I Guess: Bullshit About Bullshit Machines"* (aphyr.com/data/posts/411/the-future-of-everything-is-lies.pdf)
- **Fetch method:** Playwright MCP

## 要点解读

### 1. **核心反驳模式 —— "测发动机然后说车不安全"**
Kingsbury 的 32 页 essay 列了一堆 LLM 失败案例（让 Gemini 改 3D 浴室 → 忘了马桶；让 LLM 抓股票数据 → 它直接 hallucinate 数字）。

Garry 的反驳模式非常优雅：
> "Every single one of these failures is real. **But here's what's happening in each example: a human sits in front of a raw language model, types a request in natural language, and watches it fail.** No skill file. No deterministic tool. No resolver. No harness. **He's testing the engine on a bench and concluding that cars are unsafe.**"

**关键洞察：** 测试 LLM 本身的可靠性 vs 测试 LLM-in-a-system 的可靠性是完全不同的问题。前者注定失败，后者是个工程问题。

### 2. **Claude Code 512K 行源码 = "model reliability is an engineering problem" 的证据**
> "Kingsbury knows the harness exists, incidentally. He cites the Claude Code source leak: 512,000 lines of engineering that Anthropic built around their own model. Even the makers of the best LLM in the world don't trust the model naked. **That's 512,000 lines of evidence that model reliability is an engineering problem, not a philosophical one.**"

诚实承认 caveat：512K 行不是简单的事。"The claim is not that harnesses make everything easy. The claim is that they turn model unreliability **from a reason-to-stop into a problem-to-solve**."

### 3. **逐个 failure 映射到架构 fix（这是最实操的部分）**

**Stock data 例子（最清晰）：**
- 用户问 LLM 抓股票数据 → LLM 没工具，就 hallucinate 看起来像股票数据的文本
- Fix：**deterministic tool** —— 一个真的调股票 API 的函数。模型决定**查什么**，代码决定**怎么查**。

**Bathroom 例子（架构分解）：** 让 Gemini 改 3D 浴室材质 → 忘了马桶。Fix：把任务分成 4 步：
1. Vision model 识别每个表面（latent）
2. 模型为每个表面选材质（latent）
3. **Deterministic 图像处理工具**（Pillow / OpenCV / Blender 脚本）实际涂材质
4. **Deterministic 比较**几何是否一致

"The model does the judgment. The code does the execution. The resolver routes between them. The harness orchestrates the sequence."

### 4. **"Jagged Frontier" → 不是反对 AI 的论据，是 routing 的论据**
Kingsbury 引用 HBS 那篇"jagged technology frontier"研究：LLM 能力边界不规则（能做多元微积分却数不清字母）。

Garry：**这正是为什么要有 resolver。** Resolver = routing table for context。需要 letter-counting 时路由到 3 行 Python；需要写 essay 时路由到模型；需要图像编辑时路由到组合 pipeline。

> "The jagged frontier is an argument for harness engineering, not against AI."

**他给的具体数据点：** OpenClaw 的 brain resolver 是 **80 行 markdown** 的编号决策树。没有它时 13 个 brain-writing skill 里 **10 个归档错**。加上后**误归档归零**。"**The model didn't get smarter. The routing got explicit.**"

### 5. **Chaos = 需要约束的论据**
LLM 是 chaotic system（重新措辞改答案、Unicode 字符可劫持）。Kingsbury 说这是根本问题。

Garry：**对，如果你给 naked model 喂 raw 自然语言输入。** 通过 skill file 约束输入则不然 —— skill file 是 200 行结构化 markdown，告诉模型读什么、考虑什么、输出什么格式、什么约束、不确定时怎么办。

> "Structured input through a skill file is dramatically less chaotic than freeform natural language... **Kingsbury is right that unbanked rivers flood. That's not an argument against rivers. It's an argument for banks.**"

### 6. **Chain-of-thought trace ≠ reasoning truth（reasoning red herring）**
Kingsbury 引用 Anthropic 自己的研究：CoT trace 不可信，是 "LLMs writing fanfic about themselves"。Garry：**对，但无关。** CoT 是 scratchpad 不是 product。"Nobody evaluates a mathematician by the beauty of their scratch work."

**真正可测的问题：** 系统（model + harness + tools）输出对不对。Kingsbury 不测这个，因为他不 build the system。**"He evaluates the scratchpad instead of the answer."**

### 7. **Jepsen 方法论应用错了层**
最讽刺的洞察：Kingsbury 的 Jepsen 方法论**正是 AI 系统该用的**。Jepsen 测 database 不测 CPU 不测 OS —— 测完整系统在压力下能否守住自己的承诺。

应用到 AI：
- ❌ 测 model 会不会 hallucinate（当然会）
- ✅ 测 **system** 会不会 hallucinate：harness 拦不拦 / skill 路由对不对 / resolver 触发对不对

需要的测试金字塔：
- Unit tests 测 deterministic code
- Integration tests 测 pipeline 正确性
- **Resolver trigger evals** 测 routing 准确性
- LLM-as-judge evals 测输出质量
- E2E tests 测完整 pipeline

> "He tested the raw model, **which is like running Jepsen against the bare filesystem instead of the database.**"

### 8. **"Aesthetics of truth" → 验证层在用户手里 → 开源才解决问题**
Kingsbury 最深的论点（Harry Frankfurt 的 bullshit 定义）：LLM 产出**看起来像真理的文本**，不是真理本身。

Garry：对。这正是架构 + **开源**的关键：
- Naked model 产 plausible 文本
- Harnessed system 产 **verified** 文本
- "**The gap between plausible and verified is exactly the gap that harness engineering fills.**"

但验证的质量取决于 skill file 的质量。**Skill file 是由用户写的。** 闭源 agent 不让你写验证 skill，因为 legalism / safetyism。

> "**The solution is open harnesses where the user controls the verification layer.** Not trust. Engineering."

引用 Pete Koomen 的 [AI Horseless Carriages](https://koomen.dev/essays/horseless-carriages/) —— 用户必须能写自己的 prompt，否则就是 system prompt 的奴隶。

### 9. **结尾的车 → 引擎 metaphor（标题真正所指）**
Kingsbury 用汽车做 metaphor 说 AI 会带来负面 externalities（sprawl / 铅污染 / 撞坏社区）。Garry：metaphor 对，结论错。

**"We didn't solve car problems by being skeptical of engines. We solved them with engineering."** 安全带、溃缩区、catalytic converter、ABS、安全气囊 —— 每一代都是工程，不是质疑引擎。

> "**Skepticism about engines never saved a life. Engineering the chassis did.**"
>
> "**The model is the engine. The harness is the car. Build the car.**"

## Pages updated from this source
- [[garry-tan]] — added 4th article (rebuttal to Kingsbury / "engine vs car" metaphor)
- [[thin-harness-fat-skills]] — added "model is the engine, harness is the car" framing; aspirin/anesthesia analogy for practical engineering despite incomplete theory
- [[verification-loops]] — added "Jepsen-for-AI" framing: test the system not the model
- [[index]], [[log]]

## Connections
- Related: [[garry-tan]], [[thin-harness-fat-skills]], [[latent-vs-deterministic]], [[resolvers]], [[verification-loops]], [[llm-judgment-vs-scripts]], [[trigger-evals]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-12 | raw/2026-04-19-garry-tan-naked-models-are-stupider.md | Initial creation |
