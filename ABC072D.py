from math import ceil
n=int(input())
P=list(map(int,input().split()))
Q=["*"]*(n+1)

for i in range(n):
    if P[i]==i+1:Q[i]="#"

ans,cnt,point=0,0,0
while cnt!=n+1:
    if Q[cnt]=="#":point +=1
    elif Q[cnt]=="*" and point>=1:
        ans +=ceil(point/2)
        point=0
    cnt +=1

print(ans)