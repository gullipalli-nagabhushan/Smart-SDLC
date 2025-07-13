import streamlit as st
from api_client import chat_with_bot

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


st.set_page_config(page_title="SmartSDLC", layout="wide")
st.subheader("Your AI-powered SDLC Assistant")

if  st.session_state.logged_in:
    st.title("Welcome to Smart SDLC! 🚀")
    st.write(f"Logged in as: {st.session_state.user['email']}")


content = st.session_state.get("text_input", "")
height = max(100, min(600, len(content.splitlines()) * 20))
reply = {"success": False}
col1, col2 = st.columns([1, 2])
with col1:
    st.image(r"frontend/static/ai_sdlc.jpg", width=300)

with col2:
    with st.form("chat_form"):
        query = st.text_area("Ask SmartBot (e.g., What is SDLC?)", key="text_input", height=180)
        submit = st.form_submit_button("Chat")
        if submit:
            if query.strip():
                if st.session_state.logged_in:
                    reply = chat_with_bot(query)
                    print(reply)
                else:
                    st.warning("You are not logged in. Please log in first.")
                    st.page_link("Home.py",label="Click here to Login")   
                    st.stop()
            else:
                st.warning("what do you want to know,please write some thing...")
st.markdown("---")
if reply["success"]:
    st.error("Query: " + query)
    st.success("Response:"+ reply.get("response", "No response"))



