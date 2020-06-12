from fractions import gcd
from functools import reduce


def lcm(x,y):
    return (x*y)//gcd(x,y)


def lcm_list(nums):
    return reduce(lcm,nums,1)


n,m=map(int,input().split())
A=list(map(int,input().split()))
ans=lcm_list(A)
if ans//2>m:print(0);exit()
if (m-ans//2)%ans==0:print(m//ans//2)
print(m//ans//2+1)