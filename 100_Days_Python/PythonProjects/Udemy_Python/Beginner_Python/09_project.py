# Blind Auction Game
# import os
# print("Welcome to the Blind Auction Game")
# is_value = True
# while is_value:
#     name = input("Write your name: ")
#     bid = int(input("What is your bid: $"))
#     Highest_Bid = 0
#     anyone = input("Are there any other bidders? (Yes or No): ")
#     if anyone == "Yes":
#         clear = lambda: os.system('cls')
#         clear()
#         is_value = True
#     else:
#         print(f"The Winner is {name} of highest bid of ${Highest_Bid}")
#         is_value = False
bids = {}
bidding_finished = False
import os
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
      clear = lambda: os.system('cls')
      clear()
