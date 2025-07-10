# backend/routers/auth_service.py

from fastapi import  HTTPException
from firebase_admin import credentials, auth, firestore, initialize_app
import firebase_admin

# Initialize Firebase Admin once globally
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_admin.json")
    initialize_app(cred)

db = firestore.client()

def verify_firebase_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token["uid"]

        # Store or update user in Firestore
        user_ref = db.collection("users").document(uid)
        user_doc = user_ref.get()

        if not user_doc.exists:
            user_data = {
                "uid": uid,
                "email": decoded_token.get("email"),
                "name": decoded_token.get("name"),
                "provider": decoded_token.get("firebase", {}).get("sign_in_provider"),
                "photo": decoded_token.get("picture", ""),
                "createdAt": firestore.SERVER_TIMESTAMP,
            }
            user_ref.set(user_data)
        else:
            user_ref.update({"lastLogin": firestore.SERVER_TIMESTAMP})

        return decoded_token
    except Exception as e:
        print("Token error:", e)
        raise HTTPException(status_code=401, detail="Invalid Firebase token")
