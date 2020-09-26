import requests
from pprint import pprint
from matplotlib import pyplot


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
        if feature.lower() == 'temperature':
            Call = self.Hourly_features('temperature')
            print('The maximum Temperature was measured at {} with the value of {}'.format(Call[max(Call, key=Call.get)], max(Call, key=Call.get)))
        elif feature.lower() == 'humidity':
            Call = self.Hourly_features('humidity')
            print('The maximum humidity was measured at {} with the value of {}'.format(Call[max(Call, key=Call.get)], max(Call, key=Call.get)))
        elif feature.lower() == 'windspeed':
            Call = self.Hourly_features('windspeed')
            print('The maximum windspeed was measured at {} with the value of {}'.format(Call[max(Call, key=Call.get)], max(Call, key=Call.get)))
        elif feature.lower() == 'pressure':
            Call = self.Hourly_features('pressure')
            print('The maximum pressure was measured at {} with the value of {}'.format(Call[max(Call, key=Call.get)], max(Call, key=Call.get)))
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Min(self, feature):
        if feature.lower() == 'temperature':
            Call = self.Hourly_features('temperature')
            print(
                'The minimum Temperature was measured at {} with the value of {}'.format(Call[min(Call, key=Call.get)],
                                                                                         min(Call, key=Call.get)))
        elif feature.lower() == 'humidity':
            Call = self.Hourly_features('humidity')
            print('The minimum humidity was measured at {} with the value of {}'.format(Call[min(Call, key=Call.get)],
                                                                                        min(Call, key=Call.get)))
        elif feature.lower() == 'windspeed':
            Call = self.Hourly_features('windspeed')
            print('The minimum windspeed was measured at {} with the value of {}'.format(Call[min(Call, key=Call.get)],
                                                                                         min(Call, key=Call.get)))
        elif feature.lower() == 'pressure':
            Call = self.Hourly_features('pressure')
            print('The minimum pressure was measured at {} with the value of {}'.format(Call[min(Call, key=Call.get)],
                                                                                        min(Call, key=Call.get)))
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Graphics(self, feature):
        pyplot.style.use('ggplot')
        Call = self.Weather_City()
        Hourly = Call['hourly']
        List_Temperature = []
        List_Humidity = []
        List_WindSpeed = []
        List_Pressure = []
        List_Datetime = []
        for n in range(24):
            List_Datetime.append(Hourly[n]['dt'])
        i = 0
        if feature.lower() == 'temperature':
            while i < len(Hourly):
                List_Temperature.append(Hourly[i]['temp'])
                i += 1
            pyplot.plot(List_Datetime, List_Temperature, color='r', marker='o', linewidth=3, label='Temperature history in one day')
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Temperatura in Kelvin')
            pyplot.title('Graphic of the temperature')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        elif feature.lower() == 'humidity':
            while i < len(Hourly):
                List_Humidity.append(Hourly[i]['humidity'])
                i += 1
            pyplot.plot(List_Datetime, List_Humidity, color='b', marker='o', linewidth=3, label='Humidity history in one day')
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Humidity in porcent')
            pyplot.title('Graphic of the humidity')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        elif feature.lower() == 'windspeed':
            while i < len(Hourly):
                List_WindSpeed.append(Hourly[i]['windspeed'])
                i += 1
            pyplot.plot(List_Datetime, List_WindSpeed, color='y', marker='o', linewidth=3, label='Windspeed history in one day')
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Windspeed in Km/h')
            pyplot.title('Graphic of the Windspeed')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        elif feature.lower() == 'pressure':
            while i < len(Hourly):
                List_Pressure.append(Hourly[i]['pressure'])
                i += 1
            pyplot.plot(List_Datetime, List_Pressure, color='k', marker='o', linewidth=3, label='Pressure history in one day')
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Pressure in Km/h')
            pyplot.title('Graphic of the Pressure')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')




florianópolis = City_weather(-27, -48, 1600898984)
florianópolis.Graphics()
