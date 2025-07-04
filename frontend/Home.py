import streamlit as st
from api_client import chat_with_bot

st.set_page_config(page_title="SmartSDLC", layout="wide")
st.title("🚀 SmartSDLC")
st.subheader("Your AI-powered SDLC Assistant")

col1, col2 = st.columns(2)
with col1:
    st.image("ai_sdlc.jpg", width=300)

with col2:
    with st.form("chat_form"):
        query = st.text_input("Ask SmartBot (e.g., What is SDLC?)")
        submit = st.form_submit_button("Chat")
        if submit and query:
            reply = chat_with_bot(query)
            st.success("Query: " + query)
            st.success("Response:")
            print(reply.status_code, reply.json())
            st.success(reply.get("response", "No response"))

st.markdown("---")
st.markdown("### 📄 Navigate to Features from Sidebar")
