import streamlit as st
import plotly.express as px
from backend import get_data
import datetime
from os import path



st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, 
    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if place:
    data = get_data(place, forecast_days=days)
    if data:
        st.subheader(f"{option} for the next {days} in {place}")
        dates = [element['date'] for element in data]
        if option == 'Temperature':
            temperatures = [element['temp'] for element in data]
            figure = px.line(x=dates, y=temperatures, 
                labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        elif option == 'Sky':
            sky_conditions = [path.join('img', f'{element["sky"]}.png') 
                for element in data]
            st.image(sky_conditions, width=115, caption=dates)
                #st.text(date)
    else:
        st.subheader(f'{place} is not a valid city name. Try again.')