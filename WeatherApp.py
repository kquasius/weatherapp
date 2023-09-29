import streamlit as st
import webbrowser
# import pyown

st.set_page_config(page_title="Enter location info to begin!")

def home_page():
  location = st.text_input('Your Location')
  if "clicked" not in st.session_state:
    st.session_state.clicked = False
  if st.button('Submit') or st.session_state["clicked"]:
    getLocation(location)

def getLocation(loc):
  # mgr = pyown.weather_manager()

home_page()
