import random

print("Welcome to rock, paper and scissors!")
again = 'y'
while(again == 'y'):
    choice = int(input("What do you choose? Type 0 - Rock, 1 - Paper and 2 - Scissors : "))
    if(choice == 0):
        print('''
                       _    
                      | |   
        _ __ ___   ___| | __
        | '__/ _ \ / __| |/ /
        | | | (_) | (__|   < 
        |_|  \___/ \___|_|\_\
              ''')
    elif(choice == 1):
        print('''                            
        _ __   __ _ _ __   ___ _ __ 
        | '_ \ / _` | '_ \ / _ \ '__|
        | |_) | (_| | |_) |  __/ |   
        | .__/ \__,_| .__/ \___|_|   
        | |         | |              
        |_|         |_|      
        ''')
    else : 
        print('''  
        ___  ___ _ ___ ___  ___  _ __ ___ 
        / __|/ __| / __/ __|/ _ \| '__/ __|
        \__ \ (__| \__ \__ \ (_) | |  \__ \
        |___/\___|_|___/___/\___/|_|  |___/
        ''')
        
    print("Computer chose : ")
    cchoice = random.randint(0,2)
    if(cchoice == 0):
        print('''
                       _    
                      | |   
        _ __ ___   ___| | __
        | '__/ _ \ / __| |/ /
        | | | (_) | (__|   < 
        |_|  \___/ \___|_|\_\
              ''')
    elif(cchoice == 1):
        print('''                            
        _ __   __ _ _ __   ___ _ __ 
        | '_ \ / _` | '_ \ / _ \ '__|
        | |_) | (_| | |_) |  __/ |   
        | .__/ \__,_| .__/ \___|_|   
        | |         | |              
        |_|         |_|      
        ''')
    else : 
        print('''  
        ___  ___ _ ___ ___  ___  _ __ ___ 
        / __|/ __| / __/ __|/ _ \| '__/ __|
        \__ \ (__| \__ \__ \ (_) | |  \__ \
        |___/\___|_|___/___/\___/|_|  |___/
        ''')
        

    if(choice == cchoice):
        print("You draw!")
    elif(choice == 0 and cchoice == 2):
        print("You win!")
    elif(cchoice == 0 and choice == 2):
        print("Computer Wins")
    elif(choice<cchoice):
        print("Computer Wins")
    else: 
        print("You win!")
    again = input("Wanna play again?")
    
    #can also save the rock, paper and scissors into strings with the respective names. 