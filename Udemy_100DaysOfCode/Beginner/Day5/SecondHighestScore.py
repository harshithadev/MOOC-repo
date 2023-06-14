#just tweaked the question a little, instead of highest score, i thought i'd check out the second highest

scores = list(map(int,input().split()))
print(f"Second heightest : {sorted(scores)[-2]}")

#alternatively, without using functions :

highest = scores[0]
secondhighest = scores[0]

for score in scores :
    if(score>highest):
        secondhighest = highest 
        highest = score
print(f"Second highest : {secondhighest}")