
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from datetime import datetime
from config import MONGO_DB_URI

# Create a new client and connect to the server
client = MongoClient(MONGO_DB_URI,tls=True,serverSelectionTimeoutMS=5000)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["smart_sdlc"]

users_collection = db["users"]
chats_collection = db["chats"]
feedback_collection = db["feedback"]

