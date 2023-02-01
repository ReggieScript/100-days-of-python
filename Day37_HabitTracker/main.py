import requests
import datetime

username = ""
token = ""

#STEP 1: Create USER

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

# STEP 2: Create GRAPH

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Drawings per day",
    "unit": "Drawings",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN" : token,
}

# response = requests.post(url = graph_endpoint, json = graph_params, headers = headers)
# print(response.text)

drawing_graph = "graph1"

#STEP 3: add a PIXEL

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{drawing_graph}"

now = datetime.date.today()
date = now.strftime("%Y%m%d")

pixel_params = {
    "date": date,
    "quantity": "1",
}

response = requests.post(url = pixel_endpoint, json = pixel_params, headers = headers)
print(response.text)