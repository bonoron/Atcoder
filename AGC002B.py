n,m=map(int,input().split())
A=[list(map(int,input().split())) for i in range(m)]
water=[1]*(n+1)
red=[0]*(n+1)
red[1]=1
for x,y in A:
    water[y] +=1
    water[x] -=1
    if red[x]==1:red[y]=1
    if water[x]==0:red[x]=0

cnt=0
for i in range(1,n+1):
    if water[i]>0 and red[i]==1:
        cnt +=1

print(cnt)