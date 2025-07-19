from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()

today = datetime.datetime.now()

APP_ID = "YOUR_APP_ID"
API_KEY = os.getenv("TOKEN")
BEARER = os.getenv("BEARER")

nutri_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_post_endpoint = "YOUR_SHEETY_ENDPOINT"

query = input("Tell me which exercise you did: ")


headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

body = {
    "query": query
}

response = requests.post(url=nutri_api_endpoint, json=body, headers=headers)
response.raise_for_status()

exercise_json = response.json()

print(exercise_json)

sheety_header = {
    "Authorization": f"Bearer {BEARER}"
}

for exercise in exercise_json["exercises"]:
    running = exercise["name"]
    running_name = running.title()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    workout = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": running_name,
            "duration": duration,
            "calories": calories,
        }
    }

    print("Payload:", workout)  # Para debug

    sheety_response = requests.post(
        sheety_post_endpoint,
        json=workout,
        headers=sheety_header,
    )
    sheety_response.raise_for_status()
    print(sheety_response.text)
