s=input()
t=int(input())
x,y=0,0
cnt=0
for i in s:
    if i=="L":x -=1
    elif i=="R":x +=1
    elif i=="U":y +=1
    elif i=="D":y -=1
    elif i=="?":cnt +=1

dis=abs(x)+abs(y)
print(dis+cnt if t==1 else max(len(s)%2,dis-cnt))