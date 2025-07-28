import requests
import os
# Replace these with your actual credentials
API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")  # Use the model ID you want to delete
IAM_URL = "https://iam.cloud.ibm.com/identity/token"

# Step 1: Get bearer token
def get_access_token():
    response = requests.post(
        IAM_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=f"apikey={API_KEY}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    )
    return response.json()["access_token"]

# Step 2: Delete model
def delete_fine_tuned_model(model_id):
    token = get_access_token()
    url = f"https://us-south.ml.cloud.ibm.com/ml/v4/models/{model_id}?version=2024-07-01&project_id={PROJECT_ID}"
    
    response = requests.delete(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    if response.status_code == 204:
        print("✅ Model deleted successfully.")
    else:
        print(f"❌ Failed to delete model: {response.status_code}")
        print(response.text)

# Call the function
delete_fine_tuned_model(MODEL_ID)
