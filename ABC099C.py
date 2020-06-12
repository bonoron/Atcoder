n=int(input())
inf=float("inf")
DP=[inf]*(n+1)
DP[0]=0

for i in range(1,n+1):
    DP[i]=DP[i-1]+1
    for point in (6,9):
        cnt=1
        while point**cnt<=i:
            DP[i]=min(DP[i-1]+1,DP[i-point**cnt]+1,DP[i])
            cnt +=1

print(DP[n])