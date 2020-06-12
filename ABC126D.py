from collections import deque
import sys
input=sys.stdin.readline


def BFS():
    color=["white" for _ in range(n)]
    D=[0]*n
    M=[[] for _ in range(n)]

    for u,v,w in UVW:
        M[u-1].append([v-1,w])
        M[v-1].append([u-1,w])

    D[0]=1
    color[0]="gray"
    queue=deque([0])

    while len(queue)>0:
        u=queue.popleft()
        for i,j in M[u]:
            if color[i]=="white":
                if j%2==0:D[i]=D[u]
                elif j%2==1:D[i]=-D[u]
                color[i]="gray"
                queue.append(i)
        color[u]="black"

    return D


n=int(input())
UVW=[list(map(int,input().split())) for _ in range(n-1)]
for i in BFS():
    if i==-1:print(0)
    else:print(i)