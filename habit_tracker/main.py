import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "rojen123"
TOKEN = "qwertyuiop"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params ={
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

headers ={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_params)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
today_date = today.strftime("%Y%m%d")

pixel_params = {
    "date": today_date,
    "quantity": input("How many kilometers did you run today?"),
}

response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_params)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{today_date}"

update_params = {
    "quantity": "15",
}
# response = requests.put(url=update_endpoint, headers=headers, json=update_params)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)


