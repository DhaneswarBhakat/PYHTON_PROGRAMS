print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

from random import randint
number = randint(1,100)

def check_guess(n):
  for i in range(n, 0, -1):
    print(f"You hava {i} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    if guess_number == number:
      print(f"You got it! The answer was {guess_number}")
      break
    elif guess_number > number:
      print("To high.")
    else:
      print("To low.")
    print("Guess again.")

if difficulty == "easy":
  check_guess(10)
elif difficulty == "hard":
  check_guess(5)