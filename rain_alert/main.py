import requests

OWH_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "678a48e8761ea1e358eed541ecc2e716"

weather_params = {
    'lat': 25.032969,
    'lon': 121.565414,
    'appid': api_key
}

response = requests.get(OWH_Endpoint, params=weather_params)
print(response.json())