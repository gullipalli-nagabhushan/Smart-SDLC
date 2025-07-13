import streamlit as st
from api_client import post_file


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
st.title("📄 Upload PDF and Classify")

pdf_file = st.file_uploader("Upload your requirement PDF", type=["pdf"])
if pdf_file:
    if not st.session_state.logged_in:
        st.warning("Please log in to continue.")
        st.page_link("Home.py",label="Click here to Login")
        st.stop()
    response = post_file("/ai/upload-pdf", pdf_file)
    if response.status_code == 200:
        st.success("PDF Processed Successfully")
        st.json(response.json())
    else:
        st.error("Failed to process PDF")
