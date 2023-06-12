#Number Guessing Game Objectives:
import random
from art import logo

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
print(logo)
guessed_num = random.randint(1, 100)
print(f"correct answer is {guessed_num}")
print("I am thinking of a number between 1 and 100")
difficulty = ""
while difficulty != "easy" and  difficulty != "hard":
  difficulty = input('choose a difficulty. type: "easy" or "hard" ').lower()
    
  turns = 0
  
  
  if difficulty == "hard":
    turns = 5
      
  elif difficulty == "easy":
    turns = 10
  elif difficulty != "easy" and  difficulty != "hard":
    print("you typed a wrong  word for difficulty level")
    
    
    
    
  
  
  print(f"you have {turns} guessing attempts")
  








while 0 < turns:
  user_guess = int(input("make a guess "))
  
  if user_guess == guessed_num:
    turns = 0
    
    print(f"you win number is {guessed_num}")
  elif user_guess < guessed_num:
    turns -= 1
    print(f"you have {turns} attempts remaining ")
    if turns == 0 and user_guess < guessed_num:
      print(f"You lose. the actual number is {guessed_num}")
    print("your guess is too low")
  elif user_guess > guessed_num:
    turns -= 1
    print("your guess is to high")
    print(f"you have {turns} attempts remaining")
    if turns == 0 and user_guess > guessed_num:
      print(f"You lose. the actual number is {guessed_num}")
      

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

