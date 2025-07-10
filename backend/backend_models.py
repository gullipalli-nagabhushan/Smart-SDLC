import  requests
from config import WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_MODEL_ID, WATSONX_REGION

def get_token():
    r = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={WATSONX_API_KEY}"
    )
    r.raise_for_status()
    return r.json()["access_token"]

def list_models():
    token = get_token()
    resp = requests.get(
        f"https://{WATSONX_REGION}.ml.cloud.ibm.com/ml/v1/foundation_model_specs?version=2024-05-01",
        headers={"Authorization": f"Bearer {token}"}
    )
    resp.raise_for_status()
    models = resp.json().get("models") or resp.json().get("resources") or resp.json()
    print("Available models:")
    for m in models:
        mid = m.get("id") or m.get("model_id")
        name = m.get("name") or m.get("display_name", "")
        print(f"- {mid} : {name}")

if __name__ == "__main__":
    list_models()
