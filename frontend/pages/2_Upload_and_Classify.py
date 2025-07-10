import streamlit as st
from api_client import post_file



st.title("📄 Upload PDF and Classify")

pdf_file = st.file_uploader("Upload your requirement PDF", type=["pdf"])
if pdf_file:
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.switch_page("main.py")  # redirect to login page
        st.stop()
    response = post_file("/ai/upload-pdf", pdf_file)
    if response.status_code == 200:
        st.success("PDF Processed Successfully")
        st.json(response.json())
    else:
        st.error("Failed to process PDF")
