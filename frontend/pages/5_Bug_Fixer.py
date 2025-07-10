import streamlit as st
from api_client import post_text

st.title("🐞 Bug Fixer")


buggy_code = st.text_area("Paste buggy code", key="text_input", height=400)
if st.button("Fix Code"):
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.switch_page("main.py")  # redirect to login page
        st.stop()
    response = post_text("/ai/fix-bugs", {"code": buggy_code})
    st.code(response.json().get("fixed_code", "No fix suggested"))
