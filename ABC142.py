a,b=map(int,input().split())

def prime(n):
    is_prime=[True]*(n+1)
    is_prime[0],is_prime[1]=False,False
    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
            is_prime[j]=False
    prime_num=[i for i in range(n+1) if is_prime[i]]
    return prime_num

p=min(a,b)
count=1
for i in prime(10**6):
    if p<i or 10**6<i:break
    elif a%i==0 and b%i==0:
        count +=1
print(count)