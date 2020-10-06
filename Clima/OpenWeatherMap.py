import requests
from pprint import pprint
from matplotlib import pyplot
import datetime
from geopy.geocoders import Nominatim


class City_weather:
    def __init__(self, city, timestamp):
        self.address = city
        self.dt = timestamp

    def Get_coordinates(self):
        Address = self.address
        Geolocator = Nominatim(user_agent="Lucas")
        Location = Geolocator.geocode(Address)
        Coordinates = []
        Latitude = Location.latitude
        Longitude = Location.longitude
        Coordinates.append(Latitude)
        Coordinates.append(Longitude)
        return Coordinates

    def Weather_City(self):
        Call = self.Get_coordinates()
        dict_weather = {}
        url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

        querystring = {"lat": Call[0], "lon": Call[1], "dt": self.dt}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "c9a626ea64msh6698ab14d44886ap1f605bjsn85a708b80b0f"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()
        print(response.status_code)
        return data

    def Epoch_to_Datetime(self, epoch):
        if epoch == 'list':
            Call = self.Weather_City()
            Hourly = Call['hourly']
            List_Datetime = []
            for i in range(len(Hourly)):
                List_Datetime.append(datetime.datetime.fromtimestamp(Hourly[i]['dt']).strftime('%Y-%m-%d %H:%M:%S'))
            return List_Datetime
        else:
            return datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

    def Current_features(self, feature):
        Call = self.Weather_City()
        Current = Call['current']
        if feature.lower().strip() == 'temperature':
            pprint(Current['temp'])
            return Current['temp']
        elif feature.lower().strip() == 'humidity':
            pprint(Current['humidity'])
            return Current['humidity']
        elif feature.lower().strip() == 'windspeed':
            pprint(Current['wind_speed'])
            return Current['wind_speed']
        elif feature.lower().strip() == 'pressure':
            pprint(Current['pressure'])
            return Current['pressure']
        elif feature.lower().strip() == 'icon':
            pprint(Current['icon'])
            return Current['icon']

    def Hourly_features(self, feature):
        Call = self.Weather_City()
        Hourly = Call['hourly']
        Dict_Temperature = {}
        Dict_Humidity = {}
        Dict_WindSpeed = {}
        Dict_Pressure = {}
        i = 0
        n = 0
        if feature.lower().strip() == 'temperature':
            while i < len(Hourly):
                Dict_Temperature[self.Epoch_to_Datetime(Hourly[i]['dt'])] = Hourly[i]['temp']
                i += 1
                n += 1
            return Dict_Temperature
        elif feature.lower().strip() == 'humidity':
            while i < len(Hourly):
                Dict_Humidity[self.Epoch_to_Datetime(Hourly[i]['dt'])] = Hourly[i]['humidity']
                i += 1
                n += 1
            return Dict_Humidity
        elif feature.lower().strip() == 'windspeed':
            while i < len(Hourly):
                Dict_WindSpeed[self.Epoch_to_Datetime(Hourly[i]['dt'])] = Hourly[i]['wind_speed']
                i += 1
                n += 1
            return Dict_WindSpeed
        elif feature.lower().strip() == 'pressure':
            while i < len(Hourly):
                Dict_Pressure[self.Epoch_to_Datetime(Hourly[i]['dt'])] = Hourly[i]['pressure']
                i += 1
                n += 1
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
        if feature.lower().strip() == 'temperature':
            while i < len(Hourly):
                Hour_Temperature = Hour_Temperature + Hourly[i]['temp']
                i += 1
            print('The count of temperature measurements was {}'.format(i))
            print('the average temperature in the last {} hours is: {}'.format(i, Hour_Temperature / 24))
            return Hour_Temperature
        elif feature.lower().strip() == 'humidity':
            while i < len(Hourly):
                Hour_Humidity = Hour_Humidity + Hourly[i]['humidity']
                i += 1
            print('The count of humidity measurements was {}'.format(i))
            print('the average humidity in the last {} hours is: {}'.format(i, Hour_Humidity / 24))
            return Hour_Humidity
        elif feature.lower().strip() == 'windspeed':
            while i < len(Hourly):
                Hour_WindSpeed = Hour_WindSpeed + Hourly[i]['wind_speed']
                i += 1
            print('The count of windspeed measurements was {}'.format(i))
            print('the average windspeed in the last {} hours is: {}'.format(i, Hour_WindSpeed / 24))
            return Hour_WindSpeed
        elif feature.lower().strip() == 'pressure':
            while i < len(Hourly):
                Hour_Pressure = Hour_Pressure + Hourly[i]['pressure']
                i += 1
            print('The count of pressure measurements was {}'.format(i))
            print('the average pressure in the last {} hours is: {}'.format(i, Hour_Pressure / 24))
            return Hour_Pressure
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Max(self, feature):
        if feature.lower().strip() == 'temperature':
            Call = self.Hourly_features('temperature')
            print('The maximum Temperature was measured at {} with the value of {}'.format(max(Call, key=Call.get), Call[max(Call, key=Call.get)]))
        elif feature.lower().strip() == 'humidity':
            Call = self.Hourly_features('humidity')
            print('The maximum humidity was measured at {} with the value of {}'.format(max(Call, key=Call.get), Call[max(Call, key=Call.get)]))
        elif feature.lower().strip() == 'windspeed':
            Call = self.Hourly_features('windspeed')
            print('The maximum windspeed was measured at {} with the value of {}'.format(max(Call, key=Call.get), Call[max(Call, key=Call.get)]))
        elif feature.lower().strip() == 'pressure':
            Call = self.Hourly_features('pressure')
            print('The maximum pressure was measured at {} with the value of {}'.format(max(Call, key=Call.get), Call[max(Call, key=Call.get)]))
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Min(self, feature):
        if feature.lower().strip() == 'temperature':
            Call = self.Hourly_features('temperature')
            print(
                'The minimum Temperature was measured at {} with the value of {}'.format(min(Call, key=Call.get),
                                                                                         Call[min(Call, key=Call.get)]))
        elif feature.lower().strip() == 'humidity':
            Call = self.Hourly_features('humidity')
            print('The minimum humidity was measured at {} with the value of {}'.format(min(Call, key=Call.get),
                                                                                         Call[min(Call, key=Call.get)]))
        elif feature.lower().strip() == 'windspeed':
            Call = self.Hourly_features('windspeed')
            print('The minimum windspeed was measured at {} with the value of {}'.format(min(Call, key=Call.get),
                                                                                         Call[min(Call, key=Call.get)]))
        elif feature.lower().strip() == 'pressure':
            Call = self.Hourly_features('pressure')
            print('The minimum pressure was measured at {} with the value of {}'.format(min(Call, key=Call.get),
                                                                                         Call[min(Call, key=Call.get)]))
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')

    def Graphics(self, feature):
        pyplot.style.use('ggplot')
        Axis = pyplot.gca()
        Call = self.Weather_City()
        Hourly = Call['hourly']
        List_Temperature = []
        List_Humidity = []
        List_WindSpeed = []
        List_Pressure = []
        List_Datetime = self.Epoch_to_Datetime('list')
        i = 0
        if feature.lower().strip() == 'temperature':
            while i < len(Hourly):
                List_Temperature.append(Hourly[i]['temp'])
                i += 1
            pyplot.plot(List_Datetime, List_Temperature, color='r', marker='o', linewidth=3, label='Time-line temperature in one day')
            pyplot.xticks(rotation=70)
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Temperature in Kelvin')
            Axis.set_ylim([280, 300])
            pyplot.title('Graphic of the temperature')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        elif feature.lower().strip() == 'humidity':
            while i < len(Hourly):
                List_Humidity.append(Hourly[i]['humidity'])
                i += 1
            pyplot.plot(List_Datetime, List_Humidity, color='b', marker='o', linewidth=3, label='Time-line humidity in one day')
            pyplot.xticks(rotation=70)
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Humidity in %')
            Axis.set_ylim([0, 200])
            pyplot.title('Graphic of the humidity')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        elif feature.lower().strip() == 'windspeed':
            while i < len(Hourly):
                List_WindSpeed.append(Hourly[i]['wind_speed'])
                i += 1
            pyplot.plot(List_Datetime, List_WindSpeed, color='y', marker='o', linewidth=3, label='Time-line windspeed in one day')
            pyplot.xticks(rotation=70)
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Windspeed in Km/h')
            Axis.set_ylim([0, 10])
            pyplot.title('Graphic of the Windspeed')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        elif feature.lower().strip() == 'pressure':
            while i < len(Hourly):
                List_Pressure.append(Hourly[i]['pressure'])
                i += 1
            pyplot.plot(List_Datetime, List_Pressure, color='k', marker='o', linewidth=3, label='Time-line pressure in one day')
            pyplot.xticks(rotation=70)
            pyplot.xlabel('Datetime')
            pyplot.ylabel('Pressure in hPa')
            Axis.set_ylim([1000, 1040])
            pyplot.title('Graphic of the Pressure')
            pyplot.grid(True)
            pyplot.legend()
            pyplot.show()
        else:
            print('The feature have to be one of these: temperature, humidity, windspeed, pressure ')


florianópolis = City_weather('vvrvrvv', 1601653089)
florianópolis.Get_coordinates()

