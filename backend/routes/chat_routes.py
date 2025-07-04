from fastapi import APIRouter, Form
from services.watsonx_service import call_watsonx

router = APIRouter()

@router.post("/chat")
def chat_with_ai(message: str = Form(...)):
    prompt = f"You are a helpful SDLC assistant. {message}"
    return {"response": call_watsonx(prompt)}