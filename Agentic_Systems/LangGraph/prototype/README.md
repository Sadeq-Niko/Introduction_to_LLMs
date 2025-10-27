# LangGraph
---
## Components
- Agent workflows are represented as **Graphs**
- **State** represent the current snapshot of the application (immutable obeject)
- **Nodes** are functions and represents agent logic (take state as input, do something and return state as output)
- **Edges** are functions that determine next **Node** to be executed.

So **Nodes** do the work and **Edges** choose what to do next.

---

## 5 Steps to build a Graph
1. Define the **State** class
2. Start the **Graph Builder**
3. Create **Nodes**
4. Create **Edges**
5. Compile the **Graph**
---
## Two phases of LangGraph
1. Define what your system is trying to achieve in five steps
2. Run the application
---
## State
- **State** is immutable which means every time it has to be updated we must create a new instance of state class with new values.
---
## Reducer
- For each field in **State** you can specify a special function called a reducer
- **LangGraph** use the **Reducer** when a new **State** is returned and this will combine the field with existing state.
- This enables **LangGraph** to run multiple nodes conncurently and prevent overwriting the **State**

---
## Super steps
- With each invocation of graph we will have a new super steps
- While reducer handle the information inside a super step, it will not save it between different super steps.
- Nodes that execute parallel to each other are in the same super step but ones that run sequentially will not be in the same super step
- So we have the problem of forgetting information between super steps
## Checkpointing
- It is the answer to the super step forgetting problem
- We will assign memory to the process which will handle storing information between several super steps
- Sqlite3 could do it

---
## LangSmith
- A monitoring platform for agentic systems that support langgraph

---
## Custome tools
- You can see an example of using langchain/langgraph tools or building a custom tool in [Notebook](./chatbot_with_memory_and_tools.ipynb)

## Conditional Edges
- In **LangGraph** when an **LLM** choose to use a tool, it will return a label that show the need for tool execution. As tools are defined as nodes containing functions, there will be an edge between **LLM** node and tool node. Here we will use **conditional edge** instead of normal edge which will check if the **LLM** label show the necessity of using tool. If the condition is satisfied then the tool node will be executed.
