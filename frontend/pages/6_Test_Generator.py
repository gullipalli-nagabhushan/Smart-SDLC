import streamlit as st
from api_client import post_text


st.title("🧪 Test Case Generator")


code = st.text_area("Paste your code", key="text_input", height=400)
if st.button("Generate Tests"):
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.switch_page("main.py")  # redirect to login page
        st.stop()
    response = post_text("/ai/generate-tests", {"code": code})
    st.code(response.json().get("tests", "No tests generated"))

