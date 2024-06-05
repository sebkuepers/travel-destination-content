from textwrap import dedent
from crewai import Task

class EditorialTeamTasks():
	def profile_creation_task(self, agent, destination, duration, frequency, travelers, age, hometown, homecountry, airline, cabin):
		return Task(
			description=dedent(f"""\
				Derive form the given traveler data a detailed profile of the traveler.
				Make assumptions on the purpose of the travel and why kind of interests the traveler might have.
				Be clear on weather this might be business or leisure travel.

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
				A conseise profile of the traveler, including the purpose of the travel,
				the interests of the traveler and the preferences of the traveler."""),
			async_execution=False,
			agent=agent
		)