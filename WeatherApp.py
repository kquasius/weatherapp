import streamlit as st
import webbrowser

st.set_page_config(page_title="Katie's Weather App")
st.header("Enter your location to begin!")

def home_page():
  location = st.text_input('Your Location')
  if location != '':
    getLocation(location)

def getLocation(loc):
  st.write(loc)

home_page()
