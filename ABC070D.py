import heapq
import sys
input=sys.stdin.readline


def dijkstra(s):
    inf=float("inf")
    color=["white" for _ in range(n)]
    D=[inf for _ in range(n)]

    M=[[] for _ in range(n)]
    for a,b,c in ABC:
        M[a-1].append([b-1,c])
        M[b-1].append([a-1,c])

    D[s]=0

    H=[(0,s)]
    heapq.heapify(H)

    while len(H)>=1:
        u=heapq.heappop(H)[1]
        if color[u]=="black":continue
        color[u]="black"

        V=[(i,j) for i,j in M[u] if color[i]!="black"]
        while len(V)!=0:
            for i,j in V:
                if D[u]+j<D[i]:
                    D[i]=D[u]+j
                    color[i]="gray"
                    heapq.heappush(H,(D[i],i))
            break

    return D


n=int(input())
ABC=[list(map(int,input().split())) for _ in range(n-1)]
q,k=map(int,input().split())
XY=[list(map(int,input().split())) for _ in range(q)]
D=dijkstra(k-1)
for x,y in XY:
    print(D[x-1]+D[y-1])