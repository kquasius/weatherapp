import streamlit as st
import requests

st.set_page_config(page_title="Katie's Weather App")
st.header("Enter your location to begin!")

def home_page():
  st.write("The current weather for Chicago, IL is:")
  getWeather()

def getWeather():
  api_key = 'eee3e1e17b0471238be18e8f6cfbfee6'
  city = 'Chicago'
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    st.write("Tempurature: ", temp)
    st.write("Weather: ", desc)
  else:
    st.write("Error fetching weather data.")


home_page()
