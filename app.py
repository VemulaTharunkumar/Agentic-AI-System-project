import streamlit as st
import sys
import os

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.login_ui import show_login_page
from ui.dashboard import show_chat_page

# Set page config globally in the main app
st.set_page_config(
    page_title="Agentic AI System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Initialize authentication state
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_id = None
        st.session_state.username = None

    # Router logic
    if st.session_state.authenticated:
        show_chat_page()
    else:
        show_login_page()

if __name__ == "__main__":
    main()
