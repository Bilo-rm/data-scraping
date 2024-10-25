webscrapingFatwa

 main.py                # The main script that runs the application
question_extractor.py   # Functions related to fetching question links
 qa_extractor.py         # Functions to fetch questions and answers
requirements.txt        # Project dependencies
 README.md               # Project documentation


 # Web Scraping Fatwa

## Project Overview
Web Scraping Fatwa is a Python project that scrapes questions and answers from the IslamQA website. It collects links to questions across multiple pages and fetches the corresponding question and answer content.

## Directory Structure



## Requirements
Before running the project, ensure you have Python installed on your system. This project requires the following dependencies:

- `requests`
- `beautifulsoup4`
- `psycopg2`

You can install these dependencies using the `requirements.txt` file.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd webscrapingFatwa


2.Set up a virtual environment:
python -m venv env
source env/bin/activate  # For macOS/Linux
.\env\Scripts\activate   # For Windows

3.Install the project dependencies:
pip install -r requirements.txt
