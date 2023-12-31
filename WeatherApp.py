import streamlit as st
import requests

st.set_page_config(page_title="Katie's Weather App")
st.header("Enter your location to begin!")

cities = ['Chicago', 'Madison', 'Milwaukee', 'San Francisco', 'New York City', 'Sheboygan', 'Denver']

def home_page():
  city = st.text_input("City")
  submit = st.button("Submit")
  if submit:
    if city in cities:
      temp = getWeather(city)
      if temp != None:
        st.header("Vibe for the day:")
        if temp > 74:
          sunny_and_hot()
        elif temp > 65:
          sunny_and_warm()
    else:
      st.write("Invalid city")

def getWeather(city):
  api_key = 'eee3e1e17b0471238be18e8f6cfbfee6'
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    tempK = data['main']['temp']
    desc = data['weather'][0]['description']
    temp = ((tempK - 273.15) * 1.8) + 32
    st.write("Tempurature: ", int(temp))
    st.write("Weather: ", desc)
    return temp
  else:
    st.write("Error fetching weather data.")
    return None

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
