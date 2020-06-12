from bisect import bisect_right
n=int(input())
WH=sorted([list(map(int,input().split())) for _ in range(n)])

DP=[WH[-1]]
A=[WH[-1][0]]
length=0
for i in range(0,n-1,-1):
    if DP[length][0]>WH[i][0] and DP[length][1]>WH[i][1]:
        length +=1
        DP +=[WH[-1]]
    else:
