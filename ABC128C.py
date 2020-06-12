n,m=map(int,input().split())
S=[list(map(int,input().split()))[1:] for i in range(m)]
P=list(map(int,input().split()))
cnt=0
for i in range(2**n):
    pattern=format(i,"b").zfill(n)
    point=0
    for j in range(m):
        swi=0
        for k in S[j]:
            if pattern[k-1]=="1":swi +=1
        if swi%2==P[j]:point +=1
    if point==m:cnt +=1
print(cnt)