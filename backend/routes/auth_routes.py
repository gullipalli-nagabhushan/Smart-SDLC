import requests
import hashlib
import os, urllib.parse
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Form, Request, FastAPI, Request, HTTPException
from config import BASE_URL,FRONTEND_URL, FIREBASE_PROJECT_ID, FIREBASE_API_KEY
from services.auth_service import verify_firebase_token, auth, db
from models.user_model import LoginUser,RegisterUser
from models.token_payload_model import TokenPayload
from mongoDB import users_collection as users
from firebase_admin import firestore


router = APIRouter()

@router.post("/register")
def register_user(user: RegisterUser):
    print("----------------------------------------------------------------------------------")
    try:
        # Create user in Firebase Authentication
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
            display_name=user.name,
        )
        uid = user_record.uid
        print("✅ User registered successfully at Firebase Auth")
        # Store additional user details in Firestore
        password = user.password
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = {
            "uid": uid,
            "provider": "email",
            "password": hash_password,
            "name": user.name,
            "email": user.email,
            "createdAt": firestore.SERVER_TIMESTAMP,
            "lastLogin": firestore.SERVER_TIMESTAMP
        }
        db.collection("users").document(uid).set(user_data)
        print("✅ User registered successfully at Firestore")
        print("----------------------------------------------------------------------------------")
        return {
            "message": "User registered successfully",
            "uid": uid,
            "email": user.email,
        }

    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")




@router.post("/login")
async def login_user(user: LoginUser):
    email = user.email
    password = user.password

    # Query the Firestore users collection for a document with matching email
    user_query = db.collection("users").where("email", "==", email).limit(1).stream()

    user_doc = next(user_query, None)

    if not user_doc:
        raise HTTPException(status_code=404, detail="User not found, Please Signup first")

    user_data = user_doc.to_dict()
    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

    if user_data["password"] != hashed_input_password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    user_data.pop("password", None)  # Optional: remove password before sending
    return {"message": "Login successful", "user": user_data}


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