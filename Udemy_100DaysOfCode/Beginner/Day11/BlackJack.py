# VERSION 1
# import random
# import os
# from BlackJackArt import logo

# def gamenight():
#     print(logo)

#     cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
#     mycards = random.choices(cards,k=2)
#     computerscards = random.choices(cards,k=2)
    
#     print(f"Your cards {mycards}")
#     print(f"Computer's first card : {computerscards[0]}")
#     hitme = input("Type 'y' to get another card, else type 'n' --> ")
#     while(hitme == 'y'):
#         mycards.append(random.choice(cards))
#         print(f"Your cards {mycards}")
#         hitme = input("Type 'y' to get another card, else type 'n' --> ")
#     print(f"Your final hand : {mycards}")
#     print(f"Computer's final hand : {computerscards}")
#     if(sum(mycards)>21 or sum(mycards)<sum(computerscards)):
#         print("Computer Wins!")
#     elif(sum(mycards) == sum(computerscards)):
#         print("You Draw!")
#     else:
#         print("Dealer's count is less than player, dealer must take a card.")
#         computerscards.append(random.choice(cards))
#         if(sum(mycards) == sum(computerscards)):
#             print("You Draw!")
#         elif(sum(computerscards)>21):
#             print("You Win!")
#         elif(sum(mycards) < sum(computerscards)):
#             print("Computer Wins!")
#         else:
#             print("You Win!")
    
#     tryagain = input("Type 'y' to play again, else type  'n' --> ")
#     if(tryagain == 'y'):
#         os.system('cls')
#         gamenight()
#     else :
#         return


# print("Welcome to BlackJack!!!")
# gamenight()
# print("Good Bye!")


# VERSION 2 

import random 
import os
from BlackJackArt import logo

def dealcard():
    """Deals a card."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def getscore(deck):
    """Calculates and returns the score of the hand dealt"""
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck)>21 :
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def compare(player, computer):
    if(player>21 and computer>21):
        return "computer wins!"
    elif(player == computer):
        return " You Draw ! "
    elif(computer == 0):
        return "Computer Wins!"
    elif(player == 0):
        return "You Win!"
    elif(player > 21):
        return "Computer wins"
    elif(computer > 21):
        return "You Win"
    elif(computer > player):
        return "computer wins!"
    else:
        return "You win!"
def gamenight():
    print(logo)
    is_game_over = False
    playercards = []
    computercards = []
    for _ in range(2):
        playercards.append(dealcard())
        computercards.append(dealcard())

    while(not is_game_over):
        print(f"Players' Hand: {playercards}")
        print(f"Computers' first card : {computercards[0]}")

        if(getscore(playercards) == 0 or getscore(playercards)>21):
            is_game_over = True
        else:
            if(input("Enter 'y' to get another card : ") == 'y'):
                playercards.append(dealcard())
            else :
                is_game_over = True
    while(getscore(computercards)!= 0 and getscore(computercards)<17):
                computercards.append(dealcard())
    
    print(f"Players' Hand: {playercards}")
    print(f"Computers' first card : {computercards}")
    print(compare(getscore(playercards), getscore(computercards)))
            
    if(input("Wanna play again? 'y' or 'n' --> ") == 'y'):
        os.system('cls')
        gamenight()
    else: 
        return
        
print("Welcome to BlackJack!!!")
gamenight()
print("Good Bye!")
        
# the difference between version1 and version2 is that I started coding without understanding the rules of the game
# and thus when I tried to compare results, they weren't right.
# Version 2 is after step by step understanding of all rules