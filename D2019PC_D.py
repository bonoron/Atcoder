def make_devisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors +=[i]
            if i!=n//i:
                divisors +=[n//i]
    return divisors


n=int(input())
D=sorted(make_devisors(n))
ans=0
for i in D[1:]:
    if (n//(i-1))*i==n:
        ans +=i-1
print(ans)