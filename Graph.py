n=int(input())
A=[list(map(int,input().split())) for i in range(n)]

M=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in A[i][2:]:
        M[i][j-1]=1

for i in range(n):
    print(*M[i])