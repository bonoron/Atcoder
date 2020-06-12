n=int(input())
A=list(map(int,input().split()))
a,b=sum(A)-A[0],A[0]
cnt=abs(a-b)
for i in range(1,n-1):
    b +=A[i]
    a -=A[i]
    cnt=min(cnt,abs(a-b))
print(cnt)