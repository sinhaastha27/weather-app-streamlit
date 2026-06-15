import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="☁️", layout="centered")

st.title("🌤️ Weather App - Real Time Data")
st.write("Powered by OpenWeatherMap API")

API_KEY = "edd069fd6be3f81a213eb18b2007fe07" 

city = st.text_input("Enter City Name:", placeholder="e.g. Delhi, Mumbai, Ranchi")

if st.button("Get Weather", type="primary"):
    if city.strip() == "":
        st.warning("Please enter a city name")
    else:
        with st.spinner("Fetching weather data..."):
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                description = data['weather'][0]['description'].title()
                icon = data['weather'][0]['icon']
                country = data['sys']['country']

                st.success(f"Weather for {city}, {country}")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Temperature", f"{temp}°C", f"Feels {feels_like}°C")
                with col2:
                    st.metric("Humidity", f"{humidity}%")
                with col3:
                    st.metric("Wind", f"{wind_speed} m/s")

                st.image(f"https://openweathermap.org/img/wn/{icon}@4x.png", width=150)
                st.write(f"**Condition:** {description}")

            else:
                st.error("City not found! Check spelling and try again.")
else:
             st.info("Enter a city name and click 'Get Weather' button")
        