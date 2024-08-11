import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_parameter = {
    "token": "hmzmdcgh6732bjmds",
    "username": "sunny234",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_parameter)
print(response.text)

