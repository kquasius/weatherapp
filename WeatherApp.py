import streamlit as st
import requests

st.set_page_config(page_title="Katie's Weather App")
st.header("Enter your location to begin!")

def home_page():
  st.write("The current weather for Chicago, IL is:")
  getWeather()

def getWeather():
  API_KEY = 'eee3e1e17b0471238be18e8f6cfbfee6'
  lat = 41.881832
  lon = -87.623177
  url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_KEY}'
  response = requests.get(url)
  weather = response.json()
  st.write(weather)


home_page()
