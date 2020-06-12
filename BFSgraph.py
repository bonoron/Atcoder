import sys
from collections import deque
sys.setrecursionlimit(10**7)
inf=float("inf")


def BFS(x,y):
    color=[["white" for _ in range(w+2)] for _ in range(h+2)]
    D=[[inf for _ in range(w+2)] for _ in range(h+2)]

    color[x][y]="gray"
    D[x][y]=1
    queue=deque([[x,y]])
    while len(queue)!=0:
        a,b=queue.popleft()
        for c,d in ((1,0),(0,1),(-1,0),(0,-1)):
            X,Y=a+c,b+d
            if S[X][Y]=="." and color[X][Y]=="white":
                color[X][Y]="gray"
                D[X][Y]=D[a][b]+1
                queue.append([X,Y])
        color[a][b]="black"

    return D


h,w=map(int,input().split())
S=[["#"]+list(input())+["#"] for _ in range(h)]
S.insert(0,["#"]*(w+2))
S.append(["#"]*(w+2))
D=BFS(1,1)

black=0
for i in range(1,h+1):
    black +=S[i][1:w+1].count("#")
print(h*w-black-D[h][w] if D[h][w]!=inf else -1)