"2次元配列"
"遅い"
n,w=map(int,input().split())
DP=[[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1,n+1):
    volume,weight=map(int,input().split())
    for j in range(w+1):
        DP[i][j]=max(DP[i][j],DP[i-1][j])
        if j+weight>w:continue
        if DP[i-1][j]+volume>DP[i][weight+j]:
            DP[i][weight+j]=DP[i-1][j]+volume

print(DP[n][w])

"1次元配列"
"速い"
n,w=map(int,input().split())
DP=[0]*(w+1)

for i in range(n):
    volume,weight=map(int,input().split())
    for j in range(w,weight-1,-1):
        if volume+DP[j-weight]>DP[j]:
            DP[j]=volume+DP[j-weight]

print(DP[w])