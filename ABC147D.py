import numpy as np
mod=10**9+7
n=int(input())
A=np.array(list(map(int,input().split())))

ans=0

for i in range(60):
    cnt=np.count_nonzero(A&1)
    ans +=2**i*cnt*(n-cnt)
    A >>=1

print(ans%mod)