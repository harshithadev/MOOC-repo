import random

#first 0 or 1 -> essentially meaning that 0 is heads and 1 refers to tails. 
toss = random.randint(0,1)
print(toss)
# if(toss == 0):
#     print("heads!")
# else: 
#     print("tails!")


#or another option would be to use the choice function.
c = random.choice(['heads','tails'])
print(c)