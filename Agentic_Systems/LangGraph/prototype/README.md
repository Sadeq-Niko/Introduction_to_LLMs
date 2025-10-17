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