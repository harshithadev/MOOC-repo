import random
import os
from HangmanArt import hangmanlogo,hstages
# def loosechance(int chance):
#     pass

# def updateguesslist(List wordlist,List guesslist):
#     pass

print("Welcome to Hangman!!!!")
print(hangmanlogo)

gameover = False
guessed = False
chance = 0
words = ["hammer", "grammar", "hostile", "beetle", "busybee", "bossy"]
word = random.choice(words)
stages = hstages
wordlist = list(word)
guesslist = list("_"*len(wordlist))

while(not gameover and not guessed):
    letter = input("Guess a letter : ").lower()
    os.system("cls")
    if(letter in wordlist and letter not in guesslist):
        #updateguesslist()
        indices = [x for x in range(0,len(wordlist)) if wordlist[x] == letter]
        for index in indices:
            guesslist[index] = letter
        print(stages[chance])
        print(guesslist)
        if("_" not in guesslist):
            print("You Win!")
            guessed = True
    else:
        #loosechance(chance)
        print(stages[chance])
        print(guesslist)
        chance += 1
        print(f"neh, chances left : {7-chance}")
        if(chance == 7):
            print("You loose!")
            gameover = True
    