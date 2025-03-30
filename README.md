# ai_news_article

# Fast API with mongo database using scraping

This is a repository to fetch ai news articles based on date and store in mongo db and retrieve details from database using fast api

## Run the project locally

Clone the repository

`git clone https://github.com/hemavathim194/ai_news_article.git`

Enter into the directory

`cd src`

Source the virtual env

For Linux,

`source /venv/bin/activate`

For windows

`venv/bin/activate`

Install the dependencies

`pip install -r requirements.txt`

Run the project

`uvicorn main:app --reload`

The project will be available at `http://127.0.0.1:8000/` and the API docs is available at `http://127.0.0.1:8000/docs`
