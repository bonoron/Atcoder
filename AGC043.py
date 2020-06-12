inf=float("inf")
h,w=map(int,input().split())
D=[[inf]*w for _ in range(h)]
D[0][0]=0

S=[list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        for x,y in ((1,0),(0,1)):
            X,Y=i+x,j+y
            if 0<=X<h and 0<=Y<w:
                if S[i][j]=="." and S[X][Y]=="#":
                    D[X][Y]=min(D[i][j]+1,D[X][Y])
                else:
                    D[X][Y]=min(D[i][j],D[X][Y])

ans=D[h-1][w-1]
print(ans if S[0][0]!="#" else ans+1)