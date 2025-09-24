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
class Reporter():
    """Reporter crew"""

    agents_config: 'config/agents.yaml'
    tasks_config: 'config/tasks.yaml'

    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['reporter'], # type: ignore[index]
            verbose=False,
            llm=gemma,
        )

    @task
    def reporting(self) -> Task:
        return Task(
            config=self.tasks_config['reporting'], # type: ignore[index]
            output_file='output/report.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Reporter crew"""


        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=False,
        )
