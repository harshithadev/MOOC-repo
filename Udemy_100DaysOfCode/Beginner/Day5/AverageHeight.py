heights = list(map(int,input().split()))
print(f"Average : {sum(heights)/len(heights)}")


#alternatively :
hsum = 0
n = 0
for i in heights:
    hsum += i
    n += 1
print(f"Average : {hsum/n}")

