import streamlit as st
from api_client import post_text

st.title("🧪 Test Case Generator")
code = st.text_area("Paste your code")
if st.button("Generate Tests"):
    response = post_text("/ai/generate-tests", {"code": code})
    st.code(response.json().get("tests", "No tests generated"))

