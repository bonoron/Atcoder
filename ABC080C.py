n=int(input())
F=[input().split() for _ in range(n)]
P=[list(map(int,input().split())) for _ in range(n)]

ans=-float("inf")
for i in range(1,2**10):
    cnt=0
    num=format(i,"b").zfill(10)
    for j,k in enumerate(F):
        cnt +=P[j][len([v for v in range(10) if k[v]==num[v]=="1"])]
    ans=max(ans,cnt)
print(ans)