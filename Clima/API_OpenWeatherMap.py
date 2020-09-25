import requests
from pprint import pprint


class City_weather:
    def __init__(self, latitude, longitude, timestamp):
        self.lat = latitude
        self.lon = longitude
        self.dt = timestamp

    def Weather_City(self):
        dict_weather = {}
        url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

        querystring = {"lat": self.lat, "lon": self.lon, "dt": self.dt}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "c9a626ea64msh6698ab14d44886ap1f605bjsn85a708b80b0f"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()
        return data

    def Hourly_Temperature(self):
        call = City_weather.Weather_City(self)
        Hourly = call['hourly']
        i = 0
        list_Temperature = []
        list_Humidity = []
        list_WindSpeed = []
        list_Pressure = []
        while i < len(Hourly):
            list_Temperature.append(Hourly[i]['temp'])
            i = i + 1
        pprint(list_Temperature)

# Florianopolis = City_weather(-27, -48, 1600898984)
# Florianopolis.Hourly_Temperature()
    # hour_temperature = 0
    # hour_humidity = 0
    # hour_windspeed = 0
    # hour_pressure = 0
    # while i < len(Hourly):
    #     hour_temperature = hour_temperature + Hourly[i]['temp']
    #     hour_humidity = hour_humidity + Hourly[i]['humidity']
    #     hour_pressure = hour_pressure + Hourly[i]['pressure']
    #     hour_windspeed = hour_windspeed + Hourly[i]['wind_speed']
    #
    #     i = i + 1
    # print('The count of temperature measurements was {}'.format(i))
    # print('the average temperature in the last {} hours is: {}'.format(i, hour_temperature/24))
    # print('##########################################')
    # print('The count of humidity measurements was {}'.format(i))
    # print('the average humidity in the last {} hours is: {}'.format(i, hour_humidity / 24))
    # print('##########################################')
    # print('The count of pressure measurements was {}'.format(i))
    # print('the average pressure in the last {} hours is: {}'.format(i, hour_pressure / 24))
    # print('##########################################')
    # print('The count of windspeed measurements was {}'.format(i))
    # print('the average windspeed in the last {} hours is: {}'.format(i, hour_windspeed / 24))
    # print('##########################################')
