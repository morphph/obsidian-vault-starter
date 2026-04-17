---
type: source-summary
created: 2026-04-17
last-updated: 2026-04-17
sources:
  - raw/2026-04-16-claude-docs-opus-4-7-whats-new.md
tags: [wiki, source, anthropic, api, docs]
---

# Source — What's new in Claude Opus 4.7 (official docs)

## Summary
Official Anthropic API documentation for [[claude-opus-4-7]]. The technical companion to the [[source-anthropic-opus-4-7-announcement|blog announcement]] — specifies **breaking API changes**, code examples for the new [[task-budgets]] beta, tokenizer behavior, and the full list of behavior changes that may require prompt updates.

**URL:** https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7

## 要点解读

### 1. 三项破坏性 API 改动（只影响 Messages API；Managed Agents 不受影响）
- **Extended thinking budget 被移除**：`thinking: {type: "enabled", budget_tokens: N}` 会 400。只剩 [[adaptive-thinking]] 模式，**默认关闭**——不显式传 `{type: "adaptive"}` 就是不思考。
- **采样参数被禁用**：`temperature` / `top_p` / `top_k` 设非默认值直接 400。以后全靠 prompting。
- **Thinking content 默认不返回**：`thinking` 字段为空除非 opt-in `display: "summarized"`。流式展示推理过程的产品会看到长时间空白。

**实操**：升 4.7 前全库 grep `temperature=`、`top_p=`、`budget_tokens=`、`"enabled"` 清理干净。

### 2. Task Budgets 的 API 细节
- Beta header：`task-budgets-2026-03-13`
- **最低 20k tokens**
- 是**软提示不是硬上限**——给模型做 self-moderate；`max_tokens` 才是硬顶
- **开放式 agentic 任务（质量 > 速度）不要设 task budget**——会限制发挥

```python
output_config = {
    "effort": "xhigh",
    "task_budget": {"type": "tokens", "total": 128000},
}
```

### 3. Tokenizer 换了，成本悄悄涨
同文本多用 **1.0-1.35x tokens**（最多 +35%）。价格没变但账单会涨。给 `max_tokens` 和 compaction trigger 加 buffer。**好消息**：1M context 按标准价不加 long-context 溢价。

### 4. 行为变化（不是 bug 是 feature）
| 维度 | 4.6 | 4.7 |
|------|-----|-----|
| 指令解读 | 会"贴心地"推断你的意图 | 字面理解，不推断未要求的事 |
| 响应长度 | 偏长（固定 verbosity） | 按任务复杂度自动调整 |
| 工具调用 | 积极调用 | 更倾向推理，少调用（高 effort 会增加） |
| 语气 | 温暖、带 emoji、validation-forward | 直接、有观点、少 emoji |
| 进度汇报 | 需要 prompt 强制 | 主动汇报 |
| Subagent | 常自动 spawn | 默认不 spawn，需手动指导 |

**实操**：凡是你 prompt 里写过"be concise"、"every 5 steps give progress"、"spawn a subagent for X"，**先去掉再测**——4.7 可能原生就做了。

### 5. 官方推荐的 `effort` 矩阵
- **`xhigh`** — coding 和 agentic use case 的起点
- **最低 `high`** — 大部分对智能敏感的场景
- Messages API 才能调 effort；Claude Managed Agents 自动处理

### 6. Knowledge work 的具体提升
- **.docx redlining + .pptx 编辑** — 自检 tracked changes 和 slide layout
- **图表/figure 分析** — 程序化调用 PIL 等图像库做像素级数据 transcription

如果现有 prompt 有"double-check the slide layout before returning"这种 mitigation，**去掉它重测**——4.7 可能原生自检。

## Key Entities & Concepts Extracted
- Entities: [[claude-opus-4-7]]
- Concepts: [[adaptive-thinking]], [[task-budgets]], [[xhigh-effort-level]], [[assumptions-expire]]

## Connections
- Related: [[claude-opus-4-7]], [[source-anthropic-opus-4-7-announcement]], [[adaptive-thinking]], [[task-budgets]], [[xhigh-effort-level]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-17 | raw/2026-04-16-claude-docs-opus-4-7-whats-new.md | Initial creation with 要点解读 |
