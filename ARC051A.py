def dis(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


x1,y1,r=map(int,input().split())
x2,y2,x3,y3=map(int,input().split())

print("NO" if (x2<=x1-r)and(x1+r<=x3)and(y2<=y1-r)and(y1+r<=y3) else "YES")
print("NO" if (r>=dis(x1,y1,x2,y2))and(r>=dis(x1,y1,x2,y3))and(r>=dis(x1,y1,x3,y2))and(r>=dis(x1,y1,x3,y3)) else "YES")