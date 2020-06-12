n,k=map(int,input().split())
mod=10**9+7

DP=[0]*(n+2)
DP[0]=1
point=n
n=n+1

for i in range(1,n+1):
    DP[i]=DP[i-1]+point
    point -=2
print(sum(DP[k:])%mod)