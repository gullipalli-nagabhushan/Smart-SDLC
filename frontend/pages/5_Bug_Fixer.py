import streamlit as st
from api_client import post_text


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
st.title("🐞 Bug Fixer")


buggy_code = st.text_area("Paste buggy code", key="text_input", height=300)
if st.button("Fix Code"):
    if buggy_code.strip():
        if not st.session_state.logged_in:
            st.warning("Please log in to fix code.")
            st.page_link("Home.py",label="Click here to Login") 
            st.stop()
        response = post_text("/ai/fix-bugs", {"code": buggy_code})
        st.markdown(response.get("fixed_code", "No fix suggested"))
    else:
        st.warning("Write your buggy code")
