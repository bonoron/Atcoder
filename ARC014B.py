n=int(input())
words=[input()]
W=[input() for i in range(n-1)]
for i,j in enumerate(W):
    if (j not in words) and (words[-1][-1]==j[0]):
        words.append(j)
    else:
        print("LOSE" if i%2==1 else "WIN")
        exit()
print("DRAW")