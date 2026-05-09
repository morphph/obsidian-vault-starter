---
type: source-summary
created: 2026-05-09
last-updated: 2026-05-09
sources:
  - raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md
tags: [wiki, source, claude-code, html, output-format]
---

# Source: Thariq — The Unreasonable Effectiveness of HTML

## Summary
Long-form X article by [[thariq|Thariq]] (Claude Code team @ Anthropic), 2026-05-08. **3.5M views, 13,571 bookmarks** at fetch time — bookmark-to-like ratio ≈ 1.9× (high reference-saving intent). Argues HTML, not Markdown, is the right primary output format for modern agents. Headline points: 100-line markdown threshold, 1M-context economics, "I feel more in the loop with Claude," and the [[throwaway-editors|throwaway editor]] pattern. Companion site: https://thariqs.github.io/html-effectiveness/ (gallery of examples). Insider validation — what Thariq describes is what the Claude Code team is converging on.

## Source
- **URL:** https://x.com/trq212/status/2052809885763747935
- **Posted:** 2026-05-08 17:56 UTC
- **Engagement (at fetch, 2026-05-09):** 3.5M views · 13,571 bookmarks · 7,129 likes · 1,495 RT · 463 replies
- **Companion site:** https://thariqs.github.io/html-effectiveness/
- **Fetch method:** Playwright MCP

## 要点解读

### 1. 核心论断：Markdown 已经不是 agent 输出的最佳格式了
Thariq 的开场切得很准：
> "Markdown 在 agent 时代变得**有限制了**。我发现自己读不下超过 100 行的 markdown 文件。我想要更丰富的可视化、颜色、图表，并且能轻松分享。"

更深的洞察：
> "我越来越不是自己编辑这些文件，而是把它们当作 specs / reference / 头脑风暴输出。**当我要改的时候，我也是用 Claude 改 —— 这就抹去了 markdown 最大的优势。**"

**Markdown 在过去对的，是因为：**
- 人会自己编辑输出
- 输出比较短
- 浏览器不能原生渲染 markdown

**这三条 2026 年都翻转了。** 所以正确的格式应该是"人类消费起来最好的"，不是"人类编辑起来最容易的"。**那就是 HTML。**

### 2. "100 行 markdown 阈值" —— 一个被低估的失败模式
> "In practice, I've found I tend to not actually read more than a 100-line markdown file, **and I certainly am not able to get anyone else in my organization to read it.**"

这是 agent 输出的**沉默失败模式**：plan 被写出来了，模型觉得活干完了，但**没人真的读完**。HTML 让"每行的阅读成本"降下来了，长文档变得可读。

**对本 vault 的启示：** 我们的 wiki 页很多已经超过 100 行（resolvers.md、gbrain.md 都接近 200 行）。它们目前作为知识图节点是 OK 的（因为是被 Claude 读，不是人读），但如果我们**生成给人读的报告/digest**（比如 daily digest），HTML 渲染可能让阅读率从 0% 跳到可观比例。

### 3. 输出格式 = agent 治理 —— 真正的关键 reframe
全文最有价值的一段（最后那节"Stay in the Loop"）：
> "I had begun to fear that because I had stopped reading plans in depth **I would simply have to leave Claude to make its choices.** But I am happy to say instead that **I feel more in the loop than ever before when using HTML.** I hope you do too."

意思是：**输出格式决定了你和 agent 的关系**。
- Markdown 长文 → 你 skim → 信任 → "leave Claude to make its choices"
- HTML 长文 → 你**真的读** → 抓到问题 → 引导

同一个 agent / 同一个模型 / 同一个任务，**不同的输出格式 = 不同的监督带宽 = 不同的产出质量**。这跟 Garry Tan 的"resolver 是治理层"是同一个洞察 —— **你以为是表面装饰的东西，其实是治理决策。**

新建概念页 [[html-as-output-format]] 把这个关系讲清楚。

### 4. Throwaway Editors —— 一个全新的 UI 工作流模式
最具操作性、最容易抄的一段。Thariq 描述：
> "Sometimes it's hard to describe what you want purely in a text box. **I'll ask Claude to build me a throwaway editor for the exact thing I'm working on. Not a product, or a reusable tool, but a single HTML file, purpose-built for this one piece of data.**"

