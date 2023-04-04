#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("218b5cf4b1d0c9b7e5ea509aa7a83408")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "37.456257",
    "lon": "126.705208",
    "appid": '218b5cf4b1d0c9b7e5ea509aa7a83408'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('bring your umbrella')
