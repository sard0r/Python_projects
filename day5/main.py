import requests

GENDER = "MALE"
WEIGHT_KG = "79"
HEIGHT = "179" #entered random height in cm
AGE = "26"

APP_ID = "db0e1aca"
API_KEY = "949beff3d56633b2f0c2ae90fb1f783f"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)

from datetime import datetime

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/4526d01b0794b3df8b6e4cac1b5e0c4f/copyOfMyWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs,
                                   auth=(
                                    "sardor97",
                                    "5822613Sj$"
                                   ))

    print(sheet_response.text)