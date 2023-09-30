import streamlit as st
import requests

st.set_page_config(page_title="Katie's Weather App")
st.header("Enter your location to begin!")

def home_page():
  city = st.text_input("City")
  temp = getWeather(city)
  if temp > 74:
    sunny_and_hot()
  elif temp > 65:
    sunny_and_warm()

def getWeather(city):
  api_key = 'eee3e1e17b0471238be18e8f6cfbfee6'
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    tempK = data['main']['temp']
    desc = data['weather'][0]['description']
    temp = ((tempK - 273.15) * 1.8) + 32
    st.write("Tempurature: ", temp)
    st.write("Weather: ", desc)
  else:
    st.write("Error fetching weather data.")

  return temp

def sunny_and_hot():
  st.write("It's sunny and hot!")
  st.write("Outfit: t-shirt and shorts")
  st.write("Album: Solar Power")
  st.write("Activity: Go swimming!")

def sunny_and_warm():
  st.write("It's sunny and warm!")
  st.write("Outfit: t-shirt and pants")
  st.write("Album: Harry's House")
  st.write("Activity: Go for a walk")


home_page()
