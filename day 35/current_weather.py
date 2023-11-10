import requests

parameters = {
    "q": "Ferrara",
    "appid": "08467dcd42ecbdc1ff7922a235161ebf",
    "lang" : "it"
}

response = requests.get(url="https://pro.openweathermap.org/data/2.5/forecast/hourly", params=parameters)

data = response.json()

print(data)

