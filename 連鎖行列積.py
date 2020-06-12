def matrixChainMultiplecation(A):
    P=[A[0][0]]
    n=len(A)
    for i in range(n):
        P.append(A[i][1])
    M=[[0 for i in range(n)] for j in range(n)]
    for l in range(1,n):
        for i in range(n-l):
            j=l+i
            M[i][j]=float("inf")
            for k in range(i,j):
                M[i][j]=min(M[i][j],M[i][k]+M[k+1][j]+P[i-1]*P[k]*P[j])
    return M[0][-1]


n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
print(matrixChainMultiplecation(A))