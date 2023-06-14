height = int(input("Enter you height in m: "))
weight = int(input("Enter your weight in kg: "))

#calculating BMI
bmi = weight/height**2

#printing BMI
print(f"BMI is : {bmi}") 

if(bmi<18.5):
    print("You are underweight.")
elif(bmi<25):
    print("You are of normal weight.")
elif(bmi<30):
    print("You are over weight.")
elif(bmi<35):
    print("You are obese.")
else:
    print("You are clinically obese.")