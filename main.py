import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from dotenv import load_dotenv
load_dotenv()


# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "NA"


class CustomCrew:
    # def __init__(self, var1, var2):
    #     self.var1 = var1
    #     self.var2 = var2
    def __init__(self, var1):
        self.var1 = var1

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        expert_content_specialist = agents.expert_content_specialist()
        applicant_insight_analyst = agents.applicant_insight_analyst()
        language_and_quality_expert = agents.language_and_quality_expert()

        # Custom tasks include agent name and variables as input
        content_creation = tasks.content_creation(
            expert_content_specialist,
            self.var1
            # self.var2,
        )

        profile_matching = tasks.profile_matching(
            applicant_insight_analyst,
        )

        contnent_refinement = tasks.contnent_refinement(
            language_and_quality_expert,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_content_specialist, applicant_insight_analyst, language_and_quality_expert],
            tasks=[content_creation, profile_matching, contnent_refinement],
            verbose=True,
            process=Process.sequential,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI ##")
    print("-------------------------------")
    var1 = input(dedent("""Enter how many jobs you want to apply: """))
    # var2 = input(dedent("""Enter variable 2: """))

    # custom_crew = CustomCrew(var1, var2)
    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)