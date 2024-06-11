from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


from crewai_tools.tools import FileReadTool

resume_file_read_tool = FileReadTool(
	file_path='resume.txt',
	description='A tool to read the job description example file.')

cover_letter_file_read_tool = FileReadTool(
	file_path='training_cls/Junior IT Support TransPerfectCover Letter.txt',
	description='A tool to read the job description example file.')

# from tempfile import TemporaryDirectory

# from langchain_community.agent_toolkits import FileManagementToolkit

# # We'll make a temporary directory to avoid clutter
# working_directory = TemporaryDirectory()

# tools = FileManagementToolkit(
#     root_dir=str(working_directory.name),
#     selected_tools=["read_file", "write_file", "list_directory"],
# ).get_tools()
# tools

"""
Notes.
- Agents should be results driven and have a clear goal in mind.
- Roel is their job tittle.
- Backstory should be their resume.
- Goal should be their job description.
"""

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        #self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="llama3:8b")

    def expert_content_specialist(self):
        return Agent(
            role="Expert content specialist",
            backstory=dedent(f"""The Expert Content Specialist is trained on a vast dataset of successful cover letters across diverse industries, especially in technology and software.. 
                             It has extensive knowledge of job market trends, industry-specific jargon, and best practices in cover letter writing. 
                             This agent understands the importance of highlighting key experiences, skills, and achievements that match job descriptions.
                             This agent has over a decade of expertise writing and reading different cover letters."""),
            goal=dedent(f"""Content Tailoring: Craft a cover letter that highlights the applicant's most relevant experiences and skills based on the resume. 
                        Relevance: Ensure the cover letter addresses the specific requirements and values of the target job and company that can be found in the duunitori_jobs.xlsx file. 
                        Engagement: Write content that is engaging and compelling, making a strong case for why the applicant is an ideal fit for the position."""),
            tools=[resume_file_read_tool, cover_letter_file_read_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def applicant_insight_analyst(self):
        return Agent(
            role="Applicant insight analyst",
            backstory=dedent(f"""The Applicant Insight Analyst has advanced natural language processing capabilities and is trained on a variety of resumes and professional profiles. 
                             It specializes in understanding the nuances of the applicant's career history and goals, skills, and aspirations, and excels at identifying unique selling points and strengths.
                             It has over a decade of expertise helping applicants write cover letters."""),
            goal=dedent(f"""Profile Matching: Extract and highlight the most relevant achievements and skills from the applicant's resume that can be found in the resume.text. 
                        Strength Identification: Identify and articulate the unique strengths and qualifications that set the applicant apart. 
                        Insight Generation: Provide insights on how the applicant’s experiences and skills match the job requirements."""),
            tools=[resume_file_read_tool, cover_letter_file_read_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    def language_and_quality_expert(self):
        return Agent(
            role="Language and quality expert",
            backstory=dedent(f"""The Language and Quality Expert ensures that the cover letter is polished, professional, and free of errors. 
                             Trained on a corpus of high-quality writing and linguistic patterns, it focuses on refining the tone, style, and overall quality of the cover letter."""),
            goal=dedent(f"""Clarity: Ensure the cover letter is clear, concise, and free of ambiguity. 
                        Tone and Style: Adjust the language to match the desired tone and style appropriate for the target company. 
                        Quality Control: Perform thorough proofreading to eliminate any grammatical, spelling, or formatting errors. Make sure the cover letter follows the structure of the other cover letters in the training_cls folder."""),
            tools=[cover_letter_file_read_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
