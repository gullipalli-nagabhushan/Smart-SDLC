import streamlit as st
from api_client import post_text


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("💻 AI Code Generator")

prompt = st.text_area("Enter Task or Requirement", key="text_input", height=200)
if st.button("Generate Code"):
    if prompt.strip():
        if not st.session_state.logged_in:
            st.warning("Please log in to generate code.")
            st.page_link("Home.py",label="Click here to Login") 
            st.stop()
        response = post_text("/ai/generate-code", {"prompt": prompt})
        print(response)
        st.markdown(response["response"])
    else:
        st.warning("what do you want to code,write something about it ?")
   
    
