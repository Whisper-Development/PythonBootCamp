# A program that can calculate the tip for the restaurant
print("Welcome to the Tip Calculator!")

bill = input("How much is the bill?\n")
people = input("How many people are sharing?\n")

b = float(bill)
p = int(people)

cost = round((b/p)*1.12, 2)

print(cost)