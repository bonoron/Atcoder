n,q=map(int,input().split())
LR=[list(map(int,input().split())) for _ in range(q)]

DP=[0]*(n+2)
for l,r in LR:
    DP[l] +=1
    DP[r+1] -=1

for i in range(1,n+1):
    DP[i] +=DP[i-1]

ans=""
for i in range(1,n+1):
    ans +="0" if DP[i]%2==0 else "1"

print(ans)