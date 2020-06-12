"Pypyで通す必要がある"
def LCS_words(X,Y):
    X,Y=" "+X," "+Y
    m,n=len(X),len(Y)
    MAP=[[0 for i in range(m)] for j in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            if Y[i]==X[j]:
                MAP[i][j]=MAP[i-1][j-1]+1
            else:
                MAP[i][j]=max(MAP[i][j-1],MAP[i-1][j])

    i,j=n-1,m-1
    ans=""
    while MAP[i][j]!=0:
        if MAP[i][j]==MAP[i-1][j]:i -=1
        elif MAP[i][j]==MAP[i][j-1]:j -=1
        else:
            ans +=Y[i]
            i -=1
            j -=1
    return ans[::-1]