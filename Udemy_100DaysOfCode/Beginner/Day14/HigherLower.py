import random
import os 

print("Welcome to Higher or Lower")
comparisons = { "Neymer" : 12345, "Khole" : 23632, "Justin" : 12943, "Kylie" : 23724, "Rob" : 13847, "Ronaldo" : 33645, "Selena" : 93184 }

score = 0 
correct = True
a = random.choice(list(comparisons.keys()))
while(correct):
    b = random.choice(list(comparisons.keys()))
    print(f"SCORE : {score}\n")
    print(f"Compare A: {a}")
    print("VS")
    print(f"Compare B: {b}")
    option = input("Who has greater followers : a or b or c(equal)--> ").lower()
    if(option == 'a' and comparisons[a]>comparisons[b]) or (option == 'b' and comparisons[a]<comparisons[b]) or (option == 'c' and comparisons[a] == comparisons[b]) :
        score += 1
        print("CORRREECCT!!!")
        a = b
        os.system('cls')
    else : 
        print("WRRRRRRRONGGGGGG")
        correct = False 
        
print(f"Your final score is: {score}")