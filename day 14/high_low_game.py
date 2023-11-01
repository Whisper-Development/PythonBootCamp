from art import logo
from art import vs
from game_data import data
import random 

print(logo)

score = 0
wrong = False

while wrong is False:
    pick = random.randint(0, len(data))
    A_pick = data[pick]
    print(f"Compare A: {A_pick['name']}, a {A_pick['description']}, from {A_pick['country']}")
    print(vs)
    pick = random.randint(0, len(data))
    B_pick = data[pick]
    print(f"Compare B: {B_pick['name']}, a {B_pick['description']} from {B_pick['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if A_pick['follower_count'] > B_pick['follower_count']:
        winner = "A"
        print(winner)
    else:
        winner = "B"
        print(winner)
    if guess == winner:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"You're wrong! Final score: {score}")
        wrong = True
    




