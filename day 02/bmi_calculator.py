# Write a program that calculates the BMI of a user

height = input("Enter your height in m:")
weight = input("Enter your weight in kg:")

h = float(height)
w = int(weight)

bmi = round(w/h**2)

print(bmi)