import requests
import hashlib
import os, urllib.parse
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Form, Request, FastAPI, Request, HTTPException
from pydantic import BaseModel
from config import BASE_URL,FRONTEND_URL, FIREBASE_PROJECT_ID, FIREBASE_API_KEY
from services.auth_service import verify_firebase_token
from models import user_model
from models.token_payload_model import TokenPayload



users = {}

router = APIRouter()


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


@router.post("/verify")
async def verify_token(data: TokenPayload):
    user = verify_firebase_token(data.idToken)
    return {"user": user}



@router.get("/callback")
def auth_callback(request: Request):
    # Firebase will append three query params: 
    #   * `oobCode` (the credential), 
    #   * `providerId`, 
    #   * and `operation`="signIn"
    qp = request.query_params
    oob_code     = qp.get("oobCode")
    provider_id  = qp.get("providerId")
    if not oob_code or not provider_id:
        raise HTTPException(400, "Missing credential")

    # 2) Exchange that credential for a Firebase ID token:
    resp = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key={FIREBASE_API_KEY}",
        headers={"Content-Type": "application/json"},
        json={
            "postBody":    f"oobCode={oob_code}&providerId={provider_id}",
            "requestUri":  f"{BASE_URL}/auth/callback",
            "returnSecureToken": True
        }
    ).json()

    id_token = resp.get("idToken")
    if not id_token:
        raise HTTPException(401, f"Firebase signInWithIdp failed: {resp}")

    # 3) Redirect back to your Streamlit UI with the Firebase ID token
    redirect = RedirectResponse(f"{FRONTEND_URL}/?idToken={id_token}")
    # Optionally set a secure cookie instead:
    redirect.set_cookie("session", id_token, httponly=True, samesite="lax")
    return redirect



@router.get("/{provider}")
def start_auth(provider: str):
    if provider == "google":
        idp = "google.com"
    elif provider == "github":
        idp = "github.com"
    else:
        raise HTTPException(400, "Unknown provider")

    # Firebase’s built-in OAuth redirect endpoint:
    params = {
        "providerId": idp,
        "continueUrl": f"{BASE_URL}/auth/callback"
    }
    url = f"https://{FIREBASE_PROJECT_ID}.firebaseapp.com/__/auth/handler?{urllib.parse.urlencode(params)}"
    return RedirectResponse(url)