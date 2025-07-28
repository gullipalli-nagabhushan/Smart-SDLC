from fastapi import APIRouter, Form
from services.feedback_service import save_feedback

router = APIRouter()

@router.post("/submit")
def submit_feedback(uuid: str = Form(...), user: str = Form(...), feedback: str = Form(...)):
    try:
        save_feedback(uuid,user, feedback)
        return {"status": "Feedback recieved"}
    except Exception as e:
        return {"status": "Feedback not received"}