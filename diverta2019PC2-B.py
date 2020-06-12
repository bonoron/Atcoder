from collections import Counter
from itertools import permutations
n=int(input())
if n==1:print(1);exit()
A=[list(map(int,input().split())) for i in range(n)]
B=[(a[0]-b[0],a[1]-b[1]) for a,b in permutations(A,2)]
most=max(Counter(B).values())
print(n-most)