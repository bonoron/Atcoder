from math import factorial


def cmb(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))


n,p=map(int,input().split())
A=list(map(int,input().split()))
A=[A[i]%2 for i in range(n)]

cnt=A.count(0)
ans=0
for i in range(p,n-cnt+1,2):
    ans +=cmb(n-cnt,i)
print(ans*(2**cnt))