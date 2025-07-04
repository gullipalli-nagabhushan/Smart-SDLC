from dotenv import load_dotenv
import os
load_dotenv()

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID")
print(WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_MODEL_ID)