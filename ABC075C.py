import sys
from collections import deque
sys.setrecursionlimit(10**7)


def BFS(s,target):
    inf=float("inf")
    color=["white" for _ in range(n)]
    D=[inf for _ in range(n)]
    M=[[] for _ in range(n)]
    for i in AB:
        if i==target:continue
        a,b=i[0]-1,i[1]-1
        M[a] +=[b]
        M[b] +=[a]

    color[s]="gray"
    D[s]=0
    queue=deque([s])

    while len(queue)!=0:
        u=queue.popleft()
        color[u]="gray"
        for i in M[u]:
            if color[i]=="white":
                color[i]="gray"
                D[i]=D[u]+1
                queue.append(i)
        color[u]="black"

    return True if any([i==inf for i in D]) else False


n,m=map(int,input().split())
AB=[tuple(map(int,input().split())) for _ in range(m)]

cnt=0
for i in range(m):
    cnt +=BFS(0,AB[i])
print(cnt)