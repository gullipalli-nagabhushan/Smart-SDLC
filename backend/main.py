from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ai_routes, auth_routes, chat_routes, feedback_routes
from config import WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_MODEL_ID

app = FastAPI(title="SmartSDLC", version="1.0")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(ai_routes.router, prefix="/ai")
app.include_router(auth_routes.router, prefix="/auth")
app.include_router(chat_routes.router, prefix="/chat")
app.include_router(feedback_routes.router, prefix="/feedback")

@app.get("/")
def root():
    return {"message": "SmartSDLC Backend Running"}