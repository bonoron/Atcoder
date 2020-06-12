q,l=map(int,input().split())
Q=[list(input().split()) for _ in range(q)]

queue=[]
point=0
for i in Q:
    order=i[0]
    if order=="Push":
        queue.append([int(i[1]),int(i[2])])
        point +=int(i[1])
        if point>l:print("FULL");exit()
    elif order=="Top":
        try:print(queue[-1][1])
        except:print("EMPTY");exit()
    elif order=="Size":print(point)
    elif order=="Pop":
        num=int(i[1])
        point -=num
        while num!=0:
            try:
                if queue[-1][0]>num:
                    queue[-1][0] -=num
                    num=0
                else:num -=queue.pop()[0]
            except:print("EMPTY");exit()
print("SAFE")