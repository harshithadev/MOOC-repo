print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? Rs"))
percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
eachbill = ( bill + (percentage/100)*bill ) / people
print("Each person should pay: Rs%.2f"%eachbill)