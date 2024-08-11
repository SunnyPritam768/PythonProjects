import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

status = response.status_code
print(status)

data = response.json()
print(data)

position = data["iss_position"]["longitude"]
print(position)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
coordinates = (longitude, latitude)
print(coordinates)