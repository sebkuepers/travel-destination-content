from textwrap import dedent
from crewai import Task

class EditorialTeamTasks():
	def profile_creation_task(self, agent, destination, duration, frequency, travelers, age, hometown, homecountry, airline, cabin):
		return Task(
			description=dedent(f"""\
				Derive form the given traveler data a detailed profile of the traveler.
				Make assumptions on the purpose of the travel and why kind of interests the traveler might have.
				Be clear on weather this might be business or leisure travel. Give sufficient details of what
				kind of activities, point-of-interest and background information is relevant.

				Travel Destination: {destination}
				Duration of the journey in days: {duration}
				Number of previous visits to this destination: {frequency}
				People traveling together: {travelers}
				Average age of the travelers: {age}
				Hometown of the travelers: {hometown}
				Homecountry of the travelers: {homecountry}
				Airline choosen: {airline}
                Cabin Class booked: {cabin}
                """),
			expected_output=dedent("""\
				A conseise profile of the traveler, including the purpose, interests
				and preferences of the traveler."""),
			async_execution=False,
			agent=agent
		)
	
	def profile_review_task(self, agent):
		return Task(
			description=dedent(f"""\
				Review the profile created by the Traveler Profile Analyst.
				Ensure that the profile is accurate, detailed, and provides the necessary information for the editorial team to create relevant content.
				"""),
			expected_output=dedent("""\
				A list of tangible suggestions on how to further improve the profile."""),
			async_execution=False,
			agent=agent
		)