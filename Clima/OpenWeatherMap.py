import requests
from pprint import pprint

city = input("Enter your city: ")
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=7904d58d2274ccc17d69331fbd3b9032'.format(city)
response = requests.get(url)
data = response.json()

print('Cidade:', data['name'])
print('Vento:', data['wind']['speed'])
print('Temperatura:', data['main']['temp'])
print('Umidade:', data['main']['humidity'])
print(data)




