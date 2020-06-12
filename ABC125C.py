from fractions import gcd

n=int(input())
A=list(map(int,input().split()))
left=[0]*n
right=[0]*n

left[0]=A[0]
for i in range(1,n-1):
    left[i]=gcd(left[i-1],A[i])

right[-1]=A[-1]
for i in range(1,n-1)[::-1]:
    right[i]=gcd(right[i+1],A[i])

ans=max(left[-2],right[1])
for i in range(1,n-1):
    ans=max(ans,gcd(left[i-1],right[i+1]))
print(ans)