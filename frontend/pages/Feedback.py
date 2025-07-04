import streamlit as st
from api_client import submit_feedback

st.title("📬 Submit Feedback")
username = st.text_input("Your Name")
feedback_text = st.text_area("Your Feedback")

if st.button("Send Feedback"):
    response = submit_feedback(username, feedback_text)
    if response.status_code == 200:
        st.success("Feedback submitted successfully")
    else:
        st.error("Error submitting feedback")
