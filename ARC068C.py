x=int(input())
cnt=0
point=x//11
cnt +=point*2
x -=11*point
if 6<x<11:print(cnt+2)
else:print(cnt+1 if 0<x<=6 else cnt)