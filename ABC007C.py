from collections import deque


def BFS(S,G):
    x,y=S[0]-1,S[1]-1
    color=[["white" for i in range(w)] for j in range(h)]
    D=[[-1 for i in range(w)] for j in range(h)]

    color[x][y]="gray"
    D[x][y]=0
    queue=deque([[x,y]])

    while len(queue)!=0:
        a,b=queue.popleft()
        for c,d in [[0,1],[0,-1],[1,0],[-1,0]]:
            X,Y=a+c,b+d
            if color[X][Y]=="white" and C[X][Y]==".":
                color[X][Y]="gray"
                D[X][Y]=D[a][b]+1
                queue.append([X,Y])
        color[a][b]="black"

    return D[G[0]-1][G[1]-1]


h,w=map(int,input().split())
S=list(map(int,input().split()))
G=list(map(int,input().split()))
C=[list(input()) for i in range(h)]
print(BFS(S,G))