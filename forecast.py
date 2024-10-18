#Example url
#http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid=8078993c7d41a6f6dba2bdaa7eeb3a75

import os
from pprint import pprint
import requests
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
#pprint(data)

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date}, the temperature will be {temp}F.')




