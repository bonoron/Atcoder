def prime_factorize(n):
    a=[]
    while n%2==0:
        a.append(2)
        n //=2
    f=3
    while f**2<=n:
        if n%f==0:
            a.append(f)
            n //=f
        else:f +=2
    if n!=1:a.append(n)
    return a


mod=10**9+7
n=int(input())
cnt={}
for i in range(1,n+1):
    for j in prime_factorize(i):
        if j not in cnt:cnt[j]=1
        else:cnt[j] +=1

ans=1
for i in cnt.values():
    ans=ans*(i+1)%mod
print(ans)