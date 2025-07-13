import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
st.set_page_config(page_title="Smart SDLC - Logout", page_icon=":lock:")
st.title("Smart SDLC ")
if st.session_state.logged_in:
    st.session_state.logged_in = False
    st.session_state.user = None

    for key in st.session_state.keys():
        del st.session_state[key]

    st.success("You have been logged out successfully!")

    st.markdown("""
        <meta http-equiv="refresh" content="2; url=/" />
        <p>Redirecting to login...</p>
    """, unsafe_allow_html=True)
else:
    st.markdown("You are not logged in yet")
