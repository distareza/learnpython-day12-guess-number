#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")

# Allow the player to submit a guess for a number between 1 and 100.
import random
guess_number = random.randint(1,100)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
def check_answer(guess, answer) :
  if user_number < guess_number:
    print("Too Low")
    return False
  elif user_number > guess_number:
    print("Too High")
    return False
  else:
    print("Yeay")
    print(f"You manage to guess it")
    return True
  
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def setDificulty():
  game_level = input("Choose difficulty [easy, medium, hard] ? " )
  if game_level.lower() == "easy" :
    return 10
  elif game_level.lower() == "medium": 
    return 7
  else:
    return 5

retry = setDificulty()
attemp_count = retry

for _ in range(retry):
  user_number = int(input("Make a guess: "))
  
  if not check_answer(guess_number, user_number):
    attemp_count -= 1
    if attemp_count>0 :  
      print("Guess again..")
      print(f"Yout have {attemp_count} attemps remining to guess the number")
    elif attemp_count==0:
      print(f"You've run out of guesses, you lose")
      print(f"the number is : {guess_number}")
      break
  else:  
    break


