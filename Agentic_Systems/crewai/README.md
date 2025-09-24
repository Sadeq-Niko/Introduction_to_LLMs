
# CrewAI

This subdirectory demonstrates how to build a simple **agentic system** using [CrewAI](https://docs.crewai.com).

## 🔧 Installation

1. Install [uv](https://astral.sh/uv):

   ```bash
   pip install uv
   # or
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install CrewAI:

   ```bash
   uv tool install crewai
   ```

---

## ⚡ Usage

1. Create a crew or flow:

   ```bash
   crewai create crew demo_crew
   ```

   or

   ```bash
   crewai create flow demo_flow
   ```

2. Configure agents & tasks:

   * `src/mahpad/config/agents.yaml`
   * `src/mahpad/config/tasks.yaml`

3. Run the example:

   ```bash
   uv run src/mahpad/main.py
   # or
   crewai run demo_crew
   # for flow
   crewai flow kickoff
   ```

---
