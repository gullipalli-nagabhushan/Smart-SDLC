from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConfigurationError, ServerSelectionTimeoutError
from pymongo import MongoClient
from datetime import datetime
from config import MONGO_DB_URI

users_collection = None
chats_collection = None
feedback_collection = None

try:
    client = MongoClient(MONGO_DB_URI,tls=True,serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ MongoDB Connection Success")
    print("Pinged your deployment. You successfully connected to MongoDB!")
   

    if not client:
        raise Exception("MongoDB not connected. Please check your internet or DNS settings.")


    db = client["smart_sdlc"]

    users_collection = db["users"]
    chats_collection = db["chats"]
    feedback_collection = db["feedback"]

except (ConfigurationError, ServerSelectionTimeoutError, Exception) as e:
    print("❌ MongoDB Connection Error: No network connection or DNS issue.")

    print("May be problem is Current IP address is not added in MongoDB. Please add it.")
    # print(f"Details: {e}")
print("----------------------------------------------------------------------------------")


