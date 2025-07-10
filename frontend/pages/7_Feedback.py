import streamlit as st
from api_client import submit_feedback



st.title("📬 Submit Feedback")
username = st.text_input("Your Name")
feedback_text = st.text_area("Your Feedback", height=150)
if st.button("Send Feedback"):
    if "logged_in" in st.session_state :
        response = submit_feedback(st.session_state.user["localId"],username, feedback_text)
        if response.status_code == 200:
            st.success("Feedback submitted successfully")
        else:
            st.error("Error submitting feedback")
    else:
        st.warning("Please log in to submit feedback.")
        st.switch_page("Home.py")  # redirect to login page

    