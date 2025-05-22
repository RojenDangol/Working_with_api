import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ['ENV_NIX_APP_ID']
APP_API_KEY = os.environ['ENV_NIX_API_KEY']

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 174
AGE = 23

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINTS = os.environ['SHEETY_ENDPOINT']

exercise_input = input('Tell me which exercise you did: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_API_KEY,
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(API_ENDPOINT, headers=headers, json=parameters)
response.raise_for_status()
data = response.json()
print(data['exercises'])

GOOGLE_SHEET_NAME = "workout"
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

# print(today_date, today_time)

for exercise in data['exercises']:
    sheet_param = {
        GOOGLE_SHEET_NAME: {
            'date': today_date,
            'time': today_time,
            'exercise': exercise["name"].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    sheety_response = requests.post(SHEETY_ENDPOINTS, json=sheet_param, auth=(
        os.environ['ENV_SHEETY_USERNAME'],
        os.environ['ENV_SHEETY_PASSWORD']
    ))

    print(sheety_response.text)
