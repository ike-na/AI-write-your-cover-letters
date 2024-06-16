# AI-write-your-cover-letters
Using a simple web scraper and AI agents to automate boring cover letter writing.


![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Purpose
The purpose of this project was to automate cover letter writing by web scraping job posts from sites like LinkedIn, Duunitori, and Oikotie, and using AI agents to generate tailored cover letters for each position. With just one click, you would have dozens of cover letters ready to go.

**However:**
- I want this to be a local project and my PC can't handle the llama3 70 billion parameter model.

- My PC is close to the suns temperature just by running the llama3 8 billion parameter model.


## Purpose Now
This is an experiment in embedding my previous cover letters into a vector database to see if a **local** AI can write better cover letters than me. Also I want a tool that can generate cover letters that look like my own. 


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

The program embeds your previous cover letters into a vector database, **requiring you to load them into the training folder.**


- [Purpose](#purpose)
- [Purpose Now](#purpose-now)
- [In the Case You Are Cloning the Repository](#In-the-Case-You-Are-Cloning-the-Repository)
- [Before Runnig](#Before-Runnig)
- [P.S.](#P.S.)

## P.S.

The web scraper only scrapes Duunitori right now, but it can be modified easily. 

For this project, there is no sense to add more job advertisements to the .xlsx file where the AI would find the job description, due to the vast amount of time and computing needed to write just one cover letter locally.