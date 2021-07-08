import requests
from twilio.rest import Client

OWH_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "678a48e8761ea1e358eed541ecc2e716"
account_sid = "ACe1ae4e388a1a7390b292e744d125d13f"
auth_token = "cc19cc9ad842e61bcd100b5429efa52f"


weather_params = {
    'lat': 32.750286,
    'lon': 129.877670,
    'appid': api_key,
    'exclude': "current,minutely,daily"
}

response = requests.get(OWH_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:13]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to 🌧 today. Remember to bring an ☂.",
            from_='+17742284856',
            to='+886978199305'
    )
    print(message.status)
