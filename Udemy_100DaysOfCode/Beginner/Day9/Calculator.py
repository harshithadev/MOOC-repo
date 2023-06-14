n1 = input("Enter the first number: ")
op = input("Enter the operation: ")
n2 = input("Enter the second number: ")

def calculate(n1, op, n2):
    return(eval(n1+op+n2))

print(f"Result = {calculate(n1,op,n2)}")