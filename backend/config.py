from dotenv import load_dotenv
import os
load_dotenv()

WATSONX_API_KEY     = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID  = os.getenv("WATSONX_PROJECT_ID")
WATSONX_MODEL_ID    = os.getenv("WATSONX_MODEL_ID")
WATSONX_REGION      = os.getenv("WATSONX_REGION")

MONGO_DB_USERNAME   = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD   = os.getenv("MONGO_DB_PASSWORD")
MONGO_DB_URI        = os.getenv("MONGO_DB_URI")

FIREBASE_API_KEY    = os.getenv("FIREBASE_API_KEY")
FIREBASE_PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID')

BASE_URL            = os.getenv("BASE_URL")      
FRONTEND_URL        = os.getenv("FRONTEND_URL") 

print("----------------------------------------------------------------------------------")
print("Loading Config...")
print("✅ Config Loaded - secret keys hidden")
# print(WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_MODEL_ID) # Debugging Purpose
# print(MONGO_DB_USERNAME, MONGO_DB_PASSWORD, MONGO_DB_URI)
# print(FIREBASE_API_KEY, FIREBASE_PROJECT_ID)
# print(BASE_URL, FRONTEND_URL)
print("----------------------------------------------------------------------------------")