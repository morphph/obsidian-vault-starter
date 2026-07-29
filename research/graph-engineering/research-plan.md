# Research Plan: Graph Engineering

> depth: standard
> reader: 能使用 Claude Code / Codex / API、但不是资深系统工程师的 AI builder
> as_of: 2026-07-29
> primary languages: English, Chinese

## Research boundary

本报告研究 2026 年 AI agent 社区语境中的 **Graph Engineering**：把多个 agent、
确定性步骤、工具与人工闸门组织成显式执行图。它不是以知识图谱（knowledge graph）
为主的调研，但必须解释两种同名用法为何被混在一起。

## Question map

1. 社区中的 Graph Engineering 到底指什么？是否存在稳定定义？
2. 可追踪的术语使用、系统化阐述与 2026 年 7 月传播事件分别是什么？
3. nodes、edges、state、runtime、recovery、authority 如何组成可执行图？
4. 它与 loop engineering、harness engineering、workflow/state machine、
   multi-agent orchestration、knowledge graph 有什么边界？
5. 哪些能力是 2026 年的新变化，哪些只是旧工程模式的新标签？
6. 有哪些一手实现和实践证据？哪些只是概念演示或供应商叙事？
7. 多 agent / 图编排在哪些任务上反而更差？
8. 非资深工程师应在什么触发条件下采用，第一步应该做什么？

## Search lanes

- **Origin and discourse:** dated X posts, Josh C. Simmons, AI Builder Club timeline,
  LangChain's response, contemporary criticism.
- **Mechanism and official practice:** Anthropic workflows and multi-agent research system,
  LangGraph graph/state model, AutoGen GraphFlow.
- **Evidence and counter-evidence:** Google Research agent-scaling study, Cognition's
  single-writer argument, Anthropic cost and coordination limits, arXiv scheduler paper.
- **Disambiguation:** knowledge graph engineering literature and community pieces that merge
  knowledge graphs with agent execution graphs.

## Freshness and access limits

- X engagement counts are mutable and direct page retrieval is restricted; any captured metric
  must be marked as third-party snapshot/proxy rather than a current observed count.
- “Earliest” claims are limited to indexed English/Chinese web results and reachable primary
  sources; they are not an exhaustive social archive.
- Framework APIs and product capabilities are current only through 2026-07-29.
- Vendor case studies can establish what the vendor reports, not independent causal proof.

## Adversarial checks

- Search for uses before the July 18 viral post and before the July 4 essay.
- Separate the phrase's history from graph-shaped orchestration's much older history.
- Treat “loop versus graph” as a possible false dichotomy.
- Check whether multi-agent performance claims disclose task type, token cost, and baseline.
- Look for sequential-task penalties, context fragmentation, conflicting writers, and recovery
  failures.
- Do not publish Top-N content rankings without a comparable set and direct observed metrics.
