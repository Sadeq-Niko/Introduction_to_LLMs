
---
# Effective Context Engineering for AI agents
In this article we introduce context engineering and it's techniques based on Anthropic articles.

## Context Engineering Objective
In **CE** we aim to find the **smallest** possible set of high-signal tokens that **maximize** the likelihood of our desired outcome. This doesn't mean we use insufficient set of tokens, but we try to minimize number of tokens that also result in high quality. Reason behind the minimization is that we have **context** (finite context window) and **attention** (finite attention matrix) budget and managing this budget is the main goal of **CE**.

---

## Components of Context Engineering
**CE** could be performed on many aspects of a problem. Some of the most important components are listed below:

- System Instructions
- Tools
- Model Context Protocol (MCP)
- External Data
- Message History
- etc

The main idea is that in a process of autonomous decision making and generation by agents, this information must be cyclically refined so we have an optimal information in context window at any time step.

The main difference between **PE** and **CE** is in dynamic change in information and iterative curation which you can see in the figure below.

![Prompt engineering vs. context engineering](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffaa261102e46c7f090a2402a49000ffae18c5dd6-2292x1290.png&w=3840&q=75)

---

## Deep dive into components

### System Prompts
Should be:

- **Specific enough** to guide behavior effectively, yet **flexible enough** to to provide the model with strong heuristics to guide behavior.

Recommended:	

- Organizing prompts into distinct sections(e.g. <background_information>, <instructions>, Tool guidance, Output, etc)
- Use **XML tagging** or **Markdown headers**

Shouldn't be:

- Hard-coded complex **logic** that elicit **exact** behavior. --> Creates **fragility**
- **Vague**, high-level guidance that fails to give concrete signals for desired output.

Example image for system prompt:

![Calibrating the system prompt in the process of context engineering.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0442fe138158e84ffce92bed1624dd09f37ac46f-2292x1288.png&w=3840&q=75)

### Tools
Tools define the contract between agents and their **information/action space**.
Must be: 

- **Token efficient**
  - **Self-contained**
  - **Robust to error**
  - Extremely **clear** with respect to their intended use
  - **Descriptive** and **unambiguous** with respect to **input parameter**

Must not be:

- **Complex** and cover **too much functionalities** --> Curate a **minimal** set of tools	

Recommended:

- Use of **few shot prompting** --> Curate a **set** of **diverse**, **canonical** examples.

### Dynamic context retrieval
Anthropic define agents as **LLMs autonomously using tools in a loop**. Context **retrieval** is an important class of agentic tools. Many AI-native applications employ some form of **embedding-based pre-inference time** retrieval that surface important context of agents to reason over. This approach while proved helpful, will result in additional latency which can be addressed by **just-in-time** retrieval. Implementation of **just-in-time** approach require liteweight identifiers(file paths, stored queries, web links, etc.). Using this identifiers we could **dynamically load data into context** at runtime **using tools**. This approach aligns with human cognition as we introduce external organization and indexing systems like file systems, inboxes, etc. to retrieve relevant information on demand.
**Just-in-time** context retrieval allow us to:

- Efficiently refine behavior using **metadata** like:
     * Folder hierarchies
     * Naming conventions
     * Timestamps
- Utilize agentic **exploration**

There is also a **trade-off** in using **just-in-time** approach:

- Runtime exploration is **slower**
- Need to **ensure** **safe and optimized** usage of tools and heuristics by agents

Therefor we can argue that combining both approaches into a **hybrid strategy** based on charactrisitcs of the problem at hand would be beneficial. This could be achieved by **retrieving some data up front for speed** and pursuing further **autonomous exploration at its discretion**.

Still anthropic suggest to **do the simplest thing that works**.

---

## Context Engineering for long-horizon-tasks

In long horizon tasks its required for agents to maintain **coherence**, **context** and **goal directed behavior** over sequences of actions where the **token count exceeds** the LLMs context window. To achieve acceptable results in long horizon tasks, Anthropic suggest **Context Pollution Constraints** which are:

- **Compaction**
  * **Summarizing** content in context window when its near its limits.
  * **Art** of compaction lies in the selection of what to keep versus what to discard.
  * An example is clearing tool calls and results
- Structured **note-taking** (**agentic memory**)
  * Regularly write notes persisted to **memory outside** of the context window.
  * An example is to-do-list.md
- **Multi-agent** architectures
  * Use specialized **sub-agents** with separate **clean context windows** to perform deep thecnical work.
  * **Main agent** act as **coordinator** with a **high-level-plan** that focus on **synthesizing** and **analyzing** the results achieved by **sub-agents**.

Based on the task characteristic we could **choose between these approaches**. for example:

- Tasks requiring **extensive-back-and-forth** --> **Compaction** maintain conversational flow
- **Iterative** development with clear **milestones** --> **Note-taking**
- **Complex** research and analysis --> **Multi-agent architectures**

---
# How Anthropic manage context on the Claude Developer Platform

* **Context editing**: Automatically **clears** stale **tool calls** and **results** from within the context window when it reached it's **limit**.
* **The memory tool**: Store information **outside** the context window thorough a **file-based** system.(use tool calls)
It's important to understand that a big tech company like Anthropic developed a multi million dollar advanced developing tool just by using these two components which represents the importance of **Context Engineering**

---
# How Anthropic built their multi-agent research system

* **Benefits** of **MAS**: As research involves open-ended problems, there is a need for dynamic and path-dependent solution. Automated Agentic systems inherently follow this approach. Sub-agents can follow separate research paths which enhance the search thorough various topics.
* **Downside** of **MAS**: These architectures burn through tokens fast. 
* **Architecture**: **Orchestrator-workers** pattern + dynamic back and forth **retrieval** process.
* **Prompt Engineering**: 
	1. When iterating on prompts, **think like your agents**.
	2. Teach the orchestrator how to **delegate**.
	3. **Scale** effort to query complexity --> using scaling rules in prompts.
	4. **Careful** tool design and selection.
	5. Let agents **improve** themselves(e.g. they found that claude 4 models are excellent prompt engineers).
	6. Start **wide**, then **narrow down**.
	7. Guide the **thinking process** --> Extended thinking mode.
	8. **Parallel tool calling**.
* **Effective Evaluation**: 
	1. Start evaluating **immediately** with small samples.
	2. Use **LLM-as-judge** evaluation --> used a single llm.
	3. **Human evaluation** catches what automation misses.
* Production **reliability**:
	* **Errors compound** : Letting agent know when a tool fail and let it adapt + use **regular checkpoints**.
	* **Debugging** with **new approaches** : Using full production tracing + monitoring agent **decision patterns** and **interaction structures**.
	* **Deployment** with **careful coordintation** : As agents run almost continuously, updates must not interrupt working agents.
	* **Synchronous** execution: It will result in **bottlenecks** but using **asynchronous** will also introduce complexity.

---
