def make_divisors(n):
    A=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            A.append(i)
            if i!=n//i:
                A.append(n//i)

    return A


n=int(input())
ans=sum(make_divisors(n))-n
if n==ans:print("Perfect")
elif n<ans:print("Abundant")
else:print("Deficient")