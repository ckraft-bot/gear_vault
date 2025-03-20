import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Gear Vault", page_icon=":person_climbing:", layout="centered")

# App title
st.title("Welcome to Gear Vault 🧗‍♂️")

# Description
st.write(
    "Manage your climbing gear efficiently with **Gear Vault**. "
    "Track your equipment, monitor expiration dates, and keep notes — all in one place! "
    "**Safety is paramount** when it comes to climbing, and using expired or worn-out gear can put you at serious risk. "
    "Gear Vault helps you stay on top of maintenance and replacement schedules, ensuring your gear is always in top condition. "
    "Whether you're a beginner or a seasoned climber, Gear Vault helps you climb with confidence and peace of mind!"
)


# Create two columns for navigation buttons
col1, col2 = st.columns(2)

with col1:
    # Button to navigate to the Form page
    if st.button(":heavy_plus_sign: Add Equipment"):
        st.set_page_config(page_title="Form")
        st.switch_page("Form")  # Page name, no file path or extension

with col2:
    # Button to navigate to the Check page
    if st.button(":mag: Check Equipment"):
        st.set_page_config(page_title="Check")
        st.switch_page("Check")  # Page name, no file path or extension