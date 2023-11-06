import csv
import pandas as pd 

#with open("day 25/weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))

data = pd.read_csv("day 25/weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = data["temp"].mean()
print(avg_temp)

max_temp = data["temp"].max()
print(max_temp)

#We can also call the column like this
print(data.condition)

#Get data from the rows

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])