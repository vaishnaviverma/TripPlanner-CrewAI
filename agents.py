from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

"""AGENT TEMPLATE

Creating Agents Cheat Sheet:
    - Think like a boss. Work backwards from the goal and think which employee you need to hire to get the job done.
    - Define the Captain of the Crew who orients the other agentsn towards the goal.
    - Define which experts the captain needs to communicate with and delegate the tasks to. Build a top down structure of
        the crew.

Goal:

Captain/Manager/Boss:

Employees/Experts to hire:

Notes:
    - Agents should be result driven and have a clear goal in mind
    - Role is their job title
    - Goals should be actionable
    - Backstory should be their resume

"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def agent_1_name(self):
        return Agent(
            role="Define agent 1 role here",
            backstory=dedent(f"""Define agent 1 backstory here"""),
            goal=dedent(f"""Define agent 1 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_2_name(self):
        return Agent(
            role="Define agent 2 role here",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Define agent 2 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
