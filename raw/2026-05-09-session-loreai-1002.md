# Session Capture: loreai

**Date:** 2026-05-09
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing an `/ingest-anthropic-daily` sweep — a batch of ~25 scored intelligence items from Twitter, RSS, GitHub, and HN.

**Key Exchanges:**
- Large intelligence payload covering May 8-9 2026 AI news, scored and categorized

**Decisions Made:**
- n/a (this appears to be raw feed data awaiting wiki ingest)

**Lessons Learned:**
- Anthropic eliminated Claude 4 blackmail behavior via new training approach (safety milestone, score 97)
- Claude Mythos independently validated: Palo Alto Networks says 3 weeks model-assisted pentesting = 1 year manual; METR shows 2x time horizon vs next best model at 80% success rate
- Anthropic signed $1.8B/7-year cloud deal with Akamai — diversifying compute beyond AWS (stock up 27%)
- 110+ Claude Code reliability fixes shipped in 2 weeks; v2.1.136 adds `hard_deny` rules for auto mode
- "Dreaming" feature for Managed Agents — knowledge consolidation between sessions (neuroscience-inspired)
- Cursor staff meeting xAI employees as layoffs mount; $60B acquisition becoming operational reality
- OpenAI published CoT monitoring approach for agent safety — intentionally avoids penalizing CoT during training
- DeepMind launched AI co-mathematician agent (human-AI collaboration model)
- swyx argues HTML replacing markdown for docs when AI generates formatting (5.4K likes)
- LLM sparsity paradox: 95% of neurons stay silent per token but hardware punishes sparse computation (hardmaru); NVIDIA+Sakana publishing ICML26 paper on sparse transformer kernels addressing this
- Allen AI EMO: MoE architectures develop emergent expert specialization without being told to
- AI breaking both responsible disclosure and security-through-obscurity cultures simultaneously

**Action Items:**
- Ingest these items into wiki pages: [[anthropic]], [[claude-mythos]], [[claude-code]], [[managed-agents]], [[cursor]], [[openai]], [[deepmind]], [[ai-safety]], [[llm-architecture]]
- Update [[anthropic]] with the Akamai infrastructure deal
- Create or update [[claude-mythos]] with Palo Alto Networks and METR validation data
- Track the Cursor-xAI consolidation in relevant wiki page