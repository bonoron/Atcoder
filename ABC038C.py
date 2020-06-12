n=int(input())
A=list(map(int,input().split()))

ans=1
num,cnt=A[0],1
for i in range(1,n):
    if num<A[i]:cnt +=1
    else:cnt=1
    ans +=cnt
    num=A[i]
print(ans)