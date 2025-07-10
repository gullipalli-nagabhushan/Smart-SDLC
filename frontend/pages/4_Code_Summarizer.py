import streamlit as st
from api_client import post_text


st.title("📝 Code Summarizer")


code_input = st.text_area("Paste code to summarize", key="text_input", height=400)
if st.button("Summarize"):
    # Redirect to login if not logged in
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.switch_page("main.py")  # redirect to login page
        st.stop()
    response = post_text("/ai/summarize-code", {"code": code_input})
    st.success(response.json().get("summary", "No summary available"))
