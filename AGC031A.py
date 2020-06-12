from collections import Counter
n=int(input())
s=list(Counter(input()).items())
ans=1
for i in s:
    ans *=i[1]+1
print((ans-1)%(10**9+7))