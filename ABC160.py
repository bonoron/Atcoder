import sys
from collections import deque
sys.setrecursionlimit(10**7)


def BFS(s):
    color=["white" for _ in range(n)]
    D=[float("inf") for _ in range(n)]

    color[s-1]="gray"
    D[s-1]=0
    queue=deque([s-1])

    while len(queue)!=0:
        u=queue.popleft()
        for i in M[u]:
            if color[i]=="white":
                color[i]="gray"
                D[i]=D[u]+1
                queue.append(i)
        color[u]="black"

    return D


n,x,y=map(int,input().split())

M=[[] for _ in range(n)]
for i in range(n-1):
    M[i].append(i+1)
    M[i+1].append(i)
M[x-1].append(y-1)
M[y-1].append(x-1)

C=[0]*n
for i in range(n):
    for j in BFS(i+1)[i:]:
        C[j] +=1

for i in C[1:]:
    print(i)