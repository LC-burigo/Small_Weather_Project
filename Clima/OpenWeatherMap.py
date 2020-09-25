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

    def Hourly_features(self, feature):
        Call = self.Weather_City()
        Hourly = Call['hourly']
        Dict_Temperature = {}
        Dict_Humidity = {}
        Dict_WindSpeed = {}
        Dict_Pressure = {}
        i = 0
        n = 0
        if feature.lower() == 'temperature':
            while i < len(Hourly):
                Dict_Temperature['{}ª measured temperature {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['temp']
                i += 1
                n += 1
            print(Dict_Temperature)
            return Dict_Temperature
        elif feature.lower() == 'humidity':
            while i < len(Hourly):
                Dict_Humidity['{}ª measured humidity {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['humidity']
                i += 1
                n += 1
            print(Dict_Humidity)
            return Dict_Humidity
        elif feature.lower() == 'windspeed':
            while i < len(Hourly):
                Dict_WindSpeed['{}ª measured windwpeed {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['wind_speed']
                i += 1
                n += 1
            print(Dict_WindSpeed)
            return Dict_WindSpeed
        elif feature.lower() == 'Pressure':
            while i < len(Hourly):
                Dict_Pressure['{}ª measured pressure {}'.format(n, Hourly[i]['dt'])] = Hourly[i]['pressure']
                i += 1
                n += 1
            print(Dict_Pressure)
            return Dict_Pressure
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Average(self, feature):
        Call = self.Weather_City()
        Hourly = Call['hourly']
        Hour_Temperature = 0
        Hour_Humidity = 0
        Hour_WindSpeed = 0
        Hour_Pressure = 0
        i = 0
        if feature.lower() == 'temperature':
            while i < len(Hourly):
                Hour_Temperature = Hour_Temperature + Hourly[i]['temp']
                i += 1
            print('The count of temperature measurements was {}'.format(i))
            print('the average temperature in the last {} hours is: {}'.format(i, Hour_Temperature / 24))
        elif feature.lower() == 'humidity':
            while i < len(Hourly):
                Hour_Humidity = Hour_Humidity + Hourly[i]['humidity']
                i += 1
            print('The count of humidity measurements was {}'.format(i))
            print('the average humidity in the last {} hours is: {}'.format(i, Hour_Humidity / 24))
        elif feature.lower() == 'windspeed':
            while i < len(Hourly):
                Hour_WindSpeed = Hour_WindSpeed + Hourly[i]['wind_speed']
                i += 1
            print('The count of windspeed measurements was {}'.format(i))
            print('the average windspeed in the last {} hours is: {}'.format(i, Hour_WindSpeed / 24))
        elif feature.lower() == 'pressure':
            while i < len(Hourly):
                Hour_Pressure = Hour_Pressure + Hourly[i]['pressure']
                i += 1
            print('The count of pressure measurements was {}'.format(i))
            print('the average pressure in the last {} hours is: {}'.format(i, Hour_Pressure / 24))
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Max(self, feature):
        Call = City_weather.Weather_City(self)
        Hourly = Call['hourly']
        if feature.lower() == 'temperatura':
