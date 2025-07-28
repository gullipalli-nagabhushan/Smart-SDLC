# services/watsonx_service.py

import requests
from config import WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_MODEL_ID

def get_iam_token():
    iam_url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": WATSONX_API_KEY
    }

    try:
        response = requests.post(iam_url, headers=headers, data=data)
        response.raise_for_status()
        return response.json().get("access_token")
    
    except requests.exceptions.RequestException as e:
        print("⚠️ Failed to get IAM token:", response.status_code, response.text)
        return None

def call_watsonx(prompt: str):
    token = get_iam_token()
    if not token:
        return "Error: Unable to authenticate with Watsonx."

    url = f"https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    payload = {
        "model_id": WATSONX_MODEL_ID,
        "project_id": WATSONX_PROJECT_ID,
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200,
            "min_new_tokens": 0,
            "repetition_penalty": 1,
            "temperature": 0.6
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        print("✅ Watsonx API Response:", result)
        # Updated parsing based on current Watsonx output
        if "results" in result and isinstance(result["results"], list):
            return result["results"][0].get("generated_text", "[No Generated Text]")
        else:
            print("⚠️ Unexpected response format:", result)
            return "[Unexpected API Response Format]"

    except requests.exceptions.RequestException as e:
        print("Watsonx API error:", response.status_code, response.text)
        return "[API Error]"