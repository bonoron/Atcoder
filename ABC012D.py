def warshalFloyd(v,e,flag=0):
    inf=float("inf")
    M=[[inf if i!=j else 0 for i in range(v)] for j in range(v)]

    for i in range(e):
        s,t,d=map(int,input().split())
        M[s-1][t-1]=d
        if flag:M[t-1][s-1]=d

    for k in range(v):
        for i in range(v):
            if M[i][k]==inf:continue
            for j in range(v):
                if M[k][j]==inf:continue
                M[i][j]=min(M[i][j],M[i][k]+M[k][j])

    return M


n,m=map(int,input().split())
M=warshalFloyd(n,m,1)

ans=float("inf")
for i in range(n):
    ans=min(ans,max(M[i]))

print(ans)