rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Let's play Rock-Paper-Scissors.")
player = input("What do you pick? Type 0 for rock, 1 for paper, 2 for scissors:")

choices = [rock, paper, scissors]
playerint = int(player)
print(f"You picked:\n {choices[playerint]}")

vs = random.randint(0, 2)
print(f"Computer picked:\n{choices[vs]}")

if playerint == vs:
    print("It's a tie")
elif playerint == 0 and vs == 1:
    print("You lose")
elif playerint == 0 and vs == 2:
    print("You win")
elif playerint == 1 and vs == 0:
    print("You lose")
elif playerint == 2 and vs == 1:
    print("You win")