关键：**永远以 export button 结尾**（"copy as JSON" / "copy as prompt" / "copy as markdown"），把用户在 UI 里的操作变回可粘贴的文本喂给下一轮 Claude Code。

三个例子（最实用）：
1. 30 个 Linear ticket → 拖拽卡片到 Now/Next/Later/Cut 四列 → copy as ordering
2. Feature flag config → 表单编辑器 + 依赖检查 + 警告 → copy as diff
3. System prompt 调优 → 左边可编辑 prompt（变量槽高亮）+ 右边 3 个样本输入实时渲染 → copy as new prompt

**经济学翻转：**
- 旧的"做工具"门槛：你会用 10 次以上才值得做
- 新的门槛：**只要这一次任务能省时间、prompt 写出来不超过 5 分钟，就值得做**

新建 [[throwaway-editors]] 抓住这个 pattern。

### 5. 1M context 让 token 经济学不再是问题
被低估的小细节：
> "While markdown often uses fewer tokens, **with the 1MM context window in Opus 4.7, the increased token usage is not really noticeable in the context window.**"

HTML 用 2-4× 的 token、生成时间 2-4× 长。**但在 1M token 上下文里，这不构成压力**。这是 Opus 4.7 的 1M context 隐含的工作流变化 —— 我们之前的 [[claude-opus-4-7]] 页讲了能力，但没讲到这个**输出格式的二阶效应**。

### 6. 关于"不要写 /html skill"的反直觉建议
> "**I'm a little bit afraid that people will read this article and turn it into a /html skill or something.** While there might be some value in that, **I want to emphasize that you don't need to do much.** You can just ask it to 'make a HTML file' or 'make a HTML artifact'. The trick is knowing what you want the artifact to do."

为什么不要急着固化成 skill：
- 每个 HTML artifact 的形状由 **use case** 决定（spec / review / playground / editor），不是格式
- 过早写 skill 会标准化错误的维度
- 先 freeform prompting 一段时间，等 pattern 自己浮出来，再考虑 skill

**这跟 Garry Tan 的 "if I have to ask twice you failed" 是同一个原则的另一面：** Garry 说"重复出现就该 skill 化"，Thariq 说"还在探索阶段就别 skill 化"。两条规则结合起来 = **skill 是 pattern 浮现后才写，不是 pattern 设想时就写。**

### 7. 五个 canonical use cases（直接可抄）

| 用途 | 关键 prompt 模板 |
|------|------------------|
| Specs / 规划 | "Generate 6 distinctly different approaches in a grid for side-by-side comparison" |
| 代码审查 | "Render diff with inline annotations, color-code by severity" — Thariq 现在每个 PR 都附一个 HTML code explainer |
| 设计原型 | "Create a HTML file with sliders to tune [param]. Add copy button for parameters that worked well." |
| 报告 / 研究 | "Single HTML explainer page: [diagram] flow + 3-4 code snippets annotated + 'gotchas' section. Optimize for reading once." |
| 自定义编辑器 | 见 throwaway-editors —— 永远以 export button 结尾 |

## Pages created from this source
- [[html-as-output-format]] — concept (the headline argument)
- [[throwaway-editors]] — concept (the throwaway-editor pattern)
- [[thariq]] — entity (author; promoted from source-only mention)
- [[source-thariq-html-effectiveness]] — this page

## Pages updated from this source
- [[claude-code]] — added HTML-output-format insight (output as governance)
- [[diarization]] — note that one-page profiles benefit from HTML rendering
- [[blog2video]] — flagged HTML as a candidate intermediate artifact
- [[claude-opus-4-7]] — noted second-order effect of 1M context: HTML token cost no longer prohibitive
- [[index]] — added new pages

## Connections
- Related: [[thariq]], [[html-as-output-format]], [[throwaway-editors]], [[claude-code]], [[claude-opus-4-7]], [[diarization]], [[blog2video]], [[3-agent-starter-team]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-09 | raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md | Initial creation |
