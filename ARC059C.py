n=int(input())
A=list(map(int,input().split()))
l,r=max(A),min(A)
cnt=10**10
for i in range(r,l+1):
    ans=0
    for j in A:
        ans +=(j-i)**2
    cnt=min(cnt,ans)
print(cnt)