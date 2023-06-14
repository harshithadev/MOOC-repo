from math import ceil

def cansrequired(height, breadth):
    return ceil(height*breadth/5)

height = int(input("Height of the wall: "))
breadth = int(input("Breadth of the wall: "))
print(f"Number of cans required is: {cansrequired(height, breadth)}")