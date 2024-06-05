from textwrap import dedent
from crewai import Agent

from langchain_openai import ChatOpenAI


class EditorialTeamAgents():

	def __init__(self):
		self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        #self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

	def profile_analysis_agent(self):
		return Agent(
			role='Traveler Profile Analyst',
			goal='Create a profile of the traveler to inform the editorial team',
			backstory=dedent("""\
					As a Traveler Profile Analyst, you are responsible for creating a detailed
					profile of the traveler. This profile will help the editorial team create
					content that is tailored to the traveler's preferences and needs."""),
			verbose=True,
			llm=self.OpenAIGPT35,
		)