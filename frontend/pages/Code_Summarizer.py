import streamlit as st
from api_client import post_text

st.title("📝 Code Summarizer")
code_input = st.text_area("Paste code to summarize")
if st.button("Summarize"):
    response = post_text("/ai/summarize-code", {"code": code_input})
    st.success(response.json().get("summary", "No summary available"))
