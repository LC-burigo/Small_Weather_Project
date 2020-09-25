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
        Weather_Features = []
        Dict_Temperature = {}
        Dict_Humidity = {}
        Dict_WindSpeed = {}
        Dict_Pressure = {}
        i = 0
        n = 0
        while i < len(Hourly):
            Dict_Temperature['{}ª temperatura medida {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['temp']
            Dict_Humidity['{}ª umidade medida {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['humidity']
            Dict_WindSpeed['{}ª umidade medida {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['wind_speed']
            Dict_Pressure['{}ª umidade medida {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['pressure']
            i = i + 1
            n = n + 1
        Weather_Features.append(Dict_Temperature, Dict_Humidity, Dict_WindSpeed, Dict_Pressure)
        print(Weather_Features)
        return Dict_Temperature, Dict_Humidity, Dict_WindSpeed, Dict_Pressure

    def Average(self):
        call = City_weather.Weather_City(self)
        Hourly = call['hourly']
        Hour_Temperature = 0
        Hour_Humidity = 0
        Hour_WindSpeed = 0
        Hour_Pressure = 0
        i = 0
        while i < len(Hourly):
            Hour_Temperature = Hour_Temperature + Hourly[i]['temp']
            Hour_Humidity = Hour_Humidity + Hourly[i]['humidity']
            Hour_WindSpeed = Hour_WindSpeed + Hourly[i]['wind_speed']
            Hour_Pressure = Hour_Pressure + Hourly[i]['pressure']
            i = i + 1

        print('The count of temperature measurements was {}'.format(i))
        print('the average temperature in the last {} hours is: {}'.format(i, Hour_Temperature / 24))
        print('##########################################')
        print('The count of humidity measurements was {}'.format(i))
        print('the average humidity in the last {} hours is: {}'.format(i, Hour_Humidity / 24))
        print('##########################################')
        print('The count of windspeed measurements was {}'.format(i))
        print('the average windspeed in the last {} hours is: {}'.format(i, Hour_WindSpeed / 24))
        print('##########################################')
        print('The count of pressure measurements was {}'.format(i))
        print('the average pressure in the last {} hours is: {}'.format(i, Hour_Pressure / 24))


Florianopolis = City_weather(-27, -48, 1600898984)
Florianopolis.Average()
