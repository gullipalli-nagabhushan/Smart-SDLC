import streamlit as st
from api_client import submit_feedback

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("📬 Submit Feedback")

username = st.text_input("Your Name")
feedback_text = st.text_area("Your Feedback", height=150)
if st.button("Send Feedback"):
    if username.strip() and feedback_text.strip():
        if st.session_state.logged_in:
            response = submit_feedback(st.session_state.user["localId"],username, feedback_text)
            if response.status_code == 200:
                st.success("Feedback submitted successfully")
            else:
                st.error("Error submitting feedback")
        else:
            st.warning("Please log in to submit feedback.")
            st.page_link("Home.py",label="Click here to Login") 
    else:
        st.warning("Both Name and Feedback fields are mandatory.")
    