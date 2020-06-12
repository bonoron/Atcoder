"""n<10**7の場合に使える。
https://drken1215.hatenablog.com/entry/2018/06/08/210000"""


def cmb(n,r,mod):
    if r<0 or r>n:return 0
    return g1[r]*g2[r]%mod


mod=10**9+7
n,a,b=map(int,input().split())
k=max(a,b)
g1=[1,n]
g2=[1,1]
inverse=[0,1]

for i,j in enumerate(range(n-1,((n-k+1)-1),-1)):
    i=i+2
    g1.append((g1[-1]*j)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1]%mod))

N=pow(2,n,mod)-1
print((N-cmb(n,b,mod)-cmb(n,a,mod))%mod)