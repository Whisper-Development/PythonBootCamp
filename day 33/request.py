import requests
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")

#print(response) #This will print our response Code (HTML Codes)

response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (latitude, longitude)

print(iss_position)

parameters = {
    "lat": 44.851110, 
    "lng": 11.549920,
    "formatted": 0
}

sunrise_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

sunrise_response.raise_for_status()
data_sunrise = sunrise_response.json()

sunrise = data_sunrise["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_sunrise["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()

print(time_now.hour)





