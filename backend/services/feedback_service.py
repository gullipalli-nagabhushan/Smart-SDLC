def save_feedback(user, feedback):
    with open("feedback_store.txt", "a") as f:
        f.write(f"{user}: {feedback}\n")