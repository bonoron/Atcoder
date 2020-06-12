n=int(input())
A=sorted(list(map(int,input().split())))

XY=[]
left,right=A[0],A[-1]
for i in range(1,n-1):
    num=A[i]
    if num<0:
        XY.append([right,num])
        right -=num
    else:
        XY.append([left,num])
        left -=num
XY.append([right,left])
print(right-left)
for x,y in XY:print(x,y)