import random 

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters do you like in your password? "))
no_symbols = int(input("How many symbols do you like in your password? "))
no_numbers = int(input("How many numbers do you like in your password? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['{','}','(',')','[',']','.',':',';','+','-','*','/','&','|','<','>','=','~']
numbers = ['0','1','2','3','4','5','6','7','8','9']
password = random.choices(letters,k=no_letters)+random.choices(symbols,k=no_symbols)+random.choices(numbers,k=no_numbers)
random.shuffle(password)
password = "".join(password)
print(f"Here is a password for you : {password}")