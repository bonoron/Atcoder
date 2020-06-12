def prime_factorize(n):
    a=[]
    while n%2==0:
        a +=[2]
        n //=2
    f=3
    while f**2<=n:
        if n%f==0:
            a +=[f]
            n //=f
        else:f +=2
    if n!=1:a +=[n]

    return a


n=int(input())
A=prime_factorize(n)
print("%d:"%n,*A)