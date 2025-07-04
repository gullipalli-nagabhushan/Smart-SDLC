import streamlit as st
from api_client import post_text

st.title("🐞 Bug Fixer")
buggy_code = st.text_area("Paste buggy code")
if st.button("Fix Code"):
    response = post_text("/ai/fix-bugs", {"code": buggy_code})
    st.code(response.json().get("fixed_code", "No fix suggested"))
