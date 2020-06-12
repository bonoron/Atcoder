import numpy as np


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
    #print(np.array(MAP))
    return MAP[n-1][m-1]


s=input()
k=int(input())
base=LCS_words(s,s[::-1])
reverse=s[::-1]

for i in range(len(s)//2):
    if k==0:break
    if [s[i],reverse[-i]]==[reverse[i],reverse[-i]]:
        base +=2
        k -=1

print(base+k)