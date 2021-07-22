import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 167.64
AGE = 26

APP_ID = "fd7f3442"
API_KEY = "52605593bb5d34c75c03ee6067b961d0	"
USERNAME = "jeremy"
PASSWORD = "fjdsklhamsnvmcxzvoihp"

excise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f56d2712818edaf9c2bfdd55b917a663/workoutTracking/page1"

excise_text = input('Tell me which excises you did?: ')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": excise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=excise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "page1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD
        )
    )

    print(sheet_response.text)

