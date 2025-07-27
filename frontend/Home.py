import streamlit as st
import requests
import streamlit.components.v1 as components
from urllib.parse import urlparse, parse_qs
from api_client import login,register,verify_token
import json


BASE_URL = st.secrets["BASE_URL"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

query_params = st.query_params

if "idToken" in query_params:
    id_token = query_params["idToken"]
    response = verify_token(id_token)
    if response["success"]:
        st.session_state.user = response["user"]
        st.session_state.logged_in = True
        st.success(response["message"])
    else:
        st.error(response["message"])


if "user" in st.session_state:
    st.success(f"Welcome {st.session_state.user['name'].capitalize()} 👋")
    st.write("✅ You are now on the Smart SDLC dashboard.")
  
    

st.set_page_config(
    page_title="Smart SDLC - Login",
    page_icon="🧠",
    layout="wide",
    menu_items={
        'Get Help': 'https://github.com/gullipalli-nagabhushan/Smart-SDLC/issues',
        'Report a bug': 'https://github.com/gullipalli-nagabhushan/Smart-SDLC/issues',
        'About': 'https://github.com/gullipalli-nagabhushan/Smart-SDLC'
    })

st.title("Smart SDLC")
col1, col2 = st.columns([2, 1])

with col1:
    st.image(r"frontend/static/Smart_SDLC.png", use_container_width=True)

with col2:
    st.header("Login or Sign Up")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pwd")

        if st.button("Login", disabled=st.session_state.logged_in):
            if login_email.strip() != "" and  "@gmail.com" in login_email and login_password.strip() != "":

                result = login(login_email, login_password)
                
                if result["success"]:
                    st.success(result["message"])
                    st.session_state.user = result["user"] 
                    st.session_state.logged_in = True
                else:
                    st.error(result["message"])
                    if "details" in result:
                        st.code(result["details"])
                    if "error" in result:
                        st.code(result["error"])  
            else:
                st.error("Please enter valid email and password.")
               
    with tab2:
        signup_name = st.text_input("Name", key="signup_name")
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input("Password", type="password", key="signup_pwd")
        if st.button("Sign Up", disabled=st.session_state.logged_in):
            if signup_name.strip() != "" and signup_email.strip() != "" and  "@gmail.com" in signup_email and signup_password.strip() != "":
                try:
                    response = register(signup_name,signup_email, signup_password)
                    if response["success"]:
                        st.success(response["message"])
                        result = login(signup_email, signup_password)
                        st.session_state.user = result["user"] 
                        st.session_state.logged_in = True  
                        st.markdown("### 👤 User Data:")
                        st.code(json.dumps(result["user"], indent=2), language="json")
                    else:
                        if "details" in response:
                            st.error(response["details"])
                        if "error" in response:
                            st.code(response["error"])
                except:
                    st.error("Failed to create user. Ensure password has 6+ characters.")  
            else:
                st.error("Please enter email and password.")
    if st.session_state.logged_in:
        st.write(f"You are already logged in  !")
    else:
        st.warning("Please log in to continue.")
        # Button to trigger redirect
        # st.link_button("Continue with Google", f"{BASE_URL}/auth/google")
        # st.link_button("Continue with GitHub", f"{BASE_URL}/auth/github")


st.markdown("""
# 🚀 SmartSDLC: AI-powered Software Development Lifecycle Assistant

Welcome to **SmartSDLC**, an AI-driven platform designed to **simplify, automate, and accelerate** the Software Development Life Cycle (SDLC). 
This web application helps students, developers, and teams build better software by integrating tools and intelligence into every stage — from requirements to deployment.

---

## 🔍 What You Can Do With SmartSDLC

- 💬 **Chat with AI**: Ask development-related queries or brainstorm features with an integrated AI assistant.
- 🧾 **Summarize Code**: Upload large codebases or modules and get clean summaries of logic and structure.
- 🧑‍💻 **Code Generation**: Instantly generate boilerplate code, classes, or logic from natural language prompts.
- 📄 **Task Classification**: Upload your **SRS document** and get tasks auto-classified by functional and non-functional requirements.
- 🧪 **Test Case Generator**: Create test cases from descriptions, logic, or existing code to ensure better software testing.
- 🐞 **Bug Fixer**: Upload broken code and let the AI identify and fix potential bugs.
- 🔐 **Firebase Authentication**: Secure login and sign-up with Firebase Authentication and Firestore.
- ☁️ **Cloud Storage & Retrieval**: Store your project state, task flow, and documents in MongoDB.(*Not available *)

---

## 🧑‍💻 Technologies Used

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI Models**: IBM Watsonx.ai, LangChain
- **Database**: Firebase Firestore, MongoDB
- **Auth**: Firebase Authentication
- **CI/CD & Deployment**: GitHub + Cloud

---

## 💡 Who Is This For?

This application is built especially for:

- 🎓 Students working on academic software projects
- 🧑‍💻 Developers wanting to streamline routine SDLC tasks
- 👥 Hackathon teams needing fast, AI-supported idea execution
- 📈 Product teams building MVPs with structure and clarity

---

## 🔗 Learn More or Contribute

Visit my GitHub to explore the source code, raise issues, or contribute to this project:

👉 [GitHub Profile – Gullipalli Nagabhushan](https://github.com/gullipalli-nagabhushan)

---

Feel free to try out all features and simplify your software engineering process with **SmartSDLC**!
""")
  
