import streamlit as st
from api_client import post_text

st.title("💻 AI Code Generator")
prompt = st.text_area("Enter Task or Requirement")
if st.button("Generate Code"):
    response = post_text("/ai/generate-code", {"prompt": prompt})
    res = response.json()
    print(res)
    st.code(res.get("code", "No code generated"))
