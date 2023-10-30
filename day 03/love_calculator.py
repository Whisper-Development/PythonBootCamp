print("Welcome to the Love Calculator!")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combname = str.lower(name1+name2)

test1 = ['t', 'r', 'u', 'e']
test2 = ['l', 'o', 'v', 'e']
score1 = 0
score2 = 0

for i in combname:
    if i in test1:
        score1 += 1
    if i in test2:
        score2 += 1

totals = str(score1) + str(score2)
totalint = int(totals)

if totalint < 10 or totalint > 90:
    print(f"Your score is {totalint}, you go together like coke and mentos.")
elif 40 < totalint < 50:
    print(f"Your score is {totalint}, you are alright together.")
else:
    print(f"Your score is {totalint}")
