import smtplib
import datetime as dt
import random

#my_email = "email@mail.com"
#password = "password123"

#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls() #encrypts the message for security
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs="secondmail@mail.com", 
#                        msg="Subject:Hello\n\nThis is the body of my email!")

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day = now.day
#day_of_week = now.weekday()

#date_of_birth = dt.datetime(year=1987, month=5, day=30)
#print(date_of_birth)

#Setting email connection
my_email = "email@mail.com"
password = "password123"

#Checking day of week

thursday = 3
now = dt.datetime.now()
day_of_wheek = now.weekday()

#Makes list of quotes:
with open(file="day 32/quotes.txt") as file:
    quotes = file.readlines()
    random_quote = random.choice(quotes)


if now == day_of_wheek:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="secondmail@mail.com",
                            msg=f"Subject:It's Monday\n\n{random_quote}") 

