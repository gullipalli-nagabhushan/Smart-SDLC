from fastapi import APIRouter, Form
import hashlib
from models import user_model

router = APIRouter()
users = {}

@router.post("/register")
def register_user(username: str = Form(...), password: str = Form(...)):
    if username in users:
        return {"error": "User already exists"}
    users[username] = hashlib.sha256(password.encode()).hexdigest()
    return {"status": "Registered successfully"}

@router.post("/login")
def login_user(username: str = Form(...), password: str = Form(...)):
    if username not in users or users[username] != hashlib.sha256(password.encode()).hexdigest():
        return {"error": "Invalid credentials"}
    return {"status": "Login successful"}