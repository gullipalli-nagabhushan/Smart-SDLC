import requests

BASE_URL = "http://127.0.0.1:8000"

def post_file(endpoint, file):
    return requests.post(f"{BASE_URL}{endpoint}", files={"file": file})

def post_text(endpoint, data):
    return requests.post(f"{BASE_URL}{endpoint}", data=data)


def chat_with_bot(message):
    return post_text("/chat/chat", {"message": message})


def submit_feedback(user, feedback):
    return post_text("/feedback/submit", {"user": user, "feedback": feedback})

