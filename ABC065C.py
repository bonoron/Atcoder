from math import factorial
n,m=map(int,input().split())
a,b=max(n,m),min(n,m)
Q=10**9+7
if a-b>1:print(0);exit()
elif (a+b)%2==1:print((factorial(a)*factorial(b))%Q)
else:print((factorial(a)*2*factorial(b))%Q)