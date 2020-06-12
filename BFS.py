import sys
from collections import deque
sys.setrecursionlimit(10**7)


def BFS(s):
    color=["white" for i in range(n)]
    D=[float("inf") for i in range(n)]

    color[s-1]="gray"
    D[s-1]=0
    queue=deque([s-1])

    while len(queue)!=0:
        u=queue.popleft()
        for i in range(n):
            if M[u][i] and color[i]=="white":
                color[i]="gray"
                D[i]=D[u]+1
                queue.append(i)
        color[u]="black"

    return D


n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
M=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in A[i][2:]:
        M[i][j-1]=1

s=A[0][0]
D=BFS(s)

for i in range(n):
    print(i+1,D[i])