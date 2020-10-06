import requests
q = 'frvrv'

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q": q}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "6446924734mshd20c29c9014fd63p155d13jsnc1cdd0345c05"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response)