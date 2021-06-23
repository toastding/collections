import requests
from datetime import datetime

MY_LAT = 25.105497
MY_LNG = 121.597366
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()['iss_position']
# print(data)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)

print(datetime.now().hour)

