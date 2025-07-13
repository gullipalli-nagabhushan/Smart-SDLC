import requests

BASE_URL = "http://127.0.0.1:8000"

def post_file(endpoint, file):
    return requests.post(f"{BASE_URL}{endpoint}", files={"file": file})

def post_text(endpoint, data):
    return requests.post(f"{BASE_URL}{endpoint}", data=data)

def post_json(endpoint, json):
    print(json)
    return requests.post(f"{BASE_URL}{endpoint}", json=json, headers={"Content-Type": "application/json"})
def chat_with_bot(message):
    response = post_text("/chat/chat", {"message": message})
    if response.status_code == 200:
        return {
            "success": True,
            "response": response.json().get("response", "No response")
        }
    else:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": response.text
        }
    


def submit_feedback(uuid,user, feedback):
    return post_text("/feedback/submit", {"uuid":uuid,"user": user, "feedback": feedback})


def register(name,email, password):
    response = post_json("/auth/register", {"name":name,"email": email, "password": password})
    if response.status_code == 200:
        return {
            "success": True,
            "message": "User created successfully",
            "user": response.json().get("user")
        }
    else:
        return {
            "success": False,
            "message": f"Unexpected error: {response.status_code}",
            "details": response.json().get("detail") or response.text
        }
def login(email, password):

    response = post_json("/auth/login", {"email": email, "password": password})
    try:
        if response.status_code == 200:
                return {
                    "success": True,
                    "message": "Login successful",
                    "user": response.json().get("user")
                }
        elif response.status_code == 404:
            return {"success": False, "message": response.json().get("detail")}
        elif response.status_code == 401:
            return {"success": False, "message": response.json().get("detail")}
        else:
            return {"success": False, "message": f"Unexpected error: {response.status_code}", "details": response.text}
    except Exception as e:
        return {"success": False, "message": "Connection error", "error": str(e)}


def verify_token(token):
    response = post_json("/auth/verify", {"idToken": token})
    if response.status_code == 200:
        return {
            "success": True,
            "message": "Login successful",
            "user": response.json().get("user")
        }
    elif response.status_code == 401:
        return {
            "success": False,
            "message": "Invalid token or Token expired. Please log in again.",
            "details": response.text
        }
    elif response.status_code == 404:
        return {
            "success": False,
            "message": "User not found. Please Sign Up first.",
            "details": response.text
        }
    return {
        "success": False,
        "message": f"Unexpected error: {response.status_code}",
        "details": response.text
    }