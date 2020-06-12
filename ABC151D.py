from collections import deque


def BFS(x,y):
    color=[["white" for i in range(w+2)] for j in range(h+2)]
    D=[[-1 for i in range(w+2)] for j in range(h+2)]

    color[x][y]="gray"
    D[x][y],dis=0,0
    queue=deque([[x,y]])

    while len(queue)!=0:
        a,b=queue.popleft()
        for c,d in [[0,1],[0,-1],[1,0],[-1,0]]:
            X,Y=a+c,b+d
            if S[X][Y]=="." and color[X][Y]=="white":
                color[X][Y]="gray"
                D[X][Y]=D[a][b]+1
                dis=max(dis,D[X][Y])
                queue.append([X,Y])
        color[a][b]="black"

    return dis


h,w=map(int,input().split())
S=[["#"]+list(input())+["#"] for i in range(h)]
S.insert(0,["#"]*(w+2))
S.append(["#"]*(w+2))

ans=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if S[i][j]!="#":
            ans=max(ans,BFS(i,j))

print(ans)