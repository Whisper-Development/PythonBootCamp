import requests
import datetime

GENDER = "Your gender"
WEIGHT_KG = "Your weight"
HEIGHT_CM = "Your height"
AGE = "Your age"

NUTRITION_ID = "Your nutrition Id"
NUTRITION_KEY = "Your nutrition Key"

headers = {
    "x-app-id" : NUTRITION_ID,
    "x-app-key" : NUTRITION_KEY
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "Your sheety endpoint"

exercise_input = input("Describe exercises: ")

exercise_params = {
    "query" : exercise_input,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
result = response.json()

today_date = datetime.datetime.now().strftime("%d%m%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs={
        "workout": {
            "date":today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer your token"
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

print(sheet_response.text)


