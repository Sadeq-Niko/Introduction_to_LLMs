from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai.llm import LLM

gemma = LLM(
    model='groq/gemma2-9b-it',
    # temperature=0,
    # max_tokens=4096,
    # top_p=1,
    # top_k=1,
)

@CrewBase
class NlToSql():
    """NlToSql crew"""

    agents_config: "config/agents.yaml"
    tasks_config: "config/tasks.yaml"

    @agent
    def sql_query_translator(self) -> Agent:
        return Agent(
            config=self.agents_config['sql_query_translator'], # type: ignore[index]
            verbose=True,
            llm=gemma,
        )

    @task
    def query_generation(self) -> Task:
        return Task(
            config=self.tasks_config['query_generation'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the NlToSql crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
