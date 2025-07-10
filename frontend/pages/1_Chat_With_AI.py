import streamlit as st
from api_client import chat_with_bot



st.set_page_config(page_title="SmartSDLC", layout="wide")
st.subheader("Your AI-powered SDLC Assistant")

if "logged_in"  in st.session_state :
    st.title("Welcome to Smart SDLC! 🚀")
    st.write(f"Logged in as: {st.session_state.user['email']}")


content = st.session_state.get("text_input", "")
height = max(100, min(600, len(content.splitlines()) * 20))
respn = {}
col1, col2 = st.columns([1, 2])
with col1:
    st.image(r"frontend\static\ai_sdlc.jpg", width=300)

with col2:
    with st.form("chat_form"):
        query = st.text_area("Ask SmartBot (e.g., What is SDLC?)", key="text_input", height=200)
        submit = st.form_submit_button("Chat")
        if submit and query:
            if "logged_in"  in st.session_state or st.session_state.logged_in:
                reply = chat_with_bot(query)
                
                print(reply.status_code, reply.json())
                respn = reply.json()
            else:
                st.error("You are not logged in. Please log in first.")
                st.switch_page("main.py")
st.markdown("---")
if respn:
    st.success("Query: " + query)
    st.success("Response:"+respn.get("response", "No response"))

