import streamlit as st
from api_client import post_text


st.title("🧪 Test Case Generator")


code = st.text_area("Paste your code", key="text_input", height=300)
if st.button("Generate Tests"):
    if code.strip():
        if not st.session_state.logged_in:
            st.warning("Please login to continue")
            st.page_link("Home.py",label="Click here to Login") 
            st.stop()
        response = post_text("/ai/generate-tests", {"code": code})
        st.code(response.get("tests", "No tests generated"))
    else:
        st.warning("Write the code, for which generate test cases")

