def cross(P0, P1, P2):
    x0,y0=P0;x1,y1=P1;x2,y2=P2
    x1 -=x0;x2 -=x0
    y1 -=y0;y2 -=y0
    return x1*y2-x2*y1


a,b=map(int,input().split())
n=int(input())
XY=[list(map(int,input().split())) for _ in range(n)]
XY.append(XY[0])

cnt=10**9
for i in range(n):
    cnt=min(cnt,abs(cross(XY[i],XY[i+1],[a,b]))/((XY[i][0]-XY[i+1][0])**2+(XY[i][1]-XY[i+1][1])**2)**0.5)
print(cnt)