print("Welcome to the secret auction program.")

auction_dictionarie = {}

def find_highest_bidder(bidding_record):
  highest_bit = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bit:
      highest_bit = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bit}")

while True:
  name = input("What is your name?: ")
  bit = int(input("What's your bit?: $"))
  auction_dictionarie[name] = bit
  print("Are there any other bidders? Type 'yes' or 'no'.")
  bidder = input()
  if bidder == "yes":
    continue
  else:
    find_highest_bidder(auction_dictionarie)
    break