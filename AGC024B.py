n=int(input())
P=[int(input()) for _ in range(n)]
DP=[0]*(n+1)

for i in P:
    DP[i]=DP[i-1]+1
print(n-max(DP))