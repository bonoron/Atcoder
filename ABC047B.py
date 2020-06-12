W,H,N=map(int,input().split())
MAP=[[0 for i in range(W)] for j in range(H)]
command=[list(map(int,input().split())) for k in range(N)]
for x,y,a in command:
    if a==1:
        for i in range(H):
            for j in range(x):MAP[i][j]=1
    elif a==2:
        for i in range(H):
            for j in range(x,W):MAP[i][j]=1
    elif a==3:
        for i in range(y):
            for j in range(W):MAP[i][j]=1
    else:
        for i in range(y,H):
            for j in range(W):MAP[i][j]=1
cnt=0
for i in range(H):
    cnt +=MAP[i].count(0)
print(cnt)