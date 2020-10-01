import requests
from pprint import pprint
from matplotlib import pyplot
import datetime


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

    def Hourly_features(self):
        Call = self.Weather_City()
        Dict_Temperature = {}
        i = 0
        for key in Call:
            pprint(Call[key])


Florianopolis = City_weather(-27.5969, -48.5495, 1601089372)
Florianopolis.Hourly_features()