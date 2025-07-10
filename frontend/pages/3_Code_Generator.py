import streamlit as st
from api_client import post_text


st.title("💻 AI Code Generator")

prompt = st.text_area("Enter Task or Requirement", key="text_input", height=400)
if st.button("Generate Code"):
    
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.switch_page("main.py")  # redirect to login page
        st.stop()
    response = post_text("/ai/generate-code", {"prompt": prompt})
    res = response.json()
    print(res)
    st.code(res.get("code", "No code generated"))
