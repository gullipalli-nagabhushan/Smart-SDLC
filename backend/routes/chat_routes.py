from fastapi import APIRouter, Form
from services.watsonx_service import call_watsonx

router = APIRouter()

@router.post("/chat")
def chat_with_ai(message: str = Form(...)):
    prompt = f"You are an Smart SDLC AI assistant . You will reply to the user . Reply to: {message}"
    return {"response": call_watsonx(prompt)}