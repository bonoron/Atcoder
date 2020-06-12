n=int(input())
A=list(map(int,input().split()))+[float("inf")]

DP=[float("inf")]*n
DP[0]=0
for i in range(1,n):
    DP[i]=min(DP[i],abs(A[i]-A[i-1])+DP[i-1],abs(A[i]-A[i-2])+DP[i-2])
print(DP[-1])