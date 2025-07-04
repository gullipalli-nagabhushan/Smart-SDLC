import streamlit as st
from api_client import post_file

st.title("📄 Upload PDF and Classify")

pdf_file = st.file_uploader("Upload your requirement PDF", type=["pdf"])
if pdf_file:
    response = post_file("/ai/upload-pdf", pdf_file)
    if response.status_code == 200:
        st.success("PDF Processed Successfully")
        st.json(response.json())
    else:
        st.error("Failed to process PDF")
