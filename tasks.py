from crewai import Task
from textwrap import dedent


"""
- Gegin with the end goal in mind. Identify a specific outcome that you want to achieve.
- Break down the outcome into actionble tasks and assign each task to an eppropriate agent.
- Ensure that the tasks are descriptive and provide clear instructions.


1. Define what succession looks in your project:
    - Usable cover letters that follow a specific format and imitate the applicant's wiritng style.

2. Task breakdown:
    - 

"""
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def content_creation(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Analyzes the job description from the .xlsx file.
            Analyzes the applicant's resume from the resume.txt file to understand their skills, experiences, and achievements.
            Organizes the content of the cover letter, ensuring a logical flow from introduction to conclusion.
            Modifies the tone and style to match the industry and position.
            Emphasizes the applicant's most relevant skills and experiences.
            Adapts the cover letter to specific job descriptions, ensuring it addresses the employer's needs and requirements.
            Refines the language to be engaging, professional, and free of clichés.

            Make sure to use the most recent data as possible.

            The amount of jobs to apply is: {var1}
        
            Note: {self.__tip_section()}
            """ 
            ),
            expected_output=dedent("""\
			The Expert Content Specialist provides the initial draft. Highlights the applicant’s key experiences that match the job description, using specific examples. Details the skills and achievements that make the applicant a strong candidate. Indicates the applicant’s interest in further discussing their qualifications."""),
						
            agent=agent,
        )

    def profile_matching(self, agent):
        return Task(
            description=dedent(
                f"""
            Extracts key information from the applicant's resume, such as skills, experiences, and achievements.
            Analyzes the job description from the .xlsx file and determines how well the applicant's profile matches the job.
            Identifies the most relevant strengths and experiences to highlight in the cover letter.
            Provides recommendations for personalizing the cover letter based on the applicant's background and the job requirements.
            Identifies any gaps or weaknesses in the applicant’s profile and suggests ways to address them in the cover letter.
            Takes into consideration if some of the skills needed can be learned quickly from the job description.
            
            Make sure to use the most recent data as possible.
        
            Note: {self.__tip_section()}
            """
            ),
            expected_output=dedent("""\
			Lists the primary skills from the applicant’s resume that are relevant to the job. Summarizes the applicant’s strengths in relation to the job description. Recommends key selling points to highlight in the cover letter. Provides tips for tailoring the cover letter to the company’s culture and job specifics."""),
            agent=agent,
        )
    
    def contnent_refinement(self, agent):
        return Task(
            description=dedent(
                f"""
            Grammar and Spelling Check: Identifies and corrects any grammatical errors, typos, or inconsistencies in the cover letter.
            Ensures consistency in style, tone, and formatting throughout the document.
            Improves clarity and conciseness, removing any redundant or unclear phrases.
            Refines the language to be professional, clear, and engaging.
            Conducts a final review to ensure the cover letter meets high standards of quality.

            Make sure to use the most recent data as possible.
        
            Note*: {self.__tip_section()}
            """
            ),
            expected_output=dedent("""\
			The Language and Quality Expert reviews the draft, making necessary edits and ensuring the final cover letter is polished, error-free and imitates the applicant's writing style."""),
            agent=agent,
        )