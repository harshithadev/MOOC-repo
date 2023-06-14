import random
import os

#added the number of attempts per level as gloabal level as it could be easily changed as and when the rules change.
HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10

def result(number, guessed_no):
    """ Compares the guessed and the actual number and returns if it right, or too low or too high. """
    if(number == guessed_no):
        return True
    elif(number > guessed_no):
        print("Too low")
    else:
        print("Too High")
    return False

def guess(number, attempts):
    """ Lets the user to guess a number """
    game_over = False
    while(attempts>0 and not game_over):
        print(f"You have {attempts} attempts remaining to guess the number")
        guessed_no = int(input("Make a guess : "))
        game_over = result(number, guessed_no)
        attempts -= 1
    if(not game_over):
        print(f"The number was {number}. Better luck next time!")
    else : 
        print(f"Awesome! Good going!! The number was {number}")
        

def gamenight():
    """ Actual game"""
    number = random.randint(1,100)
    print("I am thinking of a number between 1 and 100.")
    level = input("Choose the difficulty level : easy or hard?  ")
    if(level == "hard"):
        attempts = HARD_LEVEL_ATTEMPTS
    else:
        attempts = EASY_LEVEL_ATTEMPTS
    guess(number,attempts)
    if(input("Do you want to continue? 'y'  --> ")=='y'):
        os.system('cls')
        gamenight()
    else :
        return

print("Welcome to the Number Guessing Game!")
gamenight()
print("GOod ByE!")