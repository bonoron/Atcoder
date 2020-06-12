from sys import stdin
"--Pythonだと通らない--"


def LCS(X,Y):
    X,Y=" "+X," "+Y
    m,n=len(X),len(Y)
    MAP=[[0 for i in range(m)] for j in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            if Y[i]==X[j]:
                MAP[i][j]=MAP[i-1][j-1]+1
            else:
                MAP[i][j]=max(MAP[i][j-1],MAP[i-1][j])

    return MAP[n-1][m-1]


n=int(stdin.readline())
for i in range(n):
    X=stdin.readline().rstrip()
    Y=stdin.readline().rstrip()
    print(LCS(X,Y))