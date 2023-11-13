import requests
import datetime

TOKEN = "hfduyfi9fuy84734873"
USERNAME = "whisper-dev"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hfduyfi9fuy84734873",
    "username": "whisper-dev",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"   
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.datetime.now()


pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "13.5"
}

#response = requests.post(url=post_pixel_endpoint, headers=headers, json=pixel_params)
#print(response.text)

