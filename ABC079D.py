h,w=map(int,input().split())
C=[list(map(int,input().split())) for i in range(10)]
A=[list(map(int,input().split())) for j in range(h)]
#warshall_floyd法:最短経路を全探索で求める
for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j]=min(C[i][j],C[i][k]+C[k][j])

cost=[C[i][1] for i in range(10)]+[0]
cnt=0
for i in range(h):
    for j in range(w):
        cnt +=cost[A[i][j]]
print(cnt)