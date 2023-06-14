def isPrime(number):
    prime = True
    for i in range(2,number//2):
        if(number%i==0):
            prime = False
            break
    return prime
number = int(input("Enter a number to check if prime : "))
if(number == 1):
    print("neither")
elif(isPrime(number) ):
    print("Is prime!!!")
else: 
    print("Is not prime!!!")
