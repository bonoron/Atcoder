n=int(input())
XYH=[list(map(int,input().split())) for _ in range(n)]

A=[]
cnt,add=0,[0,0]
for i in range(101):
    for j in range(101):
        for x,y,h in XYH:
            H=h+abs(x-i)+abs(y-j)
            A.append([H,i,j])

for H,cx,cy in A:
    flag=1
    for x,y,h in XYH:
        if max(H-abs(x-cx)-abs(y-cy),0)!=h:flag=0
        if not flag:break
    if flag:print(cx,cy,H);exit()