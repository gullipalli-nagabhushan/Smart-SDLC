from datetime import datetime
from mongoDB import feedback_collection
def save_feedback(user_uid: str,user_name: str, feedback: str):
    feedback_collection.insert_one({
        "user_uid": user_uid,
        "user_name": user_name,
        "feedback": feedback,
        "timestamp": datetime.utcnow()
    })
