import streamlit as st
from api_client import post_text



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
st.title("📝 Code Summarizer")


code_input = st.text_area("Paste code to summarize", key="text_input", height=300)
if st.button("Summarize"):
    if code_input.strip():
        if not st.session_state.logged_in:
            st.warning("Please log in to summarize code.")
            st.page_link("Home.py",label="Click here to Login")   
            st.stop()
        response = post_text("/ai/summarize-code", {"code": code_input})
        st.markdown(response.get("summary", "No summary available"))
    else:
        st.warning("Please provide your code.")
