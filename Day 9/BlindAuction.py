from art import logo
from collections import defaultdict

#Welcome to the Blind Auction Program
print("Welcome to the Blind Auction Python Program")
print(logo)

bidders = defaultdict(list)

def new_bidder(name, bid):
    bidders[name].append(bid)
    return bidders

def highest_bidder(bidders):
    highest_bid = 0
    highest_bidder_name = ""

    for name, bids in bidders.items():
        highest_bid = max(bids)
        highest_bidder_name = name

    return highest_bidder_name

people = 1
while people > 0:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))

    new_bidder(name, bid)

    next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next == 'no':
        people = 0

winning_bidder = highest_bidder(bidders)

print(f"The winning bidder is {winning_bidder}.")
