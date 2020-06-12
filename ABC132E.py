import sys
from collections import deque
sys.setrecursionlimit(10**7)
input=sys.stdin.readline


def BFS():
    n,m=map(int,input().split())
    color=["white" for _ in range(n+1)]
    D=[-1]*(n+1)
    M=[[] for _ in range(n+1)]

    for u,v in [list(map(int,input().split())) for _ in range(m)]:
        M[u].append(v)
    s,t=map(int,input().split())
    queue=deque([[s,0,0]])

    while len(queue)!=0:
        num,cnt,point=queue.popleft()
        if cnt==3:
            if color[num]=="white":
                cnt=0
                point +=1
                D[num]=point
                color[num]="black"
                for i in M[num]:
                    queue.append([i,cnt+1,point])
        else:
            for i in M[num]:
                queue.append([i,cnt+1,point])
    return D[t]


print(BFS())