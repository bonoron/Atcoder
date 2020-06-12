n=int(input())
C=list(list(map(int,input().split())) for i in range(n-1))
ans=0
for i in range(n-1):
    start=0
    for j in range(i,n-1):
        if i==j:
            start=C[i][0]+C[i][1]
            continue
        else:
            if start<=C[j][1]:start=C[j][1]
            elif start%C[j][2]==0:start +=0
            else:start +=C[j][2]-(start%C[j][2])
            start +=C[j][0]
    print(start)
print(0)