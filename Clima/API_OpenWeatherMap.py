import requests
from pprint import pprint


def Weather_City():
    dict_weather = {}
    latitude = input('Enter the latitude:')
    longitude = input('Enter the longitude:')
    dt = input('Enter the dt:')
    url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

    querystring = {"lat": latitude, "lon": longitude, "dt": dt}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "c9a626ea64msh6698ab14d44886ap1f605bjsn85a708b80b0f"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    hourly = data['hourly']
    i = 0
    hour_temperature = 0
    while i < len(hourly):
        hour_temperature = hour_temperature + hourly[i]['temp']
        i = i + 1
    print(hour_temperature/24)
# current_temperature = data['current']['temp']
# current_humidity = data['current']['humidity']
# current_uvi = data['current']['uvi']
# current_weather = data['current']['wind_speed']
# dict_weather['current_temperature'] = current_temperature
# dict_weather['current_humidity'] = current_humidity
# dict_weather['current_uvi'] = current_uvi
# dict_weather['current_weather'] = current_weather
# print(dict_weather)


Weather_City()
