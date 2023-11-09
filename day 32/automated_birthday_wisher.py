import smtplib
import random
import datetime as dt
import pandas as pd

#Setting email connection
my_email = "email@mail.com"
password = "password123"

#Checking for birthdays

data = pd.read_csv("day 32/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.items()}

#Checking today
today = (dt.datetime.now().month, dt.datetime.now().day)

if today in birthdays_dict:
    file_path = f"day 32/letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], 
                            msg=f"Subject: Happy Birthday!\n\n{contents}")

