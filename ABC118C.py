from fractions import gcd
from functools import reduce


def lcm_list(numbers):
    return reduce(gcd,numbers)


n=int(input())
A=sorted(list(map(int,input().split())))
print(lcm_list(A))