import sys
from collections import deque
sys.setrecursionlimit(10**7)


def BFS(s):
    color=["white" for _ in range(n)]
    D=[float("inf") for _ in range(n)]

    color[s]="gray"
    D[s]=0
    queue=deque([s])

    while len(queue)!=0:
        u=queue.popleft()
        for i,j in M[u]:
            if color[i]=="white":
                queue.append(i)
                color[i]="gray"
                D[i]=D[u]+j
        color[u]="black"

    return max(enumerate(D), key=lambda x:x[1])


n=int(input())
M=[[] for _ in range(n)]
for i in range(n-1):
    s,t,w=map(int,input().split())
    M[s].append((t,w))
    M[t].append((s,w))

add,ans=BFS(0)
print(max(ans,BFS(add)[1]))