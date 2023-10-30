# Who is gonna pay the bill?
import random

names_string = input("Give me everybody's names, separated by a comma.\n")

names = names_string.split(", ")

x = len(names)

pay = random.randint(0, x)

print(f"{names[pay]} is going to pay today!")
