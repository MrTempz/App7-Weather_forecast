import requests
import datetime

API_KEY='7a99c35e8da99f9b62610da3cb035490'

def get_data(place, forecast_days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == '200':
        result_data = [{'date':datetime.datetime.fromtimestamp(element['dt']), 
            'temp':element['main']['temp']-273.15, 
            'sky':element['weather'][0]['main']} 
            for element in data['list'][:forecast_days*8]]
        return result_data
    else:
        return None