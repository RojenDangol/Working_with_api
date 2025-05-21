import requests
from datetime import datetime


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

today = datetime(year=2025, month=5, day=20)

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}

# response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_params)
# print(response.text)
