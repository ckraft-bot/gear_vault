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

# Buttons for navigation
col1, col2 = st.columns(2)

with col1:
    if st.button(":heavy_plus_sign: Add Equipment"):
        st.switch_page("pages/Form.py")

with col2:
    if st.button(":mag: Check Equipment"):
        st.switch_page("pages/Check.py")
