from math import gcd
from functools import reduce


def gcd_(*numbers):
    return reduce(math.gcd, numbers)


#list型を受け取って最大公約数を返す
def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_(*numbers):
    return reduce(lcm_base, numbers, 1)


#list型を受け取って最小公倍数を返す
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)