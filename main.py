import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, 
    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")


def get_data(days):
    dates = [f'2023-02-{str(x).zfill(2)}' for x in range(7,10,1)]
    temperatures = [10,11,15]
    return dates, temperatures

dates, temperatures = get_data(days=days)
figure = px.line(x=dates, y=temperatures, 
    labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)