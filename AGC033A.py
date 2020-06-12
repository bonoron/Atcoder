import sys
from collections import deque
sys.setrecursionlimit(10**7)
inf=10**7


def BFS():
    color=[["white" for _ in range(w+2)] for _ in range(h+2)]
    D=[[inf for _ in range(w+2)] for _ in range(h+2)]

    queue=deque([])
    for i in range(1,h+1):
        for j in range(1,w+1):
            if A[i][j]=="#":
                queue.append([i,j])
                D[i][j]=0
                color[i][j]="gray"

    cnt=0
    while len(queue)!=0:
        a,b=queue.popleft()
        for c,d in ((1,0),(0,1),(-1,0),(0,-1)):
            X,Y=a+c,b+d
            if A[X][Y]=="." and color[X][Y]=="white":
                color[X][Y]="gray"
                D[X][Y]=D[a][b]+1
                cnt=max(cnt,D[X][Y])
                queue.append([X,Y])
        color[a][b]="black"

    return cnt


h,w=map(int,input().split())
A=[["#"]+list(input())+["#"] for _ in range(h)]
A.insert(0,["#"]*(w+2))
A.append(["#"]*(w+2))
print(BFS())