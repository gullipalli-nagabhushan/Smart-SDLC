import requests
from config import WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_MODEL_ID, WATSONX_REGION
 

# Get IAM Token
def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={WATSONX_API_KEY}"
    res = requests.post(url, headers=headers, data=data)
    return res.json()["access_token"]

# Call Model
def call_watsonx(prompt):
    token = get_token()
    url = f"https://{WATSONX_REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model_id": WATSONX_MODEL_ID,
        "project_id": WATSONX_PROJECT_ID,
        "input": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7
        }
    }
    res = requests.post(url, headers=headers, json=payload)
    print(res.json())

call_watsonx("write a python script for print 100 numbers")
