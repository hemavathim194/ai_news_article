from typing import List
from fastapi import HTTPException
from fastapi import APIRouter, HTTPException
from mongodb.connection import db
from scraper import *

router = APIRouter()

#Get all ai news articles
@router.get("/api/v1/get-all-news")
async def get_all_news():
    news_articles = list(collection.find())
    print(news_articles)

    if not news_articles:
        return []

    for news_article in news_articles:
        news_article["_id"] = str(news_article["_id"])

    return news_articles

#Get all ai news articles based on provided search date
@router.get("/api/v1/search-news-by-date")
async def search_news(year: int,month: str, date: int):
    coun_news_articles = list(collection.find({"date":date,"month":month,"year":year}))
    if not coun_news_articles:
        return []

    for news_article in coun_news_articles:
        news_article["_id"] = str(news_article["_id"])

    return coun_news_articles

#Insert news article data into database based on given date by scraping
@router.post("/api/v1/add-news-article")
async def insert_news_article(year: int,month: str, date: int):
    await ai_news_of_the_day(year,month,date)

    coun_news_articles = list(collection.find({"date":date,"month":month,"year":year}))
    if not coun_news_articles:
        return []

    for news_article in coun_news_articles:
        news_article["_id"] = str(news_article["_id"])

    return coun_news_articles
    
