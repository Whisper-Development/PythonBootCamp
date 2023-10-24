# This program can tell you if a number is an odd or even number

number = int(input("Which number do you want to check?"))

rem = number % 2

if rem == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")