import streamlit as st
import pyrebase
import requests
import streamlit.components.v1 as components
from urllib.parse import urlparse, parse_qs



FASTAPI_URL = "http://localhost:8000/auth/verify"

query_params = st.query_params

if "idToken" in query_params:
    id_token = query_params["idToken"]
    response = requests.post(FASTAPI_URL, json={"idToken": id_token})
    if response.status_code == 200:
        st.session_state.user = response.json()["user"]
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
    else:
        st.error("Login failed. Token is invalid.")


# If logged in
if "user" in st.session_state:
    st.success(f"Welcome {st.session_state.user['email']}")
    st.write("✅ You are now on the Smart SDLC dashboard.")
  
    

# Firebase Web Config 
firebaseConfig = st.secrets["firebase"]

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

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
    st.image(r"frontend\static\Smart_SDLC.png", use_container_width=True)

with col2:
    st.header("Login or Sign Up")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_pwd")

        if st.button("Login"):
            if login_email.strip() != "" and  "@gmail.com" in login_email and login_password.strip() != "":
                if not  "logged_in" in st.session_state:
                    try:
                        user = auth.sign_in_with_email_and_password(login_email, login_password)
                        st.session_state.user = user
                        st.success("Logged in successfully")
                        st.session_state.logged_in = True
                        st.switch_page("pages/1_Home.py")
                        st.stop()

                    except:
                        st.error("Failed to log in. Invalid credentials.")  
                else:
                    st.warning("You are already logged in.")
            else:
                st.error("Please enter valid email and password.")
               
    with tab2:
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input("Password", type="password", key="signup_pwd")
        if st.button("Sign Up"):
            if signup_email.strip() != "" and  "@gmail.com" in signup_email and signup_password.strip() != "":
                if not  "logged_in" in st.session_state:
                    try:
                        user = auth.create_user_with_email_and_password(signup_email, signup_password)
                        st.success("User created! You can log in now.")  
                    except:
                        st.error("Failed to create user. Ensure password has 6+ characters.")  
                else:
                    st.warning("You are already signed in.")
            else:
                st.error("Please enter email and password.")

    st.markdown("## Or ")
    
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.markdown("""
        <a href="https://gullipalli-nagabhushan.github.io/OAuth/auth.html" target="_self">
            <button style="background-color: #00000B; border:1px solid gray; border-radius: 5px; color: white; padding:10px 20px; font-size:20px;">🔐 Continue with Google or GitHub</button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.write("You are already logged in.")


   

    
