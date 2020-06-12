inf=10**8
a,b,c,d,e,f=map(int,input().split())
a,b=100*a,100*b
DP=[inf]*(f+max(a,b)+1)
DP[a],DP[b]=0,0

for i in range(f+1):
    if DP[i]!=inf:
        DP[i+a]=DP[i]
        DP[i+b]=DP[i]
        for j in c,d:
            if 100*(DP[i]+j)/(i+j)<=100*e/(100+e):
                DP[i+j]=max(DP[i],DP[i]+j)

ans,index=0,[a,0]
for i in range(f+1):
    if DP[i]!=inf:
        if ans<100*DP[i]/i:
            ans=100*DP[i]/i
            index=[i,DP[i]]

print(*index)