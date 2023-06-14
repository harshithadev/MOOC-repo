

row1 = ['☠','☠','☠']
row2 = ['☠','☠','☠']
row3 = ['☠','☠','☠']
maps = [row1, row2, row3]
#print(f"{maps[0]}\n{maps[1]}\n{maps[2]}")
print(f"{row1}\n{row1}\n{row1}")
c,r = map(int, input().split())

maps[r-1][c-1] = 'x'
print(f"{maps[0]}\n{maps[1]}\n{maps[2]}")

