def warshalFloyd(v,e):
    inf=float("inf")
    M=[[inf if i!=j else 0 for i in range(v)] for j in range(v)]

    for i in range(e):
        s,t,d=map(int,input().split())
        M[s][t]=d

    for k in range(v):
        for i in range(v):
            if M[i][k]==inf:continue
            for j in range(v):
                if M[k][j]==inf:continue
                M[i][j]=min(M[i][j],M[i][k]+M[k][j])

    return M


v,e=map(int,input().split())
M=warshalFloyd(v,e)

for i in range(v):
    if M[i][i]<0:print("NEGATIVE CYCLE");exit()

for i in range(v):
    M[i]=list(map(str,M[i]))
    for j in range(v):
        if M[i][j]=="inf":
            M[i][j]="INF"

for i in range(v):
    print(*M[i])