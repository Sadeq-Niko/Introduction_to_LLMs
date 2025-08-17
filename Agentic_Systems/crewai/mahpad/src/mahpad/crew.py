from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from mahpad.tools.retrieval_tool import Retrieve_From_Database
from crewai.llm import LLM

gemma = LLM(
    model='groq/gemma2-9b-it',
    # temperature=0,
    # max_tokens=4096,
    # top_p=1,
    # top_k=1,
)

@CrewBase
class Mahpad():
    """Mahpad crew"""

    agents_config= "config/agents.yaml"
    tasks_config= "config/tasks.yaml"

    @agent
    def sql_query_translator(self) -> Agent:
        return Agent(
            config=self.agents_config['sql_query_translator'], # type: ignore[index]
            verbose=True,
            tools=[Retrieve_From_Database()],
            llm=gemma,
        )

    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['reporter'], # type: ignore[index]
            verbose=True,
            llm=gemma,
        )


    @task
    def query_exectution(self) -> Task:
        return Task(
            config=self.tasks_config['query_exectution'], # type: ignore[index]
        )

    @task
    def reporting(self) -> Task:
        return Task(
            config=self.tasks_config['reporting'], # type: ignore[index]
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Mahpad crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
