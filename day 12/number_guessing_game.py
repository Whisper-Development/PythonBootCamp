from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

number=random.randint(1,100)

mode = None

print("I'm thinking of a number between 1 and 100")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

if mode == 'easy':
    attempt = 10
else:
    attempt = 5

while attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    my_number = int(input("Make a guess: "))
    if my_number > number:
        print("Too high.\nGuess again.")
        attempt -= 1
    elif my_number < number:
        print("Too low.\nGuess again")
        attempt -= 1
    elif my_number == number:
        print("You won!")
        attempt = 0