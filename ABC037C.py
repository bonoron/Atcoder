n,k=map(int,input().split())
A=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    A[i]=A[i-1]+A[i]
ans=0
for i in range(n-k+1):
    ans +=A[i+k]-A[i]
print(ans)