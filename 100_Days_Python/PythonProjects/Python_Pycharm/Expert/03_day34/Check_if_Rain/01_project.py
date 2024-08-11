import requests

own_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "758f3139e5cfbe2a36d815027c2c915a"

Latitude = 21.170240
Longitude = 72.831062

weather_parameters = {
    "lat": Latitude,
    "lon": Longitude,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(own_endpoint, params=weather_parameters)
print(response.status_code)
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])


