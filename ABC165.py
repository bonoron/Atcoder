from collections import deque
from bisect import bisect_left

def BFS():
    color=["white" for _ in range(n+1)]
    D=[0 for _ in range(n+1)]
    M=[[] for _ in range(n+1)]

    color[1]="gray"
    for u,v in UV:
        M[u].append(v)
        M[v].append(u)

    queue=deque([1])
    while len(queue)>0:
        u=queue.popleft()
        for i in M[u]:
            if color[i]=="white":
                D[i]=D[u]+1
                color[i]="gray"
                queue.append(i)
        color[u]="black"

    return D


n=int(input())
A=list(map(int,input().split()))
UV=[list(map(int,input().split())) for _ in range(n-1)]
D=BFS()
A=[[D[i+1],A[i]] for i in range(n)]
A.sort()
print(A)
DP=[A[0][1]]
print(len(DP))
for i in range(1,n):
    if DP[-1]<A[i][1]:
        DP.append(A[i][1])
    else:
        index=bisect_left(DP,A[i][1])
        DP[index]=A[i][1]
    print(len(DP))