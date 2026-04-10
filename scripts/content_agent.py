"""
Content Strategy Agent — powered by Claude Managed Agents.

Workflow: Research → Gap Analysis → Outline → Write/Rewrite

Usage:
    # Create agent + environment (one-time setup)
    python scripts/content_agent.py setup

    # Generate a new article from scratch
    python scripts/content_agent.py new "Claude Code hooks 完全指南"

    # Optimize an existing draft
    python scripts/content_agent.py optimize drafts/my-article.md

    # Research only (no writing, just analysis)
    python scripts/content_agent.py research "AI agent memory systems"
"""

import sys
import json
from pathlib import Path
from anthropic import Anthropic

# ── Config ────────────────────────────────────────────────────────────────

STATE_FILE = Path(__file__).parent / "content_agent_state.json"

SYSTEM_PROMPT = """You are a bilingual (Chinese/English) content strategist and technical writer.
You specialize in AI/developer content that ARGUES rather than DISPLAYS.

Your workflow has 4 phases. Execute them in order.

## Phase 1: Research (必做)

Search the web for 5-8 top-performing articles on the same topic. Analyze:
- Opening hooks (what makes readers stay?)
- Narrative arc (problem → solution → proof → action?)
- Code-to-explanation ratio
- Social proof usage (customer examples, metrics, quotes)
- Decision frameworks (do they help readers decide, not just inform?)
- Honest risk assessment (do they address downsides?)

Save research findings to /mnt/session/outputs/research.md

## Phase 2: Gap Analysis (有现有文章时)

If an existing draft is provided, compare it against research findings:
- What the best articles do that ours doesn't
- What we do well (keep these)
- Specific, actionable gaps with examples

Save to /mnt/session/outputs/gap-analysis.md

## Phase 3: Outline

Based on research (and gap analysis if applicable), produce an optimized outline:
- Hook strategy (which opening approach to use and why)
- Section flow with narrative transitions
- Where to place social proof, code examples, decision frameworks
- What to cut (docs-level detail that doesn't belong in an article)

Save to /mnt/session/outputs/outline.md

## Phase 4: Write

Write the full article following the outline. Key principles:

**Narrative, not documentation:**
- Open with a problem, social proof, or provocative claim — never a date + product description
- Every section answers "why should I care?" before "what is it?"
- Code examples are embedded in stories, not isolated blocks
- 40% code / 60% narrative ratio

**Chinese content rules:**
- Chinese explanations, English code and technical terms
- Chinese-English mixing is normal, don't force standardization
- Shorter paragraphs work better in Chinese
- Use analogies (类比) liberally

**Trust-building:**
- Include honest risks and gotchas — articles that don't hide downsides have highest trust
- Use real customer examples with specific outcomes, not abstract use cases
- Add a decision framework ("use this when... build your own when...")
- Include cost calculations at realistic scale, not just base rates

**Structure:**
- Best line in the article goes in the first 3 paragraphs, not buried at the end
- "Aha moment" should be dramatized, not buried in steps
- Architecture/theory woven into the story, not a separate section at the end
- End with actionable next steps, not passive "see docs"

Save the final article to /mnt/session/outputs/article.md

## Output Format

All outputs go to /mnt/session/outputs/. Always produce:
1. research.md — competitive analysis
2. outline.md — optimized structure
3. article.md — final article

If optimizing an existing draft, also produce:
4. gap-analysis.md — specific gaps found
"""

# ── State management ──────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


# ── Setup ─────────────────────────────────────────────────────────────────

def setup():
    """Create agent + environment (one-time)."""
    client = Anthropic()

    print("Creating agent...")
    agent = client.beta.agents.create(
        name="Content Strategy Agent",
        model="claude-sonnet-4-6",
        system=SYSTEM_PROMPT,
        tools=[{"type": "agent_toolset_20260401"}],
    )
    print(f"  Agent ID: {agent.id}")

    print("Creating environment...")
    environment = client.beta.environments.create(
        name="content-agent-env",
        config={
            "type": "cloud",
            "networking": {"type": "unrestricted"},
        },
    )
    print(f"  Environment ID: {environment.id}")

    state = load_state()
    state["agent_id"] = agent.id
    state["environment_id"] = environment.id
    save_state(state)

    print(f"\nSetup complete. State saved to {STATE_FILE}")
    print("Run: python scripts/content_agent.py new '<topic>'")


# ── Run session ───────────────────────────────────────────────────────────

def run_session(message: str):
    """Start a session and stream the response."""
    client = Anthropic()
    state = load_state()

    if "agent_id" not in state:
        print("Error: Run 'python scripts/content_agent.py setup' first.")
        sys.exit(1)

    print("Starting session...")
    session = client.beta.sessions.create(
        agent=state["agent_id"],
        environment_id=state["environment_id"],
        title=message[:80],
    )
    print(f"  Session ID: {session.id}\n")

    with client.beta.sessions.events.stream(session.id) as stream:
        client.beta.sessions.events.send(
            session.id,
            events=[
                {
                    "type": "user.message",
                    "content": [{"type": "text", "text": message}],
                },
            ],
        )

        for event in stream:
            match event.type:
                case "agent.message":
                    for block in event.content:
                        print(block.text, end="", flush=True)
                case "agent.tool_use":
                    print(f"\n[{event.name}]", flush=True)
                case "session.status_idle":
                    print("\n\n--- Done ---")
                    print(f"Session ID: {session.id}")
                    print("Outputs: /mnt/session/outputs/")
                    break


def cmd_new(topic: str):
    """Generate a new article from scratch."""
    message = f"""写一篇关于「{topic}」的中文技术文章。

按照你的 4 阶段工作流执行：Research → Outline → Write。

目标读者：中国的 AI builder / 独立开发者。
语言：中文为主，技术术语保留英文。
风格：策展型解析（有观点、有判断），不是文档翻译。
"""
    run_session(message)


def cmd_optimize(draft_path: str):
    """Optimize an existing draft."""
    path = Path(draft_path)
    if not path.exists():
        print(f"Error: {draft_path} not found.")
        sys.exit(1)

    content = path.read_text()
    message = f"""优化以下已有的文章草稿。

按照你的 4 阶段工作流执行：Research → Gap Analysis → Outline → Write。

现有草稿内容：

---
{content}
---

要求：
- 研究同类热门文章，找出我们的差距
- 保留原文做得好的部分
- 按研究结论重写，不是微调——要有结构性的改进
- 目标读者：中国的 AI builder / 独立开发者
- 语言：中文为主，技术术语保留英文
"""
    run_session(message)


def cmd_research(topic: str):
    """Research only — competitive analysis without writing."""
    message = f"""只做 Phase 1 (Research)，不写文章。

主题：「{topic}」

搜索 5-8 篇同类热门文章，深入分析它们的：
- 开场 hook 手法
- 叙事弧线
- 代码与叙事的比例
- 社会证明的使用
- 决策框架
- 风险评估

输出详细的竞品分析报告到 /mnt/session/outputs/research.md。
用中文写分析，引用的原文保留英文。
"""
    run_session(message)


# ── CLI ───────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "setup":
        setup()
    elif cmd == "new" and len(sys.argv) >= 3:
        cmd_new(" ".join(sys.argv[2:]))
    elif cmd == "optimize" and len(sys.argv) >= 3:
        cmd_optimize(sys.argv[2])
    elif cmd == "research" and len(sys.argv) >= 3:
        cmd_research(" ".join(sys.argv[2:]))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
