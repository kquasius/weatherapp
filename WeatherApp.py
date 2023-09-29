import streamlit as st
import requests

st.set_page_config(page_title="Katie's Weather App")
st.header("Enter your location to begin!")

def home_page():
  city = st.text_input('City')
  state = st.selectbox('State', {'WI', 'IL'})
  st.button('Submit')
  if submit:
    getLonLat(city, state)

def getLonLat(city, state):
  API_KEY = 'eee3e1e17b0471238be18e8f6cfbfee6'
  geo_url = 'http://api.openweathermap.org/geo/1.0/direct?q={'+ city + state + 'US&limit={limit}&appid=' + API_KEY
  geo_params = {
    "lat": lat,
    "lon": lon }
  geo = requests.get(geo_url, geo_params)
  st.write(geo)

def getLocation(lon, lat):
  st.write()

home_page()
