from pymongo import MongoClient
client = MongoClient('mongodb+srv://hemavathi194:dgYaXc2LStNc8tfU@cluster0.mmj4cmh.mongodb.net/')
db = client['ai_news']
collection = db['news_articles']


# Replace these with your MongoDB connection details
# MONGO_USERNAME = "hemavathi194"
# MONGO_PASSWORD = "dgYaXc2LStNc8tfU"
# MONGO_HOST = "cluster0.mmj4cmh.mongodb.net"
# MONGO_PORT = 27017
# MONGO_DB = "ai_news"

# # Create a MongoDB client
# client = MongoClient(
#     f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}")
# db = client[MONGO_DB]