import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
num = int(input())

if num == 0:
  print("rock")
elif num == 1:
  print("paper")
else:
  print("scissors")

com_num = random.randint(0,2)

print("Computer chose:")
if com_num == 0:
  print("rock")
elif com_num == 1:
  print("paper")
else:
  print("scissors")

if num == 0 and com_num == 1:
  print("You Loss")
elif num == 0 and com_num == 2:
  print("You Win")
elif num == 1 and com_num == 0:
  print("You Win")
elif num == 1 and com_num == 2:
  print("You Loss")
elif num == 2 and com_num == 0:
  print("You Loss")
elif num == 2 and com_num == 1:
  print("You Win")
else:
  print("It's a draw")