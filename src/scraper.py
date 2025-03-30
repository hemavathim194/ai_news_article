from typing import List
import requests as _requests
import bs4 as _bs4
from pymongo import MongoClient
from mongodb.connection import collection


def _generate_url(year: int,month: str, date: int) -> str:
    url = f"https://www.theguardian.com/technology/artificialintelligenceai/{year}/{month}/{date}/all"
    return url


def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


async def ai_news_of_the_day(year: int,month: str, date: int):
    url = _generate_url(year, month, date)
    page = _get_page(url)
    news_header = page.find_all('a', class_="u-faux-block-link__overlay js-headline-text")

    for news in news_header:
        print(f'{news.text} - {news.get('href')}')
        news_details = {
            'header': news.text,
            'link': news.get('href'),
            'month': month,
            'date': date,
            'year': year
        }
        collection.insert_one(news_details)

def get_news():
    users = collection.find()
    print(users)

# ai_news_of_the_day(2025,'mar',23)
# get_news()