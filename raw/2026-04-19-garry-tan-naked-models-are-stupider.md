# Naked Models Are Stupider

**Source URL:** https://x.com/garrytan/status/2045798603059548364
**Author:** Garry Tan (@garrytan) — President & CEO @ Y Combinator
**Posted:** 2026-04-19 09:36 UTC
**Engagement (at fetch, 2026-05-12):** 33 replies · 57 reposts · 503 likes · 668 bookmarks · **152.7K views**
**Fetch method:** Playwright MCP
**Series position:** 4th piece in Garry's agent-building series
**Subtitle/hook:** "Imagine if naked people were stupider. It turns out, naked models actually are."

---

## Article: Naked Models Are Stupider

Sorry, not that kind of naked model. But the disappointment you're feeling right now? That's exactly how Kyle Kingsbury feels about LLMs.

Kyle Kingsbury is one of the best systems engineers alive. His **Jepsen** project spent a decade methodically proving that distributed databases didn't work as advertised. That CockroachDB, MongoDB, Redis, and dozens of others made consistency guarantees they couldn't keep. He published the results, the vendors fixed the bugs, and the entire industry got more honest. Jepsen is a masterwork of applied skepticism.

Last week he published a 32-page essay called ["The Future of Everything is Lies, I Guess: Bullshit About Bullshit Machines."](https://aphyr.com/data/posts/411/the-future-of-everything-is-lies.pdf) It's beautifully written, deeply researched, genuinely funny, and **wrong about the most important thing.**

**His observations are correct. His conclusion is not.**

**Scope note:** this essay addresses Kingsbury's technical claims — that LLMs are unreliable bullshit machines incapable of producing trustworthy output. His broader concerns about labor displacement, information ecology, and cultural impact are real, separate questions that deserve their own essays. I'm addressing the architecture question: does model unreliability make useful systems impossible, or does it make them an engineering problem? **I think it's the latter. Kingsbury's essay assumes the former. That's where we disagree.**

## Testing the engine on a bench

Kingsbury's essay is structured as a catalogue of LLM failures:
- Asked Gemini to apply materials to a 3D bathroom rendering. It forgot the toilet and changed the room's shape.
- Asked Claude to do image-to-image transformation. It produced thousands of lines of JavaScript creating an incomprehensible garble of nonsense polygons.
- Asked ChatGPT to put white patches on a blue shirt. It changed the color, moved the patches, deleted them.
- Watched a colleague's LLM claim to download stock data and produce a graph of randomly generated numbers.

Every single one of these failures is real. I've seen failures like them. Everyone building with LLMs has.

**But here's what's happening in each example: a human sits in front of a raw language model, types a request in natural language, and watches it fail.**

- No **skill file** telling the model how to approach the task
- No **deterministic tool** handling the parts that require precision
- No **resolver** routing the request to the right capability
- No **harness** managing context, enforcing safety, or constraining behavior

**He's testing the engine on a bench and concluding that cars are unsafe.**

## The architecture question

Some terms for readers who haven't read the [first essay in this series](https://x.com/garrytan/status/2042925773300908103):
- A **skill file** is a reusable markdown document that teaches the model how to approach a task — a procedure, not a prompt.
- A **resolver** is a routing table that tells the model which document to read for which task.
- **Deterministic code** is software that produces the same output every time — SQL queries, API calls, math — the parts the model should never touch.
- A **harness** is the thin conductor that runs the model in a loop, reads files, and manages context.

Together: thin harness, fat skills.

Kingsbury's central claim is that LLMs are "bullshit machines." They confabulate, they're chaotic, they're vulnerable to manipulation, and they can't be trusted. **He arrives at this by testing models in isolation, the way you'd test a function:** input in, output out, evaluate the output.

The people having Kingsbury's problems are the ones doing exactly this: chatting with a **raw model** and expecting reliable output. The people who aren't having those problems built harnesses. Not because harnesses make the model trustworthy. **Because harnesses make the system trustworthy, even when the model inside it is not.**

Kingsbury knows the harness exists, incidentally. He cites the Claude Code source leak: 512,000 lines of engineering that Anthropic built around their own model. Even the makers of the best LLM in the world don't trust the model naked. They wrapped it in live repo context, prompt caching, purpose-built tools, session memory, and parallel sub-agents. **That's 512,000 lines of evidence that model reliability is an engineering problem, not a philosophical one.**

**Honest caveat:** 512,000 lines is not simple. The pattern I describe (skills, resolvers, deterministic code, testing) is conceptually clean. Robust implementation is real engineering. Harnesses fail. Skills encode wrong procedures. Verification layers are only as good as the invariants they check. **The claim is not that harnesses make everything easy. The claim is that they turn model unreliability from a reason-to-stop into a problem-to-solve.**

### The stock data example
An LLM claimed to download stock prices and produced a graph. The data was random. Kingsbury presents this as evidence that LLMs lie.

What actually happened? Someone asked a language model (a text prediction machine) to fetch data from the internet. It can't fetch data from the internet. It has no tools. It has no HTTP client. It has no API keys. **So it did what language models do: it produced text that looked like what a stock data response would look like.**

**The fix isn't a better model. The fix is a deterministic tool**: a function that actually calls a stock API, returns real numbers, and hands them to the model as context. The model never touches the data retrieval. It decides *what* to look up. The code decides *how*. Same input, same output, every time.

Push intelligence up into skills. Push execution down into deterministic code. Keep the harness thin. When you do this, the class of failures Kingsbury describes becomes far less likely. Not because the model got smarter, but because **the model was never asked to do something it can't do**. Not all failures vanish. But the failure mode shifts from "the model hallucinated" to "the skill was wrong" or "the tool had a bug." **And those are debuggable, testable, fixable problems. That's the difference between chaos and engineering.**

## The bathroom problem

Take Kingsbury's bathroom example. He asked Gemini to apply materials to a 3D rendering. Gemini isn't an image editor. It's not a 3D modeling tool. It's a text prediction system with image capabilities bolted on. Of course it forgot the toilet. Of course it changed the room's shape. **It was playing improv with pixels.**

A properly harnessed system would decompose:
- **Step 1**: identify every surface in the image (vision model)
- **Step 2**: for each surface, select the appropriate material (latent — the model decides)
- **Step 3**: apply the material using a deterministic image processing tool (code — Pillow, OpenCV, a Blender script)
- **Step 4**: verify the output geometry matches the input geometry (deterministic comparison)

**The model does the judgment. The code does the execution. The resolver routes between them. The harness orchestrates the sequence.**

Would this always work? No. The skill might decompose the task wrong. The vision model might misidentify a surface. The deterministic comparison might have the wrong tolerance. **These are real failure modes. But they're debuggable** — you can find the step that went wrong, fix it, and run it again. Kingsbury's failures aren't debuggable because there's no system to debug. There's just a model playing improv.

## Jagged doesn't mean broken

One of Kingsbury's best observations is the ["jagged technology frontier"](https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7571.pdf) — the idea that LLMs have irregular, unpredictable capability boundaries. They do multivariable calculus and fail simple word problems. They write essays and can't count letters.

This is correct and important. But Kingsbury draws the wrong conclusion. He argues that the jagged frontier makes LLMs unsuitable for tasks requiring reliability. **What it actually means is that you need routing.**

A **resolver** is a routing table for context. When task type X appears, load skill Y. When the task requires letter-counting, **route it to code** — a three-line Python function. When the task requires essay writing, route it to the model. When the task requires image editing, route it to a pipeline that **combines both**.

The jagged frontier is an argument for harness engineering, not against AI. The irregularity is real. The solution is routing around it — **put deterministic code where the model is weak and model judgment where the code can't reason.** The resolver maps the territory.

In my own system, I designed my OpenClaw's brain resolver to be 80 lines of markdown, in a numbered decision tree that routes every piece of knowledge to the right directory. When we didn't have it, skills made their own filing decisions and 10 out of 13 were wrong. **When we added it, misfilings dropped to zero. The model didn't get smarter. The routing got explicit.**

## Chaos is an argument for constraints

Kingsbury argues that LLMs are chaotic systems. They're sensitive to small input perturbations, vulnerable to adversarial manipulation, unpredictable in behavior. He's right. Rephrasing a question changes the answer. Rearranging sentences changes the output. Invisible Unicode characters can hijack behavior.

He presents this as a fundamental problem. **It is — if you're feeding raw, unstructured input to a naked model.** It doesn't have to be if you're **constraining the input through skill files**.

A skill file is a structured markdown document that defines the procedure. It tells the model what to read, what to consider, what format to output, and what constraints to observe. The input to the model isn't "fix this image" — **it's a 200-line document** that says: here's the task, here's the process, here's what good output looks like, here are the tools you have, here are the ones you don't, here's what to do if you're uncertain.

**Structured input through a skill file is dramatically less chaotic than freeform natural language.** The skill constrains the trajectory. It doesn't eliminate chaos (nothing does in a stochastic system) but it channels it, the way banks channel a river. Kingsbury is right that unbanked rivers flood. **That's not an argument against rivers. It's an argument for banks.**

## The reasoning red herring

Kingsbury makes a clever point about "reasoning" models. He notes that chain-of-thought traces (the stream-of-consciousness text that models emit while "thinking") are "essentially LLMs writing fanfic about themselves." He cites [Anthropic's finding](https://www.anthropic.com/research/reasoning-models-dont-say-think) that Claude's chain-of-thought traces don't reliably reflect its actual reasoning process.

This is true and irrelevant. The chain-of-thought trace is the scratchpad, not the product. When a human does long division, the intermediate steps on paper aren't a truthful record of their neuronal activity — they're a tool for organizing the computation. Nobody evaluates a mathematician by the beauty of their scratch work.

**What matters is the output.** Does the system (model plus harness plus tools) produce correct, verifiable results? **That's the testable question.** Kingsbury doesn't test it, because he doesn't build the system. **He evaluates the scratchpad instead of the answer.**

## We don't know why aspirin works either

Near the end of his essay, Kingsbury observes that "we don't really know why transformer models have been so successful, or how to make them better." This is true. It's also true of:
- Aspirin (mechanism wasn't fully understood until the 1970s)
- General anesthesia (still incompletely understood)
- Bicycle stability (gyroscopic theory was wrong — definitively explained only in 2011)

**Practical utility doesn't require theoretical completeness.** Engineering can proceed while research continues, which is how it always has.

We didn't stop prescribing aspirin while waiting for the 1971 mechanism paper. We didn't ground planes while debating exactly why wings generate lift. The question isn't whether we understand the mechanism. **The question is whether we can build reliable systems with the capabilities that exist**, test them rigorously, and improve them as understanding deepens.

## What Jepsen would actually find

Here's the irony. **Kingsbury's Jepsen methodology is exactly the right approach for AI systems. It's just applied to the wrong layer.**

Jepsen tests databases by injecting failures and checking invariants. It doesn't test the CPU. It doesn't test the operating system. It tests the database — the full system, under stress, against its own claims.

Apply the same methodology to AI systems and the targets are obvious. **Don't test whether the model hallucinates. Of course it does. Test whether the system hallucinates:**

- Does the **harness** prevent hallucinated data from reaching the user?
- Does the **skill file** route the task to deterministic code where precision matters?
- Does the **resolver** fire for the right inputs?
- Does the entity propagation complete?

These are testable claims. **We test them:**
- **Unit tests** for deterministic code
- **Integration tests** for pipeline correctness
- **[Resolver trigger evals](https://x.com/garrytan/status/2044479509874020852)** for routing accuracy
- **LLM-as-judge evals** for output quality
- **End-to-end tests** for the full pipeline

The testing pyramid for agent systems exists. It's just not what Kingsbury tested. **He tested the raw model, which is like running Jepsen against the bare filesystem instead of the database.**

## The aesthetics of truth

Let me address Kingsbury's deepest argument, the one that most readers will feel even if they can't articulate it. LLMs don't produce truth. They produce **text that looks like truth.** The aesthetics of truth-telling without the epistemological grounding. They are, in the philosophical sense that Harry Frankfurt defined, **bullshit machines**: systems indifferent to the truth-value of their output.

This is correct. **And it's precisely why the architecture matters.**

A naked model produces **plausible** text. A harnessed system produces **verified** text.
- The skill file says "check your work against the source data."
- The deterministic code says "compare this output to the ground truth and reject if it diverges."
- The model produces a draft.
- The system produces a verified result.

**The gap between plausible and verified is exactly the gap that harness engineering fills.**

But here's the part Kingsbury misses entirely: **the quality of the verification depends on the quality of the skill file. And the skill file is written by a human** — the founder, the developer, or the prompt writer.

**This is why open source matters so much.** A closed-source agent can never let you write the skill that verifies its output, because legalism and safetyism prevent the kind of deep customization that real verification requires. You need to be able to say: "here is my schema, here are my invariants, here is what correct looks like in my domain, now verify against that." **You can't do that through an API that guards its system prompt.**

The epistemological problem is real. **The solution is open harnesses where the user controls the verification layer.** Not trust. Engineering.

This is exactly what my YC partner and friend Pete Koomen talks about in [AI Horseless Carriages](https://koomen.dev/essays/horseless-carriages/). **The user must write their prompt**, otherwise we'll be slaves to a system prompt that we can't see.

## Cars

At the end of his essay, Kingsbury compares AI to the automobile. He asks the reader to consider not how fast cars are, but what they did to cities. His answer? Sprawl, lead poisoning, bulldozed communities, car dependency. It's a good metaphor.

But he draws exactly the wrong lesson from it. **We didn't solve car problems by being skeptical of engines. We solved them with engineering**: seatbelts, crumple zones, catalytic converters, traffic lights, highway design, fuel injection, ABS, airbags, emissions standards. Every decade brought new engineering that made the system safer, more efficient, and more useful — not by making the engine smarter, but by building better systems around it.

**Skepticism about engines never saved a life. Engineering the chassis did.**

That's the answer to Kingsbury's essay. Not "be careful." Not "these machines are liars."

The answer is:
- Build the system.
- Write the skills.
- Test the code.
- Route with resolvers.
- Make the deterministic parts deterministic.
- Make the latent (model) parts constrained.
- Test the system, not the model.
- And when the system fails — because it will — **debug the step that broke, fix the skill, and run it again.**

Kingsbury is right that naked models are unreliable. He is right that they confabulate, that they're chaotic, that they produce the aesthetics of truth rather than truth itself. **Where he goes wrong is in treating these properties as verdicts rather than constraints.** The model is unreliable. **The system doesn't have to be.**

**The model is the engine. The harness is the car. Build the car.**

--

GBrain is the knowledge layer to let you build your own personal OpenClaw/Hermes Agent. GStack is the skill layer to go fast with Claude Code.
