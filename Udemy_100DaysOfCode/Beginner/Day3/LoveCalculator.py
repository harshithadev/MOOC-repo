print("Welcome to the Love Calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

name1 = name1.lower()
name2 = name2.lower()
#alternatively a smart person would add the names up like so...
#names = name1+name2, and then count each letter once.

units = 0
units = units + name1.count('l') + name2.count('l') + name1.count('o') + name2.count('o') + name1.count('v') + name2.count('v') + name1.count('e') + name2.count('e')  

tens = 0
tens = tens + name1.count('t') + name2.count('t') + name1.count('r') + name2.count('r') + name1.count('u') + name2.count('u') + name1.count('e') + name2.count('e') 

percentage = tens*10 + units

if percentage<10 or percentage>90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")
elif percentage<50 and percentage>40:
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")