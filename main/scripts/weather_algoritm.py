import requests
from .what_is_my_ip import *
import datetime
import json

data = get_info_by_ip()

APPID = "ed0b3cbd92b3210cf1e0e8a37ebfc4c0" 
URL_BASE = "https://api.openweathermap.org/data/2.5/"


def current_weather(q: str = "Chicago", appid: str = APPID, units: str = "metric") -> dict:
    """https://openweathermap.org/api"""
    return requests.get(URL_BASE + "weather", params=locals()).json()

def current_weather_response():
    location = data.get('City')
    return current_weather(location)


def weather_forecast(q: str = "Kolkata, India", appid: str = APPID, units: str = "metric") -> dict:
    """https://openweathermap.org/forecast5"""
    return requests.get(URL_BASE + "forecast", params=locals()).json()

def filter_weather_forecast(location):
    forecast = weather_forecast(location)

    forecast_for_5days = {
        "cod": forecast["cod"],
        "message": forecast["message"],
        "cnt": forecast["cnt"],
    }

    list = forecast.get('list')
    list_for_5days = []

    for i in range(len(list)):
        dateunix = list[i].get('dt')
        datenormal = str(datetime.datetime.fromtimestamp(dateunix))
        list[i]['dt'] = datenormal

    for j in range(len(list)):
        if list[j]['dt'][11:13] == '16' or list[j]['dt'][11:13] == '04':
            if list[j]['dt'] not in list_for_5days:
                list_for_5days.append(list[j])

    forecast_for_5days["list"] = list_for_5days

    return forecast_for_5days

def weather_forecast_in_my_location(location):
    dates = []
    temps = []
    weathers = []
    info = filter_weather_forecast(location).get('list')
    for el in info:
        dates.append(el.get('dt')) 
        temps.append(el.get('main').get('temp'))
        weathers.append(el.get('weather')[0].get('main'))
    return dates, temps, weathers
    
with open('forecast.json', 'w') as file:
    file.write(json.dumps(filter_weather_forecast(data.get('City')), indent=4))

# def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID, units: str = "metric") -> dict:
#     """https://openweathermap.org/api/one-call-api"""
#     return requests.get(URL_BASE + "onecall", params=locals()).json()

# if __name__ == "__main__":
#     from pprint import pprint
#     location = data.get('City')
#     if location:
#         pprint(current_weather(location))
#     else:
#         print('Something went wrong...')
