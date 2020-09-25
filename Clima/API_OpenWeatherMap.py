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

    def Hourly_Features(self):
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
            Dict_Temperature['{}ª measured temperature {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['temp']
            Dict_Humidity['{}ª measured humidity {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['humidity']
            Dict_WindSpeed['{}ª measured wind speed {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['wind_speed']
            Dict_Pressure['{}ª measured pressure {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['pressure']
            i = i + 1
            n = n + 1
        Weather_Features.append(Dict_Temperature, Dict_Humidity, Dict_WindSpeed, Dict_Pressure)
        print(Weather_Features)
        return Weather_Features

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

    def Max(self):
        call = City_weather.Weather_City(self)
        Hourly = call['hourly']
        Dict_Temperature = {}
        Dict_Humidity = {}
        Dict_WindSpeed = {}
        Dict_Pressure = {}
        i = 0
        n = 0
        while i < len(Hourly):
            Dict_Temperature['{}ª measured temperature {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['temp']
            Dict_Humidity['{}ª measured humidity {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['humidity']
            Dict_WindSpeed['{}ª measured wind speed {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['wind_speed']
            Dict_Pressure['{}ª measured pressure {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['pressure']
            i = i + 1
            n = n + 1
        Max_Temperature = Dict_Temperature[max(Dict_Temperature, key=Dict_Temperature.get)]
        Max_Humidity = Dict_Humidity[max(Dict_Humidity, key=Dict_Humidity.get)]
        Max_WindSpeed = Dict_WindSpeed[max(Dict_WindSpeed, key=Dict_WindSpeed.get)]
        Max_Pressure = Dict_Pressure[max(Dict_Pressure, key=Dict_Pressure.get)]

        Max_Temperature_dt = max(Dict_Temperature, key=Dict_Temperature.get)
        Max_Humidity_dt = max(Dict_Humidity, key=Dict_Humidity.get)
        Max_WindSpeed_dt = max(Dict_WindSpeed, key=Dict_WindSpeed.get)
        Max_Pressure_dt = max(Dict_Pressure, key=Dict_Pressure.get)

        print('The maximum temperature was measured at {} with the value of {}'.format(Max_Temperature_dt, Max_Temperature))
        print('The maximum Humidity was measured at {} with the value of {}'.format(Max_Humidity_dt, Max_Humidity))
        print('The maximum WindSpeed was measured at {} with the value of {}'.format(Max_WindSpeed_dt, Max_WindSpeed))
        print('The maximum Pressure was measured at {} with the value of {}'.format(Max_Pressure_dt, Max_Pressure))

    def Min(self):
        call = City_weather.Weather_City(self)
        Hourly = call['hourly']
        Dict_Temperature = {}
        Dict_Humidity = {}
        Dict_WindSpeed = {}
        Dict_Pressure = {}
        i = 0
        n = 0
        while i < len(Hourly):
            Dict_Temperature['{}ª measured temperature {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['temp']
            Dict_Humidity['{}ª measured humidity {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['humidity']
            Dict_WindSpeed['{}ª measured wind speed {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['wind_speed']
            Dict_Pressure['{}ª measured pressure {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['pressure']
            i = i + 1
            n = n + 1
        Min_Temperature = Dict_Temperature[min(Dict_Temperature, key=Dict_Temperature.get)]
        Min_Humidity = Dict_Humidity[min(Dict_Humidity, key=Dict_Humidity.get)]
        Min_WindSpeed = Dict_WindSpeed[min(Dict_WindSpeed, key=Dict_WindSpeed.get)]
        Min_Pressure = Dict_Pressure[min(Dict_Pressure, key=Dict_Pressure.get)]

        Min_Temperature_dt = min(Dict_Temperature, key=Dict_Temperature.get)
        Min_Humidity_dt = min(Dict_Humidity, key=Dict_Humidity.get)
        Min_WindSpeed_dt = min(Dict_WindSpeed, key=Dict_WindSpeed.get)
        Min_Pressure_dt = min(Dict_Pressure, key=Dict_Pressure.get)

        print('The minimum temperature was measured at {} with the value of {}'.format(Min_Temperature_dt, Min_Temperature))
        print('The minimum Humidity was measured at {} with the value of {}'.format(Min_Humidity_dt, Min_Humidity))
        print('The minimum WindSpeed was measured at {} with the value of {}'.format(Min_WindSpeed_dt, Min_WindSpeed))
        print('The minimum Pressure was measured at {} with the value of {}'.format(Min_Pressure_dt, Min_WindSpeed))


Florianopolis = City_weather(-27, -48, 1600898984)
Florianopolis.Max()
Florianopolis.Min()
