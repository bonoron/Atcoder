inf=float("inf")
n=int(input())
A=list(map(int,input().split()))

ans=-inf
for i in range(n):
    tmp_a,tmp_t=-inf,-inf
    for j in range(n):
        if i==j:continue
        B=A[min(i,j):max(i,j)+1]
        if tmp_a<sum(B[1::2]):
            tmp_t=sum(B[::2])
            cnt=sum(B[1::2])
    ans=max(ans,tmp_t)
print(ans)