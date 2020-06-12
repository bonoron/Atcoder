n,m=map(int,input().split())
A=[list(input()) for i in range(n)]
B=[list(input()) for j in range(m)]
point=[[i,j] for i in range(m) for j in range(m)]
for i in range(n-(m-1)):
    for j in range(n-(m-1)):
        cnt=0
        for x,y in point:
            if B[x][y]==A[i+x][j+y]:
                cnt +=1
        if cnt==m**2:
            print("Yes")
            exit()
print("No")