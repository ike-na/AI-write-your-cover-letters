# AI-write-your-cover-letters
Using a simple web scraper and AI agents to automate cover letter writing.


![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Ex-Purpose
This project sought to automate the creation of cover letters by web scraping job posts from sites like LinkedIn, Duunitori, and Oikotie, and then employing AI agents to generate customized cover letters for each position. The end goal was to have dozens of cover letters ready to go, with a minimal effort.

**However:**
- Running a large porject with a online LLM model can easily become expensive.

- There could be privacy issues with online LLMs.


Therefore, I want to keep this as a local project, making the llama3 family of models the best choice for my needs. I am using the llama3 8-billion-parameter model instead of the 70-billion-parameter model, mainly for hardware reasons. (To be honest, my PC is close to the suns temperature just by running the llama3-8b.)


## Purpose Now
Now, this project is an experiment in embedding my previous cover letters into a vector database to see if a **local** AI can write better cover letters than me. Additionally, I want a tool that generates cover letters that mimic my writing style.


## In the Case You Are Cloning the Repository

The project leverages a local LLM model, llama3-8b, which requires about 4.7 GB of disk space. For more information, visit [Ollama](https://ollama.com/).

- If you're familiar with the WSL (Windows Subsystem for Linux) workflow and want to install a local LLM, simply run:

    ```
    curl -fsSL https://ollama.com/install.sh | sh
    ```

- Once installed, pull the llama3 model:
    ```
    ollama pull llama3
    ```


## Before Runnig

The program embeds your previous cover letters into a vector database, **requiring you to load them into the training folder.** AI will then use the vector database values to generate new cover letters replicating the users unique writing style based on the job requirements given by the user.


- [Ex-Purpose](#ex-purpose)
- [Purpose Now](#purpose-now)
- [In the Case You Are Cloning the Repository](#in-the-case-you-are-cloning-the-repository)
- [Before Runnig](#before-runnig)
- [Additional Notes](#additional-notes)
- [Post Script](#post-script)

## Additional Notes
**System Requirements:** Make sure your PC meets the necessary requirements to run the llama3-8b model smoothly. While it's not as heavy as the 70-billion-parameter model, it still requires a decent amount of computational power and memory.

- **Data Privacy:** By keeping the AI local, your data remains private and secure on your own machine.

- **Customization:** You can further customize the AI’s output by tweaking the AI prompts in the *utilities.py* and *main.py* files. You can also choose to use any cover letters you want, giving you more control over the final product.

## Post Script

The web scraper only scrapes Duunitori right now, but it can be modified easily. 

For this project, as long as I am the sole user, it is impractical to add more job advertisements to the .xlsx file for the AI. The time and computing resources required to produce a single cover letter locally are too extensive.
