from pymongo import MongoClient
import os
client = MongoClient(os.getenv('DATABASE_URL'))
db = client['ai_news']
collection = db['news_articles']

