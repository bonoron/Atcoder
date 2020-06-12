from collections import Counter


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


n,p=map(int,input().split())
A=Counter(prime_factorize(p)).items()
cnt=1
for i,j in A:
    cnt *=pow(i,j//n)
print(cnt)