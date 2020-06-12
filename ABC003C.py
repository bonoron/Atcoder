n,k=map(int,input().split())
R=sorted(list(map(int,input().split())))
ans=0
for i in range(n-k,n):
    ans=(ans+R[i])/2
print(ans)