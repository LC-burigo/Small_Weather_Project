import requests
from pprint import pprint


def Weather_City():
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

    pprint(response.text)


Weather_City()
