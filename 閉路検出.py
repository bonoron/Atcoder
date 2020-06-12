"ARC037B"
from collections import deque


def BFS(s):
    cnt=0
    queue=deque([s])
    color[s]="gray"

    while len(queue)>0:
        u=queue.popleft()
        for i in M[u]:
            if color[i]=="white":
                color[i]="gray"
                queue.append(i)
            elif color[i]=="gray":
                cnt +=1
        color[u]="black"

    return True if cnt==0 else False


n,m=map(int,input().split())
UV=[list(map(int,input().split())) for _ in range(m)]

color=["white" for _ in range(n)]
M=[[] for _ in range(n)]
for u,v in UV:
    M[u-1].append(v-1)
    M[v-1].append(u-1)

ans=0
for i in range(n):
    if color[i]=="white":
        ans +=BFS(i)
print(ans)