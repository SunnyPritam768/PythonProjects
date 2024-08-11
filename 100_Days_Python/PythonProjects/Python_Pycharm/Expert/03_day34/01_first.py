# Use of an api key
import requests

own_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "758f3139e5cfbe2a36d815027c2c915a"

My_latitude = 28.984463
My_longitude = 77.706413

parameters = {
    "lat": My_latitude,
    "lon": My_longitude,
    "appid": api_key,
}
response = requests.get(own_endpoint, params=parameters)
print(response.status_code)
json_data = response.json()
# print(json_data)


