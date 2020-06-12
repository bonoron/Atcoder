def para(ax,ay,bx,by):
    return True if ax*by-bx*ay==0 else False


def otr(ax,ay,bx,by):
    return True if ax*bx+ay*by==0 else False


n=int(input())
for i in range(n):
    x0,y0,x1,y1,x2,y2,x3,y3=map(int,input().split())
    x1 -=x0
    y1 -=y0
    x3 -=x2
    y3 -=y2
    if para(x1,y1,x3,y3):print(2)
    elif otr(x1,y1,x3,y3):print(1)
    else:print(0)