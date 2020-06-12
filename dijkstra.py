import heapq
inf=10**9


def dijkstra(s):
    color=["white" for _ in range(n+1)]
    D=[inf for _ in range(n+1)]
    P=[-1 for _ in range(n+1)]

    D[s]=0
    color[s]="gray"
    queue=[[0,s]]
    heapq.heapify(queue)

    while len(queue)>0:
        u=heapq.heappop(queue)[1]
        if color[u]=="black":continue
        color[u]="black"

        for i,j in M[u]:
            if color[j]!="white" and D[u]+i<D[j]:
                D[j]=D[u]+i
                P[j]=u
                color[j]="gray"
                heapq.heappush(queue,[D[j],j])

    return D


n,m=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(m)]
M=[[] for _ in range(n+1)]
for a,b in AB:
    M[a].append([weight,b])
    M[b].append([weight,a])
D=dijkstra(1)