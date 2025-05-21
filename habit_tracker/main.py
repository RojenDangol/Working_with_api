import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "qwertyuiop",
    "username": "rojen123",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)