import streamlit as st
import webbrowser
# import pyown

st.set_page_config(page_title="Enter location info to begin!")

def home_page():
  location = st.text_input('Your Location')
  if location != '':
    getLocation(location)

def getLocation(loc):
  # mgr = pyown.weather_manager()
  print(loc)

home_page()
