#plain fizz
for no in range(1,101):
    if(no%3 == 0):
        print("Fizz")
    else:
        print(no)
        
#fizzbuzz
for no in range(1,101):
    if(no%15 == 0):
        print("FizzBuzz")
    elif(no%3 == 0):
        print("Fizz")
    elif(no%5 == 0):
        print("Buzz")
    else:
        print(no)