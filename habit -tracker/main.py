import requests
from datetime import datetime

USERNAME = "toastding"
TOKEN = "gopadsadgre"
GRAPH_ID = "graph1"

pixel_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Jump Rope Graph",
    "unit": "jump",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=7, day=21)

pixel_data = {
   "date": today.strftime("%Y%m%d"),
   "quantity": "300"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)