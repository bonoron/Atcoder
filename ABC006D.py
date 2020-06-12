from bisect import bisect_left
n=int(input())
A=[int(input()) for _ in range(n)]

DP=[A[0]]
length,cnt=0,0
for i in range(1,n):
    if DP[length]<A[i]:
        length +=1
        DP +=[A[i]]
    else:
        index=bisect_left(DP,A[i],0,length)
        DP[index]=A[i]
        cnt +=1

print(cnt)