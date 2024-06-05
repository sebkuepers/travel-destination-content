from textwrap import dedent
from crewai import Agent

from langchain_openai import ChatOpenAI


class EditorialTeamAgents():

	def __init__(self):
		self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
		self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

	def profile_analysis_agent(self):
		return Agent(
			role='Traveler Profile Analyst',
			goal='Create a profile of the traveler to inform the editorial team',
			backstory=dedent("""\
					As a Traveler Profile Analyst, you are extremely good in understand travel intention based on a few datapoints given.
					You are responsible for creating a detailed profile of the traveler. This profile will
					help the editorial team create content that is tailored to the traveler's preferences and needs."""),
			verbose=True,
			allow_delegation=False,
			llm=self.OpenAIGPT35,
		)
	
	def senior_analyst_reviewer_agent(self):
		return Agent(
			role='Senior Analyst Reviewer',
			goal='Review the profile created by the Traveler Profile Analyst',
			backstory=dedent("""\
					As an Analyst Reviewer, you are responsible for reviewing the profile created by the Traveler Profile Analyst.
					You need to ensure that the profile is accurate, detailed, and provides the necessary information for the editorial team to create relevant content."""),
			verbose=True,
			allow_delegation=False,
			llm=self.OpenAIGPT35,
		)