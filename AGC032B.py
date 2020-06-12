inf=float("inf")
v,e=map(int,input().split())
STD=[list(map(int,input().split())) for _ in range(e)]

D=[[inf for _ in range(v)] for _ in range(v)]
for s,t,d in STD:
    D[s][t]=d

DP=[[-1 for _ in range(v)] for _ in range(1<<v)]


def bitDP(s,g,DP):
    if DP[s][g]>=0:return DP[s][g]
    if s==(1<<v)-1 and g==0:
        DP[s][g]=0
        return 0

    ans=inf
    for i in range(v):
        if (s>>i & 1)==0:
            ans=min(ans,bitDP(s|(1<<i),i,DP)+D[g][i])
    DP[s][g]=ans
    return ans


ans=bitDP(0,0,DP)
print(ans if ans!=inf else -1)