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
    return data


def Hourly_Temperature():
    call = Weather_City()
    Hourly = call['hourly']
    i = 0
    hour_temperature = 0
    hour_humidity = 0
    hour_windspeed = 0
    hour_pressure = 0
    while i < len(Hourly):
        hour_temperature = hour_temperature + Hourly[i]['temp']
        hour_humidity = hour_humidity + Hourly[i]['humidity']
        hour_pressure = hour_pressure + Hourly[i]['pressure']
        hour_windspeed = hour_windspeed + Hourly[i]['wind_speed']

        i = i + 1
    print('The count of temperature measurements was {}'.format(i))
    print('the average temperature in the last {} hours is: {}'.format(i, hour_temperature/24))
    print('##########################################')
    print('The count of humidity measurements was {}'.format(i))
    print('the average humidity in the last {} hours is: {}'.format(i, hour_humidity / 24))
    print('##########################################')
    print('The count of pressure measurements was {}'.format(i))
    print('the average pressure in the last {} hours is: {}'.format(i, hour_pressure / 24))
    print('##########################################')
    print('The count of windspeed measurements was {}'.format(i))
    print('the average windspeed in the last {} hours is: {}'.format(i, hour_windspeed / 24))
    print('##########################################')


# current_temperature = data['current']['temp']
# current_humidity = data['current']['humidity']
# current_uvi = data['current']['uvi']
# current_weather = data['current']['wind_speed']
# dict_weather['current_temperature'] = current_temperature
# dict_weather['current_humidity'] = current_humidity
# dict_weather['current_uvi'] = current_uvi
# dict_weather['current_weather'] = current_weather
# print(dict_weather)


Hourly_Temperature()

