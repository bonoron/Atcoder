import copy


def bom(point,cnt):
    global ans
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
    for x,y in dir:
        x=point[0]+x
        y=point[1]+y
        if M[x][y]==".":
            M[point[0]][point[1]]="#"
            bom([x,y],cnt+1)
        else:
            if cnt>ans:ans=cnt


h,w=map(int,input().split())
MAP=[["#"]+list(input())+["#"] for i in range(h)]
MAP.insert(0,["#"]*(w+2))
MAP.append(["#"]*(w+2))
ans=0
for i in range(1,h+1):
    for j in range(1,w+1):
        M=copy.deepcopy(MAP)
        bom([i,j],0)
print(ans-1)