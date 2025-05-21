import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "rojen123"
TOKEN = "qwertyuiop"

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
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

headers ={
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, headers=headers, json=graph_params)
print(response.text)