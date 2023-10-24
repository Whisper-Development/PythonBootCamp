# This program will tell you using maths and f-strings how many days,
# weeks and months you have left to live

age = input("What is your current age?")

year = int(age)

left = 90- year

days = left*365
months = left*12
weeks = left*52

print(f"You have {days} days, {weeks} weeks and {months} months left to live!")