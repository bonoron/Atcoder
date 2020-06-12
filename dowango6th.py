from math import factorial
mod=10**9+7
n=int(input())
A,B=list(map(int,input().split())),[]

for i in range(n-1):
    B.append(A[i+1]-A[i])

cnt=0
for i in range(1,n):
    cnt +=B[i-1]*pow(i,mod-2,mod)
    cnt %=mod

print(cnt*factorial(n-1)%mod)