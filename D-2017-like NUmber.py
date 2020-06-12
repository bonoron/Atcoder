def prime(n):
    is_prime=[True]*(n+1)
    is_prime[0],is_prime[1]=False,False
    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
            is_prime[j]=False
    return [i for i in range(n+1) if is_prime[i]]

prime_number=prime(10**5)
number=[i for i in prime_number if (i+1)//2 in prime_number]+[0]
ans=[0]*(10**5+1)
count=0

for i in range(1,10**5):
    ans[i]=ans[i-1]
    if i==number[count]:
        ans[i] +=1
        count +=1
#↑累積和を使っている。

for i in range(int(input())):
    a,b=map(int,input().split())
    print(ans[b]-ans[a-1])