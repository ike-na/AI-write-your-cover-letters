# AI-write-your-cover-letters
Using a simple web scraper and AI agents to automate boring cover letter writing.


![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Ex-Purpose
This project aimed to automate cover letter writing by web scraping job posts from sites like LinkedIn, Duunitori, and Oikotie, and using AI agents to generate tailored cover letters for each position. The end goal was to have dozens of cover letters ready to go, with a minimal effort.

**However:**
- Running a large porject with a online llm model can easily become expensive.

- There could be privacy issues with online llms.


Therefore, I want to keep this as a local project, making the llama3 family of models the best choice for my needs. I am using the llama3 8-billion-parameter model instead of the 70-billion-parameter model, mainly for hardware reasons. (To be honest, my PC is close to the suns temperature just by running the llama3-8b.)


## Purpose Now
This project is an experiment in embedding my previous cover letters into a vector database to see if a **local** AI can write better cover letters than me. Also I want a tool that can generate cover letters that look like my own. 


## In the Case You Are Cloning the Repository

The project uses a local llm model llama3-8b which takes about 4.7 GB from your drive to download. See more [Ollama](https://ollama.com/).

- If WSL workflow is familiar to you, and want to install a local llm, you can just:

    ```
    curl -fsSL https://ollama.com/install.sh | sh
    ```

- Then:
    ```
    ollama pull llama3
    ```


## Before Runnig

The program embeds your previous cover letters into a vector database, **requiring you to load them into the training folder.** AI will then use the vector database values to generate new cover letters replicating the users unique writing style based on the job requirements given by the user.


- [Purpose](#purpose)
- [Purpose Now](#purpose-now)
- [In the Case You Are Cloning the Repository](#In-the-Case-You-Are-Cloning-the-Repository)
- [Before Runnig](#Before-Runnig)
- [P.S.](#P.S.)

## P.S.

The web scraper only scrapes Duunitori right now, but it can be modified easily. 

For this project, there is no sense to add more job advertisements to the .xlsx file where the AI would find the job description, due to the vast amount of time and computing needed to write just one cover letter locally.