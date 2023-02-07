import requests
import datetime
import json

# First part: obtain the exercise data

exercise_input = input("Tell me which exercises you did: ")

params = {
    "query": exercise_input,
}


headers = {
    "x-app-id" : '',
    "x-app-key": "",
    "x-remote-user-id": "0",
}

response = requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise", json = params, headers = headers)

exercise_response = response.json()

now = datetime.datetime.now()
time = now.strftime("%H:%M")
date = now.strftime("%d/%m/%Y")

for exercise in exercise_response['exercises']:
    exercise_type = exercise['user_input']
    duration = exercise['duration_min']
    calories = exercise["nf_calories"]

    data = {
        "workout": {
                "date": date,
                "time": time,
                "exercise": exercise_type,
                "duration": duration,
                "calories": calories,
        }
    }

    response = requests.post(url = "", json = data)

