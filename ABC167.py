def cmb(n,r,mod):
    if r<0 or r>n:return 0
    r=min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod


mod=998244353
n,m,k=map(int,input().split())
g1=[1,1]
g2=[1,1]
inverse=[0,1]

for i in range(2,n):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1]%mod))

ans=m*(m-1)**(n-1)
for i in range(k):
    ans +=m*pow(m-1,n-2-i,mod)*cmb(n-1,i+1,mod)
    ans %=mod

print(ans%mod)