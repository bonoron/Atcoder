from bisect import bisect
n=int(input())
L=sorted(list(map(int,input().split())))
cnt=0
for i in range(n-2):
    for j in range(i+1,n-1):
        cnt +=bisect(L,L[i]+L[j]-1)-j-1
print(cnt)