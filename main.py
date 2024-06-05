from crewai import Crew, Process

from tasks import EditorialTeamTasks
from agents import EditorialTeamAgents

from dotenv import load_dotenv
load_dotenv()

class EditorialCrew:

    def __init__(self, destination, duration, frequency, travelers, age, hometown, homecountry, airline, cabin):
        self.destination = destination
        self.duration = duration
        self.frequency = frequency
        self.travelers = travelers
        self.age = age
        self.hometown = hometown
        self.homecountry = homecountry
        self.airline = airline
        self.cabin = cabin
        
    def run(self):
        tasks = EditorialTeamTasks()
        agents = EditorialTeamAgents()

        #create agents
        tpa_agent = agents.profile_analysis_agent()
        tpa_reviewer_agent = agents.senior_analyst_reviewer_agent()

        #create tasks
        profile_creation_task = tasks.profile_creation_task(
            tpa_agent,
            self.destination,
            self.duration,
            self.frequency,
            self.travelers,
            self.age,
            self.hometown,
            self.homecountry,
            self.airline,
            self.cabin
            )
        
        profile_review_task = tasks.profile_review_task(
            tpa_reviewer_agent
            )
        
        # Create Crew responsible for Copy
        crew = Crew(
            agents=[
                tpa_agent, tpa_reviewer_agent
            ],
            tasks=[
                profile_creation_task, profile_review_task, profile_creation_task
            ],
            process=Process.sequential,  # Optional: Sequential task execution is default
            memory=True,
            cache=True,
            max_rpm=100,
            verbose=True,
            share_crew=True
        )

        result = crew.kickoff()
        return result
    
def main():
    #gather the required customer data
    print("## Please enter the Customer Data")
    print('-------------------------------')
    destination = input("Where are they traveling to?\n")
    duration = input("For how many days is the travel booked?\n")
    frequency = input("How often has the destination been visited before?\n")
    travelers = input("How many people are traveling together?\n")
    age = input("What is the average age of the travelers?\n")
    homecountry = input("Which country are they from?\n")
    hometown = input("Which city are they from?\n")
    airline = input("Which airline are you flying with?\n")
    cabin = input("Which cabin class are you flying in?\n")

    editorial_crew = EditorialCrew(destination, duration, frequency, travelers, age, hometown, homecountry, airline, cabin)
    result = editorial_crew.run()
    print(result)

if __name__ == "__main__":
    main()